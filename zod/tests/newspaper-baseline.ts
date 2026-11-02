// Ticket 01's exact additions to the content item summary baseline.
// Zod, Defining schemas (https://zod.dev/api), read 2 November 2026:
// safeExtend retains ancestor refinements; the frozen sources remain untouched.
import { z } from 'zod/v4';
import * as frozen from './content-item-summary-baseline';
export * from './content-item-summary-baseline';

const newspaper = z.string().regex(/\S/);
export const BlockSchema = frozen.BlockSchema.extend({
	id: z.string().regex(/^blk-(?:[a-z]+-)?\d{4}-\d{2}-\d{2}-p\d+-r\d{3}$(?![\s\S])/),
});
export const PageSchema = frozen.PageSchema.extend({
	id: z.string().regex(/^page-(?:[a-z]+-)?\d{4}-\d{2}-\d{2}-\d+$(?![\s\S])/),
	blocks: z.array(BlockSchema),
	newspaper,
});
export const PagesDataSchema = frozen.PagesDataSchema.extend({ pages: z.array(PageSchema) });
export const ContentItemSchema = frozen.ContentItemSchema.safeExtend({
	id: z.string().regex(/^cu-(?:[a-z]+-)?\d{4}-\d{2}-\d{2}-i\d{4}$(?![\s\S])/),
	newspaper,
});
export const ContentItemsDataSchema = frozen.ContentItemsDataSchema.safeExtend({
	content_items: z.array(ContentItemSchema),
});
export const EditionSchema = frozen.EditionSchema.extend({
	newspaper,
	key: z.string().regex(/^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])/),
});
export const EditionsCatalogSchema = frozen.EditionsCatalogSchema.extend({
	editions: z.array(EditionSchema),
});
export const SiteIssueSchema = frozen.SiteIssueSchema.safeExtend({
	pages: PagesDataSchema,
	content_items: ContentItemsDataSchema,
});
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	issues: z.array(SiteIssueSchema),
});
