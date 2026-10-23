"""Build the isolated, deterministic issue-14 review pilot. No network or site writes."""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PACKAGE = "pruzhany_schema_pydantic"
if PACKAGE not in sys.modules:
    spec = importlib.util.spec_from_file_location(
        PACKAGE, ROOT / "pydantic/__init__.py", submodule_search_locations=[str(ROOT / "pydantic")]
    )
    package = importlib.util.module_from_spec(spec)
    sys.modules[PACKAGE] = package
    spec.loader.exec_module(package)
from pruzhany_schema_pydantic.sourced_entities_pilot import Pilot, lower_date, upper_date

EHRI = "http://lod.ehri-project-test.eu/ontology#"
RICO = "https://www.ica.org/standards/RiC/ontology#"
BASE = "https://example.org/pruzhany-pilot/issue-14/"
PC = BASE + "vocab#"
AS_OF_YEAR = 2026


def pending_review():
    return {"state": "pending"}


def pending_identity_targets(data):
    return {d["target_id"] for d in data["identity_decisions"]
            if d["applied_in_preview"] and d["review"]["state"] != "approved"}


def living_presumption(*, death=False, fate=None, birth_year=None, printed_years=(), shown=None, as_of_year=AS_OF_YEAR):
    """Copy of pruzhany-svelte/src/lib/privacy/presumption.ts's rule.

    Evidence is aggregated across editions before calling; a named, dated voucher may
    permit display. The fixed as-of year keeps the pilot reproducible.
    """
    if death or fate in ("perished", "died_before"):
        return False, "death-evidenced"
    if birth_year is not None and birth_year <= as_of_year - 110:
        return False, "born-110-years-ago"
    if any(year <= as_of_year - 85 for year in printed_years):
        return False, "printed-in-old-source"
    if shown and isinstance(shown.get("by"), str) and shown["by"].strip():
        from datetime import date
        try:
            on = shown.get("on")
            if isinstance(on, str) and date.fromisoformat(on).isoformat() == on:
                return False, "shown-at-word"
        except ValueError:
            pass
    return True, "unknown"

# Explicit annotations of the frozen newspaper excerpts. No name-based joining.
# A first name stays a first name; a surname is not invented from the registry label.
ANNOTATIONS = {
    "cu-1934-02-02-i0107": [
        ("person-esther-goldenberg", "אסתר", "betrothed", "he", "Hebr"),
        ("person-yaakov-goldenberg", "יעקב גאלדנברג", "betrothed", "he", "Hebr")],
    "cu-1934-02-02-i0108": [
        ("person-esther-goldenberg", "אסתר צרצבסקית", "betrothed", "he", "Hebr"),
        ("person-yaakov-goldenberg", "יעקב", "betrothed", "he", "Hebr")],
    "cu-1934-02-02-i0109": [
        ("person-esther-goldenberg", "אסתר", "betrothed", "he", "Hebr"),
        ("person-yaakov-goldenberg", "גולדנברג", "betrothed", "he", "Hebr")],
    "cu-1934-02-02-i0408": [
        ("person-menachem-yehuda-goldman-19340202", "מנחם־יהודה גולדמן", "betrothed", "he", "Hebr"),
        ("person-itke-langer", "איטקה לנגר", "betrothed", "he", "Hebr")],
    "cu-1934-02-09-i0108": [
        ("person-menachem-yehuda-goldman-19340209", "מנחם־יהודה גאלדמאן", "betrothed", "yi", "Hebr"),
        ("person-itke-langer", "איטקע", "betrothed", "yi", "Hebr")],
    "cu-1934-02-09-i0115": [
        ("person-esther-goldenberg", "אסתר טשערעטשעווסקי", "betrothed", "yi", "Hebr"),
        ("person-yaakov-goldenberg", "יעקב גאלדנבערג", "betrothed", "yi", "Hebr")],
    "cu-1934-02-09-i0116": [
        ("person-esther-goldenberg", "אסתר טשערעטשעווסקי", "betrothed", "yi", "Hebr"),
        ("person-yaakov-goldenberg", "יעקב גאלדענבערג", "betrothed", "yi", "Hebr")],
    "cu-13701": [
        ("person-moshe-judewicz", "משה", "parent", "yi", "Hebr"),
        ("person-rivtche-judewicz", "ריוועטשע", "parent", "yi", "Hebr"),
        ("person-leah-goldberg", "לאה", "signer", "yi", "Hebr"),
        ("person-velvel-goldberg", "וועלוול גאלדבערג", "signer", "yi", "Hebr")],
    "cu-5751": [
        ("person-sarah-epstein", "שרה", "signer", "yi", "Hebr"),
        ("person-mordechai-epstein", "מרדכי עפשטיין", "signer", "yi", "Hebr")],
    "cu-13704": [
        ("person-rachel-pomerantz", "רחל", "honoree", "yi", "Hebr"),
        ("person-chaim-shor", "חיים שור", "honoree", "yi", "Hebr")],
}


def citation_id(unit):
    return "citation-" + unit


def identity_decisions(snapshot):
    events = [e for edition in snapshot["editions"] for e in edition["events"]]
    decisions = []
    for name, test, target in [
        ("esther-yaakov", "esther-ch", "event-engagement-esther-yaakov-1934"),
        ("itke-menachem", "menachem", "event-engagement-itke-menachem-1934"),
    ]:
        group = [e for e in events if test in e["id"]]
        decisions.append({
            "id": "join-event-" + name, "kind": "event", "original_ids": [e["id"] for e in group],
            "target_id": target, "citation_ids": [citation_id(e["unit_ids"][0]) for e in group],
            "confidence": "probable", "review": pending_review(), "applied_in_preview": True,
            "reason": "Same named couple, explicit engagement wording and adjacent issues. Proposed grouping for review; dates are not inferred from publication dates.",
        })
    decisions.append({
        "id": "join-person-menachem", "kind": "person",
        "original_ids": ["person-menachem-yehuda-goldman-19340202", "person-menachem-yehuda-goldman-19340209"],
        "target_id": "person-menachem-yehuda-goldman-19340202",
        "citation_ids": [citation_id("cu-1934-02-02-i0408"), citation_id("cu-1934-02-09-i0108")],
        "confidence": "probable", "review": pending_review(), "applied_in_preview": True,
        "reason": "Full given name and surname variants, same betrothed Itke Langer and adjacent issues. Keep both original IDs and excerpts; no destructive merge.",
    })
    return decisions


def make_pilot(snapshot=None, reverse=()):
    snapshot = snapshot or json.loads((HERE / "input/newspaper-extracts.json").read_text(encoding="utf-8"))
    decisions = identity_decisions(snapshot)
    unknown = set(reverse) - {d["id"] for d in decisions}
    if unknown:
        raise ValueError(f"unknown identity decisions: {sorted(unknown)}")
    for decision in decisions:
        decision["applied_in_preview"] = decision["id"] not in reverse
    targets = {kind: {} for kind in ("person", "event")}
    for d in decisions:
        if d["applied_in_preview"]:
            targets[d["kind"]].update({old: d["target_id"] for old in d["original_ids"]})

    def target(kind, ident):
        return targets[kind].get(ident, ident)

    people, events, citations, mentions, sources = {}, {}, [], [], []
    for edition in snapshot["editions"]:
        source = "source-paper-" + edition["date"]
        sources.append({"id": source, "kind": "newspaper", "title": "Pruzhaner Shtime, " + edition["date"], "work_id": "paper-pruzhaner-shtime"})
        for p in edition["people"]:
            ident = target("person", p["id"])
            person = people.setdefault(ident, {"id": ident, "display_name": p["display_name"], "original_ids": [], "names": [], "presumed_living": True})
            if p["id"] not in person["original_ids"]:
                person["original_ids"].append(p["id"])
        for unit in edition["units"]:
            cid = citation_id(unit["id"])
            citations.append({"id": cid, "source_id": source, "edition_date": edition["date"], "unit_id": unit["id"], "locator": unit["id"], "quote": unit["text"]})
            for index, (original, printed, role, lang, script) in enumerate(ANNOTATIONS[unit["id"]]):
                ident = target("person", original)
                mentions.append({
                    "id": f"mention-{unit['id']}-{index + 1}", "entity_id": ident,
                    "original_entity_id": original, "citation_id": cid, "printed_name": printed,
                    "roles": [role], "text_sha256": hashlib.sha256(unit["text"].encode()).hexdigest(),
                })
                names = people[ident]["names"]
                name = next((n for n in names if (n["value"], n["lang"], n["script"]) == (printed, lang, script)), None)
                if name:
                    name["citation_ids"].append(cid)
                else:
                    names.append({"value": printed, "kind": "printed", "script": script, "lang": lang, "citation_ids": [cid]})
        for old in edition["events"]:
            ident = target("event", old["id"])
            event = events.setdefault(ident, {"id": ident, "type": "engagement", "name": old["name"], "original_ids": [], "citation_ids": []})
            event["original_ids"].append(old["id"])
            event["citation_ids"] += [citation_id(unit) for unit in old["unit_ids"]]

    facts = []

    def add_fact(ident, subject, kind, cited, **payload):
        facts.append({"id": ident, "subject_id": subject, "type": kind, **payload,
                      "citation_ids": cited, "evidence_confidence": "confirmed", "identity_confidence": "probable",
                      "status": "accepted", "review": pending_review(), "attributed_to": "pilot:transcript-review:2026-10-19"})

    for event in events.values():
        for person in sorted({m["entity_id"] for m in mentions if m["citation_id"] in event["citation_ids"]}):
            cited = sorted({m["citation_id"] for m in mentions if m["entity_id"] == person and m["citation_id"] in event["citation_ids"]})
            add_fact(f"fact-{event['id']}-{person}", person, "event_participation", cited, event_id=event["id"], value="betrothed")
    for person in ["person-moshe-judewicz", "person-rivtche-judewicz"]:
        add_fact("fact-parenthood-" + person, person, "parenthood", [citation_id("cu-13701")], value="Congratulated on the birth of an unnamed daughter; no birth date inferred.")
    relationships = [{
        "id": "relationship-rachel-chaim", "from_id": "person-rachel-pomerantz", "to_id": "person-chaim-shor", "type": "spouse",
        "citation_ids": [citation_id("cu-13704")], "evidence_confidence": "confirmed", "identity_confidence": "probable", "status": "accepted", "review": pending_review(),
    }]
    data = {"version": "0.1.0", "vocabulary_version": "0.1.0", "source_revision": snapshot["revision"], "as_of_year": AS_OF_YEAR,
            "sources": sources, "citations": citations, "people": list(people.values()), "places": [],
            "mentions": mentions, "facts": facts, "relationships": relationships,
            "events": list(events.values()), "identity_decisions": decisions}
    for person in data["people"]:
        years = [int(c["edition_date"][:4]) for c in citations
                 if any(m["entity_id"] == person["id"] and m["citation_id"] == c["id"] for m in mentions)]
        person["presumed_living"], person["presumption_reason"] = living_presumption(printed_years=years)
    return Pilot.model_validate(data).model_dump(exclude_none=True)


def approved(claim):
    return claim["status"] == "accepted" and claim["review"]["state"] == "approved"


def residence_at(data, person_id, when):
    """Legacy scalar only when one approved, date-applicable residence is unambiguous."""
    found = set()
    for fact in data["facts"]:
        if fact["subject_id"] != person_id or fact["type"] != "residence" or not approved(fact):
            continue
        date = fact["date"]
        if lower_date(date["start"]) <= when <= upper_date(date.get("end") or date["start"]):
            found.add(fact["place_id"])
    if len(found) > 1:
        raise ValueError(f"conflicting residences of {person_id} at {when}: {sorted(found)}")
    return next(iter(found), None)


def public_projection(data):
    """Conservative demo only. Never writes to or replaces the site's privacy projection."""
    citations = {c["id"]: c for c in data["citations"]}
    sources = {s["id"]: s for s in data["sources"]}
    # Trusted configuration, never supplied by a research answer or Source.host.
    allowed = {"collections.yadvashem.org", "collections.arolsen-archives.org", "archive.org", "jewishgen.org"}
    pending_targets = pending_identity_targets(data)

    def cleared(claim, person_ids):
        if not approved(claim) or any(p in pending_targets for p in person_ids) or claim.get("event_id") in pending_targets:
            return False
        for ident in claim["citation_ids"]:
            citation = citations[ident]
            if citation.get("url"):
                try:
                    parsed = urlparse(citation["url"])
                except ValueError:
                    return False
                if parsed.scheme != "https" or parsed.username or parsed.password or not any(parsed.hostname == h or (parsed.hostname or "").endswith("." + h) for h in allowed):
                    return False
            elif sources[citation["source_id"]]["kind"] != "newspaper":
                return False
        return True

    facts = [f for f in data["facts"] if cleared(f, [f["subject_id"]] + ([f["related_person_id"]] if f.get("related_person_id") else []))]
    relationships = [r for r in data["relationships"] if cleared(r, [r["from_id"], r["to_id"]])]
    bindings = {old: d["target_id"] for d in data["identity_decisions"]
                if d["kind"] == "person" and d["applied_in_preview"] and d["review"]["state"] == "approved"
                for old in d["original_ids"]}
    candidates = {}
    cleared_nonprint = set()
    for person in data["people"]:
        person_mentions = [m for m in data["mentions"] if m["original_entity_id"] in person["original_ids"]]
        for original in person["original_ids"]:
            ident = bindings.get(original, original)
            names, years = candidates.setdefault(ident, (set(), set()))
            mentions = [m for m in person_mentions if m["original_entity_id"] == original]
            names.update(m["printed_name"] for m in mentions)
            years.update(int(citations[m["citation_id"]]["edition_date"][:4]) for m in mentions
                         if citations[m["citation_id"]].get("edition_date"))
            if not person_mentions:
                names.update(n["value"] for n in person["names"] if n["kind"] == "printed")
            # A non-print verdict belongs to this record only if its originals
            # are still together. Never copy a preview verdict across a pending join.
            if {bindings.get(old, old) for old in person["original_ids"]} == {ident}:
                if not person["presumed_living"] and person["presumption_reason"] not in ("unknown", "printed-in-old-source"):
                    cleared_nonprint.add(ident)
    published = {ident: names for ident, (names, years) in candidates.items()
                 if ident in cleared_nonprint or not living_presumption(printed_years=years, as_of_year=data["as_of_year"])[0]}
    # Claims must refer only to people that passed this same public-ID verdict.
    facts = [f for f in facts if f["subject_id"] in published and
             (not f.get("related_person_id") or f["related_person_id"] in published)]
    relationships = [r for r in relationships if r["from_id"] in published and r["to_id"] in published]
    used = {cid for claim in [*facts, *relationships] for cid in claim["citation_ids"]}
    spouse_ids = {ident: [] for ident in published}
    for relationship in relationships:
        if relationship["type"] == "spouse":
            spouse_ids[relationship["from_id"]].append(relationship["to_id"])
            spouse_ids[relationship["to_id"]].append(relationship["from_id"])
    return {
        "people": [{"id": ident, "printed_names": sorted(names), "spouse_ids": spouse_ids[ident]} for ident, names in published.items()],
        "facts": [{k: v for k, v in f.items() if k not in ("review", "attributed_to")} for f in facts],
        "relationships": [{k: v for k, v in r.items() if k != "review"} for r in relationships],
        "citations": [{k: c[k] for k in ("id", "source_id", "locator", "url") if k in c} for c in data["citations"] if c["id"] in used],
    }


def rico_export(data):
    """Reify review assertions. Pending/disputed claims never become base RDF triples."""
    graph = []
    ref = lambda ident: {"@id": BASE + ident}
    for s in data["sources"]:
        graph.append({**ref(s["id"]), "@type": "rico:RecordSet" if s["kind"] == "newspaper" else "rico:RecordResource", "rdfs:label": s["title"], "pc:workId": s["work_id"]})
    for c in data["citations"]:
        node = {**ref(c["id"]), "@type": "rico:Record", "dcterms:bibliographicCitation": c["locator"],
                "dcterms:source": ref(c["source_id"]), "pc:quote": c["quote"]}
        if c.get("url"):
            node["rdfs:seeAlso"] = {"@id": c["url"]}
        graph.append(node)
    for p in data["people"]:
        graph.append({**ref(p["id"]), "@type": ["rico:Person", "ehri:Person"], "rdfs:label": p["display_name"], "pc:presumedLiving": p["presumed_living"]})
        for index, name in enumerate(p["names"]):
            nid = f"{p['id']}-name-{index + 1}"
            graph.append({**ref(nid), "@type": "rico:AgentName", "rico:name": {"@value": name["value"], "@language": name["lang"]},
                          "pc:recordedFor": ref(p["id"]), "pc:nameKind": name["kind"], "pc:script": name["script"],
                          "prov:wasDerivedFrom": [ref(cid) for cid in name["citation_ids"]]})
    for p in data["places"]:
        graph.append({**ref(p["id"]), "@type": ["rico:Place"] + ([{"city": "ehri:City", "region": "ehri:Region", "country": "ehri:Country"}[p["kind"]]] if p.get("kind") in {"city", "region", "country"} else []), "rdfs:label": p["label"]})
    for event in data["events"]:
        graph.append({**ref(event["id"]), "@type": "rico:Event", "rdfs:label": event["name"], "pc:eventType": event["type"],
                      "prov:wasDerivedFrom": [ref(c) for c in event["citation_ids"]]})
    for m in data["mentions"]:
        graph.append({**ref(m["id"]), "@type": "pc:Mention", "pc:entity": ref(m["entity_id"]), "pc:originalEntityId": m["original_entity_id"],
                      "pc:printedName": m["printed_name"], "pc:roles": m["roles"], "pc:textSha256": m["text_sha256"], "prov:wasDerivedFrom": ref(m["citation_id"])})

    pending_targets = pending_identity_targets(data)

    def statement(claim, subject, predicate, obj):
        node = {**ref(claim["id"]), "@type": ["rdf:Statement", "pc:Claim"],
                "rdf:subject": ref(subject), "rdf:predicate": {"@id": predicate}, "rdf:object": obj,
                "pc:status": claim["status"], "pc:reviewState": claim["review"]["state"],
                "pc:evidenceConfidence": claim["evidence_confidence"], "pc:identityConfidence": claim["identity_confidence"],
                "prov:wasDerivedFrom": [ref(cid) for cid in claim["citation_ids"]]}
        # Approval is independent of confidence. Only confirmed identity allows an
        # unqualified identity-dependent triple; otherwise retain the statement.
        target = obj.get("@id", "").removeprefix(BASE)
        if approved(claim) and claim["identity_confidence"] == "confirmed" and subject not in pending_targets and target not in pending_targets:
            graph.append({**ref(subject), predicate: obj})
            if predicate.startswith(RICO):
                node["@type"].append("rico:Relation")
                node["rico:relationCertainty"] = claim["evidence_confidence"]
                node["rico:isEvidencedBy"] = [ref(cid) for cid in claim["citation_ids"]]
                node["rico:relationConnects"] = [ref(subject), obj]
                for cid in claim["citation_ids"]:
                    graph.append({**ref(cid), "rico:evidences": ref(claim["id"])})
        graph.append(node)
        return node

    for f in data["facts"]:
        kind = f["type"]
        predicate = RICO + {"residence": "hasOrHadLocation", "occupation": "hasOrHadOccupationOfType", "birth": "hasBirthDate", "death": "hasDeathDate", "event_participation": "isOrWasParticipantIn"}.get(kind, "")
        if predicate == RICO:
            predicate = PC + kind
        if kind == "residence":
            obj = ref(f["place_id"])
        elif kind in ("birth", "death", "survival") and f.get("date"):
            obj = ref(f["id"] + "-date")
            graph.append({**obj, "@type": "rico:Date", "rico:expressedDate": f["date"].get("printed") or f["date"]["start"], "pc:normalizedDate": {"@value": f["date"], "@type": "@json"}})
        elif kind == "occupation":
            obj = ref(f["id"] + "-occupation")
            graph.append({**obj, "@type": "rico:OccupationType", "rdfs:label": f["value"]})
        elif kind == "event_participation":
            obj = ref(f["event_id"])
        else:
            # A death-place-only claim must not become hasDeathDate with a literal.
            if kind in ("birth", "death"):
                predicate = RICO + ("hasBirthPlace" if kind == "birth" else "hasDeathPlace") if f.get("place_id") else PC + kind
            obj = ref(f["place_id"]) if f.get("place_id") else (ref(f["related_person_id"]) if f.get("related_person_id") else {"@value": f.get("value", "")})
        node = statement(f, f["subject_id"], predicate, obj)
        node["pc:payload"] = {"@value": {k: v for k, v in f.items() if k in ("type", "value", "date", "place_id", "related_person_id", "event_id", "proposed_type", "holocaust_related")}, "@type": "@json"}
        if f.get("date"):
            node["pc:date"] = {"@value": f["date"], "@type": "@json"}
        if kind == "event_participation":
            node["pc:role"] = f["value"]
    for r in data["relationships"]:
        predicate = RICO + "hasOrHadSpouse" if r["type"] == "spouse" else PC + r["type"]
        statement(r, r["from_id"], predicate, ref(r["to_id"]))
    for p in data["people"]:
        if p.get("fate"):
            graph.append({**ref(p["id"] + "-fate"), "@type": "pc:FateConclusion", "pc:person": ref(p["id"]),
                          "pc:outcome": p["fate"]["outcome"], "pc:confidence": p["fate"]["confidence"],
                          "pc:reviewState": p["fate"]["review"]["state"], "prov:wasDerivedFrom": [ref(f) for f in p["fate"]["rests_on"]]})
    for d in data["identity_decisions"]:
        graph.append({**ref(d["id"]), "@type": "pc:IdentityProposal", "pc:originalIds": d["original_ids"], "pc:target": ref(d["target_id"]),
                      "pc:appliedInPreview": d["applied_in_preview"], "pc:reviewState": d["review"]["state"], "pc:reason": d["reason"],
                      "prov:wasDerivedFrom": [ref(cid) for cid in d["citation_ids"]]})
    # Explicit prefixes; no remote context, RDF store or network needed to read this.
    return {"@context": {"ehri": EHRI, "rico": RICO, "pc": PC, "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "prov": "http://www.w3.org/ns/prov#", "dcterms": "http://purl.org/dc/terms/"}, "@graph": graph}


def edition_views(data):
    """Small, self-contained read models; explicitly not full production bundles."""
    citations = {c["id"]: c for c in data["citations"]}
    views = {}
    for date in sorted({c["edition_date"] for c in data["citations"]}):
        mentions = [m for m in data["mentions"] if citations[m["citation_id"]]["edition_date"] == date]
        ids = {m["entity_id"] for m in mentions}
        views[date] = {"people": [{"id": p["id"], "name": p["display_name"], "unit_ids": sorted({citations[m["citation_id"]]["unit_id"] for m in mentions if m["entity_id"] == p["id"]}), "residence_at_publication": residence_at(data, p["id"], date)} for p in data["people"] if p["id"] in ids], "mentions": mentions}
    return views


def report(data):
    from collections import Counter
    reasons = Counter(p["presumption_reason"] for p in data["people"])
    reviews = Counter(c["review"]["state"] for c in data["facts"] + data["relationships"])
    citations = {c["id"]: c for c in data["citations"]}
    lines = ["# Issue 14: sourced entities pilot", "", "> Review preview. Identity joins below are proposals, not approved changes to the archive.", "",
             f"{len(data['people'])} people · {len(data['events'])} events · {len(data['mentions'])} mentions · {len(data['facts'])} facts · {len(data['relationships'])} relationships · {len(data['citations'])} newspaper excerpts.", "",
             "Frozen source: `dsmedia/pruzhany-svelte@" + data["source_revision"] + "`. Labels are carried forward; printed names and claims cite the selected transcripts. Scans and external archive matches have not been adjudicated in this pilot.", "",
             "## People and their roles", "", "| Person | Editions | Roles | Evidence |", "|---|---|---|---|"]
    for person in data["people"]:
        mentions = [m for m in data["mentions"] if m["entity_id"] == person["id"]]
        dates = sorted({citations[m["citation_id"]]["edition_date"] for m in mentions})
        roles = sorted({r for m in mentions for r in m["roles"]})
        evidence = sorted({m["citation_id"] for m in mentions})
        lines.append(f"| {person['display_name']} | {', '.join(dates)} | {', '.join(roles)} | " + ", ".join(f"[{c.removeprefix('citation-')}](#{c})" for c in evidence) + " |")
    lines += ["", "## Proposed joins", ""]
    for d in data["identity_decisions"]:
        lines += [f"### {d['id']}", "", f"Preview applied: **{d['applied_in_preview']}**. Confidence: **{d['confidence']}**. Approval: **{d['review']['state']}**.", "", d["reason"], "", *[f"- `{old}`" for old in d["original_ids"]], "", f"Proposed target: `{d['target_id']}`.", ""]
    lines += ["## Assertions awaiting review", "", "| Subject | Type / value | Evidence confidence | Identity confidence | Sources |", "|---|---|---|---|---|"]
    names = {p["id"]: p["display_name"] for p in data["people"]}
    for f in data["facts"]:
        value = f.get("value") or names.get(f.get("related_person_id"), "")
        lines.append(f"| {names[f['subject_id']]} | {f['type']}: {value} | {f['evidence_confidence']} | {f['identity_confidence']} | " + ", ".join(f"[{c.removeprefix('citation-')}](#{c})" for c in f["citation_ids"]) + " |")
    for relationship in data["relationships"]:
        lines.append(f"| {names[relationship['from_id']]} | spouse: {names[relationship['to_id']]} | {relationship['evidence_confidence']} | {relationship['identity_confidence']} | " + ", ".join(f"[{c.removeprefix('citation-')}](#{c})" for c in relationship["citation_ids"]) + " |")
    lines += ["", f"Presumption as of {data['as_of_year']}: " + ", ".join(f"{count} **{reason}**" for reason, count in sorted(reasons.items())) + f". The public view contains {len(public_projection(data)['people'])} person records after approved joins and privacy filtering.", "", "Editorial review: " + ", ".join(f"{count} **{state}**" for state, count in sorted(reviews.items())) + ". Public claims require approval and privacy clearance.", "",
              "## Deliberately unresolved", "",
              "- The engagement date `1934-01-27` in the existing event record is not carried into a fact: these selected printed excerpts do not establish it. The English translation supplies a date that its selected source text does not contain.",
              "- Engagements do not generate marriage facts. Unnamed newborns do not receive invented names, genders or birth dates.",
              "- Residence, occupation, fate, maiden names and external identity links are not inferred from display labels or previous prose. Temporal residence, disputed dates and fate evidence are exercised only in clearly synthetic tests.",
              "- No offset or bounding box is invented. Mention IDs are stored independently of text; a SHA-256 anchor detects transcript changes. Repeated same-name occurrences need additional occurrence selectors before production migration.",
              "- The RiC-O export reifies unapproved claims and retains local review/identity extensions. It emits no `owl:sameAs`; only approved claims with confirmed identity and no pending identity joins can become unqualified historical triples.", "", "## Newspaper excerpts", ""]
    for c in data["citations"]:
        lines += [f"### {c['id']}", "", f"{c['edition_date']} · `{c['unit_id']}`", "", *[("> " + line) if line else ">" for line in c["quote"].splitlines()], ""]
    return "\n".join(lines).rstrip() + "\n"


def artifacts(data):
    dump = lambda value: json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    return {"pilot.json": dump(data), "review.md": report(data), "review.jsonld": dump(rico_export(data)), "edition-views.json": dump(edition_views(data)), "public-projection.json": dump(public_projection(data))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if committed generated outputs are stale")
    parser.add_argument("--reverse", action="append", default=[], help="reverse a proposed join, preserving source observations")
    parser.add_argument("--output", type=Path, default=HERE / "generated")
    args = parser.parse_args()
    if args.reverse and args.output == HERE / "generated":
        parser.error("use --output for a reversed preview so the baseline stays intact")
    outputs = artifacts(make_pilot(reverse=args.reverse))
    for filename, content in outputs.items():
        path = args.output / filename
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"stale generated output: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f"pilot: {len(outputs)} reproducible artifacts {'checked' if args.check else 'written'}")


if __name__ == "__main__":
    main()
