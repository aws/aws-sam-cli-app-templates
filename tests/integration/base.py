import os
import tempfile

from pathlib import Path
from subprocess import Popen, PIPE, TimeoutExpired
from logging import getLogger, StreamHandler, INFO
from typing import Any, NamedTuple
from unittest import TestCase


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
