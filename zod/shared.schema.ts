import { ExternalReferenceShape } from './generated/shared';
import { z } from 'zod/v4';

// Zod "Defining schemas — .extend(), .safeExtend(), .pick(), .omit()",
// https://zod.dev/api, read 30 October 2026. Order/narrow unrefined generated
// objects first; keep refinements last. A refined base uses safeExtend instead.
// The released JSON exports preserve field order as well as their constraints.
export function withFieldOrder<T extends z.ZodRawShape, C extends z.core.$ZodObjectConfig>(
	schema: z.ZodObject<T, C>,
	fieldOrder: string
): z.ZodObject<T, C> {
	const order = fieldOrder.split(' ');
	if (
		order.length !== Object.keys(schema.shape).length ||
		new Set(order).size !== order.length ||
		order.some((key) => !Object.hasOwn(schema.shape, key))
	)
		throw new Error('field order must name every generated field exactly once');
	return schema.pick(
		Object.fromEntries(order.map((key) => [key, true])) as {
			[K in keyof T]: true;
		} & Record<Exclude<keyof T, keyof T>, never>
	) as z.ZodObject<T, C>;
}

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

export const ContentTypeSchema = z.enum([
	'lifecycle_event',
	'community_news',
	'opinion',
	'advertisement',
]);
export type ContentType = z.infer<typeof ContentTypeSchema>;

export const ExternalReferenceSchema = withFieldOrder(
	ExternalReferenceShape.extend({
		record_id: z.string().optional(),
		notes: z.string().optional(),
		verified: z.boolean().optional(),
	}),
	'source url record_id notes verified'
).strip();
export type ExternalReference = z.infer<typeof ExternalReferenceSchema>;

export const BboxSchema = z.object({
	x: z.number(),
	y: z.number(),
	width: z.number(),
	height: z.number(),
});
export type Bbox = z.infer<typeof BboxSchema>;
