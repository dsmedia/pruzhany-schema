"""Project output schemas matching Zod definitions.

These schemas exactly match the project's Zod schemas in src/lib/schemas/,
using project bounding box format ([x, y, width, height] in pixels).

The pipeline converts LLM output schemas to these for final JSON output.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# =============================================================================
# Shared Types (from shared.schema.ts)
# =============================================================================

HolocaustFate = Literal[
    "unknown",
    "perished",
    "likely_perished",
    "survived",
    "likely_survived",
    "died_before",
    "not_applicable",
]


class ExternalReference(BaseModel):
    """Reference to external database or resource."""

    source: str = Field(description="Source name (e.g., 'yad_vashem', 'jri_poland')")
    url: str | None = Field(default=None, description="URL to the record (may be null for negative-evidence citations)")
    record_id: str | None = Field(default=None, description="Record identifier")
    notes: str | None = Field(default=None, description="Additional notes")
    verified: bool | None = Field(
        default=None,
        description="True if a human has reviewed and confirmed this citation",
    )


EnrichmentSource = Literal["flash", "deep_research"]


# =============================================================================
# Layer 1: Pages (from page.schema.ts)
# =============================================================================


class Block(BaseModel):
    """A physical text region on a newspaper page."""

    id: str = Field(description="Block ID like 'blk-p4-001'")
    bbox: tuple[int, int, int, int] = Field(
        description="[x, y, width, height] in absolute pixels"
    )
    transcription: str = Field(description="Transcribed text content")
    confidence: float | None = Field(default=None, description="OCR confidence 0-1")
    image_crop: str | None = Field(
        default=None, description="Path to cropped image file"
    )
    unit_id: str | None = Field(description="Foreign key to content unit")


class Page(BaseModel):
    """A newspaper page with its blocks."""

    id: str = Field(description="Page ID like 'page-1938-12-16-4'")
    issue_date: str = Field(description="Issue date in ISO format")
    page_number: int = Field(description="Page number (1-4)")
    image_uri: str = Field(description="Path to page image file")
    dimensions: tuple[int, int] = Field(description="[width, height] in pixels")
    blocks: list[Block] = Field(description="All blocks on this page")


class PagesData(BaseModel):
    """Top-level wrapper for pages JSON file."""

    edition_date: str = Field(description="Edition date in ISO format")
    pages: list[Page] = Field(description="All pages in the edition")


# =============================================================================
# Layer 2: Content Units (from content-unit.schema.ts)
# =============================================================================

ContentUnitType = Literal["article", "notice", "ad", "congratulation", "obituary", "other"]


class PageBlockRef(BaseModel):
    """Reference to blocks on a specific page."""

    page_id: str = Field(description="Page ID")
    block_ids: list[str] = Field(description="Block IDs on that page")


class CrossReference(BaseModel):
    """Cross-reference between content units."""

    target_id: str = Field(description="Target content unit ID")
    confidence: float = Field(description="Confidence in the relationship (0-1)")
    relationship: str = Field(description="Type of relationship")
    evidence: str = Field(description="Evidence supporting the relationship")


class ContentUnit(BaseModel):
    """A logical editorial unit (article, notice, ad, etc.)."""

    id: str = Field(description="Content unit ID like 'cu-ball-announcement'")
    type: ContentUnitType = Field(description="Type of content")
    title: str | None = Field(description="Title if present")
    category: str | None = Field(description="Descriptive category")
    full_text: str = Field(description="Complete text content")
    english_translation: str | None = Field(description="English translation")
    block_breaks: list[int] = Field(
        default_factory=list,
        description="Character offsets where blocks join in full_text",
    )
    page_blocks: list[PageBlockRef] = Field(
        description="References to physical blocks"
    )
    person_ids: list[str] = Field(
        default_factory=list, description="IDs of mentioned people"
    )
    location_ids: list[str] = Field(
        default_factory=list, description="IDs of mentioned locations"
    )
    cross_references: list[CrossReference] = Field(
        default_factory=list, description="References to other content units"
    )
    event_id: str | None = Field(description="Parent life event ID if applicable")


class ContentUnitsData(BaseModel):
    """Top-level wrapper for content units JSON file."""

    edition_date: str = Field(description="Edition date in ISO format")
    content_units: list[ContentUnit] = Field(description="All content units")


# =============================================================================
# Layer 3: Life Events (from life-event.schema.ts)
# =============================================================================

LifeEventType = Literal[
    "wedding",
    "birth",
    "death",
    "bar_mitzvah",
    "celebration",
    "community_event",
    "other",
]

ContentUnitRole = Literal[
    "primary_announcement",
    "congratulation",
    "mention",
    "advertisement",
]


class ContentUnitRef(BaseModel):
    """Reference to a content unit with its role in the event."""

    unit_id: str = Field(description="Content unit ID")
    role: ContentUnitRole = Field(description="Role of this unit in the event")


class LifeEvent(BaseModel):
    """A life event grouping related content units."""

    id: str = Field(description="Event ID like 'event-wedding-pomerantz-shor'")
    type: LifeEventType = Field(description="Type of life event")
    name: str = Field(description="Display name for the event")
    principal_ids: list[str] = Field(
        description="Person IDs of the principals (bride/groom, deceased, etc.)"
    )
    date_hebrew: str | None = Field(description="Hebrew calendar date")
    date_gregorian: str | None = Field(description="Gregorian date in ISO format")
    location_id: str | None = Field(description="Location ID where event occurred")
    content_units: list[ContentUnitRef] = Field(
        description="Content units related to this event"
    )
    description: str | None = Field(description="Additional description")


class LifeEventsData(BaseModel):
    """Top-level wrapper for life events JSON file."""

    edition_date: str = Field(description="Edition date in ISO format")
    life_events: list[LifeEvent] = Field(description="All life events")


# =============================================================================
# Enrichment: People (from enrichment.schema.ts)
# =============================================================================

Gender = Literal["male", "female", "unknown"]


class PartisanActivity(BaseModel):
    """Partisan activity details for a person."""

    unit: str = Field(description="Partisan unit name")
    rank: str | None = Field(default=None, description="Rank if known")
    alias: str | None = Field(default=None, description="Nom de guerre")
    activities: str | None = Field(default=None, description="Known activities")


class PersonRelationship(BaseModel):
    """Relationship between two people."""

    person_id: str = Field(description="ID of related person")
    type: str = Field(description="Relationship type (spouse, parent_of, etc.)")
    evidence: str | None = Field(default=None, description="Evidence from text")


class AdditionalDetail(BaseModel):
    """Additional biographical detail."""

    label: str = Field(description="Label for the detail")
    value: str = Field(description="Detail value")


class BiographicalNarrative(BaseModel):
    """Long-form provenanced narrative produced by Flash / Deep Research pipelines."""

    source: EnrichmentSource = Field(description="Producing pipeline")
    markdown: str = Field(description="Markdown-formatted narrative text")


class ProposedRelationship(BaseModel):
    """Unconfirmed relationship hypothesis awaiting human review."""

    type: str = Field(description="Relationship type (e.g., 'sibling_of', 'cousin')")
    person_id_hint: str = Field(
        description="Free-form hint identifying the target person (id guess + context)"
    )
    evidence: str = Field(description="Evidence justifying the proposed link")
    source: EnrichmentSource = Field(description="Producing pipeline")


class EnrichedPerson(BaseModel):
    """A person with all enrichment data."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="Person ID like 'person-rachel-pomerantz'")
    name: str = Field(description="Canonical English name")
    yiddish_name: str | None = Field(default=None, description="Name in Yiddish script")
    aliases: list[str] = Field(default_factory=list, description="Alternative names")
    gender: Gender = Field(description="Gender")
    birth_year: int | None = Field(default=None, description="Birth year")
    birth_date: str | None = Field(default=None, description="Birth date if known")
    death_year: int | None = Field(default=None, description="Death year")
    death_date: str | None = Field(default=None, description="Death date if known")
    birth_location: str | None = Field(default=None, description="Birth location")
    residence_at_publication: str | None = Field(
        default=None, description="Residence in 1938"
    )
    holocaust_fate: HolocaustFate = Field(
        default="unknown", description="Holocaust fate"
    )
    holocaust_fate_notes: str | None = Field(
        default=None, description="Notes about fate"
    )
    headshot_path: str | None = Field(default=None, description="Path to photo")
    occupation: str | None = Field(default=None, description="Occupation")
    partisan_activity: PartisanActivity | None = Field(
        default=None, description="Partisan activity if any"
    )
    ghetto_role: str | None = Field(default=None, description="Role in ghetto")
    unit_ids: list[str] = Field(
        default_factory=list, description="Content unit IDs where mentioned"
    )
    relationships: list[PersonRelationship] = Field(
        default_factory=list, description="Family/social relationships"
    )
    external_references: list[ExternalReference] = Field(
        default_factory=list, description="External database references"
    )
    additional_details: list[AdditionalDetail] | None = Field(
        default=None, description="Additional biographical details"
    )
    biographical_narratives: list[BiographicalNarrative] | None = Field(
        default=None,
        description="Long-form sourced narratives from Flash / Deep Research enrichment",
    )
    proposed_relationships: list[ProposedRelationship] | None = Field(
        default=None,
        description="Unconfirmed relationship hypotheses awaiting human review",
    )


# =============================================================================
# Enrichment: Locations (from enrichment.schema.ts)
# =============================================================================

LocationType = Literal[
    "city",
    "town",
    "village",
    "shtetl",
    "street",
    "address",
    "landmark",
    "country",
    "region",
    "district",
    "ghetto",
    "camp",
    "massacre_site",
    "deportation_point",
    "forest",
]


class LocalizedNames(BaseModel):
    """Multi-language name variants."""

    en: str | None = Field(default=None, description="English")
    yi: str | None = Field(default=None, description="Yiddish")
    pl: str | None = Field(default=None, description="Polish")
    ru: str | None = Field(default=None, description="Russian")
    be: str | None = Field(default=None, description="Belarusian")
    he: str | None = Field(default=None, description="Hebrew")
    de: str | None = Field(default=None, description="German")
    uk: str | None = Field(default=None, description="Ukrainian")


class HistoricalContext(BaseModel):
    """Historical administrative context for a location."""

    period: str = Field(description="Time period (e.g., '1918-1939')")
    label: str | None = Field(default=None, description="Period label")
    parent_id: str | None = Field(default=None, description="Parent location ID")
    admin_name: str | None = Field(default=None, description="Administrative name")
    sovereignty: str | None = Field(default=None, description="Sovereign state")
    notes: str | None = Field(default=None, description="Additional notes")


class HolocaustSite(BaseModel):
    """Holocaust site metadata."""

    site_type: str | None = Field(default=None, description="Type of site")
    date_established: str | None = Field(default=None, description="Date established")
    date_liquidated: str | None = Field(default=None, description="Date liquidated")
    estimated_victims: int | None = Field(
        default=None, description="Estimated victim count"
    )
    key_events: list[str] | None = Field(default=None, description="Key events")
    sources: list[str] | None = Field(default=None, description="Sources")


class EnrichedLocation(BaseModel):
    """A location with all enrichment data."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="Location ID like 'location-pruzhany'")
    name: str = Field(description="Canonical English name")
    yiddish_name: str | None = Field(default=None, description="Yiddish name")
    aliases: list[str] = Field(default_factory=list, description="Alternative names")
    type: LocationType = Field(description="Location type")
    coordinates: tuple[float, float] | None = Field(
        default=None, description="[latitude, longitude]"
    )
    country: str | None = Field(default=None, description="Modern country")
    country_historical: str | None = Field(
        default=None, description="Country in 1938"
    )
    region: str | None = Field(default=None, description="Modern region")
    region_historical: str | None = Field(
        default=None, description="Historical region"
    )
    holocaust_history: str | None = Field(
        default=None, description="Holocaust history summary"
    )
    unit_ids: list[str] = Field(
        default_factory=list, description="Content unit IDs where mentioned"
    )
    external_references: list[ExternalReference] = Field(
        default_factory=list, description="External database references"
    )
    names: LocalizedNames | None = Field(
        default=None, description="Multi-language names"
    )
    parent_id: str | None = Field(
        default=None, description="Parent location ID for hierarchy"
    )
    wikidata_id: str | None = Field(default=None, description="Wikidata Q-number")
    geonames_id: str | None = Field(default=None, description="GeoNames ID")
    historical_contexts: list[HistoricalContext] | None = Field(
        default=None, description="Historical administrative contexts"
    )
    holocaust_site: HolocaustSite | None = Field(
        default=None, description="Holocaust site metadata"
    )


# =============================================================================
# Enrichment: Events and Topics (from enrichment.schema.ts)
# =============================================================================


class EventParticipant(BaseModel):
    """Participant in an event."""

    person_id: str = Field(description="Person ID")
    role: str = Field(description="Role in the event")


# Literal alias so callsites (e.g., utils/convert.py's validation + cast)
# can reference the same single source of truth as the schema field.
EnrichedEventType = Literal[
    "wedding",
    "birth",
    "death",
    "bar_mitzvah",
    "celebration",
    "community_event",
    "holocaust_event",
    "other",
]


class EnrichedEvent(BaseModel):
    """An event with enrichment data."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="Event ID")
    name: str = Field(description="Event name")
    type: EnrichedEventType = Field(description="Event type")
    date: str | None = Field(default=None, description="Date if known")
    date_notes: str | None = Field(default=None, description="Date notes")
    location: str | None = Field(default=None, description="Location reference")
    description: str = Field(description="Event description")
    participants: list[EventParticipant] = Field(
        default_factory=list, description="Event participants"
    )
    unit_ids: list[str] = Field(
        default_factory=list, description="Related content unit IDs"
    )
    external_references: list[ExternalReference] | None = Field(
        default=None, description="External references"
    )


class Topic(BaseModel):
    """A topic grouping content units."""

    id: str = Field(description="Topic ID")
    name: str = Field(description="Topic name")
    description: str | None = Field(default=None, description="Topic description")
    unit_ids: list[str] = Field(description="Content unit IDs in this topic")


# =============================================================================
# Enrichment: Organizations (from edition-bundle.schema.ts)
# =============================================================================


class OrganizationMember(BaseModel):
    """A person's membership in an organization."""

    person_id: str = Field(description="Person ID")
    role: str = Field(description="Role within the organization")


class EnrichedOrganization(BaseModel):
    """An organization (institution, society, congregation) with enrichment data."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="Organization ID like 'org-district-hospital'")
    name: str = Field(description="Canonical English name")
    yiddish_name: str | None = Field(default=None, description="Yiddish name")
    type: str = Field(description="Organization type (e.g., 'healthcare', 'school')")
    description: str = Field(description="Description of the organization")
    unit_ids: list[str] = Field(
        default_factory=list, description="Content unit IDs where mentioned"
    )
    members: list[OrganizationMember] | None = Field(
        default=None, description="Known members and their roles"
    )
    external_references: list[ExternalReference] | None = Field(
        default=None, description="External database references"
    )


# =============================================================================
# Enrichment: Sections (from enrichment.schema.ts)
# =============================================================================


class SectionItem(BaseModel):
    """Leaf node in section hierarchy."""

    id: str = Field(description="Item ID")
    label: str = Field(description="Display label")
    icon: str | None = Field(default=None, description="Icon name")
    event_id: str | None = Field(default=None, description="Related event ID")
    topic_id: str | None = Field(default=None, description="Related topic ID")
    unit_ids: list[str] = Field(description="Content unit IDs")


class SectionCategory(BaseModel):
    """L2 node in section hierarchy."""

    id: str = Field(description="Category ID")
    label: str = Field(description="Display label")
    icon: str | None = Field(default=None, description="Icon name")
    topic_id: str | None = Field(default=None, description="Related topic ID")
    event_ids: list[str] | None = Field(default=None, description="Related event IDs")
    unit_ids: list[str] = Field(description="Content unit IDs at this level")
    primary_unit_ids: list[str] | None = Field(
        default=None, description="Primary unit IDs"
    )
    items: list[SectionItem] | None = Field(default=None, description="Child items")


class Section(BaseModel):
    """L1 node in section hierarchy."""

    id: str = Field(description="Section ID")
    label: str = Field(description="Display label")
    icon: str | None = Field(default=None, description="Icon name")
    color: str | None = Field(default=None, description="Section color")
    defaultOpen: bool | None = Field(default=None, description="Open by default")
    categories: list[SectionCategory] = Field(description="Section categories")


# =============================================================================
# Enrichment Data (Top-Level)
# =============================================================================


class EnrichmentData(BaseModel):
    """Top-level enrichment data JSON file.

    Lossless wrapper: preserves unknown top-level keys (e.g. the self-describing
    ``holocaustFateTypes`` / ``relationshipTypes`` / ``externalSourceTypes`` taxonomy
    blocks the live JSON carries but the contract does not yet model).
    """

    model_config = ConfigDict(extra="allow")

    version: str = Field(default="1.0.0", description="Schema version")
    edition_date: str = Field(description="Edition date in ISO format")
    last_updated: str = Field(description="Last update timestamp")
    people: list[EnrichedPerson] = Field(description="All enriched people")
    locations: list[EnrichedLocation] = Field(description="All enriched locations")
    events: list[EnrichedEvent] = Field(description="All enriched events")
    organizations: list[EnrichedOrganization] = Field(
        default_factory=list, description="All enriched organizations"
    )
    topics: list[Topic] = Field(default_factory=list, description="All topics")
    sections: list[Section] | None = Field(
        default=None, description="Section hierarchy for sidebar"
    )
