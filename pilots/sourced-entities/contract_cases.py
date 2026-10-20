"""Shared positive/negative contract examples. Synthetic assertions are test-only."""
import copy
import json
import sys
from pathlib import Path
# -P keeps the repository's pydantic/ directory from shadowing the library.
# Add only this pilot directory for its sibling build module.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import make_pilot, Pilot
from pruzhany_schema_pydantic.sourced_entities_pilot import DateValue, Fact, Review


def synthetic():
    """Entirely fictional data: never add test biographies to the real-person pilot."""
    return {
        "version": "0.1.0", "vocabulary_version": "0.1.0", "source_revision": "test-only", "as_of_year": 2026,
        "sources": [{"id": "test-source", "kind": "book", "title": "FICTIONAL TEST SOURCE", "work_id": "test-work"}],
        "citations": [{"id": "test-citation", "source_id": "test-source", "locator": "fictional p. 1", "quote": "Test Person A and Test Person B are fictional characters.", "url": "https://archive.org/details/fictional-test-only"}],
        "people": [{"id": "test-person-" + x, "display_name": "Test Person " + x.upper(), "original_ids": ["test-person-" + x], "names": [{"value": "Test Person " + x.upper(), "kind": "printed", "script": "Latn", "lang": "en", "citation_ids": ["test-citation"]}], "presumed_living": False, "presumption_reason": "death-evidenced"} for x in ("a", "b")],
        "places": [{"id": "test-place-a", "label": "Fictional Place A"}, {"id": "test-place-b", "label": "Fictional Place B"}],
        "mentions": [], "facts": [], "events": [], "relationships": [], "identity_decisions": [],
    }


def fact(kind="occupation", **extra):
    return {"id": "test-fact", "subject_id": "test-person-a", "type": kind, "value": "Fictional test occupation", "citation_ids": ["test-citation"], "evidence_confidence": "confirmed", "identity_confidence": "confirmed", "status": "accepted", "review": {"state": "approved", "by": "test-fixture", "on": "2026-10-19"}, "attributed_to": "test-only", **extra}


def cases():
    baseline = make_pilot()
    result = [{"name": "real pilot", "model": "Pilot", "valid": True, "value": baseline}]

    def changed(name, mutate):
        data = copy.deepcopy(baseline)
        mutate(data)
        result.append({"name": name, "model": "Pilot", "valid": False, "value": data})

    changed("missing as-of year", lambda d: d.pop("as_of_year"))
    changed("living with old-source reason", lambda d: d["people"][0].update(presumed_living=True, presumption_reason="printed-in-old-source"))
    changed("deceased with unknown reason", lambda d: d["people"][0].update(presumed_living=False, presumption_reason="unknown"))
    changed("invalid presumption reason", lambda d: d["people"][0].update(presumption_reason="invented"))
    changed("dangling source", lambda d: d["citations"][0].update(source_id="missing"))
    changed("dangling name citation", lambda d: d["people"][0]["names"][0].update(citation_ids=["missing"]))
    changed("dangling fact subject", lambda d: d["facts"][0].update(subject_id="missing"))
    changed("dangling event", lambda d: d["facts"][0].update(event_id="missing"))
    changed("empty evidence", lambda d: d["facts"][0].update(citation_ids=[]))
    changed("duplicate id", lambda d: d["people"][1].update(id=d["people"][0]["id"]))
    changed("unknown field", lambda d: d["facts"][0].update(unchecked_prose="unexpected"))
    changed("unsupported type", lambda d: d["facts"][0].update(type="silently-invented"))
    changed("lost original identity", lambda d: d["mentions"][0].update(original_entity_id="missing"))
    changed("original identity assigned twice", lambda d: d["people"][1]["original_ids"].append(d["people"][0]["original_ids"][0]))
    changed("identity proposal loses lineage", lambda d: d["identity_decisions"][0]["original_ids"].append("missing-source-id"))
    changed("changed source text", lambda d: d["citations"][0].update(quote=d["citations"][0]["quote"] + " changed"))
    changed("invented printed name", lambda d: d["mentions"][0].update(printed_name="Never printed"))
    changed("self relationship", lambda d: d["relationships"][0].update(to_id=d["relationships"][0]["from_id"]))
    changed("approval lacks reviewer", lambda d: d["facts"][0].update(review={"state": "approved", "on": "2026-10-19"}))
    changed("fate lacks evidence", lambda d: d["people"][0].update(fate={"outcome": "perished", "confidence": "probable", "rests_on": [], "review": {"state": "pending"}}))
    changed("emigration is not a fate", lambda d: d["people"][0].update(fate={"outcome": "left_before", "confidence": "possible", "rests_on": [], "review": {"state": "pending"}}))
    changed("boolean string is not a boolean", lambda d: d["people"][0].update(presumed_living="false"))

    for reason in ["death-evidenced", "born-110-years-ago", "printed-in-old-source", "shown-at-word", "unknown"]:
        data = synthetic()
        data["people"][0].update(presumption_reason=reason, presumed_living=reason == "unknown")
        result.append({"name": "presumption " + reason, "model": "Pilot", "valid": True, "value": data})

    for name, valid, value in [
        ("mixed precision overlap", True, {"start": "1939-05", "end": "1939", "precision": "range"}),
        ("mixed precision reversed", False, {"start": "1940", "end": "1939-12", "precision": "range"}),
        ("leap month", True, {"start": "1940-02", "end": "1940-02-29", "precision": "range"}),
        ("non leap day", False, {"start": "1939-02-29", "precision": "day"}),
        ("year date", True, {"start": "1938", "precision": "year"}),
        ("Hebrew printed date", True, {"start": "1938-12-16", "precision": "day", "printed": "כ״ג כסלו תרצ״ט", "printed_calendar": "hebrew", "inferred": True}),
        ("range", True, {"start": "1937-01-01", "end": "1939-12-31", "precision": "range"}),
        ("wrong precision", False, {"start": "1938", "precision": "day"}),
        ("impossible date", False, {"start": "1938-02-30", "precision": "day"}),
        ("year zero", False, {"start": "0000", "precision": "year"}),
        ("reverse range", False, {"start": "1939", "end": "1938", "precision": "range"}),
        ("range without end", False, {"start": "1938", "precision": "range"}),
        ("calendar without printed date", False, {"start": "1938", "precision": "year", "printed_calendar": "hebrew"}),
    ]:
        result.append({"name": name, "model": "DateValue", "valid": valid, "value": value})
    for name, valid, value in [
        ("typed residence", True, fact("residence", place_id="test-place-a", date={"start": "1938", "precision": "year"})),
        ("undated residence", False, fact("residence", place_id="test-place-a")),
        ("marriage without partner", False, fact("marriage")),
        ("survival without time", False, fact("survival")),
        ("other with proposed type", True, fact("other", proposed_type="test-new-kind")),
        ("other without proposed type", False, fact("other")),
        ("possible does not mean rejected", True, fact(evidence_confidence="possible", identity_confidence="possible")),
    ]:
        result.append({"name": name, "model": "Fact", "valid": valid, "value": value})
    result.append({"name": "invalid approval day", "model": "Review", "valid": False, "value": {"state": "approved", "by": "test", "on": "2026-02-30"}})
    for name, valid, kind, date, outcome, extra in [
        ("supported survival", True, "survival", "1946", "survived", {}),
        ("prewar presence is not survival", False, "survival", "1938", "survived", {}),
        ("ordinary death is not Holocaust fate", False, "death", "1943", "perished", {}),
        ("supported Holocaust death", True, "death", "1943", "perished", {"holocaust_related": True}),
        ("supported prewar death", True, "death", "1934", "died_before", {}),
        ("postwar death is not prewar death", False, "death", "1950", "died_before", {}),
        ("ambiguous 1939 death is not definitely prewar", False, "death", "1939", "died_before", {}),
        ("uncertain identity limits fate", False, "survival", "1946", "survived", {"identity_confidence": "possible"}),
    ]:
        data = synthetic()
        data["facts"] = [fact(kind, date={"start": date, "precision": "year"}, **extra)]
        data["people"][0]["fate"] = {"outcome": outcome, "confidence": "confirmed", "rests_on": ["test-fact"], "review": {"state": "pending"}}
        result.append({"name": name, "model": "Pilot", "valid": valid, "value": data})
    return result


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    models = {"Pilot": Pilot, "DateValue": DateValue, "Fact": Fact, "Review": Review}
    output = cases()
    for case in output:
        try:
            models[case["model"]].model_validate(case["value"])
            accepted = True
        except ValueError:
            accepted = False
        if accepted != case["valid"]:
            raise AssertionError(f"Pydantic disagrees with expected result: {case['name']}")
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
