import { BlockShape, PageShape, PagesDataShape } from './generated/pages';
/**
 * Physical Newspaper Structure
 *
 * Defines the foundational schema for newspaper pages and blocks.
 * Pages represent individual newspaper pages with their metadata and dimensions.
 * Blocks represent physical regions within a page (OCR text blocks with bounding boxes).
 */

import { z } from 'zod/v4';

// Tuples preserve the public inferred type; their elements keep LinkML's bounds.
const boxPixel = BlockShape.shape.bbox.element;
export const BlockSchema = BlockShape.extend({
	bbox: z.tuple([boxPixel, boxPixel, boxPixel, boxPixel]),
	// known-looser: optional non-null confidence, required nullable unit_id.
	confidence: BlockShape.shape.confidence.unwrap().unwrap().optional(),
	unit_id: BlockShape.shape.unit_id.unwrap().unwrap().nullable(),
});

export const PageSchema = PageShape.extend({
	dimensions: z.tuple([PageShape.shape.dimensions.element, PageShape.shape.dimensions.element]),
	blocks: z.array(BlockSchema),
});

export const PagesDataSchema = PagesDataShape.extend({ pages: z.array(PageSchema) });

// Type exports
export type Block = z.infer<typeof BlockSchema>;
export type Page = z.infer<typeof PageSchema>;
export type PagesData = z.infer<typeof PagesDataSchema>;
