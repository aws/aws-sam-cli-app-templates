import json
import os
import unittest

from tests import REPO_ROOT

class TestJson(unittest.TestCase):
    def setUp(self):
        self.manifest_path = os.path.join(REPO_ROOT, "manifest.json")

    def test_manifest_valid_json(self):
        json_body = None
        with open(self.manifest_path) as f:
            body = f.read()
            json_body = json.loads(body)
        self.assertIsNotNone(json_body)
