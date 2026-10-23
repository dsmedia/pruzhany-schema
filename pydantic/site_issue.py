"""Per-issue site documents and their joins to the shared record."""
from typing import Annotated, Literal
from pydantic import Field, model_validator
from .sourced_entities import Strict, Text, Day
from .sourced_entities_vocabulary import MentionRoles, ContentUnitRoles
from .project_output import PagesData
from .site_common import PrintedAddress, unique_ids
from .content_item import ContentItemsData
from .shared_record import SharedRecord


class IssueMention(Strict):
    """Located words or whole regions; content_item_id is the current derived join."""
    id: Text
    person_id: Text
    content_item_id: Text
    address_grain: Literal['words', 'regions']
    printed_name: Text | None
    roles: list[MentionRoles] = Field(min_length=1)
    addresses: list[PrintedAddress] = Field(min_length=1)
    title: str | None = None
    function: str | None = None
    wkd_id: str | None = None

    @model_validator(mode='after')
    def mention_contract(self):
        errors = unique_ids(self.roles, 'mention role')
        if (self.address_grain == 'regions') != (self.printed_name is None):
            errors.append('printed name must be null exactly when address grain is regions')
        if (self.printed_name is not None and
                self.printed_name not in '\n'.join(a.text for a in self.addresses)):
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
    content_items: Annotated[list[ContentItemRef], Field(min_length=1)]

    @model_validator(mode='after')
    def content_item_ids(self):
        if errors := unique_ids([c.content_item_id for c in self.content_items], 'event content item'):
            raise ValueError('; '.join(errors))
        return self


class IssueLifeEventsData(Strict):
    issue_date: Day
    life_events: list[IssueLifeEvent]

    @model_validator(mode='after')
    def life_event_ids(self):
        if errors := unique_ids([e.id for e in self.life_events], 'life event id'):
            raise ValueError('; '.join(errors))
        assigned = set()
        for event in self.life_events:
            for ref in event.content_items:
                if ref.content_item_id in assigned:
                    raise ValueError('content item belongs to more than one life event')
                assigned.add(ref.content_item_id)
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


def printed_address_errors(addresses, refs, pages, match):
    errors = []
    for address in addresses:
        found = False
        for ref in refs:
            page = pages.get(ref.page_id)
            if not page or page.image_uri != address.image_uri:
                continue
            for block in page.blocks:
                if block.id not in ref.block_ids:
                    continue
                a, b = address.bbox, block.bbox
                if match == 'whole-region':
                    matches = a == b and address.text == block.transcription
                else:
                    matches = (
                        a[0] >= b[0] and a[1] >= b[1] and
                        a[0] + a[2] <= b[0] + b[2] and a[1] + a[3] <= b[1] + b[3] and
                        (match != 'text' or address.text in block.transcription)
                    )
                if matches:
                    found = True
        if not found:
            errors.append('region mention address must equal a whole region of its content item'
                          if match == 'whole-region' else
                          'printed address is outside its content item or heading')

    return errors


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
        return texts


    for item in value.content_items.content_items:
        texts = own(item.page_blocks, f'item:{item.id}', item.id)
        if not text_from_regions(texts, item.full_text, item.block_breaks):
            errors.append(f"{item.id}: full_text and block_breaks must follow the regions' line breaks and broken-word joins")
        if item.printed_title:
            errors += printed_address_errors(item.printed_title.addresses, item.page_blocks, pages, 'text')
        errors += printed_address_errors(item.supplied_title.based_on.addresses, item.page_blocks, pages, 'bounds')
        if item.translation:
            errors += printed_address_errors(item.translation.based_on.addresses, item.page_blocks, pages, 'bounds')
    for section in value.content_items.sections:
        own(section.heading_blocks, f'section:{section.id}', None)
        errors += printed_address_errors(section.printed_title.addresses, section.heading_blocks, pages, 'text')
        if section.supplied_title:
            errors += printed_address_errors(section.supplied_title.based_on.addresses, section.heading_blocks, pages, 'bounds')
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
            errors += printed_address_errors(mention.addresses, item.page_blocks, pages,
                           'whole-region' if mention.address_grain == 'regions' else 'text')
    for event in value.life_events.life_events:
        for ref in event.content_items:
            item = items.get(ref.content_item_id)
            if item is None:
                errors.append('unknown life event content item')
            elif item.event_id and item.event_id != event.id:
                errors.append('content item event disagrees with life event')
    return errors


def line_text_matches(source: str, text: str) -> bool:
    """Only LF-to-space and line-ending -/maqaf joins may change the text."""
    lines = source.split('\n')
    positions = {0}
    for i, literal in enumerate(lines):
        endings = ['\n', ' '] if i + 1 < len(lines) else ['']
        if i + 1 < len(lines) and can_join(literal, lines[i + 1]):
            sign, literal = literal[-1], literal[:-1]
            endings = [sign + '\n', sign + ' ', sign, '']
        following = set()
        for at in positions:
            for ending in endings:
                fragment = literal + ending
                if text.startswith(fragment, at):
                    following.add(at + len(fragment))
        positions = following
        if not positions:
            return False
    return len(text) in positions


def can_join(before: str, after: str) -> bool:
    return (len(before) > 1 and before[-1] in '-־' and before[-2] not in ' \t\r\n'
            and bool(after) and after[0] not in ' \t\r\n')


def text_from_regions(regions: list[str], text: str, breaks: list[int]) -> bool:
    starts = breaks or [0]
    if len(starts) != len(regions) or starts[0] != 0:
        return False
    # Keep the hand-made form, including its exact whitespace and empty regions.
    literal_starts, offset = [], 0
    for region in regions:
        literal_starts.append(offset)
        offset += len(region) + 2
    if text == '\n\n'.join(regions) and starts == literal_starts:
        return True

    states = {('', 0)}
    for i, source in enumerate(regions):
        start = starts[i]
        ends = [starts[i + 1] - 2, starts[i + 1]] if i + 1 < len(starts) else [len(text)]
        following = set()
        for carry, previous_end in states:
            choices = [(carry + source, '')]
            if i + 1 < len(regions) and can_join(source, regions[i + 1]):
                split = max(source.rfind(c) for c in ' \t\r\n')
                head, tail = source[:max(0, split)], source[split + 1:]
                # text_of emits the whole joined word in the following region.
                # A token already receiving a carry cannot also be deferred.
                if (split < 0 or source[split] in ' \n') and (head or not carry):
                    choices.extend((carry + head, pending) for pending in (tail[:-1], tail))
            for end in ends:
                if end < start:
                    continue
                separator = '\n\n' if end > start and previous_end > 0 else ''
                if start != previous_end + len(separator) or text[previous_end:start] != separator:
                    continue
                segment = text[start:end]
                for candidate, pending in choices:
                    if line_text_matches(candidate, segment):
                        following.add((pending, end))
        states = following
        if not states:
            return False
    return ('', len(text)) in states


def notice_key(c):
    return c.source_id, c.edition_date, c.unit_id


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
        first_issues = {}
        content_items = {}
        for issue in self.issues:
            date = issue.content_items.issue_date
            pages = {p.id: p for p in issue.pages.pages}
            issue_events = {e.id for e in issue.life_events.life_events}
            if any(m.person_id not in people for m in issue.mentions.mentions):
                errors.append('unknown mention person')
            for item in issue.content_items.content_items:
                content_items[(date, item.id)] = dict(text=item.full_text, page_blocks=item.page_blocks, pages=pages,
                    mentions=[m for m in issue.mentions.mentions if m.content_item_id == item.id],
                    events={e.id for e in issue.life_events.life_events
                            if any(c.content_item_id == item.id for c in e.content_items)})
                if any(id not in places for id in item.location_ids):
                    errors.append('unknown content item place')
                if any(id not in organizations for id in item.organization_ids):
                    errors.append('unknown content item organisation')
                if item.event_id and item.event_id not in events and item.event_id not in issue_events:
                    errors.append('unknown content item event')
            for event in issue.life_events.life_events:
                if event.id not in events:
                    errors.append('unknown life event')
                first_issues[event.id] = min(date, first_issues.get(event.id, date))
        for event in self.shared_record.events:
            for date in event.dates:
                if (date.qualifier == 'reported_in' and event.id in first_issues and
                        date.reported_in != first_issues[event.id]):
                    errors.append('reported_in must be the first issue date')

        def cited_content_item(c):
            return content_items.get((c.edition_date, c.unit_id)) if c.edition_date and c.unit_id else None

        assertions = [*self.shared_record.facts, *self.shared_record.relations]
        citations = [c for f in assertions for c in f.citations] + [
            c for p in self.shared_record.persons for n in p.names for c in (n.citations or [])]
        for c in citations:
            # Scope to located evidence written now; older citations keep their reading.
            if not c.addresses:
                continue
            content_item = cited_content_item(c)
            if not content_item:
                errors.append('unknown cited content item')
            else:
                if c.quote and c.quote not in content_item['text']:
                    errors.append('citation quote must occur in content item')
                errors += printed_address_errors(c.addresses, content_item['page_blocks'],
                                                 content_item['pages'], 'text')
        for child in self.shared_record.persons:
            if not any(n.kind == 'supplied' for n in child.names):
                continue
            births = [f for f in self.shared_record.facts if f.subject_id == child.id and
                      f.type == 'birth' and (f.qualifiers or {}).get('child_count') == '1' and
                      f.event_id in events and events[f.event_id].type == 'birth' and
                      any(p.person_id == child.id and p.part == 'baby' for p in events[f.event_id].main_people)]
            if not births:
                errors.append('described child needs a single-child birth fact')
            for birth in births:
                if sum(p.part == 'baby' for p in events[birth.event_id].main_people) != 1:
                    errors.append('single-child birth must have exactly one baby')
                notices = [c for c in birth.citations if c.addresses and c.quote and cited_content_item(c) and
                           birth.event_id in cited_content_item(c)['events']]
                if not any(m.person_id == child.id and m.address_grain == 'words' and
                           'subject' in m.roles and m.printed_name and m.printed_name in c.quote
                           for c in notices for m in cited_content_item(c)['mentions']):
                    errors.append('described child needs a cited designation mention')

                notice_keys = {notice_key(c) for c in notices}
                if not any(n.kind == 'supplied' and any(c.addresses and notice_key(c) in notice_keys for c in (n.citations or []))
                           for n in child.names):
                    errors.append('supplied name must cite the birth notice')
                parents = [p for p in events[birth.event_id].main_people if p.part == 'parent']
                if not parents or any(not any(r.subject_id == p.person_id and
                        r.related_person_id == child.id and r.relationship_type == 'parent_of' and
                        any(c.addresses and notice_key(c) in notice_keys for c in r.citations) for r in self.shared_record.relations)
                        for p in parents):
                    errors.append('described child needs each parent relation citing the birth notice')
        if errors:
            raise ValueError('; '.join(errors))
        return self
