"""Generated from LinkML by linkml/generate.py. Do not edit."""
from __future__ import annotations

from functools import cache, partial
from importlib import import_module
from typing import Annotated, Literal
from pydantic import AfterValidator, BeforeValidator, BaseModel, ConfigDict, Field, field_validator, model_validator

@cache
def _resolve(module, function):
    return getattr(import_module(".." + module, __package__), function)

def _call(module, function, *args):
    return _resolve(module, function)(*args)

def _typed_call(module, function, path, skip_none, value):
    if value is None and skip_none:
        return value
    if path:
        if not isinstance(value, (list, tuple)):
            return value
        return [_typed_call(module, function, path[1:], skip_none, item) for item in value]
    return _call(module, function, value)

class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

class Attribution(Strict):
    'Who made or allowed something, on what day, with an optional note.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    by: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    note: None | str = Field(default=None)


class Block(BaseModel):
    'One region of print on a page, its box and the words read in it, belonging to one content item, or to no item when it is a section heading.'
    model_config = ConfigDict(**{})
    id: str = Field(default=...)
    bbox: Annotated[tuple[int, int, int, int], Field(min_length=4, max_length=4)] = Field(default=...)
    transcription: str = Field(default=...)
    confidence: None | float = Field(default=None)
    image_crop: None | str = Field(default=None)
    unit_id: None | str = Field(default=...)


class Citation(Strict):
    "Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    via: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    reference_code: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    record_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    quote_language: Annotated[str, Field(pattern='^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$')] | None = Field(default=None)
    public_note: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    locator: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    record_id: None | str = Field(default=None)
    page: None | str = Field(default=None)
    scan: None | str = Field(default=None)
    time: None | str = Field(default=None)
    edition_date: None | str = Field(default=None)
    unit_id: None | str = Field(default=None)
    url: Annotated[str, Field(pattern='^https://[^\\s/?#]+[^\\s]*$')] | None = Field(default=None)
    quote: None | str = Field(default=None)
    note: None | str = Field(default=None)
    accessed: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)

    @model_validator(mode='after')
    def validate_contract(self):
        return _call('sourced_entities', '_Citation__validate_contract', self)


class ContentItem(Strict):
    'One article, notice, greeting or advertisement of the issue: its kind, its titles, its text and English, the regions it is printed in and what it names.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    type: Literal['ad', 'article', 'chapter', 'chronicle', 'death_notice', 'discussion', 'entertainment', 'image', 'page', 'radio_broadcast_episode', 'radio_bulletin', 'table', 'weather'] = Field(default=...)
    subtype: Literal['announcement', 'appeal', 'bar_mitzvah_greeting', 'birth_greeting', 'commercial_advertisement', 'condolence', 'death_announcement', 'departure_greeting', 'editorial', 'engagement_greeting', 'greeting', 'humour', 'letter', 'meeting_notice', 'memorial_notice', 'new_year_greeting', 'opinion', 'poem', 'sketch', 'thanks', 'wedding_greeting'] | None = Field(default=None)
    printed_title: PrintedTitle | None = Field(default=None)
    supplied_title: SuppliedTitle = Field(default=...)
    subject_ids: list[Literal['community_affairs', 'culture', 'economy', 'education', 'health', 'international_affairs', 'jewish_world', 'literature', 'palestine', 'sport', 'zionism']] = Field(default=...)
    section_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    full_text: str = Field(default=...)
    translation: Translation | None = Field(default=None)
    reading_status: ReadingStatus | None = Field(default=None)
    block_breaks: Annotated[list[Annotated[int, Field(ge=0, le=9007199254740991)]], BeforeValidator(partial(_typed_call, 'content_item', 'integer_offset', ['items'], False))] = Field(default=...)
    page_blocks: Annotated[list[ContentItemBlockRef], Field(min_length=1)] = Field(default=...)
    location_ids: list[Annotated[str, Field(pattern='\\S')]] = Field(default=...)
    organization_ids: list[Annotated[str, Field(pattern='\\S')]] = Field(default=...)
    cross_references: list[CrossReference] = Field(default=...)
    event_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)

    @model_validator(mode='after')
    def content_contract(self):
        return _call('content_item', '_ContentItem__content_contract', self)


class ContentItemBlockRef(Strict):
    'The regions of one page that a content item or a section heading covers, in reading order.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    page_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    block_ids: Annotated[list[Annotated[str, Field(pattern='\\S')]], Field(min_length=1)] = Field(default=...)


class ContentItemRef(Strict):
    'A content item that prints a life event, and the part it plays: the announcement itself, a greeting, a condolence, a mention or an advertisement.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    content_item_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    role: Literal['advertisement', 'condolence', 'congratulation', 'mention', 'primary_announcement'] = Field(default=...)


class ContentItemsData(Strict):
    "One issue's content items document: the issue's date, the vocabulary version its values are from, its content items and its printed sections."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    issue_date: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    vocabulary_version: Literal['0.1.0', '1.0.0', '1.1.0'] = Field(default=...)
    content_items: list[ContentItem] = Field(default=...)
    sections: list[PrintedSection] = Field(default=...)

    @model_validator(mode='after')
    def content_references(self):
        return _call('content_item', '_ContentItemsData__content_references', self)


class CrossReference(BaseModel):
    'A link from one content item to another in the same issue, with how sure it is and why.'
    model_config = ConfigDict(**{})
    target_id: str = Field(default=...)
    confidence: float = Field(default=...)
    relationship: str = Field(default=...)
    evidence: str = Field(default=...)


class Edition(Strict):
    'One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any.'
    model_config = ConfigDict(**{'strict': True, 'extra': 'forbid'})
    date: Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] = Field(default=...)
    hebrewDate: str = Field(default=...)
    hebrewMonth: Annotated[Annotated[int, Field(ge=1, le=13)], BeforeValidator(partial(_typed_call, 'content_item', 'integer_offset', [], False))] = Field(default=...)
    hebrewYear: Annotated[Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)], BeforeValidator(partial(_typed_call, 'content_item', 'integer_offset', [], False))] = Field(default=...)
    holiday: Annotated[None | str, BeforeValidator(partial(_typed_call, 'editions', 'present_value', [], False))] = Field(default=None, exclude_if=lambda value: value is None)


class EditionsCatalog(Strict):
    'The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site.'
    model_config = ConfigDict(**{'strict': True, 'extra': 'forbid'})
    availableDates: list[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')]] = Field(default=...)
    editions: list[Edition] = Field(default=...)
    historicalEvents: list[HistoricalEvent] = Field(default=...)
    holidays: list[Holiday] = Field(default=...)


class EnglishCheck(Strict):
    'A later, separate check of one English field against one exact reading of the printed text, bound to both and to the judgement kept by their digests.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    reading_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    reading_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    english_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    judgement_id: Annotated[str, Field(pattern='^[^\\s\\u0085\\uFEFF]+:(title|text)$')] = Field(default=...)
    judgement_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    attribution: Authorship = Field(default=...)


class ExternalReference(BaseModel):
    'A reference to a record in an outside database or resource, such as a page of testimony at Yad Vashem.'
    model_config = ConfigDict(**{})
    source: str = Field(default=...)
    url: None | str = Field(default=None)
    record_id: None | str = Field(default=None)
    notes: None | str = Field(default=None)
    verified: bool | None = Field(default=None)


class Fact(Strict):
    "One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes)."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    type: Literal['birth', 'burial', 'commemoration', 'death', 'deportation', 'education', 'emigration', 'event_participation', 'ghetto_role', 'kinship', 'membership', 'occupation', 'office', 'other', 'parenthood', 'partisan_service', 'residence', 'survival'] = Field(default=...)
    proposed_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    value: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    date: SourcedDate | None = Field(default=None)
    place_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    organization_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    event_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    related_person_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    relationship_type: Literal['child_in_law', 'child_of', 'colleague', 'cousin', 'family_member', 'friend', 'grandchild_of', 'grandparent_of', 'great_grandchild_of', 'great_grandparent_of', 'in_law', 'nephew_niece_of', 'parent_in_law', 'parent_of', 'sibling', 'sibling_in_law', 'spouse', 'student_of', 'teacher_of', 'uncle_aunt_of'] | None = Field(default=None)
    related_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    qualifiers: dict[str, str] | None = Field(default=None)
    holocaust_related: bool | None = Field(default=None)
    citations: Annotated[list[Citation], Field(min_length=1)] = Field(default=...)
    evidence_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    identity_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    status: Literal['accepted', 'disputed', 'proposed', 'rejected'] = Field(default=...)
    review: Review = Field(default=...)
    attribution: Attribution = Field(default=...)

    @model_validator(mode='after')
    def validate_contract(self):
        return _call('sourced_entities', '_Fact__validate_contract', self)


FactQualifiers = dict[str, str]

class Fate(Strict):
    'What became of a person in the Holocaust, as far as the record shows, the facts it rests on and its review.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    outcome: Literal['died_before', 'not_applicable', 'perished', 'survived', 'unknown'] = Field(default=...)
    confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    rests_on: list[str] = Field(default=...)
    review: Review = Field(default=...)
    summary: None | str = Field(default=None)

    @model_validator(mode='after')
    def validate_contract(self):
        return _call('sourced_entities', '_Fate__validate_contract', self)


class HistoricalEvent(Strict):
    'An event in the world outside the town, such as Kristallnacht, on a day or over a span of days.'
    model_config = ConfigDict(**{'strict': True, 'extra': 'forbid'})
    date: Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] = Field(default=...)
    description: str = Field(default=...)
    endDate: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, BeforeValidator(partial(_typed_call, 'editions', 'present_value', [], False))] = Field(default=None, exclude_if=lambda value: value is None)
    name: str = Field(default=...)


class Holder(Strict):
    "Who holds a source: an institution, a family or a private person, with its outside identifiers and its web host. A private holder's name is never published."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    short_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    kind: Literal['family', 'institution', 'private'] = Field(default=...)
    identifiers: Annotated[list[PlaceIdentifier], Field(min_length=1)] | None = Field(default=None)
    host: Annotated[Annotated[str, Field(pattern='^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', '_bare_host', [], True))] = Field(default=None)


class Holiday(Strict):
    'A Jewish holiday on a given day.'
    model_config = ConfigDict(**{'strict': True, 'extra': 'forbid'})
    date: Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] = Field(default=...)
    hebrewName: Annotated[None | str, BeforeValidator(partial(_typed_call, 'editions', 'present_value', [], False))] = Field(default=None, exclude_if=lambda value: value is None)
    name: str = Field(default=...)


class IssueLifeEvent(Strict):
    'A life event of the shared record as this issue prints it: the content items that print it, each with its part.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    content_items: Annotated[list[ContentItemRef], Field(min_length=1)] = Field(default=...)

    @model_validator(mode='after')
    def content_item_ids(self):
        return _call('site_issue', '_IssueLifeEvent__content_item_ids', self)


class IssueLifeEventsData(Strict):
    "One issue's life events document: the issue's date and the life events it prints."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    issue_date: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    life_events: list[IssueLifeEvent] = Field(default=...)

    @model_validator(mode='after')
    def life_event_ids(self):
        return _call('site_issue', '_IssueLifeEventsData__life_event_ids', self)


class IssueMention(Strict):
    "A person of the shared record named in a content item, pinned to the printed words of the name or to whole regions, with the person's roles there. A mention alone does not say the content item is about the person."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    person_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    content_item_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    address_grain: Literal['regions', 'words'] = Field(default=...)
    printed_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=...)
    roles: Annotated[list[Literal['advertiser', 'author', 'betrothed', 'deceased', 'donor', 'honoree', 'mourner', 'named', 'office_holder', 'parent', 'signer', 'subject']], Field(min_length=1)] = Field(default=...)
    addresses: Annotated[list[PrintedAddress], Field(min_length=1)] = Field(default=...)
    title: None | str = Field(default=None)
    function: None | str = Field(default=None)
    wkd_id: None | str = Field(default=None)

    @model_validator(mode='after')
    def mention_contract(self):
        return _call('site_issue', '_IssueMention__mention_contract', self)


class IssueMentionsData(Strict):
    "One issue's mentions document: the issue's date and its mentions."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    issue_date: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    mentions: list[IssueMention] = Field(default=...)

    @model_validator(mode='after')
    def mention_ids(self):
        return _call('site_issue', '_IssueMentionsData__mention_ids', self)


class LifeEventDate(Strict):
    "One date of a life event: the words printed with their calendar, or, where no date is printed, the day of the first issue that reported it, or the preferred record statement's date for a death known from records alone."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    record_fact_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    printed: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    printed_calendar: Literal['gregorian', 'hebrew'] | None = Field(default=None)
    start: Annotated[Annotated[str, Field(pattern='^\\d{4}(-\\d{2}(-\\d{2})?)?$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)
    qualifier: Literal['reported_in'] | None = Field(default=None)
    reported_in: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)

    @model_validator(mode='after')
    def event_date(self):
        return _call('shared_record', '_LifeEventDate__event_date', self)


class LifeEventMainPerson(Strict):
    'One main person of a life event and their part in it (the baby, a parent, the bride, the groom, the boy, the one who died, the one remembered); each part means a declared local subproperty of rico:affectsOrAffected or rico:hasOrHadParticipant (EventParts).'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    person_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    part: Literal['baby', 'boy', 'bride', 'deceased', 'groom', 'parent', 'remembered'] = Field(default=...)


class MediaConsent(Strict):
    'The private record of the permission to show a medium: its basis, who gave it by role, what it covers, the document that holds it and any withdrawal. Never public.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    basis: Literal['family-permission', 'holder-licence', 'institution-terms', 'owner-family-papers', 'public-domain'] = Field(default=...)
    granted_by: Literal['family', 'holder', 'institution', 'owner'] = Field(default=...)
    scope: MediaConsentScope = Field(default=...)
    ref: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    withdrawn_on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)


class MediaConsentScope(Strict):
    'What a permission covers: the use, the people shown, and whether people not identified are covered.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    use: Literal['site', 'site+download'] = Field(default=...)
    person_ids: list[Annotated[str, Field(pattern='\\S')]] = Field(default=...)
    unidentified: bool = Field(default=...)

    @model_validator(mode='after')
    def unique_people(self):
        return _call('media', '_MediaConsentScope__unique_people', self)


class MediaDecision(Strict):
    'A review or a clearance: whose role made it (the owner or the project) and on what day.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    role: Literal['owner', 'project'] = Field(default=...)
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)


class MediaDepicted(Strict):
    'One person a picture shows, identified or not, where in the picture, and on whose identification.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    person_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=...)
    region: MediaRegion = Field(default=...)
    identified_by: Literal['family', 'inscription', 'record'] = Field(default=...)


class MediaDerivative(Strict):
    "One served copy of a picture: a WebP file at one of the exported widths, named by the master's digest, made by resizing alone."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    url: Annotated[str, Field(pattern='^https://pictures\\.pruzhanychronicles\\.org/media/[0-9a-f]{64}-w(?:100|400|800|1200)\\.webp$')] = Field(default=...)
    width: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(default=...)
    height: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(default=...)
    process: Literal['resize'] = Field(default=...)


class MediaFamilyWords(Strict):
    "The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    page: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    quote: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    quote_language: Annotated[str, Field(pattern='^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$')] = Field(default=...)


class MediaFixity(Strict):
    'A dated check that a master file still has its digest.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    sha256: Annotated[str, Field(pattern='^[0-9a-f]{64}$')] = Field(default=...)


class MediaMaster(Strict):
    "Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    bucket: Annotated[str, Field(pattern='^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$')] = Field(default=...)
    key: Annotated[str, Field(pattern='^(?:[a-z0-9_-]+/)*[0-9a-f]{64}$')] = Field(default=...)
    sha256: Annotated[str, Field(pattern='^[0-9a-f]{64}$')] = Field(default=...)
    mime: Annotated[str, Field(pattern='^(?:image|audio|video|application)/[a-z0-9][a-z0-9.+-]*$')] = Field(default=...)
    bytes: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(default=...)
    checked: MediaFixity | None = Field(default=None)

    @model_validator(mode='after')
    def named_by_digest(self):
        return _call('media', '_MediaMaster__named_by_digest', self)


class MediaPortrait(Strict):
    "The picture a person's page shows as their portrait: a reviewed medium and the region of it to show."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    media_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    region: MediaRegion = Field(default=...)
    reviewed: MediaDecision = Field(default=...)


class MediaRegion(Strict):
    "A rectangle in a medium's master picture, in its own pixels after orientation."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    x: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(default=...)
    y: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(default=...)
    w: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(default=...)
    h: Annotated[int, Field(ge=1, le=9007199254740991)] = Field(default=...)


class MediaText(Strict):
    'Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    text: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    lang: Annotated[str, Field(pattern='^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$')] = Field(default=...)
    reviewed: MediaDecision | None = Field(default=None)


class MediaWithdrawal(Strict):
    'That a medium was withdrawn from the site, on what day and why; its record stays.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    reason: Literal['error', 'family', 'holder'] = Field(default=...)


class Mention(Strict):
    "The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    person_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    unit_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    printed_name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    role: Literal['advertiser', 'author', 'betrothed', 'deceased', 'donor', 'honoree', 'mourner', 'named', 'office_holder', 'parent', 'signer', 'subject'] | None = Field(default=None)
    title: None | str = Field(default=None)
    function: None | str = Field(default=None)
    wkd_id: None | str = Field(default=None)


class Name(Strict):
    "One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    value: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    kind: Literal['alias', 'birth', 'later', 'married', 'nickname', 'printed', 'religious', 'spelling', 'supplied'] = Field(default=...)
    script: Annotated[str, Field(pattern='^[A-Za-z]{4}$')] = Field(default=...)
    lang: Annotated[str, Field(pattern='^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$')] | None = Field(default=None)
    citations: list[Citation] | None = Field(default=None)
    attribution: Attribution | None = Field(default=None)

    @model_validator(mode='after')
    def supplied_name(self):
        return _call('sourced_entities', '_Name__supplied_name', self)


class Page(BaseModel):
    'One printed page of the issue: its picture, its size and its regions of print.'
    model_config = ConfigDict(**{})
    id: str = Field(default=...)
    issue_date: str = Field(default=...)
    page_number: int = Field(default=...)
    image_uri: str = Field(default=...)
    dimensions: Annotated[tuple[int, int], Field(min_length=2, max_length=2)] = Field(default=...)
    blocks: list[Block] = Field(default=...)


class PagesData(BaseModel):
    "One issue's pages document: the issue's date and its pages in order."
    model_config = ConfigDict(**{})
    edition_date: str = Field(default=...)
    pages: list[Page] = Field(default=...)


class PlaceIdentifier(Strict):
    "One identifier of a person, organisation, place or holder, carried only on evidence, never from a match of names. Outside ids are read on their authority's own pages; merged local ids cite the registered source of the adjudicated merge."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    value: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    url: Annotated[str, Field(pattern='^https://[^\\s/?#]+[^\\s]*$')] | None = Field(default=None)
    accessed: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    attribution: Attribution = Field(default=...)
    type: Literal['old_identifier'] | None = Field(default=None)


class PrintedAddress(Strict):
    "Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    image_uri: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    bbox: Annotated[tuple[Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)], Annotated[float, Field(gt=0)], Annotated[float, Field(gt=0)]], Field(min_length=4, max_length=4)] = Field(default=...)
    text: str = Field(default=...)


class PrintedSection(Strict):
    'A printed heading and the content items that stand beneath it, such as the title "What is heard in town?" over the town\'s news.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    printed_title: PrintedTitle = Field(default=...)
    supplied_title: SuppliedTitle | None = Field(default=None)
    content_item_ids: Annotated[list[Annotated[str, Field(pattern='\\S')]], Field(min_length=1)] = Field(default=...)
    heading_blocks: Annotated[list[ContentItemBlockRef], Field(min_length=1)] = Field(default=...)

    @model_validator(mode='after')
    def members(self):
        return _call('content_item', '_PrintedSection__members', self)


class PrintedTitle(Strict):
    'A title as printed in the paper: its words and where each line of them stands.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    text: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    addresses: Annotated[list[PrintedAddress], Field(min_length=1)] = Field(default=...)

    @model_validator(mode='after')
    def printed_words(self):
        return _call('site_common', '_PrintedTitle__printed_words', self)


class PublicMedia(Strict):
    'One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='^[a-z0-9]+(?:-[a-z0-9]+)*$')] = Field(default=...)
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    kind: Literal['audio', 'document', 'image', 'video'] = Field(default=...)
    caption: MediaText = Field(default=...)
    alt: MediaText | None = Field(default=None)
    inscription: MediaText | None = Field(default=None)
    transcript: MediaText | None = Field(default=None)
    family_words: MediaFamilyWords | None = Field(default=None)
    depicted: list[MediaDepicted] = Field(default=...)
    shows_unidentified: bool = Field(default=...)
    width: Annotated[int, Field(ge=1, le=9007199254740991)] | None = Field(default=None)
    height: Annotated[int, Field(ge=1, le=9007199254740991)] | None = Field(default=None)
    duration: Annotated[float, Field(gt=0)] | None = Field(default=None)
    credit: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    conditions_of_access: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    conditions_of_use: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    rights: Literal['http://rightsstatements.org/vocab/CNE/1.0/', 'http://rightsstatements.org/vocab/InC-EDU/1.0/', 'http://rightsstatements.org/vocab/InC-NC/1.0/', 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/', 'http://rightsstatements.org/vocab/InC-RUU/1.0/', 'http://rightsstatements.org/vocab/InC/1.0/', 'http://rightsstatements.org/vocab/NKC/1.0/', 'http://rightsstatements.org/vocab/NoC-CR/1.0/', 'http://rightsstatements.org/vocab/NoC-NC/1.0/', 'http://rightsstatements.org/vocab/NoC-OKLR/1.0/', 'http://rightsstatements.org/vocab/NoC-US/1.0/', 'http://rightsstatements.org/vocab/UND/1.0/', 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'https://creativecommons.org/licenses/by-nc-sa/4.0/', 'https://creativecommons.org/licenses/by-nc/4.0/', 'https://creativecommons.org/licenses/by-nd/4.0/', 'https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by/4.0/', 'https://creativecommons.org/publicdomain/mark/1.0/', 'https://creativecommons.org/publicdomain/zero/1.0/'] = Field(default='http://rightsstatements.org/vocab/CNE/1.0/')
    cleared: MediaDecision | None = Field(default=None)
    withdrawn: MediaWithdrawal | None = Field(default=None)
    link: Annotated[str, Field(pattern='^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\\s\\\\]*)?$')] | None = Field(default=None)
    derived: Annotated[list[MediaDerivative], Field(min_length=1)] | None = Field(default=None)

    @model_validator(mode='after')
    def media_contract(self):
        return _call('media', '_PublicMedia__media_contract', self)


class ReadingStatus(Strict):
    "How far a content item's text and its English have been checked, each recorded on its own; null for either means it is not recorded, not that it was reviewed."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    text: Literal['machine', 'person_corrected', 'session_checked'] | None = Field(default=...)
    english: Literal['machine', 'person_corrected', 'session_checked'] | None = Field(default=...)


class Review(Strict):
    'Whether a person has reviewed a statement, who and on what day.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    state: Literal['approved', 'pending'] = Field(default=...)
    by: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)

    @model_validator(mode='after')
    def validate_contract(self):
        return _call('sourced_entities', '_Review__validate_contract', self)


class SharedEvent(Strict):
    'One life event, once for each happening across every issue (a birth, a wedding, a death, a memorial and so on): its kind, its main people and their parts, its dates and its place.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    type: Literal['bar_mitzvah', 'birth', 'celebration', 'community_event', 'death', 'engagement', 'holocaust_event', 'memorial', 'other', 'wedding'] = Field(default=...)
    proposed_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    main_people: list[LifeEventMainPerson] = Field(default=...)
    evidence_basis: Literal['records_only'] | None = Field(default=None)
    dates: Annotated[list[LifeEventDate], Field(min_length=1)] = Field(default=...)
    location_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    description: None | str = Field(default=None)

    @model_validator(mode='after')
    def event_contract(self):
        return _call('shared_record', '_SharedEvent__event_contract', self)


class SharedFamily(Strict):
    'One family of the record: its id, the name shown and its names.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    names: list[Name] = Field(default=...)


class SharedPerson(Strict):
    'One person of the record, across every issue: their id, the name shown, every name they are known by, their gender, what became of them, their portrait and evidenced identifiers.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    portrait: MediaPortrait | None = Field(default=None)
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    names: list[SharedName] = Field(default=...)
    gender: Literal['female', 'male', 'unknown'] = Field(default=...)
    fate: Fate | None = Field(default=None)
    identifiers: Annotated[list[PlaceIdentifier], Field(min_length=1)] | None = Field(default=None)


class SharedRecord(Strict):
    'The shared record whole: its version, the vocabulary version it uses, and every person, family, place, organisation, event, source, holder, fact, relation and medium.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    version: Literal['1'] = Field(default=...)
    vocabulary_version: Literal['1.3.0'] = Field(default=...)
    persons: list[SharedPerson] = Field(default=...)
    families: list[SharedFamily] = Field(default=...)
    places: list[SharedPlace] = Field(default=...)
    organizations: list[SharedOrganization] = Field(default=...)
    events: list[SharedEvent] = Field(default=...)
    sources: list[Source] = Field(default=...)
    holders: list[Holder] = Field(default_factory=list)
    facts: list[SharedFact] = Field(default=...)
    relations: list[SourcedRelation] = Field(default=...)
    media: list[Media] | None = Field(default=None)

    @model_validator(mode='after')
    def record_references(self):
        return _call('shared_record', '_SharedRecord__record_references', self)


class Source(Strict):
    "A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    made_by: Literal['family', 'institution', 'perpetrator', 'studio', 'unknown'] | None = Field(default=None)
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    kind: Literal['archive_database', 'book', 'family_document', 'memoir', 'memorial_book', 'oral_history', 'photograph', 'press', 'the_paper', 'web_page'] = Field(default=...)
    title: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    short_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    holder_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    reference_code: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    language: Annotated[list[Annotated[str, Field(pattern='^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$')]], Field(min_length=1)] | None = Field(default=None)
    derived_from: Annotated[list[SourceDerivation], Field(min_length=1)] | None = Field(default=None)
    dated: SourcedDate | None = Field(default=None)
    quotes_cleared: Attribution | None = Field(default=None)
    quote_condition: Literal['unique_information'] | None = Field(default=None)
    private: bool | None = Field(default=None)
    work_id: None | str = Field(default=None)
    author: None | str = Field(default=None)
    editor: None | str = Field(default=None)
    published: None | str = Field(default=None)
    repository: None | str = Field(default=None)
    url_pattern: None | str = Field(default=None)
    host: Annotated[Annotated[str, Field(pattern='^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', '_bare_host', [], True))] = Field(default=None)
    subjects: Annotated[list[Annotated[str, Field(pattern='\\S')]], Field(min_length=1)] | None = Field(default=None)


class SourceDerivation(Strict):
    'The record a source we hold was made from, and how: a copy or a transcription of it.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    relation: Literal['copy', 'transcription'] = Field(default=...)


class SourcedDate(Strict):
    'A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    start: Annotated[Annotated[str, Field(pattern='^\\d{4}(-\\d{2}(-\\d{2})?)?$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)
    end: Annotated[Annotated[str, Field(pattern='^\\d{4}(-\\d{2}(-\\d{2})?)?$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)
    precision: Literal['day', 'month', 'range', 'year'] | None = Field(default=None)
    printed: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    printed_calendar: Literal['gregorian', 'hebrew'] | None = Field(default=None)
    inferred: bool | None = Field(default=None)

    @model_validator(mode='after')
    def validate_contract(self):
        return _call('sourced_entities', '_SourcedDate__validate_contract', self)


class SuppliedTitle(Strict):
    'A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    text: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    language: Literal['en'] = Field(default=...)
    based_on: TextBasis = Field(default=...)
    attribution: Authorship = Field(default=...)
    checked_against: TitleCheck | None = Field(default=None, exclude_if=lambda value: value is None)

    @field_validator('checked_against', mode='before')
    @classmethod
    def check_is_not_null(cls, value):
        return _call('site_common', '__AttributedEnglish__check_is_not_null', cls, value)


class TextBasis(Strict):
    'The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_text: str = Field(default=...)
    addresses: Annotated[list[PrintedAddress], Field(min_length=1)] = Field(default=...)


class Translation(Strict):
    "An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    text: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    language: Literal['en'] = Field(default=...)
    based_on: TextBasis = Field(default=...)
    attribution: Authorship = Field(default=...)
    checked_against: TranslationCheck | None = Field(default=None, exclude_if=lambda value: value is None)

    @field_validator('checked_against', mode='before')
    @classmethod
    def check_is_not_null(cls, value):
        return _call('site_common', '__AttributedEnglish__check_is_not_null', cls, value)


class Authorship(Attribution):
    'Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    by: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    on: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')], AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=...)
    note: None | str = Field(default=None)
    kind: Literal['model', 'person'] = Field(default=...)


class Media(PublicMedia):
    'One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='^[a-z0-9]+(?:-[a-z0-9]+)*$')] = Field(default=...)
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    kind: Literal['audio', 'document', 'image', 'video'] = Field(default=...)
    caption: MediaText = Field(default=...)
    alt: MediaText | None = Field(default=None)
    inscription: MediaText | None = Field(default=None)
    transcript: MediaText | None = Field(default=None)
    family_words: MediaFamilyWords | None = Field(default=None)
    depicted: list[MediaDepicted] = Field(default=...)
    shows_unidentified: bool = Field(default=...)
    width: Annotated[int, Field(ge=1, le=9007199254740991)] | None = Field(default=None)
    height: Annotated[int, Field(ge=1, le=9007199254740991)] | None = Field(default=None)
    duration: Annotated[float, Field(gt=0)] | None = Field(default=None)
    credit: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    conditions_of_access: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    conditions_of_use: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    rights: Literal['http://rightsstatements.org/vocab/CNE/1.0/', 'http://rightsstatements.org/vocab/InC-EDU/1.0/', 'http://rightsstatements.org/vocab/InC-NC/1.0/', 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/', 'http://rightsstatements.org/vocab/InC-RUU/1.0/', 'http://rightsstatements.org/vocab/InC/1.0/', 'http://rightsstatements.org/vocab/NKC/1.0/', 'http://rightsstatements.org/vocab/NoC-CR/1.0/', 'http://rightsstatements.org/vocab/NoC-NC/1.0/', 'http://rightsstatements.org/vocab/NoC-OKLR/1.0/', 'http://rightsstatements.org/vocab/NoC-US/1.0/', 'http://rightsstatements.org/vocab/UND/1.0/', 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'https://creativecommons.org/licenses/by-nc-sa/4.0/', 'https://creativecommons.org/licenses/by-nc/4.0/', 'https://creativecommons.org/licenses/by-nd/4.0/', 'https://creativecommons.org/licenses/by-sa/4.0/', 'https://creativecommons.org/licenses/by/4.0/', 'https://creativecommons.org/publicdomain/mark/1.0/', 'https://creativecommons.org/publicdomain/zero/1.0/'] = Field(default='http://rightsstatements.org/vocab/CNE/1.0/')
    cleared: MediaDecision | None = Field(default=None)
    withdrawn: MediaWithdrawal | None = Field(default=None)
    link: Annotated[str, Field(pattern='^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\\s\\\\]*)?$')] | None = Field(default=None)
    derived: Annotated[list[MediaDerivative], Field(min_length=1)] | None = Field(default=None)
    master: MediaMaster | None = Field(default=None)
    consent: MediaConsent | None = Field(default=None)

    @model_validator(mode='after')
    def consent_state(self):
        return _call('media', '_Media__consent_state', self)


class SharedFact(Fact):
    "One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    type: Literal['birth', 'burial', 'commemoration', 'death', 'deportation', 'education', 'emigration', 'event_participation', 'ghetto_role', 'kinship', 'membership', 'occupation', 'office', 'other', 'parenthood', 'partisan_service', 'residence', 'survival'] = Field(default=...)
    proposed_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    value: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    date: SourcedDate | None = Field(default=None)
    place_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    organization_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    event_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    related_person_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    relationship_type: Literal['child_in_law', 'child_of', 'colleague', 'cousin', 'family_member', 'friend', 'grandchild_of', 'grandparent_of', 'great_grandchild_of', 'great_grandparent_of', 'in_law', 'nephew_niece_of', 'parent_in_law', 'parent_of', 'sibling', 'sibling_in_law', 'spouse', 'student_of', 'teacher_of', 'uncle_aunt_of'] | None = Field(default=None)
    related_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    qualifiers: dict[str, str] | None = Field(default=None)
    holocaust_related: bool | None = Field(default=None)
    citations: Annotated[list[SiteCitation], Field(min_length=1)] = Field(default=...)
    evidence_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    identity_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    status: Literal['accepted', 'disputed', 'proposed', 'rejected'] = Field(default=...)
    review: Review = Field(default=...)
    attribution: Attribution = Field(default=...)
    subject_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    family_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    representation: Literal['image', 'prose', 'structured'] = Field(default=...)

    @model_validator(mode='after')
    def representation_contract(self):
        return _call('shared_record', '_SharedFact__representation_contract', self)


class SharedName(Name):
    'One name of a person in the shared record, with its evidence located on the printed page where the site writer found it.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    value: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    kind: Literal['alias', 'birth', 'later', 'married', 'nickname', 'printed', 'religious', 'spelling', 'supplied'] = Field(default=...)
    script: Annotated[str, Field(pattern='^[A-Za-z]{4}$')] = Field(default=...)
    lang: Annotated[str, Field(pattern='^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$')] | None = Field(default=None)
    citations: list[SiteCitation] | None = Field(default=None)
    attribution: Attribution | None = Field(default=None)


class SharedOrganization(SharedFamily):
    'One organisation of the record: its id, the name shown, its names and evidenced identifiers; its offices and members are sourced facts.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    names: list[Name] = Field(default=...)
    identifiers: Annotated[list[PlaceIdentifier], Field(min_length=1)] | None = Field(default=None)


class SharedPlace(SharedFamily):
    'One place of the record: its names, its kind, the place it lies in, its coordinates and its outside identifiers.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    name: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    names: list[Name] = Field(default=...)
    type: Literal['address', 'camp', 'city', 'country', 'deportation_point', 'district', 'forest', 'ghetto', 'landmark', 'massacre_site', 'region', 'shtetl', 'street', 'town', 'village'] = Field(default=...)
    parent_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    coordinates: Annotated[tuple[Annotated[float, Field(ge=-90, le=90)], Annotated[float, Field(ge=-180, le=180)]], Field(min_length=2, max_length=2)] | None = Field(default=None)
    identifiers: Annotated[list[PlaceIdentifier], Field(min_length=1)] | None = Field(default=None)


class SiteCitation(Citation):
    'A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes.'
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    source_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    via: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    reference_code: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    record_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    quote_language: Annotated[str, Field(pattern='^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$')] | None = Field(default=None)
    public_note: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    locator: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    record_id: None | str = Field(default=None)
    page: None | str = Field(default=None)
    scan: None | str = Field(default=None)
    time: None | str = Field(default=None)
    edition_date: None | str = Field(default=None)
    unit_id: None | str = Field(default=None)
    url: Annotated[str, Field(pattern='^https://[^\\s/?#]+[^\\s]*$')] | None = Field(default=None)
    quote: None | str = Field(default=None)
    note: None | str = Field(default=None)
    accessed: Annotated[Annotated[str, Field(pattern='^\\d{4}-\\d{2}-\\d{2}$')] | None, AfterValidator(partial(_typed_call, 'sourced_entities', 'valid_date', [], True))] = Field(default=None)
    addresses: Annotated[list[PrintedAddress], Field(min_length=1)] | None = Field(default=None)

    @model_validator(mode='after')
    def located_notice(self):
        return _call('shared_record', '_SiteCitation__located_notice', self)


class SourcedRelation(Fact):
    "One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    type: Literal['kinship', 'other'] = Field(default=...)
    proposed_type: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    value: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    date: SourcedDate | None = Field(default=None)
    place_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    organization_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    event_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    related_person_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    relationship_type: Literal['child_in_law', 'child_of', 'colleague', 'cousin', 'family_member', 'friend', 'grandchild_of', 'grandparent_of', 'great_grandchild_of', 'great_grandparent_of', 'in_law', 'nephew_niece_of', 'parent_in_law', 'parent_of', 'sibling', 'sibling_in_law', 'spouse', 'student_of', 'teacher_of', 'uncle_aunt_of'] | None = Field(default=None)
    related_name: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    qualifiers: dict[str, str] | None = Field(default=None)
    holocaust_related: bool | None = Field(default=None)
    citations: Annotated[list[SiteCitation], Field(min_length=1)] = Field(default=...)
    evidence_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    identity_confidence: Literal['confirmed', 'possible', 'probable'] = Field(default=...)
    status: Literal['accepted', 'disputed', 'proposed', 'rejected'] = Field(default=...)
    review: Review = Field(default=...)
    attribution: Attribution = Field(default=...)
    subject_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    family_id: Annotated[str, Field(pattern='\\S')] | None = Field(default=None)
    shown: Attribution | None = Field(default=None)

    @model_validator(mode='after')
    def relation_contract(self):
        return _call('shared_record', '_SourcedRelation__relation_contract', self)


class TitleCheck(EnglishCheck):
    "A check of a supplied title's English."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    reading_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    reading_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    english_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    judgement_id: Annotated[str, Field(pattern='^[^\\s\\u0085\\uFEFF]+:title$')] = Field(default=...)
    judgement_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    attribution: Authorship = Field(default=...)


class TranslationCheck(EnglishCheck):
    "A check of a translation's English."
    model_config = ConfigDict(**{'extra': 'forbid', 'strict': True})
    reading_id: Annotated[str, Field(pattern='\\S')] = Field(default=...)
    reading_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    english_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    judgement_id: Annotated[str, Field(pattern='^[^\\s\\u0085\\uFEFF]+:text$')] = Field(default=...)
    judgement_sha256: Annotated[str, Field(min_length=64, max_length=64, pattern='^[0-9a-f]{64}$')] = Field(default=...)
    attribution: Authorship = Field(default=...)


Attribution.model_rebuild()
Authorship.model_rebuild()
Block.model_rebuild()
Citation.model_rebuild()
ContentItem.model_rebuild()
ContentItemBlockRef.model_rebuild()
ContentItemRef.model_rebuild()
ContentItemsData.model_rebuild()
CrossReference.model_rebuild()
Edition.model_rebuild()
EditionsCatalog.model_rebuild()
EnglishCheck.model_rebuild()
ExternalReference.model_rebuild()
Fact.model_rebuild()
Fate.model_rebuild()
HistoricalEvent.model_rebuild()
Holder.model_rebuild()
Holiday.model_rebuild()
IssueLifeEvent.model_rebuild()
IssueLifeEventsData.model_rebuild()
IssueMention.model_rebuild()
IssueMentionsData.model_rebuild()
LifeEventDate.model_rebuild()
LifeEventMainPerson.model_rebuild()
Media.model_rebuild()
MediaConsent.model_rebuild()
MediaConsentScope.model_rebuild()
MediaDecision.model_rebuild()
MediaDepicted.model_rebuild()
MediaDerivative.model_rebuild()
MediaFamilyWords.model_rebuild()
MediaFixity.model_rebuild()
MediaMaster.model_rebuild()
MediaPortrait.model_rebuild()
MediaRegion.model_rebuild()
MediaText.model_rebuild()
MediaWithdrawal.model_rebuild()
Mention.model_rebuild()
Name.model_rebuild()
Page.model_rebuild()
PagesData.model_rebuild()
PlaceIdentifier.model_rebuild()
PrintedAddress.model_rebuild()
PrintedSection.model_rebuild()
PrintedTitle.model_rebuild()
PublicMedia.model_rebuild()
ReadingStatus.model_rebuild()
Review.model_rebuild()
SharedEvent.model_rebuild()
SharedFact.model_rebuild()
SharedFamily.model_rebuild()
SharedName.model_rebuild()
SharedOrganization.model_rebuild()
SharedPerson.model_rebuild()
SharedPlace.model_rebuild()
SharedRecord.model_rebuild()
SiteCitation.model_rebuild()
Source.model_rebuild()
SourceDerivation.model_rebuild()
SourcedDate.model_rebuild()
SourcedRelation.model_rebuild()
SuppliedTitle.model_rebuild()
TextBasis.model_rebuild()
TitleCheck.model_rebuild()
Translation.model_rebuild()
TranslationCheck.model_rebuild()

__all__ = ['Attribution', 'Authorship', 'Block', 'Citation', 'ContentItem', 'ContentItemBlockRef', 'ContentItemRef', 'ContentItemsData', 'CrossReference', 'Edition', 'EditionsCatalog', 'EnglishCheck', 'ExternalReference', 'Fact', 'FactQualifiers', 'Fate', 'HistoricalEvent', 'Holder', 'Holiday', 'IssueLifeEvent', 'IssueLifeEventsData', 'IssueMention', 'IssueMentionsData', 'LifeEventDate', 'LifeEventMainPerson', 'Media', 'MediaConsent', 'MediaConsentScope', 'MediaDecision', 'MediaDepicted', 'MediaDerivative', 'MediaFamilyWords', 'MediaFixity', 'MediaMaster', 'MediaPortrait', 'MediaRegion', 'MediaText', 'MediaWithdrawal', 'Mention', 'Name', 'Page', 'PagesData', 'PlaceIdentifier', 'PrintedAddress', 'PrintedSection', 'PrintedTitle', 'PublicMedia', 'ReadingStatus', 'Review', 'SharedEvent', 'SharedFact', 'SharedFamily', 'SharedName', 'SharedOrganization', 'SharedPerson', 'SharedPlace', 'SharedRecord', 'SiteCitation', 'Source', 'SourceDerivation', 'SourcedDate', 'SourcedRelation', 'SuppliedTitle', 'TextBasis', 'TitleCheck', 'Translation', 'TranslationCheck']
