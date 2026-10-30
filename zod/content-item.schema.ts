import {
	ReadingStatusShape,
	ContentItemShape,
	PrintedSectionShape,
	ContentItemsDataShape,
} from './generated/content_items';
import { z } from 'zod/v4';
import {
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
// known-looser: both keys are required and nullable.
export const ReadingStatusSchema = ReadingStatusShape.extend({
	text: ReadingStatusShape.shape.text.unwrap(),
	english: ReadingStatusShape.shape.english.unwrap(),
});
export type ReadingStatus = z.infer<typeof ReadingStatusSchema>;

// Rebind children to retain address, null, calendar and text checks in the document.
export const ContentItemSchema = ContentItemShape.extend({
	printed_title: PrintedTitleSchema.nullish(),
	supplied_title: SuppliedTitleSchema,
	translation: TranslationSchema.nullish(),
	reading_status: ReadingStatusSchema.nullish(),
}).superRefine((v, ctx) => {
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
export const PrintedSectionSchema = PrintedSectionShape.extend({
	printed_title: PrintedTitleSchema,
	supplied_title: SuppliedTitleSchema.nullish(),
}).superRefine((v, ctx) => {
	for (const message of uniqueIds(v.content_item_ids, 'section member'))
		ctx.addIssue({ code: 'custom', message });
});
export type PrintedSection = z.infer<typeof PrintedSectionSchema>;

export const ContentItemsDataSchema = ContentItemsDataShape.extend({
	issue_date: siteDay,
	// Preserve the released inferred union of supported vocabulary versions.
	vocabulary_version: SiteVocabularyVersionSchema,
	content_items: z.array(ContentItemSchema),
	sections: z.array(PrintedSectionSchema),
}).superRefine((v, ctx) => {
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
