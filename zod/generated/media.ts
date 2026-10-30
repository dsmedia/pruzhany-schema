// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import {
	MediaConsentBasisEnum,
	MediaConsentScopeUseEnum,
	MediaDecisionRoleEnum,
	MediaGrantedByEnum,
	MediaIdentifiedByEnum,
	MediaKindEnum,
	MediaRightsEnum,
	MediaWithdrawalReasonEnum,
} from './enums';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 =
	/^https:\/\/pictures\.pruzhanychronicles\.org\/media\/[0-9a-f]{64}-w(?:100|400|800|1200)\.webp$(?![\s\S])/;
const pattern4 =
	/^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$/;
const pattern5 = /^[0-9a-f]{64}$(?![\s\S])/;
const pattern6 = /^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$(?![\s\S])/;
const pattern7 = /^(?:[a-z0-9_-]+\/)*[0-9a-f]{64}$(?![\s\S])/;
const pattern8 = /^(?:image|audio|video|application)\/[a-z0-9][a-z0-9.+-]*$(?![\s\S])/;
const pattern9 = /^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S])/;
const pattern10 = /^https:\/\/[a-z0-9]+(?:[.-][a-z0-9]+)*(?:\/[^\s\\]*)?$(?![\s\S])/;

export const MediaConsentScopeShape = z.strictObject({
	person_ids: z.array(z.string().regex(pattern1)),
	unidentified: z.boolean(),
	use: MediaConsentScopeUseEnum,
});

export const MediaDecisionShape = z.strictObject({
	on: z.string().regex(pattern2),
	role: MediaDecisionRoleEnum,
});

export const MediaDerivativeShape = z.strictObject({
	height: z.number().int().min(1).max(9007199254740991),
	process: z.literal('resize'),
	url: z.string().regex(pattern3),
	width: z.number().int().min(1).max(9007199254740991),
});

export const MediaFamilyWordsShape = z.strictObject({
	page: z.string().regex(pattern1),
	quote: z.string().regex(pattern1),
	quote_language: z.string().regex(pattern4),
	source_id: z.string().regex(pattern1),
});

export const MediaFixityShape = z.strictObject({
	on: z.string().regex(pattern2),
	sha256: z.string().regex(pattern5),
});

export const MediaMasterShape = z.strictObject({
	bucket: z.string().regex(pattern6),
	bytes: z.number().int().min(1).max(9007199254740991),
	checked: MediaFixityShape.nullish(),
	key: z.string().regex(pattern7),
	mime: z.string().regex(pattern8),
	sha256: z.string().regex(pattern5),
});

export const MediaRegionShape = z.strictObject({
	h: z.number().int().min(1).max(9007199254740991),
	w: z.number().int().min(1).max(9007199254740991),
	x: z.number().int().min(0).max(9007199254740991),
	y: z.number().int().min(0).max(9007199254740991),
});

export const MediaTextShape = z.strictObject({
	lang: z.string().regex(pattern4),
	reviewed: MediaDecisionShape.nullish(),
	text: z.string().regex(pattern1),
});

export const MediaWithdrawalShape = z.strictObject({
	on: z.string().regex(pattern2),
	reason: MediaWithdrawalReasonEnum,
});

export const MediaConsentShape = z.strictObject({
	basis: MediaConsentBasisEnum,
	granted_by: MediaGrantedByEnum,
	ref: z.string().regex(pattern1),
	scope: MediaConsentScopeShape,
	withdrawn_on: z.string().regex(pattern2).nullish(),
});

export const MediaDepictedShape = z.strictObject({
	identified_by: MediaIdentifiedByEnum,
	person_id: z.string().regex(pattern1).nullish(),
	region: MediaRegionShape,
});

export const MediaPortraitShape = z.strictObject({
	media_id: z.string().regex(pattern1),
	region: MediaRegionShape,
	reviewed: MediaDecisionShape,
});

export const PublicMediaShape = z.strictObject({
	alt: MediaTextShape.nullish(),
	caption: MediaTextShape,
	cleared: MediaDecisionShape.nullish(),
	conditions_of_access: z.string().regex(pattern1).nullish(),
	conditions_of_use: z.string().regex(pattern1).nullish(),
	credit: z.string().regex(pattern1),
	depicted: z.array(MediaDepictedShape),
	derived: z.array(MediaDerivativeShape).min(1).nullish(),
	duration: z.number().min(0).nullish(),
	family_words: MediaFamilyWordsShape.nullish(),
	height: z.number().int().min(1).max(9007199254740991).nullish(),
	id: z.string().regex(pattern9),
	inscription: MediaTextShape.nullish(),
	kind: MediaKindEnum,
	link: z.string().regex(pattern10).nullish(),
	rights: MediaRightsEnum.optional(),
	shows_unidentified: z.boolean(),
	source_id: z.string().regex(pattern1),
	transcript: MediaTextShape.nullish(),
	width: z.number().int().min(1).max(9007199254740991).nullish(),
	withdrawn: MediaWithdrawalShape.nullish(),
});

export const MediaShape = z.strictObject({
	alt: MediaTextShape.nullish(),
	caption: MediaTextShape,
	cleared: MediaDecisionShape.nullish(),
	conditions_of_access: z.string().regex(pattern1).nullish(),
	conditions_of_use: z.string().regex(pattern1).nullish(),
	consent: MediaConsentShape.nullish(),
	credit: z.string().regex(pattern1),
	depicted: z.array(MediaDepictedShape),
	derived: z.array(MediaDerivativeShape).min(1).nullish(),
	duration: z.number().min(0).nullish(),
	family_words: MediaFamilyWordsShape.nullish(),
	height: z.number().int().min(1).max(9007199254740991).nullish(),
	id: z.string().regex(pattern9),
	inscription: MediaTextShape.nullish(),
	kind: MediaKindEnum,
	link: z.string().regex(pattern10).nullish(),
	master: MediaMasterShape.nullish(),
	rights: MediaRightsEnum.optional(),
	shows_unidentified: z.boolean(),
	source_id: z.string().regex(pattern1),
	transcript: MediaTextShape.nullish(),
	width: z.number().int().min(1).max(9007199254740991).nullish(),
	withdrawn: MediaWithdrawalShape.nullish(),
});
