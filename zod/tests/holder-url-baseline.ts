// The holder's optional URI added on 5 November 2026; previous snapshots stay unchanged.
import { z } from 'zod/v4';
import * as frozen from './catalog-keys-baseline';
export * from './catalog-keys-baseline';

const { holder, ...credit } = frozen.PictureSourceSchema.shape;
export const PictureSourceSchema = z.strictObject({
	holder,
	holder_url: z.url().nullish(),
	...credit,
});
export const NewspaperSchema = PictureSourceSchema.extend(frozen.NewspaperSchema.shape);
export const EditionsCatalogSchema = frozen.EditionsCatalogSchema.extend({
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
