import { withFieldOrder } from './shared.schema';
import {
	AttributionShape,
	SourcedDateShape,
	ReviewShape,
	SourceShape,
	SourceDerivationShape,
	CitationShape,
	FactShape,
	NameShape,
	FateShape,
	MentionShape,
} from './generated/sourced_entities';
import { z } from 'zod/v4';

import type { HolocaustFate } from './shared.schema';

const date = SourcedDateShape.shape.start
	.unwrap()
	.unwrap()
	.refine(validDate, 'invalid calendar date');
const day = AttributionShape.shape.on.refine(validDate, 'invalid ISO day');
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
export const SourcedDateSchema = withFieldOrder(
	SourcedDateShape.extend({
		start: date.nullish(),
		end: date.nullish(),
	}),
	'start end precision printed printed_calendar inferred'
).superRefine((v, ctx) => {
	const error = validateSourcedDate(v);
	if (error) ctx.addIssue({ code: 'custom', message: error });
});
export type SourcedDate = z.infer<typeof SourcedDateSchema>;
export const ReviewSchema = withFieldOrder(
	ReviewShape.extend({ on: day.nullish() }),
	'state by on'
).superRefine((v, ctx) => {
	const error = validateReview(v);
	if (error) ctx.addIssue({ code: 'custom', message: error });
});
export type Review = z.infer<typeof ReviewSchema>;
export const AttributionSchema = withFieldOrder(AttributionShape.extend({ on: day }), 'by on note');
export type Attribution = z.infer<typeof AttributionSchema>;
export const SourceHostSchema = SourceShape.shape.host
	.unwrap()
	.unwrap()
	.refine((h) => !h.startsWith('www.'), 'host without www');
// RFC 5646 §2.1, https://www.rfc-editor.org/rfc/rfc5646, read 2026-10-24:
// syntax (including private-use and grandfathered tags), not registry membership.
export const SourceLanguageSchema = SourceShape.shape.language.unwrap().unwrap().element;
export const SourceDerivationSchema = withFieldOrder(SourceDerivationShape, 'source_id relation');
export type SourceDerivation = z.infer<typeof SourceDerivationSchema>;
export const SourceSchema = withFieldOrder(
	SourceShape.extend({
		host: SourceHostSchema.nullish(),
		derived_from: z.array(SourceDerivationSchema).min(1).nullish(),
		dated: SourcedDateSchema.nullish(),
		quotes_cleared: AttributionSchema.nullish(),
	}),
	'made_by id kind title short_name holder_id reference_code language derived_from dated quotes_cleared quote_condition private work_id author editor published repository url_pattern host subjects'
);
export type Source = z.infer<typeof SourceSchema>;
export const CitationSchema = withFieldOrder(
	CitationShape.extend({ url: z.url({ protocol: /^https$/ }).nullish(), accessed: day.nullish() }),
	'source_id via reference_code record_type quote_language public_note locator record_id page scan time edition_date unit_id url quote note accessed'
).superRefine((v, ctx) => {
	const error = validateCitation(v);
	if (error) ctx.addIssue({ code: 'custom', message: error });
});
export type Citation = z.infer<typeof CitationSchema>;
export const FactSchema = withFieldOrder(
	FactShape.extend({
		date: SourcedDateSchema.nullish(),
		citations: z.array(CitationSchema).min(1),
		review: ReviewSchema,
		attribution: AttributionSchema,
	}),
	'id type proposed_type value date place_id organization_id event_id related_person_id relationship_type related_name qualifiers holocaust_related citations evidence_confidence identity_confidence status review attribution'
).superRefine((v, ctx) => {
	const error = validateFact(v);
	if (error) ctx.addIssue({ code: 'custom', message: error });
});
export type Fact = z.infer<typeof FactSchema>;
export const NameSchema = withFieldOrder(
	NameShape.extend({
		citations: z.array(CitationSchema).nullish(),
		attribution: AttributionSchema.nullish(),
	}),
	'value kind script lang citations attribution'
).superRefine((v, ctx) => {
	if (v.kind === 'supplied' && (!v.attribution || !v.citations?.length))
		ctx.addIssue({ code: 'custom', message: 'supplied name needs attribution and citations' });
	if (v.attribution && v.kind !== 'supplied')
		ctx.addIssue({
			code: 'custom',
			message: 'supplied attribution needs the supplied name kind',
		});
});
export type Name = z.infer<typeof NameSchema>;
export const FateSchema = withFieldOrder(
	FateShape.extend({ review: ReviewSchema }),
	'outcome confidence rests_on review summary'
).superRefine((v, ctx) => {
	const error = validateFate(v);
	if (error) ctx.addIssue({ code: 'custom', message: error });
});
export type Fate = z.infer<typeof FateSchema>;
export const MentionSchema = withFieldOrder(
	MentionShape,
	'id person_id unit_id printed_name role title function wkd_id'
);
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
