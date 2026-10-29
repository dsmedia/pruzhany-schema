"""Synthetic proof of the public-view export; never read historical people in this suite."""

import copy
import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import ValidationError
from rdflib import BNode, Graph, Literal, RDF, URIRef

from support import LINKML, ROOT, load

runtime, generator = load("rdf_runtime"), load("rdf_generator")
BASE = "https://example.org/fictional/"


def fixture():
    return [
        (
            "SharedPerson",
            {
                "id": "person/fictional א",
                "name": "Fictional person",
                "gender": "unknown",
            },
        ),
        (
            "SharedPerson",
            {"id": "person-child", "name": "Fictional child", "gender": "unknown"},
        ),
        ("Source", {"id": "source-book", "title": "Fictional book", "kind": "book"}),
        (
            "SharedPlace",
            {"id": "place-fictional", "name": "Fictional place", "coordinates": [1, 1]},
        ),
        (
            "SharedFact",
            {
                "id": "fact-fictional",
                "subject_id": "person/fictional א",
                "type": "death",
                "value": "perished",
                "status": "disputed",
                "review": {"state": "pending"},
                "attribution": {"by": "Fictional reader", "on": "2026-10-29"},
                "evidence_confidence": "possible",
                "identity_confidence": "probable",
                "qualifiers": {"witness": "record"},
                "date": {"start": "1942", "precision": "year"},
                "citations": [
                    {
                        "source_id": "source-book",
                        "url": "https://example.org/book",
                        "unit_id": "fictional-content",
                    }
                ],
            },
        ),
        (
            "SharedEvent",
            {
                "id": "event-fictional",
                "name": "Fictional event",
                "type": "death",
                "dates": [{"start": "1942", "record_fact_id": "fact-fictional"}],
                "main_people": [
                    {"person_id": "person/fictional א", "part": "deceased"}
                ],
            },
        ),
        (
            "PrintedAddress",
            {
                "image_uri": "fictional-scan",
                "bbox": [1, 1, 2, 2],
                "text": "Fictional words",
            },
        ),
        (
            "SourcedRelation",
            {
                "subject_id": "person/fictional א",
                "related_person_id": "person-child",
                "relationship_type": "parent_of",
                "review": {
                    "state": "approved",
                    "by": "Fictional reader",
                    "on": "2026-10-29",
                },
            },
        ),
    ]


class RdfExport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile, cls.context, cls.shapes = runtime.load_bundle(ROOT)

    def encoder(self):
        return runtime.Encoder(self.profile, self.context, BASE)

    def document(self):
        encoder = self.encoder()
        for model, value in fixture():
            encoder.add(
                model,
                value,
                None if "id" in value else encoder.derived("fixture", model, value),
            )
        return encoder.document()

    def node(self, document, kind):
        return next(
            n
            for n in document["@graph"]
            if isinstance(n["@type"], list) and kind in n["@type"]
        )

    def test_control_reifies_claims_and_preserves_order_repeats_ids_and_direction(self):
        doc = self.document()
        self.assertTrue(runtime.check_graph(doc, self.shapes)["conforms"])
        graph = Graph().parse(data=json.dumps(doc), format="json-ld")
        person = URIRef(self.encoder().iri("person/fictional א"))
        fact = URIRef(self.encoder().iri("fact-fictional"))
        self.assertIn((fact, RDF.subject, person), graph)
        self.assertFalse(
            list(
                graph.objects(
                    person, URIRef(generator.PREFIXES["rico"] + "hasDeathDate")
                )
            )
        )
        relation = URIRef(self.node(doc, "SourcedRelation")["@id"])
        self.assertIn((relation, RDF.subject, person), graph)
        self.assertIn(
            (relation, RDF.object, URIRef(self.encoder().iri("person-child"))), graph
        )
        self.assertIn(
            (relation, RDF.predicate, URIRef(generator.PREFIXES["rico"] + "hasChild")),
            graph,
        )
        bbox = URIRef(
            self.profile["models"]["PrintedAddress"]["fields"]["bbox"]["predicate"]
        )
        head = next(graph.objects(None, bbox))
        self.assertEqual([v.toPython() for v in graph.items(head)], [1, 1, 2, 2])
        self.assertEqual(self.node(doc, "SharedFact")["status"], "disputed")
        self.assertIn("person/fictional א", runtime.encoded(doc))
        self.assertEqual(
            len([n for n in doc["@graph"] if n["@type"] == "Reference"]), 1
        )

    def test_missing_unknown_null_enum_uri_and_tuple_faults_refused(self):
        for model, base, field, bad in [
            ("SharedPerson", fixture()[0][1], "gender", "invented"),
            ("SharedPerson", fixture()[0][1], "name", None),
            ("Citation", {"source_id": "source-book"}, "url", "https://[broken"),
            ("SharedPlace", fixture()[3][1], "coordinates", [91, 1]),
            ("PrintedAddress", fixture()[6][1], "bbox", [1, 1, 0, 2]),
            ("PrintedAddress", fixture()[6][1], "bbox", [1, 1, 2]),
            ("SharedPerson", fixture()[0][1], "private_notes", "canary"),
        ]:
            with (
                self.subTest(model=model, field=field),
                self.assertRaises((ValueError, ValidationError)),
            ):
                self.encoder().add(model, {**base, field: bad}, BASE + "test")
        with self.assertRaisesRegex(ValueError, "missing required"):
            self.encoder().add(
                "SharedPerson", {"id": "person-fictional"}, BASE + "test"
            )

    def test_optional_list_can_be_absent_but_present_empty_minimum_fails(self):
        encoder = self.encoder()
        encoder.add("SharedPlace", {"id": "place", "name": "Fictional place"})
        self.assertTrue(
            runtime.check_graph(encoder.document(), self.shapes)["conforms"]
        )
        doc = self.document()
        self.node(doc, "SharedPlace")["coordinates"] = []
        with self.assertRaises(ValueError):
            runtime.check_graph(doc, self.shapes)

    def test_mutated_graph_missing_field_type_unknown_predicate_reference_and_format_fail(
        self,
    ):
        cases = [
            ("SharedPerson", "gender", "invented"),
            ("SharedPerson", "name", None),
            ("SharedPerson", generator.PC + "private", "canary"),
            ("Citation", "source_id", {"@id": BASE + "nonexistent"}),
            ("Citation", "url", "https://[broken"),
            (
                "SharedFact",
                "assertion_predicate",
                generator.PC + "export_assertion_birth",
            ),
            ("PrintedAddress", "bbox", [1, 1, 0, 2]),
            ("SharedPlace", "coordinates", [91, 1]),
        ]
        for model, field, value in cases:
            with self.subTest(model=model, field=field):
                doc = self.document()
                self.node(doc, model)[field] = value
                with self.assertRaises((ValueError, ValidationError)):
                    runtime.check_graph(doc, self.shapes)
        doc = self.document()
        ref = next(n for n in doc["@graph"] if n["@type"] == "Reference")
        ref["target_model"] = "WrongModel"
        with self.assertRaises(ValueError):
            runtime.check_graph(doc, self.shapes)

    def test_list_cycle_multiple_edges_and_missing_rest_fail(self):
        for fault in ("cycle", "multiple", "missing"):
            graph = Graph()
            a, b = BNode("a"), BNode("b")
            graph.add((a, RDF.first, Literal(1)))
            if fault != "missing":
                graph.add((a, RDF.rest, a if fault == "cycle" else RDF.nil))
            if fault == "multiple":
                graph.add((a, RDF.rest, b))
            with self.subTest(fault=fault), self.assertRaises(ValueError):
                runtime.check_lists(graph)

    def test_output_determinism_and_input_preservation(self):
        original = fixture()
        before = copy.deepcopy(original)
        encoder = self.encoder()
        for model, value in reversed(original):
            encoder.add(
                model,
                value,
                None if "id" in value else encoder.derived("fixture", model, value),
            )
        self.assertEqual(
            runtime.encoded(encoder.document()), runtime.encoded(self.document())
        )
        self.assertEqual(original, before)

    def test_explicit_namespace_collision_and_wrong_target_kind(self):
        for bad in (
            "http://example.org/",
            "https://example.org",
            "https://u:p@example.org/",
            "https://example.org/?x",
            "https://example.org/#x",
        ):
            with self.subTest(base=bad), self.assertRaises(ValueError):
                runtime.base_iri(bad)
        encoder = self.encoder()
        encoder.add(*fixture()[0])
        with self.assertRaisesRegex(ValueError, "conflicting public"):
            encoder.add(
                "Source",
                {"id": fixture()[0][1]["id"], "kind": "book", "title": "Conflict"},
            )
        encoder = self.encoder()
        encoder.add(*fixture()[0])
        encoder.reference(fixture()[0][1]["id"], "Source")
        with self.assertRaisesRegex(ValueError, "wrong model"):
            encoder.document()

    def test_profile_exhaustiveness_and_reproducible_artifacts(self):
        index = json.loads((LINKML / "generated/docs/model-index.json").read_text())
        contract = json.loads((LINKML / "generated/contract.json").read_text())
        config = json.loads((LINKML / "rdf-profile.yaml").read_text())
        for mutate in ("model", "field", "reason"):
            candidate = copy.deepcopy(config)
            if mutate == "model":
                candidate["omitted_models"].pop(next(iter(candidate["omitted_models"])))
            elif mutate == "field":
                candidate["models"]["SharedPerson"]["fields"].remove("name")
            else:
                candidate["models"]["SharedPerson"]["reason"] = ""
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                generator.make_profile(index, candidate, contract)
        with tempfile.TemporaryDirectory() as folder:

            def write(path, text):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text.rstrip() + "\n", encoding="utf-8")

            generator.write_rdf(LINKML, Path(folder), index, contract, write)
            for path in (Path(folder) / "rdf").iterdir():
                self.assertEqual(
                    path.read_bytes(),
                    (LINKML / "generated/rdf" / path.name).read_bytes(),
                )

    def test_constants_unsupported_unions_and_unhandled_constraints_fail(self):
        for model, value in [
            ("LifeEventDate", {"qualifier": "invented"}),
            ("SharedEvent", {**fixture()[5][1], "evidence_basis": "invented"}),
        ]:
            with self.subTest(model=model), self.assertRaises(ValueError):
                self.encoder().add(model, value, BASE + "test")
        with self.assertRaisesRegex(ValueError, "alternative branch"):
            generator.resolved({"anyOf": [{"type": "number"}, {"type": "string"}]}, {})
        with self.assertRaisesRegex(ValueError, "recursive"):
            generator.resolved(
                {"$ref": "#/$defs/A"}, {"$defs": {"A": {"$ref": "#/$defs/A"}}}
            )
        index = json.loads((LINKML / "generated/docs/model-index.json").read_text())
        config = json.loads((LINKML / "rdf-profile.yaml").read_text())
        contract = json.loads((LINKML / "generated/contract.json").read_text())
        next(
            f for f in index["models"]["SharedPerson"]["fields"] if f["name"] == "name"
        )["shape"]["not"] = {"const": "no"}
        with self.assertRaisesRegex(ValueError, "unsupported RDF field"):
            generator.make_profile(index, config, contract)

    def test_position_overrides_match_the_live_zod_tuple_contract(self):
        import shutil
        import subprocess

        result = subprocess.run(
            [
                shutil.which("bun"),
                "-e",
                "import {z} from 'zod/v4'; import {PrintedAddressSchema} from './zod/site-common.schema'; "
                "import {SharedPlaceSchema} from './zod/shared-record.schema'; "
                "console.log(JSON.stringify([z.toJSONSchema(PrintedAddressSchema),z.toJSONSchema(SharedPlaceSchema)]))",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        bbox, place = json.loads(result.stdout)
        for model, key, shape in [
            ("PrintedAddress", "bbox", bbox["properties"]["bbox"]),
            (
                "SharedPlace",
                "coordinates",
                place["properties"]["coordinates"]["anyOf"][0],
            ),
        ]:
            positions = [
                {k: v for k, v in p.items() if k != "type"}
                for p in shape["prefixItems"]
            ]
            self.assertEqual(
                self.profile["models"][model]["fields"][key]["positions"], positions
            )

    def test_evidence_edges_point_to_resources_not_to_lists_or_citation_locators(self):
        doc = self.document()
        graph = Graph().parse(data=json.dumps(doc), format="json-ld")
        evidence = URIRef(generator.PREFIXES["rico"] + "isEvidencedBy")
        self.assertEqual(
            set(graph.objects(None, evidence)),
            {URIRef(self.encoder().iri("source-book"))},
        )
        fact = self.node(doc, "SharedFact")
        fact["evidence_sources"] = [BASE + "id/fictional-content"]
        with self.assertRaisesRegex(ValueError, "differ from citation"):
            runtime.check_graph(doc, self.shapes)

    def test_stale_definition_profile_context_and_shapes_fail_before_export(self):
        import shutil

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = [
                "linkml/rdf-profile.yaml",
                "linkml/rdf_generator.py",
                "linkml/generated/docs/model-index.json",
                "linkml/generated/contract.json",
            ]
            files += list(self.profile["source_sha256"])
            files += [
                "linkml/generated/rdf/" + p.name
                for p in (LINKML / "generated/rdf").iterdir()
            ]
            for name in files:
                destination = root / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, destination)
            runtime.load_bundle(root)
            for name in (
                "linkml/schema/shared_record.yaml",
                "linkml/generated/rdf/context.jsonld",
                "linkml/generated/rdf/shapes.ttl",
            ):
                path = root / name
                saved = path.read_bytes()
                path.write_bytes(saved + b"\n")
                with (
                    self.subTest(name=name),
                    self.assertRaisesRegex(ValueError, "stale"),
                ):
                    runtime.load_bundle(root)
                path.write_bytes(saved)
            path = root / "linkml/generated/rdf/profile.json"
            profile = json.loads(path.read_text())
            profile["models"]["SharedPerson"]["fields"]["name"]["required"] = False
            path.write_text(json.dumps(profile))
            with self.assertRaisesRegex(ValueError, "stale generated"):
                runtime.load_bundle(root)

    def test_derived_event_roles_and_types_cannot_disagree_with_preserved_fields(self):
        for field, value in [
            ("event_type", generator.PC + "event_types_birth"),
            ("role_deceased", [BASE + "id/person-child"]),
        ]:
            document = self.document()
            self.node(document, "SharedEvent")[field] = value
            with (
                self.subTest(field=field),
                self.assertRaisesRegex(ValueError, "differ"),
            ):
                runtime.check_graph(document, self.shapes)
