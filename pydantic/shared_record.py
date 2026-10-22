"""One shared record, built on production sourced facts and standing."""
from typing import Annotated, Literal
from pydantic import Field, model_validator
from .sourced_entities import Strict, Text, Fact, Name, Fate, Source, Attribution
from .sourced_entities_vocabulary import Gender, LocationTypes, EventTypes
from .site_common import unique_ids


class SharedFact(Fact):
    subject_id: Text
    family_id: Text | None = None
    representation: Literal['structured', 'prose', 'image']

    @model_validator(mode='after')
    def representation_contract(self):
        if self.representation != 'structured':
            if not self.value:
                raise ValueError('prose or image fact needs its value')
            if self.type != 'other':
                raise ValueError('prose and image forms use other with proposed_type')
        return self


def is_unreviewed_prose(fact: SharedFact) -> bool:
    """Identifies prose needing review; not a publication permission."""
    return fact.representation == 'prose' and fact.review.state != 'approved'


class SourcedRelation(Fact):
    """Relation from subject to relative; unreleased types keep other/proposed_type."""
    type: Literal['kinship', 'other']
    subject_id: Text
    family_id: Text | None = None
    shown: Attribution | None = None  # Permission to show, never death evidence.

    @model_validator(mode='after')
    def relation_contract(self):
        if not (self.related_person_id or self.related_name):
            raise ValueError('relation needs a person or an unresolved name')
        if self.type == 'other' and self.relationship_type:
            raise ValueError('unreleased relation uses proposed_type only')
        return self


class SharedPerson(Strict):
    id: Text
    name: Text
    names: list[Name]
    gender: Gender
    fate: Fate | None = None


class SharedFamily(Strict):
    id: Text
    name: Text
    names: list[Name]


class SharedPlace(SharedFamily):
    type: LocationTypes
    parent_id: Text | None = None
    coordinates: tuple[Annotated[float, Field(ge=-90, le=90)],
                       Annotated[float, Field(ge=-180, le=180)]] | None = None


class SharedOrganization(SharedFamily):
    """An organisation, with offices and membership carried by sourced facts."""


class SharedEvent(Strict):
    id: Text
    name: Text
    type: EventTypes


class SharedRecord(Strict):
    version: Literal['1']
    vocabulary_version: Literal['1.0.0']
    persons: list[SharedPerson]
    families: list[SharedFamily]
    places: list[SharedPlace]
    organizations: list[SharedOrganization]
    events: list[SharedEvent]
    sources: list[Source]
    facts: list[SharedFact]
    relations: list[SourcedRelation]

    @model_validator(mode='after')
    def record_references(self):
        identities = [*self.persons, *self.families, *self.places, *self.organizations]
        all_values = [*identities, *self.events, *self.sources, *self.facts, *self.relations]
        errors = unique_ids([x.id for x in all_values], 'shared id')
        persons = {p.id for p in self.persons}
        places = {p.id for p in self.places}
        organizations = {o.id for o in self.organizations}
        families = {f.id for f in self.families}
        events = {e.id for e in self.events}
        sources = {s.id for s in self.sources}
        subjects = {x.id for x in [*identities, *self.events, *self.relations]}
        facts = {f.id: f for f in self.facts}
        for fact in [*self.facts, *self.relations]:
            if fact.subject_id not in subjects:
                errors.append('unknown fact subject')
            for id, known, label in [(fact.place_id, places, 'place'),
                                      (fact.organization_id, organizations, 'organisation'),
                                      (fact.event_id, events, 'event'),
                                      (fact.related_person_id, persons, 'relative'),
                                      (fact.family_id, families, 'family')]:
                if id and id not in known:
                    errors.append(f'unknown fact {label}')
            if any(c.source_id not in sources for c in fact.citations):
                errors.append('unknown citation source')
        for relation in self.relations:
            if relation.subject_id not in persons:
                errors.append('relation subject must be a person')
            if relation.subject_id == relation.related_person_id:
                errors.append('self relation')
        for identity in identities:
            if any(c.source_id not in sources for n in identity.names for c in (n.citations or [])):
                errors.append('unknown name citation source')
        for person in self.persons:
            if person.fate and any(id not in facts or facts[id].subject_id != person.id for id in person.fate.rests_on):
                errors.append('fate must rest on own facts')
        by_place = {p.id: p for p in self.places}
        for place in self.places:
            seen = set()
            id = place.id
            while id:
                if id in seen:
                    errors.append('place parent cycle')
                    break
                if id not in by_place:
                    errors.append('unknown parent place')
                    break
                seen.add(id)
                id = by_place[id].parent_id
        if errors:
            raise ValueError('; '.join(errors))
        return self
