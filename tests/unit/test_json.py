import json
import os
import unittest
from pathlib import Path

from tests import REPO_ROOT


class TestJson(unittest.TestCase):
    def setUp(self):
        self.manifest_path_v2 = os.path.join(REPO_ROOT, "manifest-v2.json")

    def _load_manifest(self, manifest):
        with open(manifest) as f:
            return json.load(f)

    def test_manifest_v2_valid_json(self):
        json_body = self._load_manifest(self.manifest_path_v2)
        self.assertIsNotNone(json_body)

    def test_manifest_v2_template_exist(self):
        directories_dont_exist = []
        json_body = self._load_manifest(self.manifest_path_v2)
        for _, templates in json_body.items():
            for template in templates:
                directory = template["directory"]
                if not Path(directory).exists():
                    directories_dont_exist.append(directory)
        
        self.assertFalse(bool(directories_dont_exist), f"Following direcories do not exist: {directories_dont_exist}")

    def test_manifest_v2_all_use_case_defined(self):
        use_cases_dont_exist = []
        json_body = self._load_manifest(self.manifest_path_v2)
        for runtime, templates in json_body.items():
            for template in templates:
                use_case_name = template.get("useCaseName")
                display_name = template.get("displayName")
                if not use_case_name:
                    use_cases_dont_exist.append(f"{runtime}:{display_name}")
        
        self.assertFalse(bool(use_cases_dont_exist), f"Following runtime:display_names do not define useCaseName: {use_cases_dont_exist}")
