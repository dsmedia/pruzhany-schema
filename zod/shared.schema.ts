import { ExternalReferenceShape } from './generated/shared';
import { z } from 'zod/v4';

// The vocabulary gate inspects this released enum declaration directly.
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

// Legacy content categories have no owned LinkML class in the current documents.
export const ContentTypeSchema = z.enum([
	'lifecycle_event',
	'community_news',
	'opinion',
	'advertisement',
]);
export type ContentType = z.infer<typeof ContentTypeSchema>;

// The public inferred type requires these optional keys to reject null.
export const ExternalReferenceSchema = ExternalReferenceShape.extend({
	record_id: ExternalReferenceShape.shape.record_id.unwrap().unwrap().optional(),
	notes: ExternalReferenceShape.shape.notes.unwrap().unwrap().optional(),
	verified: ExternalReferenceShape.shape.verified.unwrap().unwrap().optional(),
});
export type ExternalReference = z.infer<typeof ExternalReferenceSchema>;

// Legacy object-valued box has no owned LinkML class (site boxes are tuples).
export const BboxSchema = z.object({
	x: z.number(),
	y: z.number(),
	width: z.number(),
	height: z.number(),
});
export type Bbox = z.infer<typeof BboxSchema>;
