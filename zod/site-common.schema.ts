import { withFieldOrder } from './shared.schema';
import {
	CrossReferenceShape,
	PrintedAddressShape,
	TextBasisShape,
	AuthorshipShape,
	EnglishCheckShape,
	TitleCheckShape,
	TranslationCheckShape,
	PrintedTitleShape,
	SuppliedTitleShape,
	TranslationShape,
	ContentItemBlockRefShape,
} from './generated/site_common';
import { z } from 'zod/v4';
import { AttributionSchema } from './sourced-entities.schema';

export const CrossReferenceSchema = withFieldOrder(
	CrossReferenceShape,
	'target_id confidence relationship evidence'
).strip();
export type CrossReference = z.infer<typeof CrossReferenceSchema>;

export const siteText = PrintedAddressShape.shape.image_uri;
export const siteDay = AttributionSchema.shape.on;
const pixelBox = z.tuple([
	z.number().nonnegative(),
	z.number().nonnegative(),
	z.number().positive(),
	z.number().positive(),
]);

// Address of a printed place: picture key, native pixels and the text read there.
export const PrintedAddressSchema = withFieldOrder(
	PrintedAddressShape.extend({ bbox: pixelBox }),
	'image_uri bbox text'
);
export type PrintedAddress = z.infer<typeof PrintedAddressSchema>;

export const TextBasisSchema = withFieldOrder(
	TextBasisShape.extend({ addresses: z.array(PrintedAddressSchema).min(1) }),
	'source_text addresses'
);
export type TextBasis = z.infer<typeof TextBasisSchema>;

export const AuthorshipSchema = withFieldOrder(
	AuthorshipShape.extend(AttributionSchema.shape),
	'by on note kind'
);
export type Authorship = z.infer<typeof AuthorshipSchema>;

// Exact UTF-8 bytes, without whitespace or Unicode normalisation.
const sha256 = z
	.string()
	.length(64)
	.regex(/^[0-9a-f]{64}$/);
// Opaque ID plus field suffix. Include NEL/BOM in whitespace in both runtimes;
// the end guard prevents JavaScript's $ from accepting a final line terminator.
export const EnglishCheckSchema = withFieldOrder(
	EnglishCheckShape.extend({
		// The existing pattern gate also reads this non-document base's regex literal.
		judgement_id: z.string().regex(/^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])/),
		reading_sha256: sha256,
		english_sha256: sha256,
		judgement_sha256: sha256,
		attribution: AuthorshipSchema,
	}),
	'reading_id reading_sha256 english_sha256 judgement_id judgement_sha256 attribution'
);
export type EnglishCheck = z.infer<typeof EnglishCheckSchema>;

export const TitleCheckSchema = withFieldOrder(
	TitleCheckShape.extend({
		...EnglishCheckSchema.shape,
		judgement_id: TitleCheckShape.shape.judgement_id,
	}),
	'reading_id reading_sha256 english_sha256 judgement_id judgement_sha256 attribution'
);
export const TranslationCheckSchema = withFieldOrder(
	TranslationCheckShape.extend({
		...EnglishCheckSchema.shape,
		judgement_id: TranslationCheckShape.shape.judgement_id,
	}),
	'reading_id reading_sha256 english_sha256 judgement_id judgement_sha256 attribution'
);

export const PrintedTitleSchema = withFieldOrder(
	PrintedTitleShape.extend({ addresses: z.array(PrintedAddressSchema).min(1) }),
	'text addresses'
).refine((v) => v.text === v.addresses.map((a) => a.text).join('\n'), {
	message: 'printed title must be its addressed words, joined by newlines',
});
export type PrintedTitle = z.infer<typeof PrintedTitleSchema>;

export const SuppliedTitleSchema = withFieldOrder(
	SuppliedTitleShape.extend({
		checked_against: TitleCheckSchema.optional(),
		based_on: TextBasisSchema,
		attribution: AuthorshipSchema,
	}),
	'text language based_on attribution checked_against'
);
export type SuppliedTitle = z.infer<typeof SuppliedTitleSchema>;

// Translation is semantic work; its basis may survive a later rereading.
export const TranslationSchema = withFieldOrder(
	TranslationShape.extend({
		checked_against: TranslationCheckSchema.optional(),
		based_on: TextBasisSchema,
		attribution: AuthorshipSchema,
	}),
	'text language based_on attribution checked_against'
);
export type Translation = z.infer<typeof TranslationSchema>;

export function textBasisMatches(basis: TextBasis, currentText: string): boolean {
	return basis.source_text === currentText;
}

export const ContentItemBlockRefSchema = withFieldOrder(
	ContentItemBlockRefShape,
	'page_id block_ids'
);
export type ContentItemBlockRef = z.infer<typeof ContentItemBlockRefSchema>;

export function uniqueIds(values: readonly string[], label: string): string[] {
	return new Set(values).size === values.length ? [] : [`duplicate ${label}`];
}
