"""Offline processor checks; every new example is fictional."""

import copy
import json
import unittest
from unittest.mock import patch

import test_rdf_export as exports
from support import ROOT

runtime = exports.runtime


class JsonLd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exports.RdfExport.setUpClass()
        cls.export = exports.RdfExport()
        cls.shapes = cls.export.shapes

    def document(self):
        return copy.deepcopy(self.export.document())

    def test_each_independent_fault_fails_in_the_shared_export_check(self):
        for fault, diagnostic in (
            ("top", "unmapped_top_level"),
            ("nested", "unmapped_nested"),
            ("type", "@type.*UnmappedFictionalType"),
            ("id", "@id"),
        ):
            document = self.document()
            if fault == "top":
                document["@graph"][0]["unmapped_top_level"] = "fictional canary"
            elif fault == "nested":
                fact = self.export.node(document, "SharedFact")
                fact["citations"][0]["unmapped_nested"] = "fictional canary"
            elif fault == "type":
                document["@graph"][0]["@type"].append("UnmappedFictionalType")
            else:
                document["@graph"][0]["@id"] = 42
            with self.subTest(fault=fault), self.assertRaisesRegex(ValueError, diagnostic):
                runtime.check_graph(document, self.shapes)

    def test_nested_type_and_syntax_errors_are_checked_too(self):
        for key, value, diagnostic in (
            ("@type", "UnmappedNestedType", "@type.*UnmappedNestedType"),
            ("@id", 42, "@id"),
            ("@value", {"fictional": "invalid non-JSON literal"}, "@value"),
        ):
            document = self.document()
            fact = self.export.node(document, "SharedFact")
            fact["citations"][0][key] = value
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, diagnostic):
                runtime.check_graph(document, self.shapes)

    def test_controls_validate_offline_and_preserve_every_input_byte(self):
        encoder = self.export.encoder()
        encoder.add("SharedPlace", {"id": "place", "name": "Fictional place"})
        for document in (self.document(), encoder.document()):
            before = runtime.encoded(document)
            with (
                patch("socket.socket", side_effect=AssertionError("network called")),
                patch("socket.create_connection", side_effect=AssertionError("network called")),
            ):
                self.assertTrue(runtime.check_graph(document, self.shapes)["conforms"])
            self.assertEqual(runtime.encoded(document), before)

    def test_existing_pilot_still_expands_offline_without_modification(self):
        # Its independent ontology profile stays isolated from production SHACL.
        path = ROOT / "pilots/sourced-entities/generated/review.jsonld"
        before = path.read_bytes()
        document = json.loads(before)
        original = copy.deepcopy(document)
        with (
            patch("socket.socket", side_effect=AssertionError("network called")),
            patch("socket.create_connection", side_effect=AssertionError("network called")),
        ):
            runtime.check_jsonld(document)
        self.assertEqual(document, original)
        self.assertEqual(path.read_bytes(), before)

    def test_remote_contexts_and_imports_fail_before_either_parser_runs(self):
        for fault in ("root", "node", "array", "used-scope", "unused-scope", "import", "scoped-import"):
            document = self.document()
            remote = "https://example.invalid/fictional-context"
            if fault == "root":
                document["@context"] = remote
            elif fault == "node":
                document["@graph"][0]["@context"] = remote
            elif fault == "array":
                document["@graph"][0]["@context"] = [{}, remote]
            elif fault in ("used-scope", "unused-scope"):
                term = "SharedPerson" if fault == "used-scope" else "UnusedFictionalType"
                document["@context"][term] = {
                    "@id": "https://example.org/FictionalType",
                    "@context": remote,
                }
            elif fault == "import":
                document["@context"]["@import"] = remote
            else:
                document["@context"]["SharedPerson"]["@context"]["@import"] = remote
            with (
                self.subTest(fault=fault),
                patch.object(runtime.jsonld, "expand", side_effect=AssertionError("processor called")),
                patch.object(runtime.Graph, "parse", side_effect=AssertionError("parser called")),
                patch("socket.socket", side_effect=AssertionError("network called")),
                self.assertRaisesRegex(ValueError, "@context|@import"),
            ):
                runtime.check_graph(document, self.shapes)

    def test_json_literals_are_opaque_to_context_and_iri_checks(self):
        document = self.document()
        fact = self.export.node(document, "SharedFact")
        payload = {
            "@context": "https://example.invalid/fictional-data-only",
            "@import": "https://example.invalid/also-data",
            "@type": "UnmappedButOpaque",
            "@id": 42,
            "unmapped_literal_key": "fictional payload",
        }
        fact["assertion_object"] = {"@type": "@json", "@value": payload}
        with patch("socket.socket", side_effect=AssertionError("network called")):
            runtime.check_jsonld(document)
        self.assertEqual(fact["assertion_object"]["@value"], payload)

    def test_terms_are_checked_in_their_active_scope(self):
        # 'gender' is defined for SharedPerson, but must not be silently dropped
        # when a writer mistakenly emits it for Source.
        document = self.document()
        self.export.node(document, "Source")["gender"] = "unknown"
        with self.assertRaisesRegex(ValueError, "gender"):
            runtime.check_graph(document, self.shapes)
