import { z } from 'zod/v4';
import { HolocaustFateSchema, ExternalReferenceSchema } from './shared.schema';

// Partisan activity (nested in Person)
const PartisanActivitySchema = z.object({
	unit: z.string(),
	rank: z.string().nullish(),
	alias: z.string().nullish(),
	activities: z.string().nullish(),
});

// Relationship (nested in Person)
const RelationshipSchema = z.object({
	person_id: z.string(),
	type: z.string(),
	evidence: z.string().nullish(),
});

// Topic
export const TopicSchema = z.object({
	id: z.string(),
	name: z.string(),
	description: z.string().nullish(),
	unit_ids: z.array(z.string()),
});
export type Topic = z.infer<typeof TopicSchema>;

// Additional detail (flexible label/value for biographical info)
export const AdditionalDetailSchema = z.object({
	label: z.string(),
	value: z.string(),
});
export type AdditionalDetail = z.infer<typeof AdditionalDetailSchema>;

// Provenanced source for narratives and proposed relationships
const EnrichmentSourceSchema = z.enum(['flash', 'deep_research']);

// Long-form biographical narrative produced by Flash / Deep Research pipelines
export const BiographicalNarrativeSchema = z.object({
	source: EnrichmentSourceSchema,
	markdown: z.string(),
});
export type BiographicalNarrative = z.infer<typeof BiographicalNarrativeSchema>;

// Unconfirmed relationship hypothesis awaiting human review
export const ProposedRelationshipSchema = z.object({
	type: z.string(),
	person_id_hint: z.string(),
	evidence: z.string(),
	source: EnrichmentSourceSchema,
});
export type ProposedRelationship = z.infer<typeof ProposedRelationshipSchema>;

// Enriched Person
export const EnrichedPersonSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().nullish(),
	aliases: z.array(z.string()),
	gender: z.enum(['male', 'female', 'unknown']),
	birth_year: z.number().nullish(),
	birth_date: z.string().nullish(),
	death_year: z.number().nullish(),
	death_date: z.string().nullish(),
	birth_location: z.string().nullish(),
	residence_at_publication: z.string().nullish(),
	holocaust_fate: HolocaustFateSchema,
	holocaust_fate_notes: z.string().nullish(),
	headshot_path: z.string().nullish(),
	occupation: z.string().nullish(),
	partisan_activity: PartisanActivitySchema.nullish(),
	ghetto_role: z.string().nullish(),
	unit_ids: z.array(z.string()),
	relationships: z.array(RelationshipSchema),
	external_references: z.array(ExternalReferenceSchema),
	additional_details: z.array(AdditionalDetailSchema).nullish(),
	biographical_narratives: z.array(BiographicalNarrativeSchema).nullish(),
	proposed_relationships: z.array(ProposedRelationshipSchema).nullish(),
});
export type EnrichedPerson = z.infer<typeof EnrichedPersonSchema>;

// Location type enum
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
export type LocationType = z.infer<typeof LocationTypeSchema>;

// Localized names for multi-language support
export const LocalizedNamesSchema = z.object({
	en: z.string().nullish(),
	yi: z.string().nullish(),
	pl: z.string().nullish(),
	ru: z.string().nullish(),
	be: z.string().nullish(),
	he: z.string().nullish(),
	de: z.string().nullish(),
	uk: z.string().nullish(),
});
export type LocalizedNames = z.infer<typeof LocalizedNamesSchema>;

// Historical administrative context (for time-varying containment)
export const HistoricalContextSchema = z.object({
	period: z.string(),
	label: z.string().nullish(),
	parent_id: z.string().nullish(),
	admin_name: z.string().nullish(),
	sovereignty: z.string().nullish(),
	notes: z.string().nullish(),
});
export type HistoricalContext = z.infer<typeof HistoricalContextSchema>;

// Holocaust site metadata
export const HolocaustSiteSchema = z.object({
	site_type: z.string().nullish(),
	date_established: z.string().nullish(),
	date_liquidated: z.string().nullish(),
	estimated_victims: z.number().nullish(),
	key_events: z.array(z.string()).nullish(),
	sources: z.array(z.string()).nullish(),
});
export type HolocaustSite = z.infer<typeof HolocaustSiteSchema>;

// Enriched Location
export const EnrichedLocationSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().nullish(),
	aliases: z.array(z.string()),
	type: LocationTypeSchema,
	coordinates: z.tuple([z.number(), z.number()]).nullish(),
	country: z.string().nullish(),
	country_historical: z.string().nullish(),
	region: z.string().nullish(),
	region_historical: z.string().nullish(),
	holocaust_history: z.string().nullish(),
	unit_ids: z.array(z.string()),
	external_references: z.array(ExternalReferenceSchema),
	// New hierarchy and enrichment fields
	names: LocalizedNamesSchema.nullish(),
	parent_id: z.string().nullish(),
	wikidata_id: z.string().nullish(),
	geonames_id: z.string().nullish(),
	historical_contexts: z.array(HistoricalContextSchema).nullish(),
	holocaust_site: HolocaustSiteSchema.nullish(),
});
export type EnrichedLocation = z.infer<typeof EnrichedLocationSchema>;

// Event type enum
const EventTypeSchema = z.enum([
	'wedding',
	'birth',
	'death',
	'bar_mitzvah',
	'celebration',
	'community_event',
	'holocaust_event',
	'other',
]);

// Event participant
const ParticipantSchema = z.object({
	person_id: z.string(),
	role: z.string(),
});

// Enriched Event
export const EnrichedEventSchema = z.object({
	id: z.string(),
	name: z.string(),
	type: EventTypeSchema,
	date: z.string().nullish(),
	date_hebrew: z.string().nullish(),
	date_notes: z.string().nullish(),
	location: z.string().nullish(),
	description: z.string(),
	participants: z.array(ParticipantSchema),
	unit_ids: z.array(z.string()),
	// Editorial role of each related unit (keyed by unit id, e.g.
	// "primary_announcement" | "congratulation" | "mention" | "advertisement")
	unit_roles: z.record(z.string(), z.string()).nullish(),
	external_references: z.array(ExternalReferenceSchema).nullish(),
});
export type EnrichedEvent = z.infer<typeof EnrichedEventSchema>;

// Organization member (nested in Organization)
const OrganizationMemberSchema = z.object({
	person_id: z.string(),
	role: z.string(),
});

// Enriched Organization (institution, society, congregation)
export const EnrichedOrganizationSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().nullish(),
	type: z.string(),
	description: z.string(),
	unit_ids: z.array(z.string()),
	members: z.array(OrganizationMemberSchema).nullish(),
	external_references: z.array(ExternalReferenceSchema).nullish(),
});
export type EnrichedOrganization = z.infer<typeof EnrichedOrganizationSchema>;

// Section hierarchy schemas (for sidebar grouping)

// Leaf node — owns articles directly
export const SectionItemSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().nullish(),
	event_id: z.string().nullish(),
	topic_id: z.string().nullish(),
	unit_ids: z.array(z.string()),
});
export type SectionItem = z.infer<typeof SectionItemSchema>;

// L2 node — either a leaf (has unit_ids, no items) or a branch (has items)
export const SectionCategorySchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().nullish(),
	topic_id: z.string().nullish(),
	event_ids: z.array(z.string()).nullish(),
	unit_ids: z.array(z.string()),
	primary_unit_ids: z.array(z.string()).nullish(),
	items: z.array(SectionItemSchema).nullish(),
});
export type SectionCategory = z.infer<typeof SectionCategorySchema>;

// L1 node — never owns articles directly
export const SectionSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().nullish(),
	color: z.string().nullish(),
	defaultOpen: z.boolean().nullish(),
	categories: z.array(SectionCategorySchema),
});
export type Section = z.infer<typeof SectionSchema>;

// Top-level enrichment data
export const EnrichmentDataSchema = z
	.object({
		version: z.string(),
		edition_date: z.string(),
		last_updated: z.string(),
		people: z.array(EnrichedPersonSchema),
		locations: z.array(EnrichedLocationSchema),
		events: z.array(EnrichedEventSchema),
		organizations: z.array(EnrichedOrganizationSchema).nullish(),
		topics: z.array(TopicSchema),
		sections: z.array(SectionSchema).nullish(),
	})
	.passthrough();
export type EnrichmentData = z.infer<typeof EnrichmentDataSchema>;

// Article enrichment context (derived, not from JSON)
export const ArticleEnrichmentSchema = z.object({
	unit_id: z.string(),
	people: z.array(EnrichedPersonSchema),
	locations: z.array(EnrichedLocationSchema),
	events: z.array(EnrichedEventSchema),
	aggregate_fate: z.enum(['perished', 'survived', 'mixed', 'unknown']),
	fate_stats: z.object({
		perished: z.number(),
		survived: z.number(),
		unknown: z.number(),
	}),
});
export type ArticleEnrichment = z.infer<typeof ArticleEnrichmentSchema>;
