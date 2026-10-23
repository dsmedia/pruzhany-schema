"""One shared record, built on production sourced facts and standing."""
from typing import Annotated, Literal, get_args
from pydantic import Field, TypeAdapter, ValidationError, model_validator
from .sourced_entities import Strict, Text, Date, Day, Fact, Name, Fate, Source, Attribution, Citation
from .sourced_entities_vocabulary import Gender, LocationTypes, EventTypes, EventParts, EVENT_PART_KINDS, VocabularyVersion
from .site_common import PrintedAddress, unique_ids

_DAY = TypeAdapter(Day)


class SiteCitation(Citation):
    """Located notice evidence; an unlocated older citation stays verbatim."""
    addresses: Annotated[list[PrintedAddress], Field(min_length=1)] | None = None

    @model_validator(mode='after')
    def located_notice(self):
        if self.addresses is None:
            return self
        if not (self.unit_id and self.unit_id.strip() and self.edition_date and
                self.quote and self.quote.strip()):
            raise ValueError('located notice citation needs content item, issue date and quote')
        try:
            _DAY.validate_python(self.edition_date)
        except ValidationError as exc:
            raise ValueError('located notice citation needs content item, issue date and quote') from exc
        if self.quote not in '\n'.join(a.text for a in self.addresses):
            raise ValueError('citation quote must occur at its printed address')
        return self


class SharedName(Name):
    """Released names with located evidence; supplied attribution is inherited."""
    citations: list[SiteCitation] | None = None


def is_printed_name(name: SharedName) -> bool:
    return name.kind == 'printed'


class LifeEventDate(Strict):
    printed: Text | None = None
    printed_calendar: Literal['gregorian', 'hebrew'] | None = None
    start: Date | None = None
    qualifier: Literal['reported_in'] | None = None
    reported_in: Day | None = None

    @model_validator(mode='after')
    def event_date(self):
        if self.qualifier == 'reported_in' and self.reported_in:
            if self.printed or self.printed_calendar or self.start:
                raise ValueError('reported_in cannot carry a printed or normalized event date')
        elif not self.printed or not self.printed_calendar or self.qualifier or self.reported_in:
            raise ValueError('event date needs printed words and calendar or reported_in qualifier')
        if self.start and self.printed_calendar == 'hebrew':
            raise ValueError('normalization requires a printed Gregorian date')
        return self


class LifeEventMainPerson(Strict):
    person_id: Text
    part: EventParts


class SharedFact(Fact):
    citations: list[SiteCitation] = Field(min_length=1)
    subject_id: Text
    family_id: Text | None = None
    representation: Literal['structured', 'prose', 'image']

    @model_validator(mode='after')
    def representation_contract(self):
        # Legacy Fact still reads parenthood; the current site writer must use a child person.
        if self.type == 'parenthood' or self.proposed_type == 'parenthood':
            raise ValueError('parenthood is deprecated; use parent_of to a child person')
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
    citations: list[SiteCitation] = Field(min_length=1)
    subject_id: Text
    family_id: Text | None = None
    shown: Attribution | None = None  # Permission to show, never death evidence.

    @model_validator(mode='after')
    def relation_contract(self):
        if not (self.related_person_id or self.related_name):
            raise ValueError('relation needs a person or an unresolved name')
        if self.type == 'other' and self.relationship_type:
            raise ValueError('unreleased relation uses proposed_type only')
        if (any(c.addresses for c in self.citations) and
                (self.relationship_type == 'child_of' or self.proposed_type == 'child_of')):
            raise ValueError('notice relation must use parent_of, not child_of')
        return self


class SharedPerson(Strict):
    id: Text
    name: Text
    names: list[SharedName]
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
    proposed_type: Text | None = None
    main_people: list[LifeEventMainPerson]
    dates: Annotated[list[LifeEventDate], Field(min_length=1)]
    location_id: Text | None = None
    description: str | None = None

    @model_validator(mode='after')
    def event_contract(self):
        errors = unique_ids([p.person_id for p in self.main_people], 'event main person')
        if (self.type == 'other') != bool(self.proposed_type):
            errors.append('event proposed_type exactly for other')
        if self.proposed_type in get_args(EventTypes):
            errors.append('released event kind cannot be proposed_type')
        kind = self.proposed_type or self.type
        if any(kind not in EVENT_PART_KINDS[p.part] for p in self.main_people):
            errors.append('part does not fit event kind')
        if any(d.qualifier == 'reported_in' for d in self.dates) and len(self.dates) != 1:
            errors.append('reported_in must be the only date when no date is printed')
        if errors:
            raise ValueError('; '.join(errors))
        return self


class SharedRecord(Strict):
    version: Literal['1']
    vocabulary_version: VocabularyVersion
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
        births, deaths = set(), set()
        for event in self.events:
            if event.location_id and event.location_id not in places:
                errors.append('unknown life event place')
            for main_person in event.main_people:
                if main_person.person_id not in persons:
                    errors.append('main person must resolve to a person')
                # RiC-CM R070/R072, not an OWL functional-property claim.
                seen = (births if event.type == 'birth' and main_person.part == 'baby' else
                        deaths if event.type == 'death' and main_person.part == 'deceased' else None)
                if seen is not None:
                    if main_person.person_id in seen:
                        errors.append(f'person has more than one {event.type}')
                    seen.add(main_person.person_id)
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
        notice_relations = set()
        for relation in self.relations:
            if relation.subject_id not in persons:
                errors.append('relation subject must be a person')
            if relation.subject_id == relation.related_person_id:
                errors.append('self relation')
            if any(c.addresses for c in relation.citations):
                key = (relation.subject_id, relation.relationship_type or relation.proposed_type,
                       relation.related_person_id or relation.related_name)
                if key in notice_relations:
                    errors.append('duplicate notice relation')
                notice_relations.add(key)
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
