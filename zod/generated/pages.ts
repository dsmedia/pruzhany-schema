// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import { PictureSourceShape } from './picture_source';

const pattern1 = /^blk-(?:[a-z]+-)?\d{4}-\d{2}-\d{2}-p\d+-r\d{3}$(?![\s\S])/;
const pattern2 = /^page-(?:[a-z]+-)?\d{4}-\d{2}-\d{2}-\d+$(?![\s\S])/;
const pattern3 = /\S/;

export const BlockShape = z.strictObject({
	id: z.string().regex(pattern1),
	bbox: z.array(z.number().int().min(0).max(9007199254740991)).min(4).max(4),
	transcription: z.string(),
	confidence: z.number().nullish(),
	image_crop: z.string().nullish(),
	unit_id: z.string().nullish(),
});

export const PageShape = z.strictObject({
	id: z.string().regex(pattern2),
	issue_date: z.string(),
	page_number: z.number().int(),
	image_uri: z.string(),
	dimensions: z.array(z.number().int()).min(2).max(2),
	blocks: z.array(BlockShape),
	newspaper: z.string().regex(pattern3),
	picture_source: PictureSourceShape.nullish(),
});

export const PagesDataShape = z.strictObject({
	edition_date: z.string(),
	pages: z.array(PageShape),
});
