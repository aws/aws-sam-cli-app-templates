import ipaddress
import json
import os
import tempfile
from abc import abstractmethod

from pathlib import Path
from subprocess import Popen, PIPE, TimeoutExpired
from logging import getLogger, StreamHandler, INFO
from typing import Dict, Any, Optional, List, NamedTuple
from unittest import TestCase

import pytest

from tests import REPO_ROOT

PROJECT_NAME = "project"


class CommandResult(NamedTuple):
    process: Popen
    stdout: str
    stderr: str


TIMEOUT = 300

LOG = getLogger(__name__)
LOG.addHandler(StreamHandler())
LOG.setLevel(INFO)


def run_command(command_list, cwd=None, env=None, timeout=TIMEOUT) -> CommandResult:
    if not env:
        env = os.environ.copy()
    LOG.info("PATH=%s", env["PATH"])
    process_execute = Popen(command_list, cwd=cwd, env=env, stdout=PIPE, stderr=PIPE)
    try:
        stdout_data, stderr_data = process_execute.communicate(timeout=timeout)
        stdout = stdout_data.decode()
        stderr = stderr_data.decode()
        LOG.info(f"Stdout: {stdout}")
        LOG.info(f"Stderr: {stderr}")
        return CommandResult(process_execute, stdout, stderr)
    except TimeoutExpired:
        LOG.error(f"Command: {command_list}, TIMED OUT")
        LOG.error(f"Return Code: {process_execute.returncode}")
        process_execute.kill()
        raise


class Base:
    """
    Contains base unittest classes:
        - IntegBase and xyzIntegBase
        - UnitTestBase and xyzUnitTestBase
    """

    class IntegBase(TestCase):
        tempdir: Any
        directory: str

        def setUp(self) -> None:
            self.tempdir = tempfile.TemporaryDirectory()
            self.cwd = Path(self.tempdir.name, PROJECT_NAME)
            LOG.info(f"Temporary directory {self.tempdir.name} created")

        def tearDown(self) -> None:
            LOG.info(f"Clean up temporary directory {self.tempdir.name}")
            self.tempdir.cleanup()

        def _test_init_template(self):
            template_path = Path(REPO_ROOT, self.directory)
            cmdlist = [
                "sam",
                "init",
                "--no-input",
                "--location",
                template_path,
                "--name",
                PROJECT_NAME,
            ]
            LOG.info(cmdlist)
            run_command(cmdlist, self.tempdir.name)
            self.assertTrue(self.cwd.exists())

    #   ____  _   _ ___ _     ____            _     ___   ____    _    _       ___ _   ___     _____  _  _______
    #  | __ )| | | |_ _| |   |  _ \     _    | |   / _ \ / ___|  / \  | |     |_ _| \ | \ \   / / _ \| |/ | ____|
    #  |  _ \| | | || || |   | | | |  _| |_  | |  | | | | |     / _ \ | |      | ||  \| |\ \ / | | | | ' /|  _|
    #  | |_) | |_| || || |___| |_| | |_   _| | |__| |_| | |___ / ___ \| |___   | || |\  | \ V /| |_| | . \| |___
    #  |____/ \___/|___|_____|____/    |_|   |_____\___/ \____/_/   \_|_____| |___|_| \_|  \_/  \___/|_|\_|_____|
    #
    class BuildInvokeBase(IntegBase):
        """
        BuildInvokeBase will test the following sam commands:
        1. sam init
        2. sam build --use-container (if self.use_container is False, --use-container will be omitted)
        3. (if there are event jsons), for each event json, check `sam local invoke` response is a valid json
        """

        function_id_by_event: Optional[Dict[str, str]] = None
        invoke_output: Dict[str, Any]
        use_container: bool = True

        def _test_build(self):
            cmdlist = ["sam", "build", "--debug"]
            if self.use_container:
                cmdlist.append("--use-container")
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd)
            self.assertIn("Build Succeeded", str(result.stdout))

        def _test_local_invoke(self):
            events_path = Path(self.cwd, "events")
            if not events_path.exists():
                LOG.info(f"Skip event testing, {events_path} does not exist")
                return
            event_files = os.listdir(events_path)
            for event_file in event_files:
                if self.function_id_by_event:
                    cmdlist = [
                        "sam",
                        "local",
                        "invoke",
                        self.function_id_by_event[event_file],
                        "-e",
                        Path("events", event_file),
                    ]
                else:
                    cmdlist = [
                        "sam",
                        "local",
                        "invoke",
                        "-e",
                        Path("events", event_file),
                    ]
                LOG.info(cmdlist)
                result = run_command(cmdlist, self.cwd)
                try:
                    self.invoke_output = json.loads(result.stdout)
                except json.decoder.JSONDecodeError:
                    self.fail(f"Response is not a valid JSON: {result.stdout}")

        @pytest.mark.flaky(reruns=3)
        def test_buld_and_invoke(self):
            self._test_init_template()
            self._test_build()
            self._test_local_invoke()

    class HelloWorldWithLocationBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, HelloWorldWithLocationBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "hello world" and location is a valid IP address
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(
                self.invoke_output["headers"],
                {"X-Custom-Header": "application/json", "Content-Type": "application/json",},
            )
            body = json.loads(self.invoke_output["body"])
            self.assertEqual(body["message"], "hello world")
            # make sure it is an IP address
            try:
                ipaddress.ip_address(body["location"])
            except ValueError:
                self.fail(f'Invalid location: {body["location"]}')

    class EventBridgeHelloWorldBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, EventBridgeHelloWorldBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's detail, detail-type, resources, source, account and region
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(
                self.invoke_output["detail"], {"instance-id": "i-abcd1111", "state": "pending"},
            )
            self.assertEqual(
                self.invoke_output["detail-type"],
                "HelloWorldFunction updated event of EC2 Instance State-change Notification",
            )
            self.assertEqual(
                self.invoke_output["resources"], ["arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"],
            )
            self.assertEqual(self.invoke_output["source"], "aws.ec2")
            self.assertEqual(self.invoke_output["account"], "123456789012")
            self.assertEqual(self.invoke_output["region"], "us-east-1")

    class HelloWorldExclamationBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, HelloWorldExclamationBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "Hello World!"
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "Hello World!"})

    class SimpleHelloWorldBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, SimpleHelloWorldBuildInvokeBase will the these extra checking:
        - check `sam local invoke` response's message is "hello world!"
        """

        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "hello world"})

    class QuickStartWebBuildInvokeBase(BuildInvokeBase):
        """
        Based on BuildInvokeBase, quick start web templates have multiple events that call different lambda functions.
        """

        function_id_by_event = {
            "event-get-all-items.json": "getAllItemsFunction",
            "event-get-by-id.json": "getByIdFunction",
            "event-post-item.json": "putItemFunction",
        }

    class DotNetCoreExtraRerunBuildInvokeBase(BuildInvokeBase):
        """
        dotnet templates' building tends to fail arbitrarily, adding extra reruns here 
        """

        @pytest.mark.flaky(reruns=5)
        def test_buld_and_invoke(self):
            super().test_buld_and_invoke()

    #   _   _ _   _ ___ _____   _____ _____ ____ _____
    #  | | | | \ | |_ _|_   _| |_   _| ____/ ___|_   _|
    #  | | | |  \| || |  | |     | | |  _| \___ \ | |
    #  | |_| | |\  || |  | |     | | | |___ ___) || |
    #   \___/|_| \_|___| |_|     |_| |_____|____/ |_|
    #
    class UnitTestBase(IntegBase):
        """
        UnitTestBase will run the local unit tests (if available).
        This class cannot be used directly, please create a subclass and implement these two methods:
        - _test_install()
        - _test_unit_tests()
        """

        # by default, the code is not in a nested directory
        code_directories: List[str] = ["."]

        @abstractmethod
        def _test_install(self, code_directory: str):
            """
            Setup the project dependencies to build, run unit tests, and verify the output.
            """
            pass

        @abstractmethod
        def _test_unit_tests(self, code_directory: str):
            """
            Execute unit tests and verify the output.
            """
            pass

        def test_unit_tests(self):
            self._test_init_template()
            for code_directory in self.code_directories:
                self._test_install(code_directory)
                self._test_unit_tests(code_directory)

    class NodejsUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. npm i # install dependencies
        2. npm test # run local unit tests
        """

        def _test_install(self, code_directory: str):
            cmdlist = [
                "npm",
                "i",
            ]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertRegex(
                result.stdout, r"added \d+ packages from \d+ contributors and audited \d+ packages",
            )
            self.assertIn(
                "found 0 vulnerabilities", result.stdout,
            )

        def _test_unit_tests(self, code_directory: str):
            cmdlist = [
                "npm",
                "test",
            ]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("pass", result.stdout + result.stderr)
            self.assertNotIn("fail", result.stdout + result.stderr)

    class PythonUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. pip install -r requirements.txt pytest pytest-mock # install dependencies and test dependencies
        2. pytest tests # run local unit tests
        """

        python_executable = "python"

        def _test_install(self, code_directory: str):
            cmdlist = [
                self.python_executable,
                "-m",
                "pip",
                "install",
                "-t",
                "lib",
                "-r",
                f"{code_directory}/requirements.txt",
                # to run pytest, pytest needs to be installed
                "pytest",
                "pytest-mock",
            ]
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd)
            if result.stdout:
                # when requirements.txt is empty, the stdout is also empty
                self.assertIn("Successfully installed", result.stdout)

        def _test_unit_tests(self, code_directory: str):
            env = os.environ.copy()
            env["PYTHONPATH"] = "lib:."
            cmdlist = [self.python_executable, "-m", "pytest", "tests"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd, env=env)
            self.assertNotIn("ERRORS", result.stdout)

    class Python27UnitTestBase(PythonUnitTestBase):
        python_executable = "python2.7"

    class Python36UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.6"

    class Python37UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.7"

    class Python38UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.8"

    class JavaUnitTestGradleBase(UnitTestBase):
        """
        Execute the following commands:
        1. gradle test # install dependencies and run tests
        """

        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["gradle", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("BUILD SUCCESSFUL", result.stdout)

    class JavaUnitTestMavenBase(UnitTestBase):
        """
        Execute the following commands:
        1. mvn test # install dependencies and run tests
        """

        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["mvn", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("BUILD SUCCESS", result.stdout)

    class DotNetCoreUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. dotnet test # install dependencies and run tests
        """

        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["dotnet", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("Passed", result.stdout)
            self.assertNotIn("Failed", result.stdout)

    class GoUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. go test # install dependencies and run tests
        """

        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["go", "test", "-v"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("PASS", result.stdout)
            self.assertNotIn("FAIL", result.stdout)

    class RubyUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. bundle install # install dependencies
        2. ruby <code-directory> # run local unit tests
        """

        def _test_install(self, code_directory: str):
            cmdlist = ["ruby", "--version"]
            LOG.info(cmdlist)
            run_command(cmdlist, self.cwd)

            cmdlist = ["bundle", "install"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd)
            self.assertIn("Bundle complete!", result.stdout)

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["ruby", code_directory]
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd)
            self.assertIn("100% passed", result.stdout)
