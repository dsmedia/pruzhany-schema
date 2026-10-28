"""Content items and printed sections in the current site documents."""
from .generated.models import ContentItem, ContentItemsData, PrintedSection, ReadingStatus
from typing import Annotated, Literal
from pydantic import BeforeValidator, Field, model_validator
from .sourced_entities import Strict, Text, Day
from .site_common import CrossReference, ContentItemBlockRef, PrintedTitle, SuppliedTitle, Translation, unique_ids
from .site_content_vocabulary import ImpressoTypes, ContentItemSubtypes, Subjects, SiteVocabularyVersion, SUBTYPE_PARENTS


def integer_offset(value):
    # JSON 1 and 1.0 are the same number in Zod; strings and booleans stay invalid.
    return int(value) if isinstance(value, float) and value.is_integer() else value


Offset = Annotated[int, BeforeValidator(integer_offset), Field(ge=0, le=9007199254740991)]


ReadingStatusValue = Literal['machine', 'session_checked', 'person_corrected']


def _ContentItem__content_contract(self):
    if self.subtype and SUBTYPE_PARENTS[self.subtype] != self.type:
        raise ValueError('subtype has a different Impresso parent')
    errors = unique_ids(self.subject_ids, 'subject id')
    if any(n > len(self.full_text) or (i > 0 and n <= self.block_breaks[i - 1])
           for i, n in enumerate(self.block_breaks)):
        errors.append('block breaks must be ordered offsets within full_text')
    if errors:
        raise ValueError('; '.join(errors))
    return self


def _PrintedSection__members(self):
    if errors := unique_ids(self.content_item_ids, 'section member'):
        raise ValueError('; '.join(errors))
    return self


def _ContentItemsData__content_references(self):
    errors = unique_ids([i.id for i in self.content_items], 'content item id')
    errors += unique_ids([s.id for s in self.sections], 'section id')
    items = {i.id: i for i in self.content_items}
    sections = {s.id: s for s in self.sections}
    for item in self.content_items:
        if item.section_id and (item.section_id not in sections or
                                item.id not in sections[item.section_id].content_item_ids):
            errors.append('content item must belong to its named section')
        if any(r.target_id not in items for r in item.cross_references):
            errors.append('unknown cross-reference content item')
    for section in self.sections:
        if any(id not in items or items[id].section_id != section.id for id in section.content_item_ids):
            errors.append('section membership must agree in both directions')
    if errors:
        raise ValueError('; '.join(errors))
    return self
