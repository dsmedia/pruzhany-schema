import { withFieldOrder } from './shared.schema';
import { BlockShape, PageShape, PagesDataShape } from './generated/pages';
/**
 * Physical Newspaper Structure
 *
 * Defines the foundational schema for newspaper pages and blocks.
 * Pages represent individual newspaper pages with their metadata and dimensions.
 * Blocks represent physical regions within a page (OCR text blocks with bounding boxes).
 */

import { z } from 'zod/v4';

export const BlockSchema = withFieldOrder(
	BlockShape.extend({
		bbox: z.tuple([z.number(), z.number(), z.number(), z.number()]),
		confidence: z.number().optional(),
		unit_id: z.string().nullable(),
	}),
	'id bbox transcription confidence image_crop unit_id'
).strip();

export const PageSchema = withFieldOrder(
	PageShape.extend({
		page_number: z.number(),
		dimensions: z.tuple([z.number(), z.number()]),
		blocks: z.array(BlockSchema),
	}),
	'id issue_date page_number image_uri dimensions blocks'
).strip();

export const PagesDataSchema = withFieldOrder(
	PagesDataShape.extend({ pages: z.array(PageSchema) }),
	'edition_date pages'
).strip();

// Type exports
export type Block = z.infer<typeof BlockSchema>;
export type Page = z.infer<typeof PageSchema>;
export type PagesData = z.infer<typeof PagesDataSchema>;
