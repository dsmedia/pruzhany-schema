"""Behavioral checks: real newspaper pilot plus explicitly fictional edge cases."""
import copy
import hashlib
import json
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, URIRef
from build import HERE, BASE, PC, RICO, Pilot, artifacts, edition_views, make_pilot, public_projection, residence_at, rico_export
from contract_cases import synthetic, fact, cases


class PilotTests(unittest.TestCase):
    def test_real_scope_and_evidence(self):
        data = make_pilot()
        self.assertEqual((len(data["people"]), len(data["events"]), len(data["mentions"]), len(data["facts"])), (12, 2, 22, 8))
        self.assertTrue(all(not p.get("fate") for p in data["people"]))
        self.assertTrue(all(f["citation_ids"] and f["review"]["state"] == "pending" for f in data["facts"]))
        self.assertEqual(set(edition_views(data)), {"1934-02-02", "1934-02-09", "1938-12-16"})
        self.assertTrue(all(f["type"] != "marriage" for f in data["facts"] if f.get("event_id")))

    def test_reversals_preserve_all_source_observations(self):
        data = make_pilot()
        reversed_data = make_pilot(reverse=[d["id"] for d in data["identity_decisions"]])
        self.assertEqual((len(reversed_data["people"]), len(reversed_data["events"])), (13, 4))
        key = lambda d: {(m["id"], m["original_entity_id"], m["citation_id"], m["printed_name"]) for m in d["mentions"]}
        self.assertEqual(key(data), key(reversed_data))
        self.assertEqual(data["citations"], reversed_data["citations"])
        self.assertEqual(make_pilot(), data)
        with self.assertRaisesRegex(ValueError, "unknown identity"):
            make_pilot(reverse=["invented-decision"])

    def test_temporal_residence_and_contradictions(self):
        data = synthetic()
        data["facts"] = [
            fact("residence", id="test-prewar-home", place_id="test-place-a", date={"start": "1937-01-01", "end": "1939-12-31", "precision": "range"}),
            fact("residence", id="test-postwar-home", place_id="test-place-b", date={"start": "1948-01-01", "end": "1950-12-31", "precision": "range"}),
        ]
        Pilot.model_validate(data)
        self.assertEqual(residence_at(data, "test-person-a", "1938-12-16"), "test-place-a")
        self.assertEqual(residence_at(data, "test-person-a", "1949-01-01"), "test-place-b")
        self.assertIsNone(residence_at(data, "test-person-a", "1945-01-01"))
        data["facts"].append(fact("residence", id="test-conflicting-home", place_id="test-place-b", date={"start": "1938", "precision": "year"}))
        with self.assertRaisesRegex(ValueError, "conflicting residences"):
            residence_at(data, "test-person-a", "1938-12-16")

    def test_real_preview_publishes_only_printed_names(self):
        public = public_projection(make_pilot())
        self.assertEqual(len(public["people"]), 12)
        self.assertEqual([public["facts"], public["relationships"], public["citations"]], [[], [], []])
        self.assertNotIn("née", json.dumps(public))

    def test_review_confidence_and_privacy_are_independent(self):
        data = synthetic()
        data["facts"] = [fact(evidence_confidence="possible", identity_confidence="possible")]
        self.assertEqual(public_projection(data)["facts"][0]["evidence_confidence"], "possible")
        data["facts"][0]["review"] = {"state": "pending"}
        self.assertFalse(public_projection(data)["facts"])
        data["facts"][0]["review"] = {"state": "approved", "by": "test", "on": "2026-10-19"}
        data["people"][0]["presumed_living"] = True
        self.assertFalse(public_projection(data)["facts"])

    def test_urls_and_quotes_do_not_grant_clearance(self):
        data = synthetic()
        data["facts"] = [fact()]
        for url in ["http://archive.org/details/x", "https://archive.org.evil.example/x", "https://evil.example/archive.org", "https://user@archive.org/x", "https://[invalid"]:
            data["citations"][0]["url"] = url
            self.assertFalse(public_projection(data)["facts"], url)
        data["citations"][0]["url"] = "https://archive.org/details/fictional-test-only"
        data["citations"][0]["quote"] += " PRIVATE QUOTE"
        data["citations"][0]["note"] = "PRIVATE NOTE"
        public = public_projection(data)
        self.assertEqual(len(public["facts"]), 1)
        self.assertNotIn("PRIVATE", json.dumps(public))

    def test_relationship_to_presumed_living_person_stays_private(self):
        data = synthetic()
        data["relationships"] = [{"id": "test-relationship", "from_id": "test-person-a", "to_id": "test-person-b", "type": "spouse", "citation_ids": ["test-citation"], "evidence_confidence": "confirmed", "identity_confidence": "confirmed", "status": "accepted", "review": {"state": "approved", "by": "test", "on": "2026-10-19"}}]
        self.assertEqual(len(public_projection(data)["relationships"]), 1)
        data["people"][1]["presumed_living"] = True
        self.assertFalse(public_projection(data)["relationships"])

    def test_unapproved_identity_join_blocks_promotion(self):
        data = make_pilot()
        f = data["facts"][0]
        for p in data["people"]:
            p["presumed_living"] = False
        f["review"] = {"state": "approved", "by": "test", "on": "2026-10-19"}
        f["identity_confidence"] = "confirmed"
        self.assertFalse(public_projection(data)["facts"])
        graph = self.rdf(data)
        self.assertFalse(list(graph.triples((None, URIRef(RICO + "isOrWasParticipantIn"), None))))

    def rdf(self, data):
        return Graph().parse(data=json.dumps(rico_export(data)), format="json-ld")

    def test_pending_rdf_assertions_are_reified(self):
        graph = self.rdf(make_pilot())
        rico = Namespace(RICO)
        owl = Namespace("http://www.w3.org/2002/07/owl#")
        self.assertFalse(list(graph.triples((None, owl.sameAs, None))))
        self.assertFalse(list(graph.triples((None, rico.relationState, None))))
        self.assertFalse(list(graph.triples((None, rico.hasOrHadSpouse, None))))
        self.assertFalse(list(graph.triples((None, rico.isOrWasParticipantIn, None))))
        self.assertEqual(len(list(graph.subjects(RDF.type, RDF.Statement))), 9)  # eight facts, one relationship
        self.assertEqual(len(list(graph.subjects(RDF.type, rico.Person))), 12)

    def test_reviewed_claim_can_export_as_sourced_rico_relation(self):
        data = synthetic()
        data["facts"] = [fact("marriage", related_person_id="test-person-b")]
        graph = self.rdf(data)
        rico = Namespace(RICO)
        self.assertIn((URIRef(BASE + "test-person-a"), rico.hasOrHadSpouse, URIRef(BASE + "test-person-b")), graph)
        self.assertIn((URIRef(BASE + "test-fact"), RDF.type, rico.Relation), graph)
        self.assertIn((URIRef(BASE + "test-citation"), rico.evidences, URIRef(BASE + "test-fact")), graph)
        self.assertIn((URIRef(BASE + "test-fact"), rico.relationHasSource, URIRef(BASE + "test-citation")), graph)

    def test_date_range_and_hebrew_printed_date_survive_jsonld(self):
        data = synthetic()
        data["facts"] = [fact("birth", date={"start": "1938", "precision": "year", "printed": "תרצ״ח", "printed_calendar": "hebrew", "inferred": True})]
        graph = self.rdf(data)
        rico = Namespace(RICO)
        self.assertIn((URIRef(BASE + "test-fact-date"), RDF.type, rico.Date), graph)
        payload = graph.value(URIRef(BASE + "test-fact"), URIRef(PC + "payload"))
        self.assertEqual(json.loads(str(payload))["date"]["printed"], "תרצ״ח")

    def test_conflicting_dates_and_rejected_claims_are_retained_without_assertion(self):
        data = synthetic()
        data["facts"] = [fact("birth", id="test-date-a", date={"start": "1938", "precision": "year"}, status="disputed"), fact("birth", id="test-date-b", date={"start": "1939", "precision": "year"}, status="rejected")]
        Pilot.model_validate(data)
        graph = self.rdf(data)
        self.assertEqual(len(list(graph.subjects(RDF.type, RDF.Statement))), 2)
        self.assertFalse(list(graph.triples((None, URIRef(RICO + "hasBirthDate"), None))))
        self.assertFalse(public_projection(data)["facts"])

    def test_only_real_rico_terms_are_used(self):
        profile = json.loads((HERE / "ric-o-profile.json").read_text())
        known = {v["iri"] for v in profile["terms"].values()}
        data = synthetic()
        data["facts"] = [fact("birth", date={"start": "1938", "precision": "year"})]
        for graph in [self.rdf(make_pilot()), self.rdf(data)]:
            used = {str(x) for triple in graph for x in triple if isinstance(x, URIRef) and str(x).startswith(RICO)}
            self.assertFalse(used - known, used - known)
        self.assertIn("present, past", profile["terms"]["relationState"]["comment"][0])

    def test_local_extensions_are_declared(self):
        profile = Graph().parse(HERE / "profile.ttl", format="turtle")
        graph = self.rdf(make_pilot())
        local = {x for triple in graph for x in triple if isinstance(x, URIRef) and str(x).startswith(PC)}
        for term in local:
            self.assertTrue(list(profile.triples((term, RDF.type, None))), term)

    def test_reproducible_outputs(self):
        for name, text in artifacts(make_pilot()).items():
            self.assertEqual((HERE / "generated" / name).read_text(), text, name)


if __name__ == "__main__":
    unittest.main()
