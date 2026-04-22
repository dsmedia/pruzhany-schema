"""LLM output schemas for ADK pipeline.

These schemas use Gemini's native bounding box format ([ymin, xmin, ymax, xmax]
normalized 0-1000) and rich Field descriptions to guide model output.

The LLM outputs are later converted to project schemas via conversion utilities.
"""

from typing import Literal

from pydantic import BaseModel, Field


# =============================================================================
# Region Types and Enums
# =============================================================================

RegionType = Literal[
    "headline",
    "article_body",
    "advertisement",
    "congratulation",
    "notice",
    "masthead",
    "other",
]

PrimaryLanguage = Literal["yiddish", "hebrew", "polish", "mixed"]

ContentUnitType = Literal["article", "notice", "ad", "congratulation", "obituary", "other"]

LifeEventType = Literal[
    "wedding",
    "birth",
    "death",
    "bar_mitzvah",
    "celebration",
    "community_event",
    "other",
]

Gender = Literal["male", "female", "unknown"]

LocationType = Literal[
    "city",
    "town",
    "village",
    "shtetl",
    "street",
    "country",
    "region",
    "district",
]


# =============================================================================
# Per-Crop Transcription (Stage 1)
# =============================================================================


class LlmTranscription(BaseModel):
    """Transcription result for a single cropped bbox region.

    Used in per-crop Stage 1: Gemini receives one crop image and returns
    the transcription. Bbox coordinates come from bboxes.json, not from
    the LLM output.
    """

    transcription: str = Field(
        description=(
            "Exact text in original script(s). "
            "Yiddish/Hebrew: Use Hebrew script. Polish: Use Latin script. "
            "Preserve abbreviations: ה׳ (Mr.), ד״ר (Dr.), ר׳ (Rabbi). "
            "Common Yiddish ligatures: װ, ױ, ײ. "
            "Use [?] ONLY after zooming in and verifying text is truly illegible."
        )
    )
    confidence: Literal["high", "medium", "low"] = Field(
        description=(
            "high: Text clearly readable. "
            "medium: Some uncertainty in characters. "
            "low: Significant portions unclear even after zooming."
        )
    )
    primary_language: PrimaryLanguage = Field(
        description=(
            "yiddish: Standard content in Hebrew script. "
            "hebrew: Religious quotes, blessings. "
            "polish: Latin script content. "
            "mixed: Multiple languages in same region."
        )
    )
    region_type: RegionType = Field(
        description=(
            "headline, article_body, advertisement, congratulation, "
            "notice, masthead, or other."
        )
    )


# =============================================================================
# Layer 1: Page Layout Detection
# =============================================================================


class LlmBlock(BaseModel):
    """A detected text region on the newspaper page.

    The model outputs bounding boxes in Gemini's native format for layout analysis.
    """

    region_id: str = Field(
        description=(
            "Unique ID like 'blk-001'. Number in Yiddish reading order: "
            "right-to-left columns, top-to-bottom within columns."
        )
    )
    box_2d: list[int] = Field(
        description=(
            "Bounding box as [ymin, xmin, ymax, xmax] normalized 0-1000. "
            "Must have exactly 4 integers. "
            "Tightly bound the text region without excess whitespace."
        )
    )
    region_type: RegionType = Field(
        description=(
            "headline: Large bold text, 1-2 lines. "
            "article_body: Multi-line body text. "
            "advertisement: Commercial content with business names. "
            "congratulation: Mazel tov notices for life events. "
            "notice: Short announcements. "
            "masthead: Newspaper title, date, issue number."
        )
    )
    primary_language: PrimaryLanguage = Field(
        description=(
            "yiddish: Standard content in Hebrew script. "
            "hebrew: Religious quotes, blessings (lashon kodesh). "
            "polish: Official notices, some ads in Latin script. "
            "mixed: Multiple languages in same block."
        )
    )
    transcription: str = Field(
        description=(
            "Exact text in original script(s). "
            "Yiddish/Hebrew: Use Hebrew script (אבגדהוזחטיכלמנסעפצקרשת). "
            "Polish: Use Latin script. "
            "Preserve abbreviations: ה׳ (Mr.), ד״ר (Dr.), ר׳ (Rabbi). "
            "Common Yiddish ligatures: װ (vov-vov), ױ (vov-yud), ײ (yud-yud). "
            "Use [?] ONLY after zooming in and verifying text is truly illegible."
        )
    )
    confidence: Literal["high", "medium", "low"] = Field(
        description=(
            "high: Text clearly readable, confident in transcription. "
            "medium: Some uncertainty in characters. "
            "low: Significant portions unclear even after zooming."
        )
    )


class LlmPageLayout(BaseModel):
    """Layout analysis result for a single newspaper page."""

    page_number: int = Field(ge=1, le=4, description="Page number (1-4 for quadrant images)")
    blocks: list[LlmBlock] = Field(
        description="All detected text regions in Yiddish reading order"
    )


# =============================================================================
# Cross-References
# =============================================================================


class LlmCrossReference(BaseModel):
    """A cross-reference from this content unit to another."""

    target_id: str = Field(description="ID of the related content unit")
    confidence: float = Field(description="Confidence 0-1 in this relationship")
    relationship: str = Field(
        description=(
            "Type: 'references' (mentions same person/event), "
            "'same_event' (about the same life event), "
            "'continuation' (article continues from another block group)"
        )
    )
    evidence: str = Field(description="Brief explanation of why these units are related")


# =============================================================================
# Layer 2: Content Units (Logical Editorial Objects)
# =============================================================================


class LlmContentUnit(BaseModel):
    """A logical editorial unit from a 1938 Yiddish newspaper page.

    Group adjacent physical text blocks into one coherent editorial object.
    A headline block + its body text blocks = one content unit.
    Each block should belong to exactly one content unit.
    """

    id: str = Field(
        description=(
            "Semantic ID based on content. Format: 'cu-' + lowercase-hyphenated topic. "
            "Examples: 'cu-pomerantz-shor-wedding-announcement', "
            "'cu-weinstein-bakery-ad', 'cu-community-meeting-notice'. "
            "Must be unique across the edition."
        )
    )
    type: ContentUnitType = Field(
        description=(
            "article: News story, feature, or editorial piece. "
            "notice: Short announcement or official notice. "
            "ad: Commercial advertisement with a business name. "
            "congratulation: Mazel tov message for a specific life event (wedding, birth, bar mitzvah). "
            "obituary: Death notice or memorial tribute. "
            "other: Masthead, filler, or content that doesn't fit above."
        )
    )
    title: str | None = Field(
        default=None,
        description=(
            "Headline or title in English translation, if the unit has one. "
            "Translate from Yiddish. None for untitled units like small congratulations."
        ),
    )
    category: str = Field(
        description=(
            "Specific descriptive label that distinguishes this unit from others. "
            "ALWAYS include principal people's names. "
            "Good: 'Rachel Pomerantz & Chaim Shor Wedding Congratulation', "
            "'Birth Announcement: Baby Tsvia Goldberg', "
            "'Weinstein Bakery Grand Opening Ad'. "
            "Bad: 'Wedding', 'Birth', 'Advertisement' (too generic)."
        )
    )
    block_ids: list[str] = Field(
        description=(
            "Block IDs (e.g. 'blk-8014', 'blk-8015') from the input that comprise "
            "this unit. Use the exact block IDs from the transcribed blocks provided. "
            "A headline block and its body blocks should be grouped together."
        )
    )
    full_text: str = Field(
        description=(
            "Complete text in original Yiddish (Hebrew script), concatenated from "
            "all blocks in reading order. Preserve the original text exactly as "
            "transcribed — do not correct or normalize."
        )
    )
    english_translation: str | None = Field(
        default=None,
        description=(
            "Full English translation of the content — translate EVERY sentence "
            "completely. NEVER truncate, summarize, abbreviate, or use '...' ellipses. "
            "Long articles must be translated in full, not condensed. "
            "Translate names phonetically (e.g., רחל → Rachel). "
            "None only if the text is truly untranslatable (e.g., severely damaged)."
        ),
    )
    mentioned_people: list[str] = Field(
        description=(
            "All people mentioned, in English transliteration. "
            "Include: senders, recipients, honorees, family members, signatories. "
            "Use consistent name forms (e.g., 'Rachel Pomerantz' not 'R. Pomerantz'). "
            "These names will be used to create person entities in the next stage."
        )
    )
    mentioned_locations: list[str] = Field(
        description=(
            "All locations mentioned, using modern English names. "
            "E.g., 'Pruzhany', 'Buenos Aires', 'Palestine'. "
            "Include sender locations from signatures like '(הי)' = Pruzhany, "
            "'(ארגענטינע)' = Argentina. These will become location entities."
        )
    )
    life_event_type: LifeEventType | None = Field(
        default=None,
        description=(
            "If this unit is about a specific life event, which type. "
            "wedding: Marriage announcement or congratulation. "
            "birth: Birth announcement. death: Obituary. "
            "bar_mitzvah: Coming of age. None if not about a life event."
        ),
    )
    life_event_hint: str | None = Field(
        default=None,
        description=(
            "Grouping key so multiple units about the SAME event can be linked. "
            "Use a consistent phrase across all related units. "
            "E.g., if 15 congratulations are for the Pomerantz-Shor wedding, "
            "ALL should use: 'Pomerantz-Shor wedding'. "
            "The primary announcement and all congratulations for the same event "
            "MUST share the same hint string."
        ),
    )
    cross_references: list[LlmCrossReference] = Field(
        default_factory=list,
        description="Links to related content units in this edition",
    )


# =============================================================================
# Enrichment: People
# =============================================================================


class LlmPersonRelationship(BaseModel):
    """A resolved family/social relationship between two people."""

    person_id: str = Field(
        description=(
            "ID of the related person (e.g., 'person-david-pomerantz'). "
            "Must match an ID from the people array."
        )
    )
    type: str = Field(
        description=(
            "Relationship type: 'spouse', 'parent_of', 'child_of', 'sibling', "
            "'grandchild_of', 'in_law', 'cousin', 'uncle_aunt', 'nephew_niece', "
            "'business_partner', 'community_member', 'other'"
        )
    )
    evidence: str = Field(
        description=(
            "Quote from the text supporting this relationship. "
            "Use the Yiddish text or English translation."
        )
    )


class LlmPerson(BaseModel):
    """A unique person identified across all content units in this edition.

    Deduplicate: the same person appearing in multiple units (e.g., as bride in
    announcement AND in 15 congratulations) should be ONE entry with all unit_ids.
    Different spellings of the same name = one person with aliases.
    """

    id: str = Field(
        description=(
            "Format: 'person-' + lowercase-hyphenated canonical English name. "
            "E.g., 'person-rachel-pomerantz', 'person-chaim-shor'. "
            "Must be unique — one ID per real person."
        )
    )
    name: str = Field(
        description=(
            "Canonical full name in English transliteration. "
            "E.g., 'Rachel Pomerantz', 'Chaim Shor'. "
            "Use the most complete form found across all mentions."
        )
    )
    yiddish_name: str | None = Field(
        default=None,
        description=(
            "Name in original Yiddish/Hebrew script as it appears in the newspaper. "
            "E.g., 'רחל פאמעראנץ'. Include diacritics if present."
        ),
    )
    aliases: list[str] = Field(
        default_factory=list,
        description=(
            "Alternative spellings, diminutives, or name forms found across articles. "
            "E.g., ['Rochel Pomerantz', 'R. Pomerantz']. "
            "Helps downstream deduplication."
        ),
    )
    gender: Gender = Field(
        description=(
            "Infer from: names (רחל=female, חיים=male), "
            "roles (כלה/bride=female, חתן/groom=male), "
            "pronouns, occupations. Use 'unknown' only if truly ambiguous."
        )
    )
    birth_year: int | None = Field(
        default=None,
        description=(
            "Birth year if mentioned or calculable from age. "
            "The edition date is 1938 — if someone is described as '20 years old', "
            "birth_year = 1918."
        ),
    )
    death_year: int | None = Field(
        default=None,
        description="Death year if mentioned. Relevant for obituaries and memorials.",
    )
    birth_location: str | None = Field(
        default=None,
        description=(
            "Location ID (e.g., 'location-pruzhany') for birthplace if mentioned. "
            "Must match an ID from the locations array."
        ),
    )
    residence_at_publication: str | None = Field(
        default=None,
        description=(
            "CRITICAL — determines likely Holocaust fate. "
            "Location ID for where this person lived in 1938. "
            "Clues: (הי) or (פה) = Pruzhany; (א״י) = Palestine; "
            "sender signatures often include location. "
            "Argentina/Palestine/USA residents likely survived. "
            "Pruzhany/Poland residents were in the danger zone. "
            "Must match an ID from the locations array."
        ),
    )
    occupation: str | None = Field(
        default=None,
        description=(
            "Profession, trade, or role if mentioned. "
            "E.g., 'baker', 'rabbi', 'teacher', 'merchant'."
        ),
    )
    relationship_hints: list[LlmPersonRelationship] = Field(
        default_factory=list,
        description=(
            "Family and social relationships to resolve in post-processing. "
            "E.g., 'daughter of David Pomerantz', 'married to Chaim Shor'. "
            "Include the evidence (quote) that supports each relationship."
        ),
    )
    unit_ids: list[str] = Field(
        description=(
            "All content unit IDs where this person is mentioned. "
            "Must use exact IDs from the content units (e.g., 'cu-pomerantz-shor-wedding-announcement'). "
            "Include ALL units — announcements, congratulations, ads that mention them."
        )
    )


# =============================================================================
# Enrichment: Locations
# =============================================================================


class LlmLocation(BaseModel):
    """A unique location identified across all content units in this edition.

    Deduplicate: the same place mentioned in multiple units = ONE entry with all
    unit_ids. Different Yiddish spellings of the same place = one location with aliases.
    Include both explicitly named places and places inferred from abbreviations
    like (הי) = Pruzhany, (א״י) = Palestine.
    """

    id: str = Field(
        description=(
            "Format: 'location-' + lowercase-hyphenated canonical name. "
            "E.g., 'location-pruzhany', 'location-buenos-aires', 'location-palestine'. "
            "Must be unique — one ID per real place."
        )
    )
    name: str = Field(
        description=(
            "Canonical name in modern English. "
            "E.g., 'Pruzhany', 'Buenos Aires', 'Warsaw', 'Palestine'. "
            "Use the most commonly recognized English form."
        )
    )
    yiddish_name: str | None = Field(
        default=None,
        description=(
            "Name in Yiddish script as found in the newspaper. "
            "E.g., 'פרוזשאן' (Pruzhany), 'ווארשע' (Warsaw), 'ארגענטינע' (Argentina)."
        ),
    )
    polish_name: str | None = Field(
        default=None,
        description=(
            "Polish name if the location is in Poland/former Poland. "
            "E.g., 'Pru\u017cana' for Pruzhany, 'Warszawa' for Warsaw."
        ),
    )
    aliases: list[str] = Field(
        default_factory=list,
        description=(
            "Alternative spellings found across articles. "
            "Include Yiddish transliteration variants."
        ),
    )
    type: LocationType = Field(
        description=(
            "city: Major urban center (Warsaw, Buenos Aires). "
            "town: Smaller urban area (Pruzhany, Brest). "
            "village: Rural settlement. "
            "shtetl: Jewish market town in Eastern Europe — use for small "
            "Jewish-majority towns in the Pale of Settlement. "
            "street: Specific street address. "
            "country: Sovereign state (Poland, Argentina). "
            "region/district: Administrative subdivisions."
        )
    )
    parent_location_hint: str | None = Field(
        default=None,
        description=(
            "Parent in the location hierarchy, by name (not ID). "
            "E.g., 'Poland' for Pruzhany, 'Argentina' for Buenos Aires. "
            "Used to build the location tree in post-processing."
        ),
    )
    country_1938: str | None = Field(
        default=None,
        description=(
            "Country as of December 1938. "
            "E.g., 'Poland' for Pruzhany (before Soviet/Nazi occupation), "
            "'United Kingdom' for Palestine (British Mandate)."
        ),
    )
    country_modern: str | None = Field(
        default=None,
        description=(
            "Modern-day country for geographic mapping. "
            "E.g., 'Belarus' for Pruzhany, 'Israel' for locations in Palestine."
        ),
    )
    unit_ids: list[str] = Field(
        description=(
            "All content unit IDs where this location is mentioned. "
            "Must use exact IDs from the content units. "
            "Include units where the location appears in signatures, "
            "datelines, or abbreviations like (הי)."
        )
    )


# =============================================================================
# Layer 3: Life Events
# =============================================================================


class LlmEventParticipant(BaseModel):
    """A participant in a life event with their role."""

    person_id: str = Field(description="Person ID from the people array")
    role: str = Field(
        description=(
            "Role in the event. Wedding: 'bride', 'groom', 'father_of_bride', "
            "'mother_of_groom', etc. Birth: 'newborn', 'mother', 'father'. "
            "Death: 'deceased', 'mourner'. General: 'principal', 'speaker'."
        )
    )


class LlmContentUnitRef(BaseModel):
    """A reference linking a content unit to its role in a life event."""

    unit_id: str = Field(
        description=(
            "Exact content unit ID from the input (e.g., 'cu-pomerantz-shor-wedding-announcement'). "
            "Must match an ID from the content units provided."
        )
    )
    role: Literal["primary_announcement", "congratulation", "mention", "advertisement"] = Field(
        description=(
            "primary_announcement: The main news item announcing the event (usually 1 per event). "
            "congratulation: A mazel tov / well-wishes message about the event. "
            "mention: Passing reference to the event in an unrelated article. "
            "advertisement: Commercial tie-in (e.g., venue ad, caterer ad near wedding content)."
        )
    )


class LlmLifeEvent(BaseModel):
    """A real-world lifecycle event that groups related content units.

    Yiddish newspapers devote many columns to life events: a wedding might have
    1 primary announcement + 10-20 individual congratulation messages + related ads.
    Group ALL of these under one event. Use the life_event_hint from content units
    to identify which units belong together.
    """

    id: str = Field(
        description=(
            "Format: 'event-' + event type + principal names, lowercase-hyphenated. "
            "E.g., 'event-wedding-pomerantz-shor', 'event-birth-goldberg-tsvia', "
            "'event-death-leibovich-moshe'. Must be unique."
        )
    )
    type: LifeEventType = Field(
        description=(
            "wedding: Marriage ceremony — the most common type in this newspaper. "
            "birth: Birth announcement or brit milah. "
            "death: Obituary, memorial, or yahrzeit notice. "
            "bar_mitzvah: Coming of age ceremony. "
            "celebration: General simcha (e.g., anniversary, homecoming). "
            "community_event: Town-wide event (meeting, fundraiser, cultural event). "
            "other: Doesn't fit above categories."
        )
    )
    name: str = Field(
        description=(
            "Human-readable display name with principal people's names. "
            "Wedding: 'Rachel Pomerantz & Chaim Shor Wedding'. "
            "Birth: 'Birth of Tsvia Goldberg'. "
            "Death: 'Memorial for Moshe Leibovich'. "
            "Always include the actual names, not generic descriptions."
        )
    )
    participants: list[LlmEventParticipant] = Field(
        description=(
            "ALL participants with typed roles. "
            "Wedding: bride, groom, father_of_bride, mother_of_groom, etc. "
            "Birth: newborn, mother, father. Death: deceased, mourner. "
            "Bar mitzvah: the boy (principal). "
            "NEVER include well-wishers or congratulation senders. "
            "Person IDs must match IDs from the people array."
        )
    )
    date_hebrew: str | None = Field(
        default=None,
        description=(
            "Hebrew calendar date if mentioned in any related unit. "
            "Use Hebrew script: e.g., 'כ״ה כסלו תרצ״ט'. "
            "Often found in the primary announcement."
        ),
    )
    date_gregorian: str | None = Field(
        default=None,
        description=(
            "Gregorian date in ISO format (YYYY-MM-DD). "
            "E.g., '1938-12-18'. Calculate from Hebrew date if possible "
            "(the edition date is provided as context). None if unknown."
        ),
    )
    location_id: str | None = Field(
        default=None,
        description=(
            "Location ID where the event took place. "
            "Must match an ID from the locations provided in the input. "
            "Often Pruzhany for local events."
        ),
    )
    content_units: list[LlmContentUnitRef] = Field(
        description=(
            "ALL content units related to this event — be exhaustive. "
            "A wedding typically includes 1 primary_announcement + many congratulations. "
            "Search ALL content units with matching life_event_hint. "
            "Missing a congratulation means losing a connection to the senders."
        )
    )
    description: str | None = Field(
        default=None,
        description=(
            "Brief additional context about the event in English. "
            "E.g., notable details, family connections, or significance to the community."
        ),
    )


# =============================================================================
# Per-CU Translation (vision-aware, used by `translate` command)
# =============================================================================


class TranslationResult(BaseModel):
    """Result of translating a single content unit with Gemini vision.

    The model sees the page image + bbox crop + OCR text, and produces
    a complete English translation with confidence and optional OCR corrections.
    """

    english_translation: str = Field(
        description=(
            "Complete English translation of the Yiddish text. "
            "Translate EVERY sentence fully. NEVER truncate, summarize, "
            "abbreviate, or use '...' ellipses. Long articles must be "
            "translated in their entirety. "
            "Translate names phonetically (e.g., רחל → Rachel)."
        )
    )
    confidence: float = Field(
        description=(
            "Confidence 0.0–1.0 that the translation is complete and accurate. "
            "Lower if text is damaged, partially illegible, or ambiguous."
        )
    )
    ocr_corrections: list[str] | None = Field(
        default=None,
        description=(
            "OCR errors noticed when comparing the provided transcription text "
            "against what is visible in the image. Each entry describes one "
            "correction, e.g., 'Line 3: פאמעראנץ should be פּאָמעראַנץ'. "
            "None if no corrections needed."
        ),
    )


# =============================================================================
# Per-Stage Response Wrappers (for structured output)
# =============================================================================


class LlmStage2Response(BaseModel):
    """All logical editorial units extracted from a 1938 Yiddish newspaper edition.

    Group the provided transcribed text blocks into coherent content units:
    articles, notices, advertisements, congratulations, and obituaries.
    Every block should belong to exactly one content unit.
    """

    content_units: list[LlmContentUnit] = Field(
        description=(
            "Complete list of content units for the edition. "
            "Every input block must appear in exactly one unit's block_ids. "
            "Order by page number, then by position on page."
        )
    )


class LlmStage3Response(BaseModel):
    """All people and locations identified across every content unit in the edition.

    Extract entities from the provided content units. Deduplicate: if 'Rachel
    Pomerantz' appears in 15 congratulations and 1 announcement, output ONE
    person entry with all 16 unit_ids.
    """

    people: list[LlmPerson] = Field(
        description=(
            "Every unique person mentioned in any content unit, deduplicated. "
            "One entry per real person — merge different spellings. "
            "Include all people: principals, senders, family members, honorees."
        )
    )
    locations: list[LlmLocation] = Field(
        description=(
            "Every unique location mentioned in any content unit, deduplicated. "
            "One entry per real place — merge Yiddish/Polish/English variants. "
            "Include locations from abbreviations: (הי) = Pruzhany, (א״י) = Palestine."
        )
    )


class LlmStage4Response(BaseModel):
    """All life events detected in the edition, grouping related content units.

    Identify real-world lifecycle events (weddings, births, deaths, etc.) and
    link every relevant content unit to its event. A single wedding may have
    1 announcement + 10-20 congratulations + related ads — group them all.
    """

    life_events: list[LlmLifeEvent] = Field(
        description=(
            "All lifecycle events found in the edition. "
            "Use life_event_hint from content units to identify groupings. "
            "Be exhaustive: every content unit with a life_event_type should appear "
            "in at least one event's content_units list."
        )
    )


# =============================================================================
# Complete Edition Output
# =============================================================================


class LlmEditionOutput(BaseModel):
    """Complete LLM output for an entire newspaper edition.

    This is the final structured output from the ADK pipeline,
    ready for conversion to project schemas.
    """

    edition_date: str = Field(
        description="Edition date in ISO format (e.g., '1938-12-16')"
    )
    pages: list[LlmPageLayout] = Field(
        description="Layout analysis for each page"
    )
    content_units: list[LlmContentUnit] = Field(
        description="All logical content units extracted"
    )
    people: list[LlmPerson] = Field(
        description="All identified people (deduplicated)"
    )
    locations: list[LlmLocation] = Field(
        description="All identified locations (deduplicated)"
    )
    life_events: list[LlmLifeEvent] = Field(
        description="All detected life events"
    )
