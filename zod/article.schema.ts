import { z } from 'zod/v4';
import { BboxSchema } from './shared.schema';

// Cross reference between articles
const CrossReferenceSchema = z.object({
	target_id: z.number(),
	confidence: z.number(),
	relationship: z.string(),
	evidence: z.string(),
});

// Masked region (for OCR exclusion)
const MaskedRegionSchema = z.object({
	x: z.number(),
	y: z.number(),
	width: z.number(),
	height: z.number(),
});

// Article schema matching JSON structure
export const ArticleSchema = z.object({
	annotation_id: z.number(),
	page_number: z.number(),
	page_oid: z.string(),
	bbox: BboxSchema,
	masked_regions: z.array(MaskedRegionSchema),
	image_file: z.string(),
	visual_reasoning: z.string(),
	confidence: z.number(),
	cross_references: z.array(CrossReferenceSchema),
	cluster_ids: z.array(z.union([z.string(), z.number()])),
	preliminary_transcription: z.string(),
	preliminary_english_translation: z.string(),
	category: z.string(),
	content_summary: z.string(),
});
export type Article = z.infer<typeof ArticleSchema>;

// Top-level article data wrapper
export const ArticleDataSchema = z.object({
	edition_date: z.string(),
	run_id: z.string(),
	model: z.string(),
	article_count: z.number(),
	articles: z.array(ArticleSchema),
});
export type ArticleData = z.infer<typeof ArticleDataSchema>;
