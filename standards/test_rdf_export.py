"""Every export mapping is checked against pins; every new local term needs a reason."""

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_alignment import check_export

ROOT = Path(__file__).resolve().parents[1]


class ExportAlignment(unittest.TestCase):
    def test_current_export_is_aligned(self):
        self.assertEqual(check_export(ROOT), [])

    def test_unpinned_undeclared_and_unexplained_terms_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "standards", root / "standards")
            folder = root / "linkml/generated/rdf"
            shutil.copytree(ROOT / "linkml/generated/rdf", folder)
            context = folder / "context.jsonld"
            original = context.read_text()
            for term, message in [
                ("https://www.ica.org/standards/RiC/ontology#Unpinned", "unapproved"),
                ("http://lod.ehri-project-test.eu/ontology#Unpinned", "unapproved"),
                (
                    "https://pruzhany.org/ns/sourced-entities#export_Undeclared",
                    "undeclared",
                ),
            ]:
                value = json.loads(original)
                value["@context"]["bad"] = term
                context.write_text(json.dumps(value))
                self.assertTrue(any(message in e for e in check_export(root)))
            context.write_text(original)
            ontology = folder / "ontology.ttl"
            ontology.write_text(
                "\n".join(
                    line
                    for line in ontology.read_text().splitlines()
                    if "<http://www.w3.org/2000/01/rdf-schema#comment>" not in line
                )
            )
            self.assertTrue(any("unexplained" in e for e in check_export(root)))
