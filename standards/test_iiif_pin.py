"""Validate fictional manifests with the fetched pin, and refuse damaged or missing downloads."""

import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

from jsonschema import Draft7Validator, FormatChecker, ValidationError

from fetch_iiif import CACHE, PIN, fetch

ROOT = Path(__file__).resolve().parents[1]
COMMIT = "3891f47ce7dbaa896027a5fab5f63a109de4bd70"
DIGEST = "14dd7ee8aee25d959be4b12feddb4179c726909fc85b925f6707f4ab3bfe2ad6"


class IIIFPin(unittest.TestCase):
    def test_unchanged_schema_and_provenance(self):
        folder = (ROOT / PIN).parent
        pin = json.loads((ROOT / PIN).read_text(encoding="utf-8"))
        self.assertEqual(pin["repo"], "IIIF/presentation-validator")
        self.assertEqual(pin["commit"], COMMIT)
        self.assertEqual(pin["read_on"], "2026-10-31")
        self.assertEqual(
            pin["license"], "not redistributed: the upstream repository grants no licence"
        )
        self.assertTrue(pin["attribution"])
        self.assertEqual(set(pin["files"]), {"iiif_3_0.json"})
        info = pin["files"]["iiif_3_0.json"]
        self.assertEqual(info["sha256"], DIGEST)
        self.assertEqual(
            info["url"], f"https://raw.githubusercontent.com/{pin['repo']}/{COMMIT}/{info['path']}"
        )
        self.assertFalse((folder / "iiif_3_0.json").exists())
        self.assertFalse((folder / "upstream-README.md").exists())
        raw = fetch(ROOT).read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), DIGEST)
        schema = json.loads(raw)
        self.assertEqual(schema["$schema"], "http://json-schema.org/draft-07/schema#")
        # Upstream schema/iiif_3_0.json and Python jsonschema 4.26.0 Schema Validation,
        # read 31 October 2026: https://python-jsonschema.readthedocs.io/en/v4.26.0/validate/
        validator = Draft7Validator(
            {**schema, "$ref": "#/classes/manifest"}, format_checker=FormatChecker()
        )
        manifest = {
            "@context": "http://iiif.io/api/presentation/3/context.json",
            "id": "https://example.org/fictional/manifest",
            "type": "Manifest",
            "label": {"en": ["A fictional newspaper edition"]},
            "items": [],
        }
        validator.validate(manifest)
        manifest["label"] = {"en": "not an array"}
        with self.assertRaises(ValidationError):
            validator.validate(manifest)

    def make_pin(self, root, raw=b"{}"):
        pin = json.loads((ROOT / PIN).read_text(encoding="utf-8"))
        pin["files"]["iiif_3_0.json"]["sha256"] = hashlib.sha256(raw).hexdigest()
        path = root / PIN
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(pin), encoding="utf-8")

    def test_download_and_cache_are_verified(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_pin(root)
            with patch("fetch_iiif.urllib.request.urlopen", return_value=io.BytesIO(b"{}")) as get:
                target = fetch(root)
                self.assertEqual(target, root / CACHE)
                self.assertEqual(target.read_bytes(), b"{}")
                self.assertEqual(fetch(root), target)
                get.assert_called_once()
            target.write_bytes(b"changed")
            with patch("fetch_iiif.urllib.request.urlopen") as get:
                with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
                    fetch(root)
                get.assert_not_called()

    def test_download_mismatch_and_failure_leave_no_cache(self):
        for response in (io.BytesIO(b"changed"), URLError("network unavailable")):
            with (
                self.subTest(response=type(response).__name__),
                tempfile.TemporaryDirectory() as temporary,
            ):
                root = Path(temporary)
                self.make_pin(root)
                arguments = (
                    {"side_effect": response}
                    if isinstance(response, URLError)
                    else {"return_value": response}
                )
                with patch("fetch_iiif.urllib.request.urlopen", **arguments):
                    with self.assertRaises((ValueError, URLError)):
                        fetch(root)
                self.assertFalse((root / CACHE).exists())
                self.assertFalse((root / CACHE).parent.exists())

    def test_unpinned_url_is_refused_even_with_cache(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_pin(root)
            pin_path = root / PIN
            pin = json.loads(pin_path.read_text(encoding="utf-8"))
            pin["files"]["iiif_3_0.json"]["url"] = (
                "https://raw.githubusercontent.com/IIIF/presentation-validator/main/schema/iiif_3_0.json"
            )
            pin_path.write_text(json.dumps(pin), encoding="utf-8")
            target = root / CACHE
            target.parent.mkdir(parents=True)
            target.write_bytes(b"{}")
            with patch("fetch_iiif.urllib.request.urlopen") as get:
                with self.assertRaisesRegex(ValueError, "invalid IIIF schema pin"):
                    fetch(root)
                get.assert_not_called()
