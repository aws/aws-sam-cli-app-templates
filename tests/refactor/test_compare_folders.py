"""
Runs `sam init` for old folder and new folder and then compares these folders to assert their contents are the same.
These tests are created to make sure we are not introducing a side effect with this refactoring (merge same programming language templates into single folder)
"""
from logging import INFO, StreamHandler, getLogger
from pathlib import Path
import shutil
import tempfile
from typing import Optional
from unittest import TestCase
from parameterized import parameterized
from tests import REPO_ROOT
from tests.integration.base import PROJECT_NAME, SAM_CLI_EXECUTABLE, run_command


LOG = getLogger(__name__)
LOG.addHandler(StreamHandler())
LOG.setLevel(INFO)


class CompareNewAndOldFolders(TestCase):

    def setUp(self) -> None:
        self.old_cwd = tempfile.TemporaryDirectory()
        self.new_cwd = tempfile.TemporaryDirectory()
        LOG.info(f"Temporary directories {self.old_cwd}, {self.new_cwd} created")
    
    def tearDown(self) -> None:
        LOG.info(f"Clean up temporary directories {self.old_cwd}, {self.new_cwd}")
        self.old_cwd.cleanup()
        self.new_cwd.cleanup()
    
    def test(self):
        """Dummy test to run for refactor test CI checks"""
        self.assertTrue(True)
    
    # Update following parameters when we refactor any other runtime
    # @parameterized.expand([
    #     ("ruby2.7/hello", "ruby/hello", "ruby2.7"),
    #     ("ruby2.7/hello-img", "ruby/hello-img", "ruby2.7"),
    #     ("ruby2.7/step-func", "ruby/step-func", "ruby2.7"),
    #     ("ruby3.2/hello", "ruby/hello", "ruby3.2"),
    #     ("ruby3.2/hello-img", "ruby/hello-img", "ruby3.2"),
    #     ("ruby3.2/step-func", "ruby/step-func", "ruby3.2"),
    # ])
    # def test_compare_folders(self, old_folder, new_folder, runtime):
    #     self.old_template_path = Path(REPO_ROOT, old_folder)
    #     self.new_template_path = Path(REPO_ROOT, new_folder)

    #     LOG.info("Running `sam init` for old folder (%s) and new folder (%s)", old_folder, new_folder)
    #     self._run_init(self.old_template_path, Path(self.old_cwd.name))
    #     self._run_init(self.new_template_path, Path(self.new_cwd.name), runtime)

    #     LOG.info("Comparing generated application for old folder (%s) with new folder (%s) and runtime (%s)", old_folder, new_folder, runtime)
    #     diff_result = run_command([
    #         "diff",
    #         "-rs",
    #         self.old_cwd.name,
    #         self.new_cwd.name,
    #     ])
    #     self.assertEqual(0, diff_result.process.returncode)

    def _run_init(self, template_path: Path, cwd: Path, runtime: Optional[str] = None):
        cmdlist = [
            SAM_CLI_EXECUTABLE,
            "init",
            "--no-input",
            "--location",
            template_path,
            "--name",
            PROJECT_NAME,
        ]
        if runtime:
            cmdlist.append("--extra-context")
            cmdlist.append(f'{{"runtime": "{runtime}"}}')
        init_result = run_command(cmdlist, cwd=cwd)
        self.assertEqual(0, init_result.process.returncode)
        self.assertTrue(cwd.exists())