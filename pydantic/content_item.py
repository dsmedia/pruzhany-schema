"""Content items and printed sections, beside the unchanged ContentUnit."""
from typing import Annotated, Literal
from pydantic import BeforeValidator, Field, model_validator
from .sourced_entities import Strict, Text, Day
from .project_output import CrossReference
from .site_common import ContentItemBlockRef, PrintedTitle, SuppliedTitle, Translation, unique_ids
from .site_content_vocabulary import ImpressoTypes, ContentItemSubtypes, Subjects, SUBTYPE_PARENTS


def integer_offset(value):
    # JSON 1 and 1.0 are the same number in Zod; strings and booleans stay invalid.
    return int(value) if isinstance(value, float) and value.is_integer() else value


Offset = Annotated[int, BeforeValidator(integer_offset), Field(ge=0, le=9007199254740991)]


class ContentItem(Strict):
    id: Text
    type: ImpressoTypes
    subtype: ContentItemSubtypes | None = None
    printed_title: PrintedTitle | None = None
    supplied_title: SuppliedTitle
    subject_ids: list[Subjects]
    section_id: Text | None = None
    full_text: str  # Copy made for the site from the physical source's lines.
    translation: Translation | None = None
    block_breaks: list[Offset]
    page_blocks: list[ContentItemBlockRef] = Field(min_length=1)
    location_ids: list[Text]  # Places in the shared record; site spelling retained.
    organization_ids: list[Text]
    cross_references: list[CrossReference]
    event_id: Text | None = None

    @model_validator(mode='after')
    def content_contract(self):
        if self.subtype and SUBTYPE_PARENTS[self.subtype] != self.type:
            raise ValueError('subtype has a different Impresso parent')
        errors = unique_ids(self.subject_ids, 'subject id')
        if any(n > len(self.full_text) or (i > 0 and n <= self.block_breaks[i - 1])
               for i, n in enumerate(self.block_breaks)):
            errors.append('block breaks must be ordered offsets within full_text')
        if errors:
            raise ValueError('; '.join(errors))
        return self


class PrintedSection(Strict):
    """A printed heading and the content items beneath it, not a side list."""
    id: Text
    printed_title: PrintedTitle
    # Pydantic 2.12, "Fields / Default values", read 2026-10-22:
    # https://pydantic.dev/docs/validation/2.12/concepts/fields/#default-values
    # None in the type permits null; the default also permits omission.
    supplied_title: SuppliedTitle | None = None
    content_item_ids: list[Text] = Field(min_length=1)
    heading_blocks: list[ContentItemBlockRef] = Field(min_length=1)

    @model_validator(mode='after')
    def members(self):
        if errors := unique_ids(self.content_item_ids, 'section member'):
            raise ValueError('; '.join(errors))
        return self


class ContentItemsData(Strict):
    issue_date: Day
    vocabulary_version: Literal['0.1.0']
    content_items: list[ContentItem]
    sections: list[PrintedSection]

    @model_validator(mode='after')
    def content_references(self):
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
