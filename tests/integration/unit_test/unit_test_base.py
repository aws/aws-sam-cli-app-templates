import os
from abc import abstractmethod
from pathlib import Path
from typing import List

from tests.integration.base import Base, LOG, run_command


class UnitTestBase:
    class UnitTestBase(Base.IntegBase):
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
                result.stdout,
                r"added \d+ packages from \d+ contributors and audited \d+ packages",
            )
            self.assertIn(
                "found 0 vulnerabilities",
                result.stdout,
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
            cmdlist = [self.python_executable, "-m", "pytest", "tests/unit"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, self.cwd, env=env)
            self.assertNotIn("ERRORS", result.stdout)

    class Python36UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.6"

    class Python37UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.7"

    class Python38UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.8"

    class Python39UnitTestBase(PythonUnitTestBase):
        python_executable = "python3.9"

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
            LOG.info("Running in folder %s", self.cwd)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertEqual(result.process.returncode, 0)
            self.assertNotIn("Failed!", result.stdout)

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

    class RustUnitTestBase(UnitTestBase):
        """
        Execute the following commands:
        1. cargo test # install dependencies and run tests
        """

        def _test_install(self, code_directory: str):
            pass

        def _test_unit_tests(self, code_directory: str):
            cmdlist = ["cargo", "test"]
            LOG.info(cmdlist)
            result = run_command(cmdlist, Path(self.cwd, code_directory))
            self.assertNotIn("FAILED", result.stdout)