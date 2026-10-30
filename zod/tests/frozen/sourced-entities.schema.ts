// Frozen from main e3e80c1 for ticket 20: shapes only; never import production shapes here.
import { z } from 'zod/v4';
import {
	FactTypesSchema,
	RelationshipTypesSchema,
	NameKindsSchema,
	MentionRolesSchema,
	SourceKindsSchema,
	ConfidenceSchema,
	ClaimStatusSchema,
	ReviewStatesSchema,
	FateOutcomesSchema,
} from './sourced-entities.vocabulary';

import { citationRequirements } from './citation-requirements.table';

const text = z.string().regex(/\S/);
const date = z.string().regex(/^\d{4}(-\d{2}(-\d{2})?)?$/);
const day = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);
export const SourcedDateSchema = z.strictObject({
	start: date.nullish(),
	end: date.nullish(),
	precision: z.enum(['year', 'month', 'day', 'range']).nullish(),
	printed: text.nullish(),
	printed_calendar: z.enum(['gregorian', 'hebrew']).nullish(),
	inferred: z.boolean().nullish(),
});
export type SourcedDate = z.infer<typeof SourcedDateSchema>;
export const ReviewSchema = z.strictObject({
	state: ReviewStatesSchema,
	by: text.nullish(),
	on: day.nullish(),
});
export type Review = z.infer<typeof ReviewSchema>;
export const AttributionSchema = z.strictObject({
	by: text,
	on: day,
	note: z.string().nullish(),
});
export type Attribution = z.infer<typeof AttributionSchema>;
export const SourceHostSchema = z
	.string()
	.regex(/^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/);
// RFC 5646 §2.1, https://www.rfc-editor.org/rfc/rfc5646, read 2026-10-24:
// syntax (including private-use and grandfathered tags), not registry membership.
export const SourceLanguageSchema = z
	.string()
	.regex(new RegExp(citationRequirements.language_tag_pattern));
export const SourceDerivationSchema = z.strictObject({
	source_id: text,
	relation: z.enum(['copy', 'transcription']),
});
export type SourceDerivation = z.infer<typeof SourceDerivationSchema>;
export const SourceSchema = z.strictObject({
	made_by: z.enum(['family', 'studio', 'institution', 'perpetrator', 'unknown']).nullish(),
	id: text,
	kind: SourceKindsSchema,
	title: text,
	short_name: text.nullish(),
	holder_id: text.nullish(),
	reference_code: text.nullish(),
	language: z.array(SourceLanguageSchema).min(1).nullish(),
	derived_from: z.array(SourceDerivationSchema).min(1).nullish(),
	dated: SourcedDateSchema.nullish(),
	quotes_cleared: AttributionSchema.nullish(),
	// The owner's condition on cleared quotes (24 October 2026): shown only where no other record says it.
	quote_condition: z.enum(['unique_information']).nullish(),
	private: z.boolean().nullish(),
	work_id: z.string().nullish(),
	author: z.string().nullish(),
	editor: z.string().nullish(),
	published: z.string().nullish(),
	repository: z.string().nullish(), // Read for one release: site projection and retained research.
	url_pattern: z.string().nullish(),
	// A bare lowercase host name: the source's addresses are on it or a subdomain of it.
	host: SourceHostSchema.nullish(),
	subjects: z.array(text).min(1).nullish(),
});
export type Source = z.infer<typeof SourceSchema>;
export const CitationSchema = z.strictObject({
	source_id: text,
	via: text.nullish(),
	reference_code: text.nullish(),
	record_type: text.nullish(),
	quote_language: SourceLanguageSchema.nullish(),
	public_note: text.nullish(),
	locator: text.nullish(), // Internal only; never a holder's record number.
	record_id: z.string().nullish(),
	page: z.string().nullish(),
	scan: z.string().nullish(),
	time: z.string().nullish(),
	edition_date: z.string().nullish(),
	unit_id: z.string().nullish(),
	url: z.url({ protocol: /^https$/ }).nullish(),
	quote: z.string().nullish(),
	note: z.string().nullish(),
	accessed: day.nullish(),
});
export type Citation = z.infer<typeof CitationSchema>;
export const FactSchema = z.strictObject({
	id: text,
	type: FactTypesSchema,
	proposed_type: text.nullish(),
	value: text.nullish(),
	date: SourcedDateSchema.nullish(),
	place_id: text.nullish(),
	organization_id: text.nullish(),
	event_id: text.nullish(),
	related_person_id: text.nullish(),
	relationship_type: RelationshipTypesSchema.nullish(),
	related_name: text.nullish(),
	qualifiers: z.record(z.string(), z.string()).nullish(),
	holocaust_related: z.boolean().nullish(),
	citations: z.array(CitationSchema).min(1),
	evidence_confidence: ConfidenceSchema,
	identity_confidence: ConfidenceSchema,
	status: ClaimStatusSchema,
	review: ReviewSchema,
	attribution: AttributionSchema,
});
export type Fact = z.infer<typeof FactSchema>;
export const NameSchema = z.strictObject({
	value: text,
	kind: NameKindsSchema,
	script: z.string().regex(/^[A-Za-z]{4}$/),
	lang: z
		.string()
		.regex(/^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/)
		.nullish(),
	citations: z.array(CitationSchema).nullish(),
	attribution: AttributionSchema.nullish(),
});
export type Name = z.infer<typeof NameSchema>;
export const FateSchema = z.strictObject({
	outcome: FateOutcomesSchema,
	confidence: ConfidenceSchema,
	rests_on: z.array(z.string()),
	review: ReviewSchema,
	summary: z.string().nullish(),
});
export type Fate = z.infer<typeof FateSchema>;
export const MentionSchema = z.strictObject({
	id: text,
	person_id: text,
	unit_id: text,
	printed_name: text,
	role: MentionRolesSchema.nullish(),
	title: z.string().nullish(),
	function: z.string().nullish(),
	wkd_id: z.string().nullish(),
});
export type Mention = z.infer<typeof MentionSchema>;
