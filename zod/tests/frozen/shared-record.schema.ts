// Frozen from main e3e80c1 for ticket 20: shapes only; never import production shapes here.
import { z } from 'zod/v4';
import {
	FactSchema,
	NameSchema,
	FateSchema,
	SourceSchema,
	AttributionSchema,
	SourcedDateSchema,
	CitationSchema,
	SourceHostSchema,
} from './sourced-entities.schema';
import {
	GenderSchema,
	LocationTypesSchema,
	EventTypesSchema,
	EventPartsSchema,
	vocabularyVersion,
} from './sourced-entities.vocabulary';
import { PrintedAddressSchema, siteText, siteDay } from './site-common.schema';
import { MediaSchema, MediaPortraitSchema } from './media.schema';

// Located notice evidence written by the site writer. An older Citation without
// addresses retains its locator and quote verbatim, even after a rereading.
export const SiteCitationSchema = CitationSchema.safeExtend({
	addresses: z.array(PrintedAddressSchema).min(1).nullish(),
});
export type SiteCitation = z.infer<typeof SiteCitationSchema>;

// Released names with the site's located evidence; supplied attribution is inherited.
export const SharedNameSchema = NameSchema.safeExtend({
	citations: z.array(SiteCitationSchema).nullish(),
});
export type SharedName = z.infer<typeof SharedNameSchema>;

// Printed dates keep their original rules. A record date refers to the preferred
// fact, whose SourcedDate retains ranges, inference and even an unknown date.
export const LifeEventDateSchema = z.strictObject({
	record_fact_id: siteText.nullish(),
	printed: SourcedDateSchema.shape.printed,
	printed_calendar: SourcedDateSchema.shape.printed_calendar,
	start: SourcedDateSchema.shape.start,
	qualifier: z.literal('reported_in').nullish(),
	reported_in: siteDay.nullish(),
});
export type LifeEventDate = z.infer<typeof LifeEventDateSchema>;
export const LifeEventMainPersonSchema = z.strictObject({
	person_id: siteText,
	part: EventPartsSchema,
});
export type LifeEventMainPerson = z.infer<typeof LifeEventMainPersonSchema>;

// Fact and standing reuse the production contract, including its sources and review.
export const SharedFactSchema = FactSchema.safeExtend({
	citations: z.array(SiteCitationSchema).min(1),
	subject_id: siteText,
	family_id: siteText.nullish(),
	representation: z.enum(['structured', 'prose', 'image']),
});
export type SharedFact = z.infer<typeof SharedFactSchema>;

// Relation: subject -> relative; unreleased types keep other/proposed_type.
export const SourcedRelationSchema = FactSchema.safeExtend({
	citations: z.array(SiteCitationSchema).min(1),
	type: z.enum(['kinship', 'other']),
	subject_id: siteText,
	family_id: siteText.nullish(),
	shown: AttributionSchema.nullish(), // Permission to show a relative, never death evidence.
});
export type SourcedRelation = z.infer<typeof SourcedRelationSchema>;

const identity = { id: siteText, name: siteText, names: z.array(NameSchema) };
export const SharedPersonSchema = z.strictObject({
	portrait: MediaPortraitSchema.nullish(),
	...identity,
	names: z.array(SharedNameSchema),
	gender: GenderSchema,
	fate: FateSchema.nullish(),
});
export type SharedPerson = z.infer<typeof SharedPersonSchema>;
export const SharedFamilySchema = z.strictObject(identity);
export type SharedFamily = z.infer<typeof SharedFamilySchema>;
// An outside id of a place (rico:Identifier), read on its authority's own pages: the
// authority list is a registered source, so its host and address form are described once.
// Carried only on evidence, never from a name match (vetting §4).
export const PlaceIdentifierSchema = z.strictObject({
	source_id: siteText,
	value: siteText,
	url: z.url({ protocol: /^https$/ }).nullish(),
	accessed: siteDay,
	attribution: AttributionSchema,
});
export type PlaceIdentifier = z.infer<typeof PlaceIdentifierSchema>;
// Same evidence and uniqueness rules as places; a private holder's name is never public.
export const HolderSchema = z.strictObject({
	id: siteText,
	name: siteText,
	short_name: siteText.nullish(),
	kind: z.enum(['institution', 'family', 'private']),
	identifiers: z.array(PlaceIdentifierSchema).min(1).nullish(),
	host: SourceHostSchema.nullish(),
});
export type Holder = z.infer<typeof HolderSchema>;
// Plain object: the site derives its public place with .omit(). The identifiers' own
// rules (once per place, a registered authority, its host) are the shared record's.
export const SharedPlaceSchema = z.strictObject({
	...identity,
	type: LocationTypesSchema,
	parent_id: siteText.nullish(),
	coordinates: z.tuple([z.number().min(-90).max(90), z.number().min(-180).max(180)]).nullish(),
	identifiers: z.array(PlaceIdentifierSchema).min(1).nullish(),
});
export type SharedPlace = z.infer<typeof SharedPlaceSchema>;
export const SharedOrganizationSchema = z.strictObject(identity);
export type SharedOrganization = z.infer<typeof SharedOrganizationSchema>;
export const SharedEventSchema = z.strictObject({
	id: siteText,
	name: siteText,
	type: EventTypesSchema,
	proposed_type: siteText.nullish(),
	main_people: z.array(LifeEventMainPersonSchema),
	evidence_basis: z.literal('records_only').nullish(),
	dates: z.array(LifeEventDateSchema).min(1),
	location_id: siteText.nullish(),
	description: z.string().nullish(),
});
export type SharedEvent = z.infer<typeof SharedEventSchema>;

export const SharedRecordSchema = z.strictObject({
	version: z.literal('1'),
	vocabulary_version: z.literal(vocabularyVersion),
	persons: z.array(SharedPersonSchema),
	families: z.array(SharedFamilySchema),
	places: z.array(SharedPlaceSchema),
	organizations: z.array(SharedOrganizationSchema),
	events: z.array(SharedEventSchema),
	sources: z.array(SourceSchema),
	holders: z.array(HolderSchema).optional(),
	facts: z.array(SharedFactSchema),
	relations: z.array(SourcedRelationSchema),
	media: z.array(MediaSchema).nullish(),
});
export type SharedRecord = z.infer<typeof SharedRecordSchema>;
