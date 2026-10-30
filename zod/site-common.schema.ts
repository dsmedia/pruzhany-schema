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

export const CrossReferenceSchema = CrossReferenceShape;
export type CrossReference = z.infer<typeof CrossReferenceSchema>;

export const siteText = PrintedAddressShape.shape.image_uri;
export const siteDay = AttributionSchema.shape.on;
// known-looser: positional bounds; a tuple also preserves the public inferred type.
const pixelBox = z.tuple([
	z.number().nonnegative(),
	z.number().nonnegative(),
	z.number().positive(),
	z.number().positive(),
]);

// Address of a printed place: picture key, native pixels and the text read there.
export const PrintedAddressSchema = PrintedAddressShape.extend({ bbox: pixelBox });
export type PrintedAddress = z.infer<typeof PrintedAddressSchema>;

// Rebind children to carry tuple, calendar and text checks into generated parents.
export const TextBasisSchema = TextBasisShape.extend({
	addresses: z.array(PrintedAddressSchema).min(1),
});
export type TextBasis = z.infer<typeof TextBasisSchema>;

// Keep the retained calendar refinement inside generated parents.
export const AuthorshipSchema = AuthorshipShape.extend({ on: siteDay });
export type Authorship = z.infer<typeof AuthorshipSchema>;

// Opaque ID plus field suffix. Include NEL/BOM in whitespace in both runtimes;
// the end guard prevents JavaScript's $ from accepting a final line terminator.
export const EnglishCheckSchema = EnglishCheckShape.extend({
	// The existing pattern gate also reads this non-document base's regex literal.
	judgement_id: z.string().regex(/^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])/),
	attribution: AuthorshipSchema,
});
export type EnglishCheck = z.infer<typeof EnglishCheckSchema>;

export const TitleCheckSchema = TitleCheckShape.extend({
	attribution: AuthorshipSchema,
});
export const TranslationCheckSchema = TranslationCheckShape.extend({
	attribution: AuthorshipSchema,
});

export const PrintedTitleSchema = PrintedTitleShape.extend({
	addresses: z.array(PrintedAddressSchema).min(1),
}).refine((v) => v.text === v.addresses.map((a) => a.text).join('\n'), {
	message: 'printed title must be its addressed words, joined by newlines',
});
export type PrintedTitle = z.infer<typeof PrintedTitleSchema>;

export const SuppliedTitleSchema = SuppliedTitleShape.extend({
	checked_against: TitleCheckSchema.optional(),
	based_on: TextBasisSchema,
	attribution: AuthorshipSchema,
});
export type SuppliedTitle = z.infer<typeof SuppliedTitleSchema>;

// Translation is semantic work; its basis may survive a later rereading.
export const TranslationSchema = TranslationShape.extend({
	checked_against: TranslationCheckSchema.optional(),
	based_on: TextBasisSchema,
	attribution: AuthorshipSchema,
});
export type Translation = z.infer<typeof TranslationSchema>;

export function textBasisMatches(basis: TextBasis, currentText: string): boolean {
	return basis.source_text === currentText;
}

export const ContentItemBlockRefSchema = ContentItemBlockRefShape;
export type ContentItemBlockRef = z.infer<typeof ContentItemBlockRefSchema>;

export function uniqueIds(values: readonly string[], label: string): string[] {
	return new Set(values).size === values.length ? [] : [`duplicate ${label}`];
}
