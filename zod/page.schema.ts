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
// Today's documents carry extensions; the old shape stripped unknown keys.
export const BlockSchema = z.object({
	...BlockShape.shape,
	bbox: z.tuple([boxPixel, boxPixel, boxPixel, boxPixel]),
	// known-looser: optional non-null confidence, required nullable unit_id.
	confidence: BlockShape.shape.confidence.unwrap().unwrap().optional(),
	unit_id: BlockShape.shape.unit_id.unwrap().unwrap().nullable(),
});

// Today's documents carry extensions; the old shape stripped unknown keys.
export const PageSchema = z.object({
	...PageShape.shape,
	dimensions: z.tuple([PageShape.shape.dimensions.element, PageShape.shape.dimensions.element]),
	blocks: z.array(BlockSchema),
});

// Today's documents carry extensions; the old shape stripped unknown keys.
export const PagesDataSchema = z.object({ ...PagesDataShape.shape, pages: z.array(PageSchema) });

// Type exports
export type Block = z.infer<typeof BlockSchema>;
export type Page = z.infer<typeof PageSchema>;
export type PagesData = z.infer<typeof PagesDataSchema>;
