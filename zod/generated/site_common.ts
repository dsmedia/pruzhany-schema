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
	kind: AuthorshipKindEnum,
	note: z.string().nullish(),
	on: z.string().regex(pattern2),
});

export const ContentItemBlockRefShape = z.strictObject({
	block_ids: z.array(z.string().regex(pattern1)).min(1),
	page_id: z.string().regex(pattern1),
});

export const CrossReferenceShape = z.strictObject({
	confidence: z.number(),
	evidence: z.string(),
	relationship: z.string(),
	target_id: z.string(),
});

export const EnglishCheckShape = z.strictObject({
	attribution: AuthorshipShape,
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern4),
	judgement_sha256: z.string().regex(pattern3),
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
});

export const PrintedAddressShape = z.strictObject({
	bbox: z.array(z.number().min(0)).min(4).max(4),
	image_uri: z.string().regex(pattern1),
	text: z.string(),
});

export const PrintedTitleShape = z.strictObject({
	addresses: z.array(PrintedAddressShape).min(1),
	text: z.string().regex(pattern1),
});

export const TextBasisShape = z.strictObject({
	addresses: z.array(PrintedAddressShape).min(1),
	source_text: z.string(),
});

export const TitleCheckShape = z.strictObject({
	attribution: AuthorshipShape,
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern5),
	judgement_sha256: z.string().regex(pattern3),
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
});

export const TranslationCheckShape = z.strictObject({
	attribution: AuthorshipShape,
	english_sha256: z.string().regex(pattern3),
	judgement_id: z.string().regex(pattern6),
	judgement_sha256: z.string().regex(pattern3),
	reading_id: z.string().regex(pattern1),
	reading_sha256: z.string().regex(pattern3),
});

export const SuppliedTitleShape = z.strictObject({
	attribution: AuthorshipShape,
	based_on: TextBasisShape,
	checked_against: TitleCheckShape.nullish(),
	language: z.literal('en'),
	text: z.string().regex(pattern1),
});

export const TranslationShape = z.strictObject({
	attribution: AuthorshipShape,
	based_on: TextBasisShape,
	checked_against: TranslationCheckShape.nullish(),
	language: z.literal('en'),
	text: z.string().regex(pattern1),
});
