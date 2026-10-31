"""Unchanged, redistributable archival pins; metadata never upgrades delivered bytes."""

import hashlib
import json
import unittest
from pathlib import Path


class HoldingPins(unittest.TestCase):
    def test_bytes_provenance_and_redistribution_licences(self):
        root = Path(__file__).parent
        expected = {
            "ehri-holdings-1.1-1c2325f9": {
                "holdings.shacl.ttl": "39798f412e5fb3e2d7d012b80817e1e278665ebcbb88927d3bc77b6dc631e278",
                "holdings.shex": "ded21267f8268f41ff1e82a19fff32b6267aed1660fc7330d54a0a022812c405",
                "repositories.shacl.ttl": "ff3eeba4dce6a6bd0a4b71cb39a1e43c5cc772754c97cae809e44a1147d76964",
                "repositories.shex": "895b14b9c2ba83292e861201a89d083d51faac291f022454fa45fe5dbb9a8c0c",
                "LICENSE.md": "44905a5dff88eb1872d9e1a1880e5c8cd302ed3d20008de53cf07c83ca6a131d",
            },
            "ead3-1.1.1-c3576974": {
                "ead3.xsd": "c357697461e566a880098a72eec6af2c1af9d3137bee27819206b29acd30459b",
                "LICENSE": "36ffd9dc085d529a7e60e1276d73ae5a030b020313e6c5408593a6ae2af39673",
            },
        }
        for folder, files in expected.items():
            pin = json.loads((root / folder / "pin.json").read_text())
            self.assertEqual(pin["read_on"], "2026-10-31")
            self.assertEqual(set(pin["files"]), set(files))
            for name, sha in files.items():
                with self.subTest(folder=folder, file=name):
                    self.assertEqual(pin["files"][name]["sha256"], sha)
                    self.assertEqual(
                        hashlib.sha256((root / folder / name).read_bytes()).hexdigest(), sha
                    )
                    self.assertTrue(pin["files"][name]["url"].startswith("https://"))
            if folder.startswith("ehri"):
                self.assertEqual(pin["commit"], "1c2325f9d2267a8a0c639cd041be54ec9a73e517")
                self.assertEqual(pin["license"], "EUPL-1.2")
            else:
                self.assertEqual(pin["version"], "1.1.1")
                self.assertEqual(pin["license"], "CC0-1.0")
                self.assertIn("Release: 1.1.1", (root / folder / "ead3.xsd").read_text())
