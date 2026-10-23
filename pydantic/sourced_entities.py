"""Optional stage-1 sourced assertions. All models are closed and strict."""
from typing import Literal, Annotated
from datetime import date as calendar_date
from calendar import monthrange
from pydantic import BaseModel, ConfigDict, Field, AfterValidator, model_validator
from .sourced_entities_vocabulary import FactTypes, RelationshipTypes, NameKinds, MentionRoles, SourceKinds, Confidence, ClaimStatus, ReviewStates, FateOutcomes, HolocaustFateTypes

class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


def valid_date(v):
    calendar_date.fromisoformat(v + {4: "-01-01", 7: "-01", 10: ""}[len(v)])
    return v

Text = Annotated[str, Field(pattern=r"\S")]
Date = Annotated[str, Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$"), AfterValidator(valid_date)]
Day = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}$"), AfterValidator(valid_date)]


class SourcedDate(Strict):
    start: Date | None = None
    end: Date | None = None
    precision: Literal["year", "month", "day", "range"] | None = None
    printed: Text | None = None
    printed_calendar: Literal["gregorian", "hebrew"] | None = None
    inferred: bool | None = None

    @model_validator(mode="after")
    def validate_contract(self):
        validate_SourcedDate(self)
        return self


class Review(Strict):
    state: ReviewStates
    by: Text | None = None
    on: Day | None = None

    @model_validator(mode="after")
    def validate_contract(self):
        validate_Review(self)
        return self


class Attribution(Strict):
    by: Text
    on: Day
    note: str | None = None


class Source(Strict):
    id: Text
    kind: SourceKinds
    title: Text
    work_id: str | None = None
    author: str | None = None
    editor: str | None = None
    published: str | None = None
    repository: str | None = None
    url_pattern: str | None = None
    host: str | None = None
    ehri_institution_id: str | None = None


class Citation(Strict):
    source_id: Text
    record_id: str | None = None
    page: str | None = None
    scan: str | None = None
    time: str | None = None
    edition_date: str | None = None
    unit_id: str | None = None
    url: Annotated[str, Field(pattern=r"^https://[^\s/?#]+[^\s]*$")] | None = None
    quote: str | None = None
    note: str | None = None
    accessed: Day | None = None

    @model_validator(mode="after")
    def validate_contract(self):
        validate_Citation(self)
        return self


class Fact(Strict):
    id: Text
    type: FactTypes
    proposed_type: Text | None = None
    value: Text | None = None
    date: SourcedDate | None = None
    place_id: Text | None = None
    organization_id: Text | None = None
    event_id: Text | None = None
    related_person_id: Text | None = None
    relationship_type: RelationshipTypes | None = None
    related_name: Text | None = None
    qualifiers: dict[str, str] | None = None
    holocaust_related: bool | None = None
    citations: list[Citation] = Field(min_length=1)
    evidence_confidence: Confidence
    identity_confidence: Confidence
    status: ClaimStatus
    review: Review
    attribution: Attribution

    @model_validator(mode="after")
    def validate_contract(self):
        validate_Fact(self)
        return self


class Name(Strict):
    value: Text
    kind: NameKinds
    script: Annotated[str, Field(pattern=r"^[A-Za-z]{4}$")]
    lang: Annotated[str, Field(pattern=r"^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$")] | None = None
    citations: list[Citation] | None = None
    attribution: Attribution | None = None

    @model_validator(mode='after')
    def supplied_name(self):
        if self.kind == 'supplied' and (not self.attribution or not self.citations):
            raise ValueError('supplied name needs attribution and citations')
        if self.attribution and self.kind != 'supplied':
            raise ValueError('supplied attribution needs the supplied name kind')
        return self


class Fate(Strict):
    outcome: FateOutcomes
    confidence: Confidence
    rests_on: list[str]
    review: Review
    summary: str | None = None

    @model_validator(mode="after")
    def validate_contract(self):
        validate_Fate(self)
        return self


class Mention(Strict):
    id: Text
    person_id: Text
    unit_id: Text
    printed_name: Text
    role: MentionRoles | None = None
    title: str | None = None
    function: str | None = None
    wkd_id: str | None = None


def validate_SourcedDate(v):
    if not (v.start or (v.printed and v.printed.strip())):
        raise ValueError('date needs start or printed')
    if v.printed_calendar and not (v.printed and v.printed.strip()):
        raise ValueError('calendar needs printed')
    if v.end and v.precision != 'range':
        raise ValueError('end needs range precision')
    if v.precision == 'range':
        if not v.start or not v.end:
            raise ValueError('range needs bounds')
        lower = v.start + {4:'-01-01',7:'-01',10:''}[len(v.start)]
        upper = v.end + '-12-31' if len(v.end) == 4 else v.end + f'-{monthrange(int(v.end[:4]), int(v.end[5:]))[1]:02}' if len(v.end) == 7 else v.end
        if lower > upper:
            raise ValueError('range reversed')
    elif v.precision and (not v.start or len(v.start) != {'year':4,'month':7,'day':10}[v.precision]):
        raise ValueError('precision mismatch')


def validate_Review(v):
    if v.state == 'approved' and not (v.by and v.by.strip() and v.on):
        raise ValueError('approval requires reviewer and day')


def validate_Citation(v):
    if not any(x and x.strip() for x in (v.record_id,v.page,v.scan,v.time,v.unit_id,v.url)):
        raise ValueError('citation needs locator')


def validate_Fact(v):
    if (v.type == 'other') != bool(v.proposed_type and v.proposed_type.strip()):
        raise ValueError('proposed_type exactly for other')
    if v.type == 'kinship' and not (v.relationship_type and (v.related_name or v.related_person_id)):
        raise ValueError('kinship needs relationship and relative')
    if v.type == 'occupation' and not v.value:
        raise ValueError('occupation needs value')
    if v.type == 'residence' and not (v.place_id or v.value):
        raise ValueError('residence needs place or value')
    if v.type == 'event_participation' and not v.event_id:
        raise ValueError('participation needs event')
    if v.type in ('birth','death') and not (v.date or v.place_id or v.value):
        raise ValueError('birth/death needs payload')


def validate_Fate(v):
    if v.outcome != 'unknown' and not v.rests_on:
        raise ValueError('known fate needs facts')


def legacyHolocaustFate(fate: Fate) -> HolocaustFateTypes:
    if fate.outcome in ('perished','survived') and fate.confidence != 'confirmed':
        return 'likely_' + fate.outcome
    return fate.outcome
