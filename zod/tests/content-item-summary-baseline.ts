// The content item's optional summary (openings, approved by the coordinator 2 November 2026):
// exactly that optional key added to the immutable migration baseline, prescribed here
// independently of the generator. Zod 4.3.5 (package.json), Defining schemas
// (https://zod.dev/api), read 2 November 2026: nullish permits absence and explicit null;
// .extend replaces a key and throws only on an object with refinements, and these four have none.
import { z } from 'zod/v4';
import * as frozen from './masthead-imprint-baseline';
export * from './masthead-imprint-baseline';

const nonBlank = z.string().regex(/\S/);
const summary = z
	.strictObject({
		text: nonBlank,
		language: z.literal('en'),
		based_on: z.strictObject({ english_sha256: z.string().regex(/^[0-9a-f]{64}$(?![\s\S])/) }),
		attribution: z.strictObject({
			by: nonBlank,
			on: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
			note: z.string().nullish(),
			kind: z.enum(['model']),
			effort: nonBlank,
			checked_by_person: z.boolean(),
		}),
	})
	.nullish();
export const ContentItemSchema = frozen.ContentItemSchema.extend({ summary });
export const ContentItemsDataSchema = frozen.ContentItemsDataSchema.extend({
	content_items: z.array(ContentItemSchema),
});
export const SiteIssueSchema = frozen.SiteIssueSchema.extend({
	content_items: ContentItemsDataSchema,
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.extend({
	issues: z.array(SiteIssueSchema),
});
