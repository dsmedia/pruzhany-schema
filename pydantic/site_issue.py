"""Per-issue site documents and their joins to the shared record."""
from pydantic import Field, model_validator
from .sourced_entities import Strict, Text, Day
from .sourced_entities_vocabulary import MentionRoles, LifeEventTypes, ContentUnitRoles
from .project_output import PagesData
from .site_common import PrintedAddress, unique_ids
from .content_item import ContentItemsData
from .shared_record import SharedRecord


class IssueMention(Strict):
    """An addressed printed name; content_item_id is its current derived join."""
    id: Text
    person_id: Text
    content_item_id: Text
    printed_name: Text
    roles: list[MentionRoles] = Field(min_length=1)
    addresses: list[PrintedAddress] = Field(min_length=1)
    title: str | None = None
    function: str | None = None
    wkd_id: str | None = None

    @model_validator(mode='after')
    def mention_contract(self):
        errors = unique_ids(self.roles, 'mention role')
        if self.printed_name not in '\n'.join(a.text for a in self.addresses):
            errors.append('printed name must occur at the mention address')
        if errors:
            raise ValueError('; '.join(errors))
        return self


class IssueMentionsData(Strict):
    issue_date: Day
    mentions: list[IssueMention]

    @model_validator(mode='after')
    def mention_ids(self):
        if errors := unique_ids([m.id for m in self.mentions], 'mention id'):
            raise ValueError('; '.join(errors))
        return self


class ContentItemRef(Strict):
    content_item_id: Text
    role: ContentUnitRoles  # Content item's role, not the person's role.


class IssueLifeEvent(Strict):
    id: Text
    type: LifeEventTypes
    name: str
    principal_ids: list[Text]  # Persons in the shared record.
    date_hebrew: str | None
    date_gregorian: str | None
    location_id: str | None
    content_items: list[ContentItemRef]
    description: str | None


class IssueLifeEventsData(Strict):
    issue_date: Day
    life_events: list[IssueLifeEvent]

    @model_validator(mode='after')
    def life_event_ids(self):
        if errors := unique_ids([e.id for e in self.life_events], 'life event id'):
            raise ValueError('; '.join(errors))
        return self


class SiteIssue(Strict):
    """In-memory check of four documents. Pages keep their existing file shape."""
    pages: PagesData
    content_items: ContentItemsData
    mentions: IssueMentionsData
    life_events: IssueLifeEventsData

    @model_validator(mode='after')
    def issue_references(self):
        if errors := site_issue_errors(self):
            raise ValueError('; '.join(errors))
        return self


def site_issue_errors(value):
    errors = []
    date = value.content_items.issue_date
    if any(d != date for d in [value.pages.edition_date, value.mentions.issue_date,
                               value.life_events.issue_date, *[p.issue_date for p in value.pages.pages]]):
        errors.append('issue dates disagree')
    errors += unique_ids([p.id for p in value.pages.pages], 'page id')
    pages = {p.id: p for p in value.pages.pages}
    items = {i.id: i for i in value.content_items.content_items}
    owners = {}

    def own(refs, owner, unit):
        texts = []
        for ref in refs:
            for id in ref.block_ids:
                page = pages.get(ref.page_id)
                block = next((b for b in page.blocks if b.id == id), None) if page else None
                if block is None:
                    errors.append('unknown page or block')
                    continue
                key = (ref.page_id, id)
                if key in owners:
                    errors.append('region has more than one owner')
                owners[key] = owner
                if block.unit_id != unit:
                    errors.append('block content item disagrees with owner')
                texts.append(block.transcription)
        return '\n\n'.join(texts)

    def address_errors(addresses, refs, check_text):
        for address in addresses:
            found = False
            for ref in refs:
                page = pages.get(ref.page_id)
                if not page or page.image_uri != address.image_uri:
                    continue
                for block in page.blocks:
                    a, b = address.bbox, block.bbox
                    if (block.id in ref.block_ids and a[0] >= b[0] and a[1] >= b[1] and
                            a[0] + a[2] <= b[0] + b[2] and a[1] + a[3] <= b[1] + b[3] and
                            (not check_text or address.text in block.transcription)):
                        found = True
            if not found:
                errors.append('printed address is outside its content item or heading')

    for item in value.content_items.content_items:
        if own(item.page_blocks, f'item:{item.id}', item.id) != item.full_text:
            errors.append('full_text must be the block transcriptions joined by blank lines')
        if item.printed_title:
            address_errors(item.printed_title.addresses, item.page_blocks, True)
        address_errors(item.supplied_title.based_on.addresses, item.page_blocks, False)
        if item.translation:
            address_errors(item.translation.based_on.addresses, item.page_blocks, False)
    for section in value.content_items.sections:
        own(section.heading_blocks, f'section:{section.id}', None)
        address_errors(section.printed_title.addresses, section.heading_blocks, True)
        address_errors(section.supplied_title.based_on.addresses, section.heading_blocks, False)
    for page in value.pages.pages:
        errors += unique_ids([b.id for b in page.blocks], 'block id')
        for block in page.blocks:
            if (page.id, block.id) not in owners:
                errors.append('region has no owner')
    for mention in value.mentions.mentions:
        item = items.get(mention.content_item_id)
        if item is None:
            errors.append('unknown mention content item')
        else:
            address_errors(mention.addresses, item.page_blocks, True)
    for event in value.life_events.life_events:
        if any(r.content_item_id not in items for r in event.content_items):
            errors.append('unknown life event content item')
    return errors


class SiteArchive(Strict):
    """Validate joins without copying any person into an issue's files."""
    shared_record: SharedRecord
    issues: list[SiteIssue]

    @model_validator(mode='after')
    def shared_references(self):
        errors = unique_ids([i.content_items.issue_date for i in self.issues], 'issue date')
        people = {p.id for p in self.shared_record.persons}
        places = {p.id for p in self.shared_record.places}
        organizations = {o.id for o in self.shared_record.organizations}
        events = {e.id: e for e in self.shared_record.events}
        for issue in self.issues:
            issue_events = {e.id for e in issue.life_events.life_events}
            if any(m.person_id not in people for m in issue.mentions.mentions):
                errors.append('unknown mention person')
            for item in issue.content_items.content_items:
                if any(id not in places for id in item.location_ids):
                    errors.append('unknown content item place')
                if any(id not in organizations for id in item.organization_ids):
                    errors.append('unknown content item organisation')
                if item.event_id and item.event_id not in events and item.event_id not in issue_events:
                    errors.append('unknown content item event')
            for event in issue.life_events.life_events:
                if any(id not in people for id in event.principal_ids):
                    errors.append('unknown life event person')
                if event.location_id and event.location_id not in places:
                    errors.append('unknown life event place')
                if event.id in events and events[event.id].type != event.type:
                    errors.append('life event must agree with shared event')
        if errors:
            raise ValueError('; '.join(errors))
        return self
