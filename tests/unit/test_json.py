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
                use_case_name = template.get("useCaseName")
                self.assertTrue(Path(directory).exists(), f"{directory} does not exist")
                self.assertIsNotNone(use_case_name, "Template property 'useCaseName' was not specified")
