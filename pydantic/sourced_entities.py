"""Optional stage-1 sourced assertions. All models are closed and strict."""
from .generated.models import Attribution, Citation, Fact, Fate, Mention, Name, Review, Source, SourceDerivation, SourcedDate, Strict
from typing import Literal, Annotated
from datetime import date as calendar_date
from calendar import monthrange
import json
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field, AfterValidator, model_validator
from .sourced_entities_vocabulary import FactTypes, RelationshipTypes, NameKinds, MentionRoles, SourceKinds, Confidence, ClaimStatus, ReviewStates, FateOutcomes, HolocaustFateTypes

def valid_date(v):
    calendar_date.fromisoformat(v + {4: "-01-01", 7: "-01", 10: ""}[len(v)])
    return v

Text = Annotated[str, Field(pattern=r"\S")]
Date = Annotated[str, Field(pattern=r"^\d{4}(-\d{2}(-\d{2})?)?$"), AfterValidator(valid_date)]
Day = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}$"), AfterValidator(valid_date)]
CITATION_REQUIREMENTS = json.loads((Path(__file__).resolve().parents[1] / 'vocabulary/citation-requirements.json').read_text(encoding='utf-8'))
# RFC 5646 §2.1, https://www.rfc-editor.org/rfc/rfc5646, read 2026-10-24: syntax, not registry membership.
SourceLanguage = Annotated[str, Field(pattern=CITATION_REQUIREMENTS['language_tag_pattern'])]


def _SourcedDate__validate_contract(self):
    validate_SourcedDate(self)
    return self


def _Review__validate_contract(self):
    validate_Review(self)
    return self


def _bare_host(value: str) -> str:
    if value.startswith('www.'):
        raise ValueError('host without www')
    return value

SourceHost = Annotated[str, Field(pattern=r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$"), AfterValidator(_bare_host)]


def _Citation__validate_contract(self):
    validate_Citation(self)
    return self


def _Fact__validate_contract(self):
    validate_Fact(self)
    return self


def _Name__supplied_name(self):
    if self.kind == 'supplied' and (not self.attribution or not self.citations):
        raise ValueError('supplied name needs attribution and citations')
    if self.attribution and self.kind != 'supplied':
        raise ValueError('supplied attribution needs the supplied name kind')
    return self


def _Fate__validate_contract(self):
    validate_Fate(self)
    return self


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
    if not any(x and x.strip() for x in (v.record_id,v.page,v.scan,v.time,v.unit_id,v.url,v.locator,v.reference_code)):
        raise ValueError('citation needs locator')


def validate_Fact(v):
    originals = {c.source_id for c in v.citations}
    if any(c.via in originals for c in v.citations if c.via):
        raise ValueError('citation via cannot also be an original for the same statement')
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
