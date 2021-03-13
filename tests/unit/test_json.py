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

    def _find_template_yaml(self, directory):
        for root, dirs, files in os.walk(directory):
            for name in files:
                if name in ("template.yaml", "template.yml"):
                    return os.path.join(root, name)
        raise Exception("Cannot find template.yaml")

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
                cookiecutter_json_path = Path(template["directory"], "cookiecutter.json")
                with open(cookiecutter_json_path) as f:
                    try:
                        cookiecutter_json_body = json.load(f)
                    except:
                        self.fail(f"{cookiecutter_json_path} is an invalid JSON file.")
                    self.assertIn(
                        "project_name",
                        cookiecutter_json_body,
                        f"{cookiecutter_json_path} does not have project_name",
                    )
                    if template["packageType"] == "Zip":
                        # for zip type, we verify the template.yaml has the Runtime: runtime
                        template_path = self._find_template_yaml(template["directory"])
                        self.assertIn(
                            f"Runtime: {runtime}",
                            open(template_path).read(),
                            f"{template_path}'s runtime does not match the one in manifest.json",
                        )
