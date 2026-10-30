// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import { AuthorshipKindEnum } from './enums';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 = /^[0-9a-f]{64}$(?![\s\S])/;
const pattern4 = /^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])/;
const pattern5 = /^[^\s\u0085\uFEFF]+:title$(?![\s\S])/;
const pattern6 = /^[^\s\u0085\uFEFF]+:text$(?![\s\S])/;

export const AuthorshipShape = z.strictObject({
	by: z.string().regex(pattern1),
	on: z.string().regex(pattern2),
	note: z.string().nullish(),
	kind: AuthorshipKindEnum,
});

export const ContentItemBlockRefShape = z.strictObject({
	page_id: z.string().regex(pattern1),
	block_ids: z.array(z.string().regex(pattern1)).min(1),
});

export const CrossReferenceShape = z.strictObject({
	target_id: z.string(),
	confidence: z.number(),
	relationship: z.string(),
	evidence: z.string(),
});

export const EnglishCheckShape = z.strictObject({
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern4),
	judgement_sha256: z.string().regex(pattern3),
	attribution: AuthorshipShape,
});

export const PrintedAddressShape = z.strictObject({
	image_uri: z.string().regex(pattern1),
	bbox: z.array(z.number().min(0)).min(4).max(4),
	text: z.string(),
});

export const PrintedTitleShape = z.strictObject({
	text: z.string().regex(pattern1),
	addresses: z.array(PrintedAddressShape).min(1),
});

export const TextBasisShape = z.strictObject({
	source_text: z.string(),
	addresses: z.array(PrintedAddressShape).min(1),
});

export const TitleCheckShape = z.strictObject({
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern5),
	judgement_sha256: z.string().regex(pattern3),
	attribution: AuthorshipShape,
});

export const TranslationCheckShape = z.strictObject({
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern6),
	judgement_sha256: z.string().regex(pattern3),
	attribution: AuthorshipShape,
});

export const SuppliedTitleShape = z.strictObject({
	text: z.string().regex(pattern1),
	language: z.literal('en'),
	based_on: TextBasisShape,
	attribution: AuthorshipShape,
	checked_against: TitleCheckShape.nullish(),
});

export const TranslationShape = z.strictObject({
	text: z.string().regex(pattern1),
	language: z.literal('en'),
	based_on: TextBasisShape,
	attribution: AuthorshipShape,
	checked_against: TranslationCheckShape.nullish(),
});
