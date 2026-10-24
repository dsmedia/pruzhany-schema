"""Current site contracts and LLM extraction schemas."""

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
from .page import Block, Page, PagesData
from .shared import ExternalReference
from .site_common import CrossReference

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
    # Physical pages and shared references
    "Block",
    "Page",
    "PagesData",
    "CrossReference",
    "ExternalReference",
]

from .sourced_entities import SourcedDate, Review, Attribution, Source, Citation, Fact, Name, Fate, Mention, legacyHolocaustFate

__all__ += ["SourcedDate", "Review", "Attribution", "Source", "Citation", "Fact", "Name", "Fate", "Mention", "legacyHolocaustFate"]

from .site_common import EnglishCheck, TitleCheck, TranslationCheck, PrintedAddress, TextBasis, Authorship, PrintedTitle, SuppliedTitle, Translation, ContentItemBlockRef, text_basis_matches
from .content_item import ContentItem, PrintedSection, ContentItemsData
from .shared_record import SharedFact, SourcedRelation, SharedPerson, SharedFamily, PlaceIdentifier, SharedPlace, SharedOrganization, SharedEvent, SharedRecord, is_unreviewed_prose
from .shared_record import SiteCitation, SharedName, LifeEventDate, LifeEventMainPerson, is_printed_name
from .site_issue import IssueMention, IssueMentionsData, ContentItemRef, IssueLifeEvent, IssueLifeEventsData, SiteIssue, SiteArchive
from .media import MediaDecision, MediaText, MediaMaster, MediaDerivative, Media, PublicMedia, public_media

__all__ += ['MediaDecision', 'MediaText', 'MediaMaster', 'MediaDerivative', 'Media', 'PublicMedia', 'public_media']

__all__ += [
    'SiteCitation', 'SharedName', 'LifeEventDate', 'LifeEventMainPerson', 'is_printed_name',
    'EnglishCheck', 'TitleCheck', 'TranslationCheck', 'PrintedAddress', 'TextBasis', 'Authorship', 'PrintedTitle', 'SuppliedTitle', 'Translation',
    'ContentItemBlockRef', 'text_basis_matches', 'ContentItem', 'PrintedSection', 'ContentItemsData',
    'SharedFact', 'SourcedRelation', 'SharedPerson', 'SharedFamily', 'PlaceIdentifier', 'SharedPlace',
    'SharedOrganization', 'SharedEvent', 'SharedRecord', 'is_unreviewed_prose',
    'IssueMention', 'IssueMentionsData', 'ContentItemRef', 'IssueLifeEvent',
    'IssueLifeEventsData', 'SiteIssue', 'SiteArchive',
]

from .shared_record import Holder
from .sourced_entities import SourceDerivation
__all__ += ["Holder", "SourceDerivation"]

from .citation_requirements import statement_citation_shortfalls, shared_record_citation_shortfalls
from .quote_publication import quote_shown, corroborated
__all__ += ['statement_citation_shortfalls', 'shared_record_citation_shortfalls']
