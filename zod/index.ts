export {
	HolocaustFateSchema,
	ContentTypeSchema,
	ExternalReferenceSchema,
	BboxSchema,
	type HolocaustFate,
	type ContentType,
	type ExternalReference,
	type Bbox,
} from './shared.schema';

export {
	TopicSchema,
	AdditionalDetailSchema,
	EnrichedPersonSchema,
	EnrichedLocationSchema,
	EnrichedEventSchema,
	EnrichmentDataSchema,
	ArticleEnrichmentSchema,
	SectionItemSchema,
	SectionCategorySchema,
	SectionSchema,
	LocationTypeSchema,
	LocalizedNamesSchema,
	HistoricalContextSchema,
	HolocaustSiteSchema,
	type Topic,
	type AdditionalDetail,
	type EnrichedPerson,
	type EnrichedLocation,
	type EnrichedEvent,
	type EnrichmentData,
	type ArticleEnrichment,
	type SectionItem,
	type SectionCategory,
	type Section,
	type LocationType,
	type LocalizedNames,
	type HistoricalContext,
	type HolocaustSite,
} from './enrichment.schema';

export { ArticleSchema, ArticleDataSchema, type Article, type ArticleData } from './article.schema';

export {
	EditionSchema,
	HolidaySchema,
	HistoricalEventSchema,
	EditionsCatalogSchema,
	type Edition,
	type Holiday,
	type HistoricalEvent,
	type EditionsCatalog,
} from './editions.schema';

// Three-layer data model schemas
export {
	BlockSchema,
	PageSchema,
	PagesDataSchema,
	type Block,
	type Page,
	type PagesData,
} from './page.schema';

export {
	PageBlockRefSchema,
	CrossReferenceSchema,
	ContentUnitTypeSchema,
	ContentUnitSchema,
	ContentUnitsDataSchema,
	type PageBlockRef,
	type CrossReference,
	type ContentUnit,
	type ContentUnitsData,
} from './content-unit.schema';

export {
	ContentUnitRefSchema,
	LifeEventSchema,
	LifeEventsDataSchema,
	type ContentUnitRef,
	type LifeEvent,
	type LifeEventsData,
} from './life-event.schema';

// Unified edition bundle schema
export {
	EditionBundleSchema,
	EditionIdentitySchema,
	EditionPageSchema,
	EditionBlockSchema,
	EditionContentUnitSchema,
	EditionEventSchema,
	EditionPersonSchema,
	EditionLocationSchema,
	EditionOrganizationSchema,
	EditionTopicSchema,
	EventTypeSchema,
	type EditionBundle,
	type EditionIdentity,
	type EditionPage,
	type EditionBlock,
	type PageImage,
	type EditionContentUnit,
	type EditionEvent,
	type EventParticipant,
	type EventContentUnitRef,
	type EditionPerson,
	type EditionLocation,
	type EditionOrganization,
	type EditionTopic,
	type ReferenceData,
} from './edition-bundle.schema';
