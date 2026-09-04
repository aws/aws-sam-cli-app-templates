import os
import re
import tempfile

from pathlib import Path
from subprocess import Popen, PIPE, TimeoutExpired
from logging import getLogger, StreamHandler, INFO
from typing import Any, NamedTuple
from unittest import TestCase


from tests import REPO_ROOT

PROJECT_NAME = "project-name"


class CommandResult(NamedTuple):
    process: Popen
    stdout: str
    stderr: str

# TODO: make refactor so timeout and run_command is in Base class so we can override it
TIMEOUT = 3600

LOG = getLogger(__name__)
LOG.addHandler(StreamHandler())
LOG.setLevel(INFO)

# NOTE: Using `samdev` as against `sam` in cmdlist enables test with samcli in your dev environment.
SAM_CLI_EXECUTABLE = "samdev" if os.getenv("SAM_CLI_DEV") else "sam"

# Matches a cfn-lint rule id in `sam validate --lint` output, e.g. "[W2531: Check if ...]"
LINT_RULE_PATTERN = re.compile(r"\[([EWI]\d{4}):")

# cfn-lint rules that are not template defects and so must not fail the lint test.
#
# These are cfn-lint's three deprecated-runtime rules, all of which fire on a calendar
# date passing rather than on a change to a template:
#   W2531 - runtime is past its EOL date
#   E2531 - runtime is past the date new function creation was disabled
#   E2533 - runtime is past the date function updates were disabled
# This repo deliberately ships one template variant per runtime, including runtimes
# past those dates (provided.al2, java8.al2, ...). All three are listed on purpose: if
# only W2531 were allowed, every PR in the repo would go red again the day a runtime
# crosses its next threshold, with no template having changed. Retiring an EOL template
# variant is a product decision and is tracked separately from keeping CI honest.
ALLOWED_LINT_RULES = {"W2531", "E2531", "E2533"}

def run_command(command_list, cwd=None, env=None, timeout=TIMEOUT) -> CommandResult:
    LOG.info("Running command: %s", " ".join(map(lambda x: str(x), command_list)))
    LOG.info("cwd:             %s", cwd)
    LOG.info("env:             %s", env)
    LOG.info("timeout:         %s", timeout)
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
        should_test_lint: bool = True
        runtime = None

        def setUp(self) -> None:
            self.tempdir = tempfile.TemporaryDirectory()
            self.cwd = Path(self.tempdir.name, PROJECT_NAME)
            self.template_path = Path(REPO_ROOT, self.directory)

            LOG.info(f"Temporary directory {self.tempdir.name} created")

        def tearDown(self) -> None:
            LOG.info(f"Clean up temporary directory {self.tempdir.name}")
            self.tempdir.cleanup()

        def _test_init_template(self):
            cmdlist = [
                SAM_CLI_EXECUTABLE,
                "init",
                "--no-input",
                "--location",
                self.template_path,
                "--name",
                PROJECT_NAME,
            ]
            if self.runtime:
                cmdlist.append("--extra-context")
                cmdlist.append(f'{{"runtime": "{self.runtime}"}}')
            run_command(cmdlist, self.tempdir.name)
            self.assertTrue(self.cwd.exists())

            self._test_file_path_lengths()
            if self.should_test_lint:
                self._test_lint()

        def _test_lint(self):
            """
            Test if sam validate --lint passes, ignoring ALLOWED_LINT_RULES
            """
            cmdlist = [
                SAM_CLI_EXECUTABLE,
                "validate",
                "--lint",
            ]
            result = run_command(cmdlist, Path(self.tempdir.name) / PROJECT_NAME)
            if result.process.returncode == 0:
                return

            matched_rules = set(LINT_RULE_PATTERN.findall(result.stdout))
            unexpected_rules = matched_rules - ALLOWED_LINT_RULES
            self.assertTrue(
                matched_rules and not unexpected_rules,
                f"sam validate --lint failed with {sorted(unexpected_rules) or 'no parsable rule id'}"
                f"\nstdout: {result.stdout}\nstderr: {result.stderr}",
            )

        def _test_file_path_lengths(self):
            """
            Tests the length of the file paths to make sure
            we are under Windows' max path length limit
            """

            # drive + user folder + max length username + temp folder + template folder
            MOCK_WINDOWS_PATH = "C:/Users/abcdefghijklmnopqrst/AppData/Local/Temp/2/tmp0h55doro/tmpl"
            WINDOWS_MAX_PATH = 260

            for root, _, files in os.walk(self.template_path):
                for file in files:
                    file_full_path = os.path.join(root, file)
                    file_rel_path = os.path.relpath(file_full_path, REPO_ROOT)

                    file_windows_path = os.path.join(MOCK_WINDOWS_PATH, file_rel_path)
                    self.assertLess(len(file_windows_path), WINDOWS_MAX_PATH)
