/**
 * Unified Edition Bundle Schema
 *
 * A single canonical document that captures ALL content and metadata for one
 * newspaper edition. From this file alone (plus referenced image assets),
 * the full content of the edition is portable and self-contained.
 *
 * Merges the current 5-file model:
 *   - pages.json (Layer 1: physical layout)
 *   - content-units.json (Layer 2: editorial content)
 *   - life-events.json (Layer 3: semantic events)
 *   - enrichment.json (knowledge graph: people, locations, events, orgs, topics, sections)
 *   - editions-catalog.json (edition identity only — catalog stays separate)
 *
 * Key design decisions:
 *   1. Unified event model — merges LifeEvent + EnrichedEvent with a `source` field
 *   2. Organizations are first-class entities with optional membership
 *   3. Reference data (taxonomies) embedded for self-description
 *   4. All image paths relative to the edition directory root
 */

import { z } from 'zod/v4';
import { ContentUnitTypeSchema } from './content-unit.schema';
import { ExternalReferenceSchema } from './shared.schema';

// ── Shared Primitives ─────────────────────────────────────────────

const IsoDateString = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);

export { ExternalReferenceSchema };

export const HolocaustFateSchema = z.enum([
	'unknown',
	'perished',
	'likely_perished',
	'survived',
	'likely_survived',
	'died_before',
	'not_applicable',
]);

// ── Edition Identity ──────────────────────────────────────────────

export const EditionIdentitySchema = z.object({
	date: IsoDateString,
	hebrew_date: z.string(),
	hebrew_month: z.number().int().min(1).max(13),
	hebrew_year: z.number().int(),
	holiday: z.string().nullable(),
	publication: z.object({
		name: z.string(),
		language: z.string(),
		place_of_publication: z.string(),
	}),
});

// ── Layer 1: Physical Layout ──────────────────────────────────────

export const EditionBlockSchema = z.object({
	id: z.string(),
	bbox: z.tuple([z.number(), z.number(), z.number(), z.number()]),
	transcription: z.string(),
	confidence: z.number().optional(),
	image_crop: z.string().optional(),
	content_unit_id: z.string().nullable(),
});

export const PageImageSchema = z.object({
	uri: z.string(),
	width: z.number().int(),
	height: z.number().int(),
	format: z.string(),
});

export const EditionPageSchema = z.object({
	id: z.string(),
	page_number: z.number().int(),
	image: PageImageSchema,
	blocks: z.array(EditionBlockSchema),
});

// ── Layer 2: Content Units ────────────────────────────────────────

export const PageBlockRefSchema = z.object({
	page_id: z.string(),
	block_ids: z.array(z.string()),
});

export const CrossReferenceSchema = z.object({
	target_id: z.string(),
	confidence: z.number(),
	relationship: z.string(),
	evidence: z.string(),
});

export const EditionContentUnitSchema = z.object({
	id: z.string(),
	type: ContentUnitTypeSchema,
	title: z.string().nullable(),
	category: z.string().nullable(),

	// Text
	full_text: z.string(),
	english_translation: z.string().nullable(),
	block_breaks: z.array(z.number()),

	// Physical provenance
	page_blocks: z.array(PageBlockRefSchema),

	// Semantic links (FKs into other collections)
	event_id: z.string().nullable(),
	person_ids: z.array(z.string()),
	location_ids: z.array(z.string()),
	organization_ids: z.array(z.string()),

	// Inter-unit references
	cross_references: z.array(CrossReferenceSchema),
});

// ── Layer 3: Unified Events ───────────────────────────────────────

export const EventTypeSchema = z.enum([
	'wedding',
	'birth',
	'death',
	'bar_mitzvah',
	'celebration',
	'community_event',
	'holocaust_event',
	'other',
]);

export const ContentUnitRoleSchema = z.enum([
	'primary_announcement',
	'congratulation',
	'mention',
	'advertisement',
]);

export const EventContentUnitRefSchema = z.object({
	unit_id: z.string(),
	role: ContentUnitRoleSchema,
});

export const EventParticipantSchema = z.object({
	person_id: z.string(),
	role: z.string(),
});

export const EditionEventSchema = z.object({
	id: z.string(),
	type: EventTypeSchema,
	source: z.enum(['edition', 'historical']),
	name: z.string(),
	description: z.string().nullable(),

	// Dates (dual calendar)
	date_gregorian: z.string().nullable(),
	date_hebrew: z.string().nullable(),
	date_notes: z.string().nullable(),

	// Location
	location_id: z.string().nullable(),

	// Participants
	participants: z.array(EventParticipantSchema),

	// Content unit roles
	content_units: z.array(EventContentUnitRefSchema),

	// External sources
	external_references: z.array(ExternalReferenceSchema),
});

// ── Knowledge Graph: People ───────────────────────────────────────

const PartisanActivitySchema = z.object({
	unit: z.string(),
	alternate_unit: z.string().optional(),
	rank: z.string().optional(),
	alias: z.string().optional(),
	activities: z.string().optional(),
});

const RelationshipSchema = z.object({
	person_id: z.string(),
	type: z.string(),
	evidence: z.string().optional(),
});

const AdditionalDetailSchema = z.object({
	label: z.string(),
	value: z.string(),
});

const EnrichmentSourceSchema = z.enum(['flash', 'deep_research']);

const BiographicalNarrativeSchema = z.object({
	source: EnrichmentSourceSchema,
	markdown: z.string(),
});

const ProposedRelationshipSchema = z.object({
	type: z.string(),
	person_id_hint: z.string(),
	evidence: z.string(),
	source: EnrichmentSourceSchema,
});

export const EditionPersonSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().optional(),
	aliases: z.array(z.string()),
	gender: z.enum(['male', 'female', 'unknown']),

	// Biographical
	birth_year: z.number().optional(),
	birth_date: z.string().optional(),
	death_year: z.number().optional(),
	death_date: z.string().optional(),
	birth_location_id: z.string().optional(),
	residence_at_publication_id: z.string().optional(),
	occupation: z.string().optional(),

	// Holocaust fate
	holocaust_fate: HolocaustFateSchema,
	holocaust_fate_notes: z.string().optional(),

	// Connections
	unit_ids: z.array(z.string()),
	relationships: z.array(RelationshipSchema),

	// Extended
	partisan_activity: PartisanActivitySchema.optional(),
	ghetto_role: z.string().optional(),
	headshot_path: z.string().optional(),
	additional_details: z.array(AdditionalDetailSchema).optional(),
	biographical_narratives: z.array(BiographicalNarrativeSchema).optional(),
	proposed_relationships: z.array(ProposedRelationshipSchema).optional(),
	external_references: z.array(ExternalReferenceSchema),
});

// ── Knowledge Graph: Locations ────────────────────────────────────

export const LocationTypeSchema = z.enum([
	'city',
	'town',
	'village',
	'shtetl',
	'street',
	'address',
	'landmark',
	'country',
	'region',
	'district',
	'ghetto',
	'camp',
	'massacre_site',
	'deportation_point',
	'forest',
]);

const LocalizedNamesSchema = z.object({
	en: z.string().optional(),
	yi: z.string().optional(),
	pl: z.string().optional(),
	ru: z.string().optional(),
	be: z.string().optional(),
	he: z.string().optional(),
	de: z.string().optional(),
	uk: z.string().optional(),
});

const HistoricalContextSchema = z.object({
	period: z.string(),
	label: z.string().optional(),
	parent_id: z.string().optional(),
	admin_name: z.string().optional(),
	sovereignty: z.string().optional(),
	notes: z.string().optional(),
});

const HolocaustSiteSchema = z.object({
	site_type: z.string().optional(),
	date_established: z.string().optional(),
	date_liquidated: z.string().optional(),
	estimated_victims: z.number().optional(),
	key_events: z.array(z.string()).optional(),
	sources: z.array(z.string()).optional(),
});

export const EditionLocationSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().optional(),
	aliases: z.array(z.string()),
	type: LocationTypeSchema,
	coordinates: z.tuple([z.number(), z.number()]).optional(),
	country: z.string().optional(),
	country_historical: z.string().optional(),
	region: z.string().optional(),
	region_historical: z.string().optional(),
	holocaust_history: z.string().optional(),
	unit_ids: z.array(z.string()),
	external_references: z.array(ExternalReferenceSchema),

	// Hierarchy and multi-language
	names: LocalizedNamesSchema.optional(),
	parent_id: z.string().optional(),
	wikidata_id: z.string().optional(),
	geonames_id: z.string().optional(),
	historical_contexts: z.array(HistoricalContextSchema).optional(),
	holocaust_site: HolocaustSiteSchema.optional(),
});

// ── Knowledge Graph: Organizations ────────────────────────────────

const OrganizationMemberSchema = z.object({
	person_id: z.string(),
	role: z.string(),
});

export const EditionOrganizationSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().optional(),
	type: z.string(),
	description: z.string(),
	unit_ids: z.array(z.string()),
	members: z.array(OrganizationMemberSchema).optional(),
	external_references: z.array(ExternalReferenceSchema).optional(),
});

// ── Navigation: Topics ────────────────────────────────────────────

export const EditionTopicSchema = z.object({
	id: z.string(),
	name: z.string(),
	description: z.string().optional(),
	unit_ids: z.array(z.string()),
});

// ── Navigation: Sections ──────────────────────────────────────────

const SectionItemSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	event_id: z.string().optional(),
	topic_id: z.string().optional(),
	unit_ids: z.array(z.string()),
});

const SectionCategorySchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	topic_id: z.string().optional(),
	event_ids: z.array(z.string()).optional(),
	unit_ids: z.array(z.string()),
	primary_unit_ids: z.array(z.string()).optional(),
	items: z.array(SectionItemSchema).optional(),
});

const SectionSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	color: z.string().optional(),
	default_open: z.boolean().optional(),
	categories: z.array(SectionCategorySchema),
});

// ── Reference Data (self-describing taxonomies) ───────────────────

const HolocaustFateTypeSchema = z.object({
	id: z.string(),
	label: z.string(),
	description: z.string(),
});

const RelationshipTypeSchema = z.object({
	id: z.string(),
	label: z.string(),
	inverse: z.string(),
});

const ExternalSourceTypeSchema = z.object({
	id: z.string(),
	name: z.string(),
	base_url: z.string().optional(),
	description: z.string(),
});

const ReferenceDataSchema = z.object({
	content_unit_types: z.array(z.string()),
	event_types: z.array(z.string()),
	location_types: z.array(z.string()),
	holocaust_fate_types: z.array(HolocaustFateTypeSchema),
	relationship_types: z.array(RelationshipTypeSchema),
	external_source_types: z.array(ExternalSourceTypeSchema),
});

// ── Top-Level Edition Bundle ──────────────────────────────────────

export const EditionBundleSchema = z.object({
	$schema: z.string().optional(),
	schema_version: z.string(),
	generated_at: z.string(),
	pipeline_run_id: z.string().optional(),

	edition: EditionIdentitySchema,
	pages: z.array(EditionPageSchema),
	content_units: z.array(EditionContentUnitSchema),
	events: z.array(EditionEventSchema),
	people: z.array(EditionPersonSchema),
	locations: z.array(EditionLocationSchema),
	organizations: z.array(EditionOrganizationSchema),
	topics: z.array(EditionTopicSchema),
	sections: z.array(SectionSchema),
	reference_data: ReferenceDataSchema,
});

// ── Type Exports ──────────────────────────────────────────────────

export type EditionBundle = z.infer<typeof EditionBundleSchema>;
export type EditionIdentity = z.infer<typeof EditionIdentitySchema>;
export type EditionPage = z.infer<typeof EditionPageSchema>;
export type EditionBlock = z.infer<typeof EditionBlockSchema>;
export type PageImage = z.infer<typeof PageImageSchema>;
export type EditionContentUnit = z.infer<typeof EditionContentUnitSchema>;
export type EditionEvent = z.infer<typeof EditionEventSchema>;
export type EventParticipant = z.infer<typeof EventParticipantSchema>;
export type EventContentUnitRef = z.infer<typeof EventContentUnitRefSchema>;
export type EditionPerson = z.infer<typeof EditionPersonSchema>;
export type EditionLocation = z.infer<typeof EditionLocationSchema>;
export type EditionOrganization = z.infer<typeof EditionOrganizationSchema>;
export type EditionTopic = z.infer<typeof EditionTopicSchema>;
export type ReferenceData = z.infer<typeof ReferenceDataSchema>;
