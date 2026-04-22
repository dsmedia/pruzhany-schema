/**
 * Layer 1: Physical Newspaper Structure
 *
 * Defines the foundational schema for newspaper pages and blocks.
 * Pages represent individual newspaper pages with their metadata and dimensions.
 * Blocks represent physical regions within a page (OCR text blocks with bounding boxes).
 */

import { z } from 'zod/v4';

export const BlockSchema = z.object({
	id: z.string(), // "blk-p4-001"
	bbox: z.tuple([z.number(), z.number(), z.number(), z.number()]), // [x, y, w, h]
	transcription: z.string(),
	confidence: z.number().optional(),
	image_crop: z.string().optional(),
	unit_id: z.string().nullable(), // FK to content unit
});

export const PageSchema = z.object({
	id: z.string(), // "page-1938-12-16-4"
	issue_date: z.string(), // "1938-12-16"
	page_number: z.number(),
	image_uri: z.string(),
	dimensions: z.tuple([z.number(), z.number()]), // [width, height]
	blocks: z.array(BlockSchema),
});

export const PagesDataSchema = z.object({
	edition_date: z.string(),
	pages: z.array(PageSchema),
});

// Type exports
export type Block = z.infer<typeof BlockSchema>;
export type Page = z.infer<typeof PageSchema>;
export type PagesData = z.infer<typeof PagesDataSchema>;
