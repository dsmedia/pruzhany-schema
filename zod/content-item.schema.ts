import { withFieldOrder } from './shared.schema';
import {
	ReadingStatusShape,
	ContentItemShape,
	PrintedSectionShape,
	ContentItemsDataShape,
} from './generated/content_items';
import { z } from 'zod/v4';
import {
	CrossReferenceSchema,
	ContentItemBlockRefSchema,
	PrintedTitleSchema,
	SuppliedTitleSchema,
	TranslationSchema,
	siteDay,
	uniqueIds,
} from './site-common.schema';
import { SiteVocabularyVersionSchema, subtypeParents } from './site-content.vocabulary';

// Local field-level provenance, not a claim that every word was checked.
// The vocabulary gate inspects this released enum declaration directly.
export const ReadingStatusValueSchema = z.enum(['machine', 'session_checked', 'person_corrected']);
export const ReadingStatusSchema = withFieldOrder(
	ReadingStatusShape.extend({
		text: ReadingStatusValueSchema.nullable(),
		english: ReadingStatusValueSchema.nullable(),
	}),
	'text english'
);
export type ReadingStatus = z.infer<typeof ReadingStatusSchema>;

// Content item: the logical shape in the current site documents.
export const ContentItemSchema = withFieldOrder(
	ContentItemShape.extend({
		printed_title: PrintedTitleSchema.nullish(),
		supplied_title: SuppliedTitleSchema,
		translation: TranslationSchema.nullish(),
		reading_status: ReadingStatusSchema.nullish(),
		page_blocks: z.array(ContentItemBlockRefSchema).min(1),
		cross_references: z.array(CrossReferenceSchema),
	}),
	'id type subtype printed_title supplied_title subject_ids section_id full_text translation reading_status block_breaks page_blocks location_ids organization_ids cross_references event_id'
).superRefine((v, ctx) => {
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
export const PrintedSectionSchema = withFieldOrder(
	PrintedSectionShape.extend({
		printed_title: PrintedTitleSchema,
		supplied_title: SuppliedTitleSchema.nullish(),
		heading_blocks: z.array(ContentItemBlockRefSchema).min(1),
	}),
	'id printed_title supplied_title content_item_ids heading_blocks'
).superRefine((v, ctx) => {
	for (const message of uniqueIds(v.content_item_ids, 'section member'))
		ctx.addIssue({ code: 'custom', message });
});
export type PrintedSection = z.infer<typeof PrintedSectionSchema>;

export const ContentItemsDataSchema = withFieldOrder(
	ContentItemsDataShape.extend({
		issue_date: siteDay,
		vocabulary_version: SiteVocabularyVersionSchema,
		content_items: z.array(ContentItemSchema),
		sections: z.array(PrintedSectionSchema),
	}),
	'issue_date vocabulary_version content_items sections'
).superRefine((v, ctx) => {
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
