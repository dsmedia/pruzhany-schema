// Issue #56's exact optional addition to the immutable migration baseline.
// Zod, Defining schemas (https://zod.dev/api), read 1 November 2026:
// safeExtend preserves refinements; nullish permits absence and explicit null.
import { z } from 'zod/v4';
import * as frozen from './words-english-baseline';
export * from './words-english-baseline';

const language = z
	.string()
	.regex(/^[a-z]{2,3}$(?![\s\S])/)
	.nullish();
export const ContentItemSchema = frozen.ContentItemSchema.safeExtend({ language });
export const ContentItemsDataSchema = frozen.ContentItemsDataSchema.safeExtend({
	content_items: z.array(ContentItemSchema),
});
export const SiteIssueSchema = frozen.SiteIssueSchema.safeExtend({
	content_items: ContentItemsDataSchema,
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	issues: z.array(SiteIssueSchema),
});
