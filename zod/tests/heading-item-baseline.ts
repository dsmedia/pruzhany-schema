// Site-content 1.4.0, agreed by the data and website lanes on 6 November 2026:
// exactly the optional nullable heading-item reference added to the prior baseline.
// Zod Defining schemas (https://zod.dev/api), read 6 November 2026: nullish permits
// absence and explicit null; these baseline objects have no refinements to preserve.
import { z } from 'zod/v4';
import * as frozen from './fiction-baseline';
export * from './fiction-baseline';

export const PrintedSectionSchema = frozen.PrintedSectionSchema.extend({
	heading_item_id: z.string().nullish(),
});
export const ContentItemsDataSchema = frozen.ContentItemsDataSchema.extend({
	sections: z.array(PrintedSectionSchema),
});
export const SiteIssueSchema = frozen.SiteIssueSchema.extend({
	content_items: ContentItemsDataSchema,
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.extend({
	issues: z.array(SiteIssueSchema),
});
