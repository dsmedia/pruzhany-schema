// The owner's site-content 1.2.0 release, 2 November 2026 (docs/vocabulary-approvals.md):
// exactly the masthead and imprint subtypes appended to the immutable migration baseline.
// Zod 4.3.5 (package.json), read in node_modules 2 November 2026: z.enum takes an enum-like
// object, which keeps every frozen value and its order; .extend replaces a key and throws
// only on an object with refinements (v4/core/util.js, extend), and these four have none.
import { z } from 'zod/v4';
import { ContentItemSubtypesSchema } from './frozen/site-content.vocabulary';
import * as frozen from './content-item-language-baseline';
export * from './content-item-language-baseline';

const subtype = z
	.enum({ ...ContentItemSubtypesSchema.enum, masthead: 'masthead', imprint: 'imprint' })
	.nullish();
export const ContentItemSchema = frozen.ContentItemSchema.extend({ subtype });
export const ContentItemsDataSchema = frozen.ContentItemsDataSchema.extend({
	content_items: z.array(ContentItemSchema),
});
export const SiteIssueSchema = frozen.SiteIssueSchema.extend({
	content_items: ContentItemsDataSchema,
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.extend({
	issues: z.array(SiteIssueSchema),
});
