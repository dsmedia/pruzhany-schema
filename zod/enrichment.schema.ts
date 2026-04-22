import { z } from 'zod/v4';
import { HolocaustFateSchema, ExternalReferenceSchema } from './shared.schema';

// Partisan activity (nested in Person)
const PartisanActivitySchema = z.object({
	unit: z.string(),
	rank: z.string().optional(),
	alias: z.string().optional(),
	activities: z.string().optional(),
});

// Relationship (nested in Person)
const RelationshipSchema = z.object({
	person_id: z.string(),
	type: z.string(),
	evidence: z.string().optional(),
});

// Topic
export const TopicSchema = z.object({
	id: z.string(),
	name: z.string(),
	description: z.string().optional(),
	unit_ids: z.array(z.string()),
});
export type Topic = z.infer<typeof TopicSchema>;

// Additional detail (flexible label/value for biographical info)
export const AdditionalDetailSchema = z.object({
	label: z.string(),
	value: z.string(),
});
export type AdditionalDetail = z.infer<typeof AdditionalDetailSchema>;

// Enriched Person
export const EnrichedPersonSchema = z.object({
	id: z.string(),
	name: z.string(),
	yiddish_name: z.string().optional(),
	aliases: z.array(z.string()),
	gender: z.enum(['male', 'female', 'unknown']),
	birth_year: z.number().optional(),
	birth_date: z.string().optional(),
	death_year: z.number().optional(),
	death_date: z.string().optional(),
	birth_location: z.string().optional(),
	residence_at_publication: z.string().optional(),
	holocaust_fate: HolocaustFateSchema,
	holocaust_fate_notes: z.string().optional(),
	headshot_path: z.string().optional(),
	occupation: z.string().optional(),
	partisan_activity: PartisanActivitySchema.optional(),
	ghetto_role: z.string().optional(),
	unit_ids: z.array(z.string()),
	relationships: z.array(RelationshipSchema),
	external_references: z.array(ExternalReferenceSchema),
	additional_details: z.array(AdditionalDetailSchema).optional(),
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
	en: z.string().optional(),
	yi: z.string().optional(),
	pl: z.string().optional(),
	ru: z.string().optional(),
	be: z.string().optional(),
	he: z.string().optional(),
	de: z.string().optional(),
	uk: z.string().optional(),
});
export type LocalizedNames = z.infer<typeof LocalizedNamesSchema>;

// Historical administrative context (for time-varying containment)
export const HistoricalContextSchema = z.object({
	period: z.string(),
	label: z.string().optional(),
	parent_id: z.string().optional(),
	admin_name: z.string().optional(),
	sovereignty: z.string().optional(),
	notes: z.string().optional(),
});
export type HistoricalContext = z.infer<typeof HistoricalContextSchema>;

// Holocaust site metadata
export const HolocaustSiteSchema = z.object({
	site_type: z.string().optional(),
	date_established: z.string().optional(),
	date_liquidated: z.string().optional(),
	estimated_victims: z.number().optional(),
	key_events: z.array(z.string()).optional(),
	sources: z.array(z.string()).optional(),
});
export type HolocaustSite = z.infer<typeof HolocaustSiteSchema>;

// Enriched Location
export const EnrichedLocationSchema = z.object({
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
	// New hierarchy and enrichment fields
	names: LocalizedNamesSchema.optional(),
	parent_id: z.string().optional(),
	wikidata_id: z.string().optional(),
	geonames_id: z.string().optional(),
	historical_contexts: z.array(HistoricalContextSchema).optional(),
	holocaust_site: HolocaustSiteSchema.optional(),
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
	date: z.string().optional(),
	date_notes: z.string().optional(),
	location: z.string().optional(),
	description: z.string(),
	participants: z.array(ParticipantSchema),
	unit_ids: z.array(z.string()),
	external_references: z.array(ExternalReferenceSchema).optional(),
});
export type EnrichedEvent = z.infer<typeof EnrichedEventSchema>;

// Section hierarchy schemas (for sidebar grouping)

// Leaf node — owns articles directly
export const SectionItemSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	event_id: z.string().optional(),
	topic_id: z.string().optional(),
	unit_ids: z.array(z.string()),
});
export type SectionItem = z.infer<typeof SectionItemSchema>;

// L2 node — either a leaf (has unit_ids, no items) or a branch (has items)
export const SectionCategorySchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	topic_id: z.string().optional(),
	event_ids: z.array(z.string()).optional(),
	unit_ids: z.array(z.string()),
	primary_unit_ids: z.array(z.string()).optional(),
	items: z.array(SectionItemSchema).optional(),
});
export type SectionCategory = z.infer<typeof SectionCategorySchema>;

// L1 node — never owns articles directly
export const SectionSchema = z.object({
	id: z.string(),
	label: z.string(),
	icon: z.string().optional(),
	color: z.string().optional(),
	defaultOpen: z.boolean().optional(),
	categories: z.array(SectionCategorySchema),
});
export type Section = z.infer<typeof SectionSchema>;

// Top-level enrichment data
export const EnrichmentDataSchema = z.object({
	version: z.string(),
	edition_date: z.string(),
	last_updated: z.string(),
	people: z.array(EnrichedPersonSchema),
	locations: z.array(EnrichedLocationSchema),
	events: z.array(EnrichedEventSchema),
	topics: z.array(TopicSchema),
	sections: z.array(SectionSchema).optional(),
});
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
