/**
 * Layer 3: Life Events Schema
 *
 * Defines the structure for Life Events - groups of related content units
 * representing real-world events (weddings, celebrations, births, deaths, etc.)
 * that occurred in the community described by the newspaper.
 *
 * Layer hierarchy:
 * - Layer 1: Pages/Blocks (physical structure + OCR)
 * - Layer 2: Content Units (editorial groupings)
 * - Layer 3: Life Events (groups of related content units)
 */

import { z } from 'zod/v4';

export const ContentUnitRefSchema = z.object({
	unit_id: z.string(),
	role: z.enum(['primary_announcement', 'congratulation', 'mention', 'advertisement']),
});

export const LifeEventSchema = z.object({
	id: z.string(), // "evt-wedding-pomerantz-shor"
	type: z.enum([
		'wedding',
		'birth',
		'death',
		'bar_mitzvah',
		'celebration',
		'community_event',
		'other',
	]),
	name: z.string(), // Display name

	// Principals
	principal_ids: z.array(z.string()), // Person IDs

	// Timing
	date_hebrew: z.string().nullable(),
	date_gregorian: z.string().nullable(), // ISO format

	// Location
	location_id: z.string().nullable(),

	// Content references
	content_units: z.array(ContentUnitRefSchema),

	// Notes
	description: z.string().nullable(),
});

export const LifeEventsDataSchema = z.object({
	edition_date: z.string(),
	life_events: z.array(LifeEventSchema),
});

// Type exports
export type ContentUnitRef = z.infer<typeof ContentUnitRefSchema>;
export type LifeEvent = z.infer<typeof LifeEventSchema>;
export type LifeEventsData = z.infer<typeof LifeEventsDataSchema>;
