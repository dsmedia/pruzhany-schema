// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import {
	ContentItemSubtypesEnum,
	ImpressoTypesEnum,
	ReadingStatusValueEnum,
	SubjectsEnum,
} from './enums';
import {
	ContentItemBlockRefShape,
	CrossReferenceShape,
	PrintedTitleShape,
	SuppliedTitleShape,
	TranslationShape,
} from './site_common';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 = /^(0\.1\.0|1\.0\.0)$(?![\s\S])/;

export const ReadingStatusShape = z.strictObject({
	english: ReadingStatusValueEnum.nullish(),
	text: ReadingStatusValueEnum.nullish(),
});

export const ContentItemShape = z.strictObject({
	block_breaks: z.array(z.number().int().min(0).max(9007199254740991)),
	cross_references: z.array(CrossReferenceShape),
	event_id: z.string().regex(pattern1).nullish(),
	full_text: z.string(),
	id: z.string().regex(pattern1),
	location_ids: z.array(z.string().regex(pattern1)),
	organization_ids: z.array(z.string().regex(pattern1)),
	page_blocks: z.array(ContentItemBlockRefShape).min(1),
	printed_title: PrintedTitleShape.nullish(),
	reading_status: ReadingStatusShape.nullish(),
	section_id: z.string().regex(pattern1).nullish(),
	subject_ids: z.array(SubjectsEnum),
	subtype: ContentItemSubtypesEnum.nullish(),
	supplied_title: SuppliedTitleShape,
	translation: TranslationShape.nullish(),
	type: ImpressoTypesEnum,
});

export const PrintedSectionShape = z.strictObject({
	content_item_ids: z.array(z.string().regex(pattern1)).min(1),
	heading_blocks: z.array(ContentItemBlockRefShape).min(1),
	id: z.string().regex(pattern1),
	printed_title: PrintedTitleShape,
	supplied_title: SuppliedTitleShape.nullish(),
});

export const ContentItemsDataShape = z.strictObject({
	content_items: z.array(ContentItemShape),
	issue_date: z.string().regex(pattern2),
	sections: z.array(PrintedSectionShape),
	vocabulary_version: z.string().regex(pattern3),
});
