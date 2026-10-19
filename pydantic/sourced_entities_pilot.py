"""Experimental issue-14 contract. Deliberately not imported by production schemas."""
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator
from .sourced_entities_pilot_vocabulary import (
    FactType, MentionRole, NameKind, PilotEventType, RelationshipType, VOCABULARY_VERSION,
)

Confidence = Literal["confirmed", "probable", "possible"]
Status = Literal["accepted", "disputed", "rejected"]


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


def upper_date(value):
    from calendar import monthrange
    if len(value) == 4:
        return value + "-12-31"
    if len(value) == 7:
        return value + f"-{monthrange(int(value[:4]), int(value[5:]))[1]:02}"
    return value


class Review(Strict):
    state: Literal["pending", "approved"] = "pending"
    by: str | None = None
    on: str | None = Field(default=None, pattern=r"^\d{4}-\d{2}-\d{2}$")

    @model_validator(mode="after")
    def clearance(self):
        from datetime import date
        if self.on:
            date.fromisoformat(self.on)
        if self.state == "approved" and (not self.by or not self.by.strip() or not self.on):
            raise ValueError("approval requires who and when")
        return self


class DateValue(Strict):
    start: str = Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    end: str | None = Field(default=None, pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$")
    precision: Literal["year", "month", "day", "range"]
    printed: str | None = None
    printed_calendar: Literal["gregorian", "hebrew"] | None = None
    inferred: bool = False

    @model_validator(mode="after")
    def interval(self):
        from datetime import date
        for value in (self.start, self.end):
            if value:
                date.fromisoformat(value + {4: "-01-01", 7: "-01", 10: ""}[len(value)])
        length = {"year": 4, "month": 7, "day": 10}
        if self.precision in length and (len(self.start) != length[self.precision] or self.end):
            raise ValueError("date precision does not match value")
        if self.precision == "range" and (not self.end or self.start > self.end):
            raise ValueError("range needs ordered start and end")
        if self.printed_calendar and not self.printed:
            raise ValueError("printed calendar needs printed date")
        return self


class Source(Strict):
    id: str
    kind: Literal["newspaper", "book", "archive_record"]
    title: str
    work_id: str


class Citation(Strict):
    id: str
    source_id: str
    edition_date: str | None = None
    unit_id: str | None = None
    locator: str
    quote: str = Field(min_length=1)
    url: str | None = None
    note: str | None = None


class Name(Strict):
    value: str = Field(min_length=1)
    kind: NameKind
    script: Literal["Hebr", "Latn"]
    lang: Literal["yi", "he", "en"]
    citation_ids: list[str] = Field(min_length=1)


class Fate(Strict):
    outcome: Literal["perished", "survived", "died_before", "unknown"]
    confidence: Confidence
    rests_on: list[str]
    review: Review


class Person(Strict):
    id: str
    display_name: str
    original_ids: list[str] = Field(min_length=1)
    names: list[Name] = Field(min_length=1)
    presumed_living: bool = True
    fate: Fate | None = None


class Place(Strict):
    id: str
    label: str


class Mention(Strict):
    id: str
    entity_id: str
    original_entity_id: str
    citation_id: str
    printed_name: str = Field(min_length=1)
    roles: list[MentionRole] = Field(min_length=1)
    text_sha256: str = Field(pattern=r"^[a-f0-9]{64}$")


class Fact(Strict):
    id: str
    subject_id: str
    type: FactType
    value: str | None = None
    date: DateValue | None = None
    place_id: str | None = None
    related_person_id: str | None = None
    event_id: str | None = None
    proposed_type: str | None = None
    holocaust_related: bool | None = None
    citation_ids: list[str] = Field(min_length=1)
    evidence_confidence: Confidence
    identity_confidence: Confidence
    status: Status
    review: Review
    attributed_to: str

    @model_validator(mode="after")
    def payload(self):
        if self.type == "residence" and (not self.place_id or not self.date):
            raise ValueError("residence requires place and time")
        if self.type == "occupation" and not self.value:
            raise ValueError("occupation requires a value")
        if self.type == "survival" and not self.date:
            raise ValueError("survival needs a time at which alive")
        if self.type in ("birth", "death") and not (self.date or self.place_id or self.value):
            raise ValueError("birth/death assertion needs a payload")
        if self.type == "parenthood" and not (self.value or self.related_person_id):
            raise ValueError("parenthood needs a child or description")
        if self.type == "marriage" and not self.related_person_id:
            raise ValueError("marriage requires the other person")
        if self.type == "event_participation" and not (self.event_id and self.value):
            raise ValueError("event participation requires event and role")
        if self.type == "other" and not (self.value and self.proposed_type):
            raise ValueError("other requires a value and proposed type")
        return self


class Relationship(Strict):
    id: str
    from_id: str
    to_id: str
    type: RelationshipType
    citation_ids: list[str] = Field(min_length=1)
    evidence_confidence: Confidence
    identity_confidence: Confidence
    status: Status
    review: Review


class Event(Strict):
    id: str
    type: PilotEventType
    name: str
    original_ids: list[str] = Field(min_length=1)
    citation_ids: list[str] = Field(min_length=1)


class IdentityDecision(Strict):
    id: str
    kind: Literal["person", "event"]
    original_ids: list[str] = Field(min_length=2)
    target_id: str
    citation_ids: list[str] = Field(min_length=2)
    confidence: Confidence
    review: Review
    applied_in_preview: bool
    reason: str


class Pilot(Strict):
    version: Literal["0.1.0"]
    vocabulary_version: Literal[VOCABULARY_VERSION]
    source_revision: str
    sources: list[Source]
    citations: list[Citation]
    people: list[Person]
    places: list[Place]
    mentions: list[Mention]
    facts: list[Fact]
    relationships: list[Relationship]
    events: list[Event]
    identity_decisions: list[IdentityDecision]

    @model_validator(mode="after")
    def integrity(self):
        import hashlib
        groups = [self.sources, self.citations, self.people, self.places, self.mentions,
                  self.facts, self.relationships, self.events, self.identity_decisions]
        ids = [v.id for group in groups for v in group]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate id")
        sources = {v.id for v in self.sources}
        citations = {v.id: v for v in self.citations}
        people = {v.id: v for v in self.people}
        places = {v.id for v in self.places}
        events = {v.id for v in self.events}
        facts = {v.id: v for v in self.facts}
        for entities in (self.people, self.events):
            originals = [ident for entity in entities for ident in entity.original_ids]
            if len(originals) != len(set(originals)):
                raise ValueError("original identity belongs to more than one entity")

        def refs(values, known, label):
            if any(v not in known for v in values):
                raise ValueError(f"dangling {label}")

        for c in self.citations:
            refs([c.source_id], sources, "source")
        for p in self.people:
            for name in p.names:
                refs(name.citation_ids, citations, "name citation")
            if p.fate:
                refs(p.fate.rests_on, facts, "fate fact")
                if p.fate.outcome != "unknown" and not p.fate.rests_on:
                    raise ValueError("known fate needs supporting facts")
                for ident in p.fate.rests_on:
                    fact = facts[ident]
                    if fact.subject_id != p.id or fact.status != "accepted":
                        raise ValueError("fate must rest on own accepted facts")
                    if p.fate.outcome in ("perished", "died_before") and fact.type != "death":
                        raise ValueError("death outcome requires death evidence")
                    if p.fate.outcome == "perished" and fact.holocaust_related is not True:
                        raise ValueError("perished needs Holocaust-related death evidence")
                    if p.fate.outcome == "died_before" and (not fact.date or upper_date(fact.date.end or fact.date.start) >= "1939-09-01"):
                        raise ValueError("died_before needs death evidence before the pilot's 1939-09-01 cutoff")
                    if p.fate.outcome == "survived" and (fact.type != "survival" or not fact.date or fact.date.start < "1945-05-08"):
                        raise ValueError("survived needs evidence alive after the pilot's explicit 1945-05-08 cutoff")
                    rank = {"possible": 0, "probable": 1, "confirmed": 2}
                    if rank[p.fate.confidence] > min(rank[fact.evidence_confidence], rank[fact.identity_confidence]):
                        raise ValueError("fate confidence exceeds its supporting evidence or identity match")
        for m in self.mentions:
            refs([m.entity_id], people, "mention person")
            refs([m.citation_id], citations, "mention citation")
            quote = citations[m.citation_id].quote
            if m.printed_name not in quote or hashlib.sha256(quote.encode()).hexdigest() != m.text_sha256:
                raise ValueError("mention anchor no longer matches source text")
            if m.original_entity_id not in people[m.entity_id].original_ids:
                raise ValueError("mention lost its original identity")
        for f in self.facts:
            refs([f.subject_id], people, "fact subject")
            refs(f.citation_ids, citations, "fact citation")
            if f.place_id:
                refs([f.place_id], places, "place")
            if f.related_person_id:
                refs([f.related_person_id], people, "related person")
            if f.event_id:
                refs([f.event_id], events, "event")
        for r in self.relationships:
            refs([r.from_id, r.to_id], people, "relationship person")
            refs(r.citation_ids, citations, "relationship citation")
            if r.from_id == r.to_id:
                raise ValueError("self relationship")
        for event in self.events:
            refs(event.citation_ids, citations, "event citation")
        for decision in self.identity_decisions:
            refs(decision.citation_ids, citations, "identity citation")
            if len(set(decision.original_ids)) != len(decision.original_ids):
                raise ValueError("identity proposal repeats an original id")
            if decision.applied_in_preview:
                refs([decision.target_id], people if decision.kind == "person" else events, "identity target")
                entity = people[decision.target_id] if decision.kind == "person" else next(e for e in self.events if e.id == decision.target_id)
                if not set(decision.original_ids) <= set(entity.original_ids):
                    raise ValueError("identity proposal lost its source identities")
        return self
