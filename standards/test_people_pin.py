"""The owner's 30–31 October 2026 shape pin is immutable and self-contained."""

import hashlib
import json
import unittest
from pathlib import Path


class PeoplePin(unittest.TestCase):
    def test_unchanged_upstream_files_and_provenance(self):
        root = Path(__file__).parent / "ehri-people-1.1-1c2325f9"
        pin = json.loads((root / "pin.json").read_text(encoding="utf-8"))
        self.assertEqual(pin["repo"], "EHRI/ehri-kg-mapping")
        self.assertEqual(pin["commit"], "1c2325f9d2267a8a0c639cd041be54ec9a73e517")
        self.assertEqual(pin["read_on"], "2026-10-31")
        self.assertEqual(pin["license"], "EUPL-1.2")
        expected = {
            "people.shacl.ttl": "341bbf120657a5e9975f2bb6db068958ff583003ccbb1960bae974d4af8e4d18",
            "people.shex": "4b808aa2a60e01b9ce41b46347b81db44578b79c3617f0a6f33be09149be4a47",
            "LICENSE.md": "44905a5dff88eb1872d9e1a1880e5c8cd302ed3d20008de53cf07c83ca6a131d",
        }
        self.assertEqual(set(pin["files"]), set(expected))
        for name, digest in expected.items():
            with self.subTest(file=name):
                info = pin["files"][name]
                self.assertEqual(info["sha256"], digest)
                self.assertEqual(hashlib.sha256((root / name).read_bytes()).hexdigest(), digest)
                self.assertEqual(
                    info["url"],
                    f"https://github.com/{pin['repo']}/blob/{pin['commit']}/{info['path']}",
                )
