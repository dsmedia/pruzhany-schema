"""Schema definitions for the ADK edition pipeline."""

from .llm_output import (
    LlmBlock,
    LlmContentUnit,
    LlmContentUnitRef,
    LlmEditionOutput,
    LlmLifeEvent,
    LlmLocation,
    LlmPageLayout,
    LlmPerson,
    LlmPersonRelationship,
)
from .project_output import (
    Block,
    ContentUnit,
    ContentUnitsData,
    ContentUnitRef,
    EnrichedEvent,
    EnrichedLocation,
    EnrichedOrganization,
    EnrichedPerson,
    EnrichmentData,
    LifeEvent,
    LifeEventsData,
    OrganizationMember,
    Page,
    PagesData,
    Topic,
)

__all__ = [
    # LLM Output Schemas
    "LlmBlock",
    "LlmContentUnit",
    "LlmContentUnitRef",
    "LlmEditionOutput",
    "LlmLifeEvent",
    "LlmLocation",
    "LlmPageLayout",
    "LlmPerson",
    "LlmPersonRelationship",
    # Project Output Schemas
    "Block",
    "ContentUnit",
    "ContentUnitsData",
    "ContentUnitRef",
    "EnrichedEvent",
    "EnrichedLocation",
    "EnrichedOrganization",
    "EnrichedPerson",
    "EnrichmentData",
    "LifeEvent",
    "LifeEventsData",
    "OrganizationMember",
    "Page",
    "PagesData",
    "Topic",
]

from .sourced_entities import SourcedDate, Review, Attribution, Source, Citation, Fact, Name, Fate, Mention, legacyHolocaustFate

__all__ += ["SourcedDate", "Review", "Attribution", "Source", "Citation", "Fact", "Name", "Fate", "Mention", "legacyHolocaustFate"]

from .site_common import PrintedAddress, TextBasis, Authorship, PrintedTitle, SuppliedTitle, Translation, ContentItemBlockRef, text_basis_matches
from .content_item import ContentItem, PrintedSection, ContentItemsData
from .shared_record import SharedFact, SourcedRelation, SharedPerson, SharedFamily, SharedPlace, SharedOrganization, SharedEvent, SharedRecord, is_unreviewed_prose
from .site_issue import IssueMention, IssueMentionsData, ContentItemRef, IssueLifeEvent, IssueLifeEventsData, SiteIssue, SiteArchive

__all__ += [
    'PrintedAddress', 'TextBasis', 'Authorship', 'PrintedTitle', 'SuppliedTitle', 'Translation',
    'ContentItemBlockRef', 'text_basis_matches', 'ContentItem', 'PrintedSection', 'ContentItemsData',
    'SharedFact', 'SourcedRelation', 'SharedPerson', 'SharedFamily', 'SharedPlace',
    'SharedOrganization', 'SharedEvent', 'SharedRecord', 'is_unreviewed_prose',
    'IssueMention', 'IssueMentionsData', 'ContentItemRef', 'IssueLifeEvent',
    'IssueLifeEventsData', 'SiteIssue', 'SiteArchive',
]
