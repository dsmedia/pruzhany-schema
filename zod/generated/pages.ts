// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

export const BlockShape = z.strictObject({
	id: z.string(),
	bbox: z.array(z.number().int().min(0).max(9007199254740991)).min(4).max(4),
	transcription: z.string(),
	confidence: z.number().nullish(),
	image_crop: z.string().nullish(),
	unit_id: z.string().nullish(),
});

export const PageShape = z.strictObject({
	id: z.string(),
	issue_date: z.string(),
	page_number: z.number().int(),
	image_uri: z.string(),
	dimensions: z.array(z.number().int()).min(2).max(2),
	blocks: z.array(BlockShape),
});

export const PagesDataShape = z.strictObject({
	edition_date: z.string(),
	pages: z.array(PageShape),
});
