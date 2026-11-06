// The owner's site-content 1.3.0 release, 6 November 2026 (docs/vocabulary-approvals.md):
// exactly fiction appended to the prior migration baseline; earlier baselines stay unchanged.
// As in masthead-imprint-baseline.ts, these four objects have no refinements.
import { z } from 'zod/v4';
import * as frozen from './picture-service-baseline';
export * from './picture-service-baseline';

const priorSubtype = frozen.ContentItemSchema.shape.subtype.unwrap().unwrap();
const subtype = z.enum({ ...priorSubtype.enum, fiction: 'fiction' }).nullish();
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
