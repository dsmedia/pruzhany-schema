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
import type { HolocaustFate } from './shared.schema';
import citationRequirements from '../vocabulary/citation-requirements.json';

const text = z.string().regex(/\S/);
const date = z
	.string()
	.regex(/^\d{4}(-\d{2}(-\d{2})?)?$/)
	.refine(validDate, 'invalid calendar date');
const day = z
	.string()
	.regex(/^\d{4}-\d{2}-\d{2}$/)
	.refine(validDate, 'invalid ISO day');
function validDate(v: string): boolean {
	const full = v + ({ 4: '-01-01', 7: '-01', 10: '' }[v.length] ?? 'invalid');
	const d = new Date(`${full}T00:00:00Z`);
	return (
		Number(v.slice(0, 4)) > 0 && !Number.isNaN(d.valueOf()) && d.toISOString().slice(0, 10) === full
	);
}
const lower = (v: string) => v + ({ 4: '-01-01', 7: '-01', 10: '' }[v.length] ?? '');
function upper(v: string): string {
	if (v.length === 4) return `${v}-12-31`;
	if (v.length !== 7) return v;
	const year = Number(v.slice(0, 4));
	const month = Number(v.slice(5));
	const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
	const days = month === 2 ? (leap ? 29 : 28) : [4, 6, 9, 11].includes(month) ? 30 : 31;
	return `${v}-${days}`;
}
export const SourcedDateSchema = z
	.strictObject({
		start: date.nullish(),
		end: date.nullish(),
		precision: z.enum(['year', 'month', 'day', 'range']).nullish(),
		printed: text.nullish(),
		printed_calendar: z.enum(['gregorian', 'hebrew']).nullish(),
		inferred: z.boolean().nullish(),
	})
	.superRefine((v, ctx) => {
		const error = validateSourcedDate(v);
		if (error) ctx.addIssue({ code: 'custom', message: error });
	});
export type SourcedDate = z.infer<typeof SourcedDateSchema>;
export const ReviewSchema = z
	.strictObject({
		state: ReviewStatesSchema,
		by: text.nullish(),
		on: day.nullish(),
	})
	.superRefine((v, ctx) => {
		const error = validateReview(v);
		if (error) ctx.addIssue({ code: 'custom', message: error });
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
	.regex(/^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/)
	.refine((h) => !h.startsWith('www.'), 'host without www');
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
export const CitationSchema = z
	.strictObject({
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
	})
	.superRefine((v, ctx) => {
		const error = validateCitation(v);
		if (error) ctx.addIssue({ code: 'custom', message: error });
	});
export type Citation = z.infer<typeof CitationSchema>;
export const FactSchema = z
	.strictObject({
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
	})
	.superRefine((v, ctx) => {
		const error = validateFact(v);
		if (error) ctx.addIssue({ code: 'custom', message: error });
	});
export type Fact = z.infer<typeof FactSchema>;
export const NameSchema = z
	.strictObject({
		value: text,
		kind: NameKindsSchema,
		script: z.string().regex(/^[A-Za-z]{4}$/),
		lang: z
			.string()
			.regex(/^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/)
			.nullish(),
		citations: z.array(CitationSchema).nullish(),
		attribution: AttributionSchema.nullish(),
	})
	.superRefine((v, ctx) => {
		if (v.kind === 'supplied' && (!v.attribution || !v.citations?.length))
			ctx.addIssue({ code: 'custom', message: 'supplied name needs attribution and citations' });
		if (v.attribution && v.kind !== 'supplied')
			ctx.addIssue({
				code: 'custom',
				message: 'supplied attribution needs the supplied name kind',
			});
	});
export type Name = z.infer<typeof NameSchema>;
export const FateSchema = z
	.strictObject({
		outcome: FateOutcomesSchema,
		confidence: ConfidenceSchema,
		rests_on: z.array(z.string()),
		review: ReviewSchema,
		summary: z.string().nullish(),
	})
	.superRefine((v, ctx) => {
		const error = validateFate(v);
		if (error) ctx.addIssue({ code: 'custom', message: error });
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

function validateSourcedDate(v: SourcedDate) {
	if (!(v.start || v.printed?.trim())) return 'date needs start or printed';
	if (v.printed_calendar && !v.printed?.trim()) return 'calendar needs printed';
	if (v.end && v.precision !== 'range') return 'end needs range precision';
	if (v.precision === 'range' && (!v.start || !v.end || lower(v.start) > upper(v.end)))
		return 'range needs ordered bounds';
	if (
		v.precision &&
		v.precision !== 'range' &&
		(!v.start || v.start.length !== { year: 4, month: 7, day: 10 }[v.precision])
	)
		return 'precision mismatch';
}
function validateReview(v: Review) {
	if (v.state === 'approved' && !(v.by?.trim() && v.on))
		return 'approval requires reviewer and day';
}
function validateCitation(v: Citation) {
	if (
		![v.record_id, v.page, v.scan, v.time, v.unit_id, v.url, v.locator, v.reference_code].some(
			(x) => x?.trim()
		)
	)
		return 'citation needs locator';
}
function validateFact(v: Fact) {
	const originals = new Set(v.citations.map((c) => c.source_id));
	if (v.citations.some((c) => c.via && originals.has(c.via)))
		return 'citation via cannot also be an original for the same statement';
	if ((v.type === 'other') !== !!v.proposed_type?.trim()) return 'proposed_type exactly for other';
	if (v.type === 'kinship' && !(v.relationship_type && (v.related_name || v.related_person_id)))
		return 'kinship needs relationship and relative';
	if (v.type === 'occupation' && !v.value) return 'occupation needs value';
	if (v.type === 'residence' && !(v.place_id || v.value)) return 'residence needs place or value';
	if (v.type === 'event_participation' && !v.event_id) return 'participation needs event';
	if (['birth', 'death'].includes(v.type) && !(v.date || v.place_id || v.value))
		return 'birth/death needs payload';
}
function validateFate(v: Fate) {
	if (v.outcome !== 'unknown' && !v.rests_on.length) return 'known fate needs facts';
}
export function legacyHolocaustFate(fate: Fate): HolocaustFate {
	return (fate.outcome === 'perished' || fate.outcome === 'survived') &&
		fate.confidence !== 'confirmed'
		? `likely_${fate.outcome}`
		: fate.outcome;
}
