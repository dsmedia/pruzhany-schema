"""The owner's 30–31 October 2026 shape pin is immutable and self-contained."""

import hashlib
import json
import unittest
from pathlib import Path


class ImpressoPin(unittest.TestCase):
    def test_unchanged_upstream_files_and_provenance(self):
        root = Path(__file__).parent / "impresso-329323c"
        pin = json.loads((root / "pin.json").read_text(encoding="utf-8"))
        self.assertEqual(pin["repo"], "impresso/impresso-schemas")
        self.assertEqual(pin["commit"], "329323c73712c33110e28531726847210617c418")
        self.assertEqual(pin["read_on"], "2026-10-31")
        self.assertEqual(pin["license"], "AGPL-3.0-or-later")
        self.assertTrue(pin["attribution"])
        expected = {'issue.schema.json': '96d3b80366d3e37b52e9ec7b0d0758133d19b739db9de94fe03b6c23e0ada799', 'page.schema.json': 'b6a6ca37167b30d318eb175a844dc50c80d245f9753ddc279a5e198b47f53b2c', 'paper_contentitem.schema.json': '3aa22833cb9ff069a86f94f5775d73dac727f45b854ca72a0260ab734a98bc9a', 'LICENSE': '8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef'}
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
