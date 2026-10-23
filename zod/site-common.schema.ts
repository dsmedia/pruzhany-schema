import { z } from 'zod/v4';
import { AttributionSchema } from './sourced-entities.schema';

export const siteText = z.string().regex(/\S/);
export const siteDay = AttributionSchema.shape.on;
const pixelBox = z.tuple([
	z.number().nonnegative(),
	z.number().nonnegative(),
	z.number().positive(),
	z.number().positive(),
]);

// Address of a printed place: picture key, native pixels and the text read there.
export const PrintedAddressSchema = z.strictObject({
	image_uri: siteText,
	bbox: pixelBox,
	text: z.string(), // May be empty for a patch without a readable line.
});
export type PrintedAddress = z.infer<typeof PrintedAddressSchema>;

export const TextBasisSchema = z.strictObject({
	source_text: z.string(), // Exact text used, without normalisation or a later overwrite.
	addresses: z.array(PrintedAddressSchema).min(1),
});
export type TextBasis = z.infer<typeof TextBasisSchema>;

export const AuthorshipSchema = AttributionSchema.extend({
	kind: z.enum(['person', 'model']),
});
export type Authorship = z.infer<typeof AuthorshipSchema>;

// Exact UTF-8 bytes, without whitespace or Unicode normalisation.
const sha256 = z
	.string()
	.length(64)
	.regex(/^[0-9a-f]{64}$/);
// Opaque ID plus field suffix. Include NEL/BOM in whitespace in both runtimes;
// the end guard prevents JavaScript's $ from accepting a final line terminator.
export const EnglishCheckSchema = z.strictObject({
	reading_id: siteText,
	reading_sha256: sha256,
	english_sha256: sha256,
	judgement_id: z.string().regex(/^[^\s\u0085\uFEFF]+:(title|text)$(?![\s\S])/),
	judgement_sha256: sha256,
	attribution: AuthorshipSchema,
});
export type EnglishCheck = z.infer<typeof EnglishCheckSchema>;

export const TitleCheckSchema = EnglishCheckSchema.extend({
	judgement_id: z.string().regex(/^[^\s\u0085\uFEFF]+:title$(?![\s\S])/),
});
export const TranslationCheckSchema = EnglishCheckSchema.extend({
	judgement_id: z.string().regex(/^[^\s\u0085\uFEFF]+:text$(?![\s\S])/),
});

export const PrintedTitleSchema = z
	.strictObject({
		text: siteText,
		addresses: z.array(PrintedAddressSchema).min(1),
	})
	.refine((v) => v.text === v.addresses.map((a) => a.text).join('\n'), {
		message: 'printed title must be its addressed words, joined by newlines',
	});
export type PrintedTitle = z.infer<typeof PrintedTitleSchema>;

const attributedEnglish = {
	text: siteText,
	language: z.literal('en'),
	based_on: TextBasisSchema,
	attribution: AuthorshipSchema,
};

export const SuppliedTitleSchema = z.strictObject({
	...attributedEnglish,
	checked_against: TitleCheckSchema.optional(),
});
export type SuppliedTitle = z.infer<typeof SuppliedTitleSchema>;

// Translation is semantic work; its basis may survive a later rereading.
export const TranslationSchema = z.strictObject({
	...attributedEnglish,
	checked_against: TranslationCheckSchema.optional(),
});
export type Translation = z.infer<typeof TranslationSchema>;

export function textBasisMatches(basis: TextBasis, currentText: string): boolean {
	return basis.source_text === currentText;
}

export const ContentItemBlockRefSchema = z.strictObject({
	page_id: siteText,
	block_ids: z.array(siteText).min(1), // Regions, in reading order; site spelling retained.
});
export type ContentItemBlockRef = z.infer<typeof ContentItemBlockRefSchema>;

export function uniqueIds(values: readonly string[], label: string): string[] {
	return new Set(values).size === values.length ? [] : [`duplicate ${label}`];
}
