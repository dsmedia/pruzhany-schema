/**
 * Layer 2: Content Units Schema
 *
 * Defines logical editorial units extracted from newspaper pages.
 * Content Units represent coherent editorial objects (articles, notices, ads, etc.)
 * that may span multiple physical blocks on the page.
 */

import { z } from 'zod/v4';

export const PageBlockRefSchema = z.object({
	page_id: z.string(),
	block_ids: z.array(z.string()),
});

export const CrossReferenceSchema = z.object({
	target_id: z.string(),
	confidence: z.number(),
	relationship: z.string(),
	evidence: z.string(),
});

export const ContentUnitTypeSchema = z
	.enum(['article', 'notice', 'ad', 'congratulation', 'obituary', 'other'])
	.meta({
		description: [
			'article: editorial content, news, opinion, event coverage.',
			'notice: announcements, public notices, official statements.',
			'ad: commercial advertisements.',
			'congratulation: primary announcements AND individual mazel tov messages when they appear as a group for the same event (weddings, births).',
			'obituary: death notices, memorial tributes.',
			'other: masthead, structural content.',
		].join(' '),
	});

export const ContentUnitSchema = z.object({
	id: z.string(), // "cu-ball-announcement"
	type: ContentUnitTypeSchema,
	title: z.string().nullable(),
	category: z.string().nullable(),

	// Text
	full_text: z.string(),
	english_translation: z.string().nullable(),
	block_breaks: z.array(z.number()), // Offsets where blocks join

	// Physical references
	page_blocks: z.array(PageBlockRefSchema),

	// Enrichment references
	person_ids: z.array(z.string()),
	location_ids: z.array(z.string()),
	cross_references: z.array(CrossReferenceSchema),

	// Parent event (optional)
	event_id: z.string().nullable(),
});

export const ContentUnitsDataSchema = z.object({
	edition_date: z.string(),
	content_units: z.array(ContentUnitSchema),
});

// Type exports
export type PageBlockRef = z.infer<typeof PageBlockRefSchema>;
export type CrossReference = z.infer<typeof CrossReferenceSchema>;
export type ContentUnit = z.infer<typeof ContentUnitSchema>;
export type ContentUnitsData = z.infer<typeof ContentUnitsDataSchema>;
