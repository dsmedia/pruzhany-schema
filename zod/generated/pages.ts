// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

export const BlockShape = z.strictObject({
	bbox: z.array(z.number().int().min(0).max(9007199254740991)).min(4).max(4),
	confidence: z.number().nullish(),
	id: z.string(),
	image_crop: z.string().nullish(),
	transcription: z.string(),
	unit_id: z.string().nullish(),
});

export const PageShape = z.strictObject({
	blocks: z.array(BlockShape),
	dimensions: z.array(z.number().int()).min(2).max(2),
	id: z.string(),
	image_uri: z.string(),
	issue_date: z.string(),
	page_number: z.number().int(),
});

export const PagesDataShape = z.strictObject({
	edition_date: z.string(),
	pages: z.array(PageShape),
});
