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

export const PrintedTitleSchema = z
	.strictObject({
		text: siteText,
		addresses: z.array(PrintedAddressSchema).min(1),
	})
	.refine((v) => v.text === v.addresses.map((a) => a.text).join('\n'), {
		message: 'printed title must be its addressed words, joined by newlines',
	});
export type PrintedTitle = z.infer<typeof PrintedTitleSchema>;

export const SuppliedTitleSchema = z.strictObject({
	text: siteText,
	language: z.literal('en'),
	based_on: TextBasisSchema,
	attribution: AuthorshipSchema,
});
export type SuppliedTitle = z.infer<typeof SuppliedTitleSchema>;

// Translation is semantic work; its basis may survive a later rereading.
export const TranslationSchema = z.strictObject({
	text: siteText,
	language: z.literal('en'),
	based_on: TextBasisSchema,
	attribution: AuthorshipSchema,
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
