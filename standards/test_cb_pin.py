"""The owner's 30–31 October 2026 corporate-body shape pin is immutable."""

import hashlib
import json
import unittest
from pathlib import Path


class CorporateBodyPin(unittest.TestCase):
    def test_unchanged_upstream_files_and_provenance(self):
        root = Path(__file__).parent / "ehri-cb-1.1-1c2325f9"
        pin = json.loads((root / "pin.json").read_text(encoding="utf-8"))
        self.assertEqual(pin["repo"], "EHRI/ehri-kg-mapping")
        self.assertEqual(pin["commit"], "1c2325f9d2267a8a0c639cd041be54ec9a73e517")
        self.assertEqual(pin["read_on"], "2026-10-31")
        self.assertEqual(pin["version"], "1.1")
        self.assertEqual(pin["license"], "EUPL-1.2")
        expected = {
            "cb.shacl.ttl": "2b8d9bbde8a8378a8aec2e98ce30d161ba608b7353addb6fd0674c387fcdd14d",
            "cb.shex": "a348f61b00403a820ee4b73a925bd2e92c39e362c8d7bba842140bc37cd77355",
            "LICENSE.md": "44905a5dff88eb1872d9e1a1880e5c8cd302ed3d20008de53cf07c83ca6a131d",
        }
        self.assertEqual(set(pin["files"]), set(expected))
        for name, digest in expected.items():
            with self.subTest(file=name):
                info = pin["files"][name]
                path = "LICENSE.md" if name == "LICENSE.md" else "src/shapes/1.1/" + name
                self.assertEqual(info["path"], path)
                self.assertEqual(info["sha256"], digest)
                self.assertEqual(hashlib.sha256((root / name).read_bytes()).hexdigest(), digest)
                self.assertEqual(
                    info["url"],
                    f"https://github.com/{pin['repo']}/blob/{pin['commit']}/{path}",
                )
