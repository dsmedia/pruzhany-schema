// Ticket 03's exact optional additions to the released newspaper baseline.
// Independent shape declarations keep the frozen migration sources unchanged.
import { z } from 'zod/v4';
import * as frozen from './newspaper-baseline';
export * from './newspaper-baseline';

const text = z.string().regex(/\S/);
export const PictureSourceSchema = z.strictObject({
	holder: text,
	route: text.nullish(),
	shelf_mark: text.nullish(),
	url: z.url().nullish(),
});
export const NewspaperSchema = PictureSourceSchema.extend({
	id: text,
	code: z.string().regex(/^[a-z]+$(?![\s\S])/),
	title: text,
	rights: text.nullish(),
	rights_url: z.url().nullish(),
});
export const EditionSchema = frozen.EditionSchema.extend({ object_url: z.url().nullish() });
export const EditionsCatalogSchema = frozen.EditionsCatalogSchema.extend({
	editions: z.array(EditionSchema),
	newspapers: z.array(NewspaperSchema).nullish(),
});
export const PageSchema = frozen.PageSchema.extend({
	picture_source: PictureSourceSchema.nullish(),
});
export const PagesDataSchema = frozen.PagesDataSchema.extend({ pages: z.array(PageSchema) });
export const SiteIssueSchema = frozen.SiteIssueSchema.safeExtend({ pages: PagesDataSchema });
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	issues: z.array(SiteIssueSchema),
});
