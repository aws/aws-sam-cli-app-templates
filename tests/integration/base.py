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

    class BuildInvokeBase(IntegBase):
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
        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "Hello World!"})

    class SimpleHelloWorldBuildInvokeBase(BuildInvokeBase):
        def _test_local_invoke(self):
            super()._test_local_invoke()
            self.assertEqual(self.invoke_output["statusCode"], 200)
            self.assertEqual(json.loads(self.invoke_output["body"]), {"message": "hello world"})

    class QuickStartWebBuildInvokeBase(BuildInvokeBase):
        function_id_by_event = {
            "event-get-all-items.json": "getAllItemsFunction",
            "event-get-by-id.json": "getByIdFunction",
            "event-post-item.json": "putItemFunction",
        }

    # Unit Tests
    class UnitTestBase(IntegBase):
        # by default, the code is not in a nested directory
        code_directories: List[str] = ["."]

        @abstractmethod
        def _test_install(self, code_directory: str):
            pass

        @abstractmethod
        def _test_unit_tests(self, code_directory: str):
            pass

        def test_unit_tests(self):
            self._test_init_template()
            for code_directory in self.code_directories:
                self._test_install(code_directory)
                self._test_unit_tests(code_directory)

    class NodejsUnitTestBase(UnitTestBase):
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

    class Python27UnitTestBase(UnitTestBase):
        python_executable = "python27"

    class Python36UnitTestBase(UnitTestBase):
        python_executable = "python36"

    class Python37UnitTestBase(UnitTestBase):
        python_executable = "python37"

    class Python38UnitTestBase(UnitTestBase):
        python_executable = "python38"

    class JavaUnitTestGradleBase(UnitTestBase):
        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["gradle", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("BUILD SUCCESSFUL", result.stdout)

    class JavaUnitTestMavenBase(UnitTestBase):
        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["mvn", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("BUILD SUCCESS", result.stdout)

    class DotNetCoreUnitTestBase(UnitTestBase):
        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["dotnet", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("Passed", result.stdout)
            self.assertNotIn("Failed", result.stdout)

    class GoUnitTestBase(UnitTestBase):
        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["go", "test", "-v"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertIn("PASS", result.stdout)
            self.assertNotIn("FAIL", result.stdout)

    class RubyUnitTestBase(UnitTestBase):
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
