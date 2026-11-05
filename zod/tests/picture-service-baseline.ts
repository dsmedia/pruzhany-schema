// Picture-source rights and the optional holder's service, 5 November 2026.
// Preserve the earlier baselines and prescribe only these additions/inheritance.
import { z } from 'zod/v4';
import * as frozen from './holder-url-baseline';
export * from './holder-url-baseline';

export const PictureSourceSchema = frozen.PictureSourceSchema.extend({
	rights: frozen.NewspaperSchema.shape.rights,
	rights_url: frozen.NewspaperSchema.shape.rights_url,
});
export const NewspaperSchema = PictureSourceSchema.extend(
	frozen.NewspaperSchema.pick({ id: true, code: true, title: true }).shape
);
export const EditionsCatalogSchema = frozen.EditionsCatalogSchema.extend({
	newspapers: z.array(NewspaperSchema).nullish(),
});
export const PageSchema = frozen.PageSchema.extend({
	picture_source: PictureSourceSchema.nullish(),
	image_service: z.url().nullish(),
});
export const PagesDataSchema = frozen.PagesDataSchema.extend({ pages: z.array(PageSchema) });
export const SiteIssueSchema = frozen.SiteIssueSchema.safeExtend({ pages: PagesDataSchema });
export const SiteArchiveSchema = frozen.SiteArchiveSchema.safeExtend({
	issues: z.array(SiteIssueSchema),
});
