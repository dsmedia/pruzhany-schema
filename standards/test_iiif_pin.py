"""The Presentation 3 schema stays byte-identical to its reviewed upstream pin."""

import hashlib
import json
import unittest
from pathlib import Path


class IIIFPin(unittest.TestCase):
    def test_unchanged_schema_and_provenance(self):
        folder = Path(__file__).parent / "iiif-presentation-3-3891f47"
        pin = json.loads((folder / "pin.json").read_text(encoding="utf-8"))
        self.assertEqual(pin["repo"], "IIIF/presentation-validator")
        self.assertEqual(pin["commit"], "3891f47ce7dbaa896027a5fab5f63a109de4bd70")
        self.assertEqual(pin["read_on"], "2026-10-31")
        self.assertTrue(pin["license"])
        self.assertTrue(pin["attribution"])
        self.assertEqual(set(pin["files"]), {"iiif_3_0.json", "upstream-README.md"})
        self.assertEqual(pin["files"]["iiif_3_0.json"]["sha256"],
                         "14dd7ee8aee25d959be4b12feddb4179c726909fc85b925f6707f4ab3bfe2ad6")
        for name, info in pin["files"].items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((folder / name).read_bytes()).hexdigest(),
                                 info["sha256"])
                self.assertEqual(info["url"],
                                 f"https://github.com/{pin['repo']}/blob/{pin['commit']}/{info['path']}")
        schema = json.loads((folder / "iiif_3_0.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "http://json-schema.org/draft-07/schema#")
        self.assertIn("manifest", schema["classes"])
