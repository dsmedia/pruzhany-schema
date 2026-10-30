// Frozen from main e3e80c1 for ticket 20: shapes only; never import production shapes here.
import { z } from 'zod/v4';
import { siteDay, siteText } from './site-common.schema';
import { SourceLanguageSchema } from './sourced-entities.schema';

import { MEDIA_WIDTH_LIST } from './media-widths.table';
import { MEDIA_RIGHTS, COPYRIGHT_NOT_EVALUATED } from './media-rights.table';
export { MEDIA_RIGHTS, COPYRIGHT_NOT_EVALUATED } from './media-rights.table';

export const MEDIA_WIDTHS: readonly number[] = MEDIA_WIDTH_LIST;
// Local RepresentationType concepts, linked by rico:hasRepresentationType.
export const MediaKindSchema = z.enum(['image', 'audio', 'video', 'document']);
export const MediaDecisionSchema = z.strictObject({
	role: z.enum(['owner', 'project']),
	on: siteDay,
});
export type MediaDecision = z.infer<typeof MediaDecisionSchema>;
export const MediaTextSchema = z.strictObject({
	text: siteText,
	lang: SourceLanguageSchema,
	reviewed: MediaDecisionSchema.nullish(),
});
export type MediaText = z.infer<typeof MediaTextSchema>;
const digest = z.string().regex(/^[0-9a-f]{64}$(?![\s\S])/);
const pixels = z.number().int().positive().max(Number.MAX_SAFE_INTEGER);
const coordinate = z.number().int().nonnegative().max(Number.MAX_SAFE_INTEGER);
export const MediaRegionSchema = z.strictObject({
	x: coordinate,
	y: coordinate,
	w: pixels,
	h: pixels,
});
export type MediaRegion = z.infer<typeof MediaRegionSchema>;
export const MediaDepictedSchema = z.strictObject({
	person_id: siteText.nullable(),
	region: MediaRegionSchema,
	identified_by: z.enum(['family', 'record', 'inscription']),
});
export const MediaPortraitSchema = z.strictObject({
	media_id: siteText,
	region: MediaRegionSchema,
	reviewed: MediaDecisionSchema,
});
export type MediaPortrait = z.infer<typeof MediaPortraitSchema>;
export const MediaWithdrawalSchema = z.strictObject({
	on: siteDay,
	reason: z.enum(['family', 'holder', 'error']),
});
export const MediaConsentScopeSchema = z.strictObject({
	use: z.enum(['site', 'site+download']),
	person_ids: z.array(siteText),
	unidentified: z.boolean(),
});
export const MediaConsentSchema = z.strictObject({
	basis: z.enum([
		'institution-terms',
		'holder-licence',
		'family-permission',
		'public-domain',
		'owner-family-papers',
	]),
	// A role, never a person's name: the private `ref` names the permission document.
	granted_by: z.enum(['owner', 'family', 'holder', 'institution']),
	scope: MediaConsentScopeSchema,
	ref: siteText,
	withdrawn_on: siteDay.nullish(),
});
// A public Citation subset: exact words and their recorded part. No private note or locator.
export const MediaFamilyWordsSchema = z.strictObject({
	source_id: siteText,
	page: siteText,
	quote: siteText,
	quote_language: SourceLanguageSchema,
});
export const MediaFixitySchema = z.strictObject({ on: siteDay, sha256: digest });
export const MediaMasterSchema = z.strictObject({
	bucket: z.string().regex(/^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$(?![\s\S])/),
	key: z.string().regex(/^(?:[a-z0-9_-]+\/)*[0-9a-f]{64}$(?![\s\S])/),
	sha256: digest,
	mime: z.string().regex(/^(?:image|audio|video|application)\/[a-z0-9][a-z0-9.+-]*$(?![\s\S])/),
	bytes: pixels,
	checked: MediaFixitySchema.nullish(),
});
export type MediaMaster = z.infer<typeof MediaMasterSchema>;
export const MediaDerivativeSchema = z.strictObject({
	url: z
		.string()
		.regex(
			new RegExp(
				`^https://pictures\\.pruzhanychronicles\\.org/media/[0-9a-f]{64}-w(?:${MEDIA_WIDTHS.join('|')})\\.webp$(?![\\s\\S])`
			)
		),
	width: pixels,
	height: pixels,
	process: z.literal('resize'),
});
export type MediaDerivative = z.infer<typeof MediaDerivativeSchema>;
const publicFields = z.strictObject({
	id: z.string().regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S])/),
	source_id: siteText,
	kind: MediaKindSchema,
	caption: MediaTextSchema,
	alt: MediaTextSchema.nullish(),
	inscription: MediaTextSchema.nullish(),
	transcript: MediaTextSchema.nullish(),
	family_words: MediaFamilyWordsSchema.nullish(),
	depicted: z.array(MediaDepictedSchema),
	shows_unidentified: z.boolean(),
	width: pixels.nullish(),
	height: pixels.nullish(),
	duration: z.number().positive().nullish(),
	credit: siteText,
	conditions_of_access: siteText.nullish(),
	conditions_of_use: siteText.nullish(),
	rights: z.enum(MEDIA_RIGHTS).default(COPYRIGHT_NOT_EVALUATED).optional(),
	cleared: MediaDecisionSchema.nullish(),
	withdrawn: MediaWithdrawalSchema.nullish(),
	link: z
		.string()
		.regex(/^https:\/\/[a-z0-9]+(?:[.-][a-z0-9]+)*(?:\/[^\s\\]*)?$(?![\s\S])/)
		.nullish(),
	derived: z.array(MediaDerivativeSchema).min(1).nullish(),
});
export const MediaSchema = publicFields.extend({
	master: MediaMasterSchema.nullish(),
	consent: MediaConsentSchema.nullish(),
});
export type Media = z.infer<typeof MediaSchema>;
export const PublicMediaSchema = publicFields;
export type PublicMedia = z.infer<typeof PublicMediaSchema>;
