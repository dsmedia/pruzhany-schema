import { z } from 'zod/v4';

export const HolocaustFateSchema = z.enum([
	'unknown',
	'perished',
	'likely_perished',
	'survived',
	'likely_survived',
	'died_before',
	'not_applicable',
]);
export type HolocaustFate = z.infer<typeof HolocaustFateSchema>;

export const ContentTypeSchema = z.enum([
	'lifecycle_event',
	'community_news',
	'opinion',
	'advertisement',
]);
export type ContentType = z.infer<typeof ContentTypeSchema>;

export const ExternalReferenceSchema = z.object({
	source: z.string(),
	url: z.string().optional(),
	record_id: z.string().optional(),
	notes: z.string().optional(),
});
export type ExternalReference = z.infer<typeof ExternalReferenceSchema>;

export const BboxSchema = z.object({
	x: z.number(),
	y: z.number(),
	width: z.number(),
	height: z.number(),
});
export type Bbox = z.infer<typeof BboxSchema>;
