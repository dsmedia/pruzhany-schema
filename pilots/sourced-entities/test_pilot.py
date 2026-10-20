"""Behavioral checks: real newspaper pilot plus explicitly fictional edge cases."""
import copy
import hashlib
import json
import unittest
from pathlib import Path
from rdflib import Graph, Namespace, RDF, URIRef
from build import HERE, BASE, PC, RICO, Pilot, artifacts, edition_views, make_pilot, public_projection, residence_at, rico_export, living_presumption, report
from contract_cases import synthetic, fact, cases


class PilotTests(unittest.TestCase):
    def test_real_scope_and_evidence(self):
        data = make_pilot()
        self.assertEqual((len(data["people"]), len(data["events"]), len(data["mentions"]), len(data["facts"])), (12, 2, 22, 6))
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
        self.assertEqual(len(public["people"]), 13)
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
        self.assertEqual(len(list(graph.subjects(RDF.type, RDF.Statement))), 7)  # six facts, one relationship
        self.assertEqual(len(list(graph.subjects(RDF.type, rico.Person))), 12)

    def test_reviewed_claim_can_export_as_sourced_rico_relation(self):
        data = synthetic()
        claim = fact()
        for key in ("subject_id", "value", "attributed_to"):
            claim.pop(key)
        claim.update(type="spouse", from_id="test-person-a", to_id="test-person-b")
        data["relationships"] = [claim]
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
        profile = json.loads((HERE / "ric-o-profile.json").read_text(encoding="utf-8"))
        known = {v["iri"] for v in profile["terms"].values()}
        data = synthetic()
        data["facts"] = [fact("birth", date={"start": "1938", "precision": "year"})]
        for graph in [self.rdf(make_pilot()), self.rdf(data)]:
            used = {str(x) for triple in graph for x in triple if isinstance(x, URIRef) and str(x).startswith(RICO)}
            self.assertFalse(used - known, used - known)
        self.assertIn("present, past", profile["terms"]["relationState"]["comment"][0])

    def test_local_extensions_are_declared(self):
        profile = Graph().parse(data=(HERE / "profile.ttl").read_text(encoding="utf-8"), format="turtle")
        graph = self.rdf(make_pilot())
        local = {x for triple in graph for x in triple if isinstance(x, URIRef) and str(x).startswith(PC)}
        for term in local:
            self.assertTrue(list(profile.triples((term, RDF.type, None))), term)

    def test_presumption_branches(self):
        for evidence, reason in [({"death": True}, "death-evidenced"),
                                 ({"fate": "perished"}, "death-evidenced"),
                                 ({"fate": "died_before"}, "death-evidenced"),
                                 ({"birth_year": 1916}, "born-110-years-ago"),
                                 ({"printed_years": [2020, 1941]}, "printed-in-old-source"),
                                 ({"shown": {"by": "Fictional Voucher", "on": "2026-10-19"}}, "shown-at-word")]:
            self.assertEqual(living_presumption(**evidence), (False, reason))
        self.assertEqual(living_presumption(birth_year=1917, printed_years=[1942], shown={"by": " ", "on": "2026-10-19"}), (True, "unknown"))
        data = synthetic()
        data["people"][0]["presumed_living"], data["people"][0]["presumption_reason"] = living_presumption()
        self.assertNotIn("test-person-a", {p["id"] for p in public_projection(data)["people"]})
        self.assertTrue(all(not p["presumed_living"] and p["presumption_reason"] == "printed-in-old-source" for p in make_pilot()["people"]))

    def test_vouch_requires_name_and_iso_day(self):
        for shown in [{"by": " ", "on": "2026-10-19"}, {"by": "Fictional Voucher"},
                      {"by": "Fictional Voucher", "on": "2026-02-30"},
                      {"by": "Fictional Voucher", "on": "20261019"},
                      {"by": "Fictional Voucher", "on": "2026-10-19T00:00:00"}]:
            self.assertEqual(living_presumption(shown=shown), (True, "unknown"), shown)

    def test_public_presumption_does_not_follow_pending_preview_join(self):
        data = synthetic()
        a, b = data["people"]
        a["original_ids"].append(b["id"])
        a["names"] += b["names"]
        a.update(presumed_living=False, presumption_reason="printed-in-old-source")
        data["people"] = [a]
        data["citations"][0].update(edition_date="1938-12-16")
        data["mentions"] = [{"id": "test-mention", "entity_id": a["id"],
                             "original_entity_id": a["id"], "citation_id": "test-citation",
                             "printed_name": "Test Person A", "roles": ["named"],
                             "text_sha256": hashlib.sha256(data["citations"][0]["quote"].encode()).hexdigest()}]
        data["identity_decisions"] = [{"id": "test-join", "kind": "person", "original_ids": a["original_ids"][:],
                                       "target_id": a["id"], "citation_ids": ["test-citation", "test-citation"],
                                       "confidence": "probable", "review": {"state": "pending"},
                                       "applied_in_preview": True, "reason": "Fictional test proposal"}]
        Pilot.model_validate(data)
        public = public_projection(data)["people"]
        self.assertEqual(public, [{"id": a["id"], "printed_names": ["Test Person A"], "spouse_ids": []}])
        data["identity_decisions"][0]["review"] = {"state": "approved", "by": "fictional reviewer", "on": "2026-10-19"}
        self.assertEqual(public_projection(data)["people"], public)
        # No mention evidence means neither original inherits the preview verdict
        # or attempts a lookup of the absent preview key for person B.
        data["identity_decisions"][0]["review"] = {"state": "pending"}
        data["mentions"] = []
        self.assertEqual(public_projection(data)["people"], [])
        data["identity_decisions"][0]["review"] = {"state": "approved", "by": "fictional reviewer", "on": "2026-10-19"}
        self.assertEqual(public_projection(data)["people"], [])

    def test_no_mention_names_are_person_local_and_printed(self):
        data = synthetic()
        data["people"][0]["names"].append({**data["people"][0]["names"][0], "value": "Fictional later label", "kind": "later"})
        data["citations"][0]["edition_date"] = "1938-12-16"
        data["mentions"] = [{"original_entity_id": "test-person-b", "citation_id": "test-citation", "printed_name": "Test Person B"}]
        public = public_projection(data)["people"]
        self.assertEqual([p["printed_names"] for p in public], [["Test Person A"], ["Test Person B"]])

    def test_report_uses_current_counts_year_and_reasons(self):
        data = make_pilot()
        data["as_of_year"] = 2030
        data["people"][0].update(presumed_living=True, presumption_reason="unknown")
        text = report(data)
        self.assertIn("Presumption as of 2030:", text)
        self.assertIn("11 **printed-in-old-source**, 1 **unknown**", text)
        self.assertIn("contains 13 person records", text)
        data["identity_decisions"][-1]["review"] = {"state": "approved", "by": "fictional reviewer", "on": "2026-10-19"}
        self.assertIn("contains 12 person records", report(data))
        reversed_data = make_pilot(reverse=[d["id"] for d in data["identity_decisions"]])
        self.assertIn("13 **printed-in-old-source**", report(reversed_data))
        self.assertIn("contains 13 person records", report(reversed_data))

    def test_public_join_approval_and_reversal(self):
        data = make_pilot()
        prefix = "person-menachem-yehuda-goldman-"
        people = [p for p in public_projection(data)["people"] if p["id"].startswith(prefix)]
        self.assertEqual(len(people), 2)
        self.assertTrue(all(len(p["printed_names"]) == 1 for p in people))
        decision = data["identity_decisions"][-1]
        decision["review"] = {"state": "approved", "by": "fictional reviewer", "on": "2026-10-19"}
        people = [p for p in public_projection(data)["people"] if p["id"].startswith(prefix)]
        self.assertEqual([p["id"] for p in people], [decision["target_id"]])
        self.assertEqual(len(people[0]["printed_names"]), 2)
        reversed_data = make_pilot(reverse=[d["id"] for d in data["identity_decisions"]])
        self.assertEqual({p["id"] for p in public_projection(reversed_data)["people"]}, {m["original_entity_id"] for m in data["mentions"]})

    def test_names_keep_language_and_script(self):
        from unittest.mock import patch
        from build import ANNOTATIONS
        annotations = copy.deepcopy(ANNOTATIONS)
        original, printed, role, _, script = annotations["cu-1934-02-02-i0109"][0]
        annotations["cu-1934-02-02-i0109"][0] = (original, printed, role, "yi", script)
        with patch("build.ANNOTATIONS", annotations):
            data = make_pilot()
        names = next(p for p in data["people"] if p["id"] == original)["names"]
        self.assertEqual({n["lang"] for n in names if n["value"] == printed}, {"he", "yi"})

    def test_public_references_use_public_people(self):
        data = synthetic()
        data["facts"] = [fact("parenthood", related_person_id="test-person-b")]
        public = public_projection(data)
        ids = {p["id"] for p in public["people"]}
        self.assertTrue(all(f["subject_id"] in ids and f["related_person_id"] in ids for f in public["facts"]))

    def test_reviews_are_independent(self):
        data = make_pilot()
        data["facts"][0]["review"]["state"] = "approved"
        self.assertTrue(all(f["review"]["state"] == "pending" for f in data["facts"][1:] + data["relationships"] + data["identity_decisions"]))

    def test_one_marriage_decision(self):
        data = synthetic()
        relationship = {"id": "test-marriage", "from_id": "test-person-a", "to_id": "test-person-b", "type": "spouse", "citation_ids": ["test-citation"], "evidence_confidence": "confirmed", "identity_confidence": "confirmed", "status": "accepted", "review": {"state": "pending"}}
        data["relationships"] = [relationship]
        self.assertTrue(all(not p["spouse_ids"] for p in public_projection(data)["people"]))
        relationship["review"] = {"state": "approved", "by": "fictional reviewer", "on": "2026-10-19"}
        self.assertEqual([p["spouse_ids"] for p in public_projection(data)["people"]], [["test-person-b"], ["test-person-a"]])
        graph = self.rdf(data)
        self.assertEqual(len(list(graph.triples((None, URIRef(RICO + "hasOrHadSpouse"), None)))), 1)
        self.assertEqual(len(list(graph.subjects(RDF.predicate, URIRef(RICO + "hasOrHadSpouse")))), 1)

    def test_annotation_languages(self):
        data = make_pilot()
        names = [n for p in data["people"] for n in p["names"] if "citation-cu-1934-02-02-i0408" in n["citation_ids"]]
        self.assertEqual([n["lang"] for n in names], ["he", "he"])
        graph = self.rdf(data)
        for name in names:
            self.assertTrue(any(str(value) == name["value"] and value.language == "he" for value in graph.objects(None, URIRef(RICO + "name"))))

    def test_reproducible_outputs(self):
        for name, text in artifacts(make_pilot()).items():
            self.assertEqual((HERE / "generated" / name).read_text(encoding="utf-8"), text, name)


if __name__ == "__main__":
    unittest.main()
