// Frozen from main e3e80c1 for ticket 20: shapes only; never import production shapes here.
import { z } from 'zod/v4';
import {
	CrossReferenceSchema,
	ContentItemBlockRefSchema,
	PrintedTitleSchema,
	SuppliedTitleSchema,
	TranslationSchema,
	siteText,
	siteDay,
} from './site-common.schema';
import {
	ImpressoTypesSchema,
	ContentItemSubtypesSchema,
	SubjectsSchema,
	SiteVocabularyVersionSchema,
} from './site-content.vocabulary';

// Local field-level provenance, not a claim that every word was checked.
export const ReadingStatusValueSchema = z.enum(['machine', 'session_checked', 'person_corrected']);
export const ReadingStatusSchema = z.strictObject({
	text: ReadingStatusValueSchema.nullable(),
	english: ReadingStatusValueSchema.nullable(),
});
export type ReadingStatus = z.infer<typeof ReadingStatusSchema>;

// Content item: the logical shape in the current site documents.
export const ContentItemSchema = z.strictObject({
	id: siteText,
	type: ImpressoTypesSchema,
	subtype: ContentItemSubtypesSchema.nullish(),
	printed_title: PrintedTitleSchema.nullish(),
	supplied_title: SuppliedTitleSchema,
	subject_ids: z.array(SubjectsSchema),
	section_id: siteText.nullish(),
	full_text: z.string(), // Copy made for the site from the physical source's lines.
	translation: TranslationSchema.nullish(),
	reading_status: ReadingStatusSchema.nullish(), // null/omission means unrecorded.
	block_breaks: z.array(z.number().int().nonnegative()),
	page_blocks: z.array(ContentItemBlockRefSchema).min(1),
	location_ids: z.array(siteText), // Places in the shared record; site spelling retained.
	organization_ids: z.array(siteText),
	cross_references: z.array(CrossReferenceSchema),
	event_id: siteText.nullish(),
});
export type ContentItem = z.infer<typeof ContentItemSchema>;

// Section means a printed heading and the content items beneath it, not a side list.
export const PrintedSectionSchema = z.strictObject({
	id: siteText,
	printed_title: PrintedTitleSchema,
	// Zod 4, "Nullish" (https://zod.dev/api#nullish), read 2026-10-22:
	// accept omission and null, matching the Pydantic default.
	supplied_title: SuppliedTitleSchema.nullish(),
	content_item_ids: z.array(siteText).min(1),
	heading_blocks: z.array(ContentItemBlockRefSchema).min(1),
});
export type PrintedSection = z.infer<typeof PrintedSectionSchema>;

export const ContentItemsDataSchema = z.strictObject({
	issue_date: siteDay,
	vocabulary_version: SiteVocabularyVersionSchema,
	content_items: z.array(ContentItemSchema),
	sections: z.array(PrintedSectionSchema),
});
export type ContentItemsData = z.infer<typeof ContentItemsDataSchema>;
