import { z } from 'zod/v4';
import {
	CrossReferenceSchema,
	ContentItemBlockRefSchema,
	PrintedTitleSchema,
	SuppliedTitleSchema,
	TranslationSchema,
	siteText,
	siteDay,
	uniqueIds,
} from './site-common.schema';
import {
	ImpressoTypesSchema,
	ContentItemSubtypesSchema,
	SubjectsSchema,
	siteVocabularyVersion,
	subtypeParents,
} from './site-content.vocabulary';

// Content item: the logical shape in the current site documents.
export const ContentItemSchema = z
	.strictObject({
		id: siteText,
		type: ImpressoTypesSchema,
		subtype: ContentItemSubtypesSchema.nullish(),
		printed_title: PrintedTitleSchema.nullish(),
		supplied_title: SuppliedTitleSchema,
		subject_ids: z.array(SubjectsSchema),
		section_id: siteText.nullish(),
		full_text: z.string(), // Copy made for the site from the physical source's lines.
		translation: TranslationSchema.nullish(),
		block_breaks: z.array(z.number().int().nonnegative()),
		page_blocks: z.array(ContentItemBlockRefSchema).min(1),
		location_ids: z.array(siteText), // Places in the shared record; site spelling retained.
		organization_ids: z.array(siteText),
		cross_references: z.array(CrossReferenceSchema),
		event_id: siteText.nullish(),
	})
	.superRefine((v, ctx) => {
		if (v.subtype && subtypeParents[v.subtype] !== v.type)
			ctx.addIssue({ code: 'custom', message: 'subtype has a different Impresso parent' });
		const errors = uniqueIds(v.subject_ids, 'subject id');
		const length = [...v.full_text].length; // Unicode code points, as in Python.
		if (v.block_breaks.some((n, i) => n > length || (i > 0 && n <= v.block_breaks[i - 1])))
			errors.push('block breaks must be ordered offsets within full_text');
		for (const message of errors) ctx.addIssue({ code: 'custom', message });
	});
export type ContentItem = z.infer<typeof ContentItemSchema>;

// Section means a printed heading and the content items beneath it, not a side list.
export const PrintedSectionSchema = z
	.strictObject({
		id: siteText,
		printed_title: PrintedTitleSchema,
		// Zod 4, "Nullish" (https://zod.dev/api#nullish), read 2026-10-22:
		// accept omission and null, matching the Pydantic default.
		supplied_title: SuppliedTitleSchema.nullish(),
		content_item_ids: z.array(siteText).min(1),
		heading_blocks: z.array(ContentItemBlockRefSchema).min(1),
	})
	.superRefine((v, ctx) => {
		for (const message of uniqueIds(v.content_item_ids, 'section member'))
			ctx.addIssue({ code: 'custom', message });
	});
export type PrintedSection = z.infer<typeof PrintedSectionSchema>;

export const ContentItemsDataSchema = z
	.strictObject({
		issue_date: siteDay,
		vocabulary_version: z.literal(siteVocabularyVersion),
		content_items: z.array(ContentItemSchema),
		sections: z.array(PrintedSectionSchema),
	})
	.superRefine((v, ctx) => {
		const errors = [
			...uniqueIds(
				v.content_items.map((i) => i.id),
				'content item id'
			),
			...uniqueIds(
				v.sections.map((s) => s.id),
				'section id'
			),
		];
		const items = new Map(v.content_items.map((i) => [i.id, i]));
		const sections = new Map(v.sections.map((s) => [s.id, s]));
		for (const item of v.content_items) {
			if (item.section_id && !sections.get(item.section_id)?.content_item_ids.includes(item.id))
				errors.push('content item must belong to its named section');
			if (item.cross_references.some((r) => !items.has(r.target_id)))
				errors.push('unknown cross-reference content item');
		}
		for (const section of v.sections)
			if (section.content_item_ids.some((id) => items.get(id)?.section_id !== section.id))
				errors.push('section membership must agree in both directions');
		for (const message of errors) ctx.addIssue({ code: 'custom', message });
	});
export type ContentItemsData = z.infer<typeof ContentItemsDataSchema>;
