import json
import os
import unittest
from pathlib import Path

from tests import REPO_ROOT


class TestJson(unittest.TestCase):
    def setUp(self):
        self.manifest_path = os.path.join(REPO_ROOT, "manifest.json")

    def _load_manifest(self):
        with open(self.manifest_path) as f:
            return json.load(f)

    def test_manifest_valid_json(self):
        json_body = self._load_manifest()
        self.assertIsNotNone(json_body)

    def test_manifest_template_exist(self):
        json_body = self._load_manifest()
        for runtime, templates in json_body.items():
            for template in templates:
                directory = template["directory"]
                self.assertTrue(Path(directory).exists(), f"{directory} does not exist")

    def test_cookiecutter_json(self):
        json_body = self._load_manifest()
        for runtime, templates in json_body.items():
            for template in templates:
                cookiecutter_json_path = Path(
                    template["directory"], "cookiecutter.json"
                )
                with open(cookiecutter_json_path) as f:
                    cookiecutter_json_body = json.load(f)
                    self.assertIn(
                        "project_name",
                        cookiecutter_json_body,
                        f"{cookiecutter_json_path} does not have project_name",
                    )
                    self.assertIn(
                        "runtime",
                        cookiecutter_json_body,
                        f"{cookiecutter_json_path} does not have runtime",
                    )
                    actual_runtime = cookiecutter_json_body["runtime"]
                    self.assertIn(
                        runtime,
                        {runtime, f"amazon/{actual_runtime}-base"},
                        f"{cookiecutter_json_path} has incorrect runtime {actual_runtime}",
                    )
