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
	use: MediaConsentScopeUseEnum,
	person_ids: z.array(z.string().regex(pattern1)),
	unidentified: z.boolean(),
});

export const MediaDecisionShape = z.strictObject({
	role: MediaDecisionRoleEnum,
	on: z.string().regex(pattern2),
});

export const MediaDerivativeShape = z.strictObject({
	url: z.string().regex(pattern3),
	width: z.number().int().min(1).max(9007199254740991),
	height: z.number().int().min(1).max(9007199254740991),
	process: z.literal('resize'),
});

export const MediaFamilyWordsShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	page: z.string().regex(pattern1),
	quote: z.string().regex(pattern1),
	quote_language: z.string().regex(pattern4),
});

export const MediaFixityShape = z.strictObject({
	on: z.string().regex(pattern2),
	sha256: z.string().regex(pattern5),
});

export const MediaMasterShape = z.strictObject({
	bucket: z.string().regex(pattern6),
	key: z.string().regex(pattern7),
	sha256: z.string().regex(pattern5),
	mime: z.string().regex(pattern8),
	bytes: z.number().int().min(1).max(9007199254740991),
	checked: MediaFixityShape.nullish(),
});

export const MediaRegionShape = z.strictObject({
	x: z.number().int().min(0).max(9007199254740991),
	y: z.number().int().min(0).max(9007199254740991),
	w: z.number().int().min(1).max(9007199254740991),
	h: z.number().int().min(1).max(9007199254740991),
});

export const MediaTextShape = z.strictObject({
	text: z.string().regex(pattern1),
	lang: z.string().regex(pattern4),
	reviewed: MediaDecisionShape.nullish(),
});

export const MediaWithdrawalShape = z.strictObject({
	on: z.string().regex(pattern2),
	reason: MediaWithdrawalReasonEnum,
});

export const MediaConsentShape = z.strictObject({
	basis: MediaConsentBasisEnum,
	granted_by: MediaGrantedByEnum,
	scope: MediaConsentScopeShape,
	ref: z.string().regex(pattern1),
	withdrawn_on: z.string().regex(pattern2).nullish(),
});

export const MediaDepictedShape = z.strictObject({
	person_id: z.string().regex(pattern1).nullish(),
	region: MediaRegionShape,
	identified_by: MediaIdentifiedByEnum,
});

export const MediaPortraitShape = z.strictObject({
	media_id: z.string().regex(pattern1),
	region: MediaRegionShape,
	reviewed: MediaDecisionShape,
});

export const PublicMediaShape = z.strictObject({
	id: z.string().regex(pattern9),
	source_id: z.string().regex(pattern1),
	kind: MediaKindEnum,
	caption: MediaTextShape,
	alt: MediaTextShape.nullish(),
	inscription: MediaTextShape.nullish(),
	transcript: MediaTextShape.nullish(),
	family_words: MediaFamilyWordsShape.nullish(),
	depicted: z.array(MediaDepictedShape),
	shows_unidentified: z.boolean(),
	width: z.number().int().min(1).max(9007199254740991).nullish(),
	height: z.number().int().min(1).max(9007199254740991).nullish(),
	duration: z.number().min(0).nullish(),
	credit: z.string().regex(pattern1),
	conditions_of_access: z.string().regex(pattern1).nullish(),
	conditions_of_use: z.string().regex(pattern1).nullish(),
	rights: MediaRightsEnum.optional(),
	cleared: MediaDecisionShape.nullish(),
	withdrawn: MediaWithdrawalShape.nullish(),
	link: z.string().regex(pattern10).nullish(),
	derived: z.array(MediaDerivativeShape).min(1).nullish(),
});

export const MediaShape = z.strictObject({
	id: z.string().regex(pattern9),
	source_id: z.string().regex(pattern1),
	kind: MediaKindEnum,
	caption: MediaTextShape,
	alt: MediaTextShape.nullish(),
	inscription: MediaTextShape.nullish(),
	transcript: MediaTextShape.nullish(),
	family_words: MediaFamilyWordsShape.nullish(),
	depicted: z.array(MediaDepictedShape),
	shows_unidentified: z.boolean(),
	width: z.number().int().min(1).max(9007199254740991).nullish(),
	height: z.number().int().min(1).max(9007199254740991).nullish(),
	duration: z.number().min(0).nullish(),
	credit: z.string().regex(pattern1),
	conditions_of_access: z.string().regex(pattern1).nullish(),
	conditions_of_use: z.string().regex(pattern1).nullish(),
	rights: MediaRightsEnum.optional(),
	cleared: MediaDecisionShape.nullish(),
	withdrawn: MediaWithdrawalShape.nullish(),
	link: z.string().regex(pattern10).nullish(),
	derived: z.array(MediaDerivativeShape).min(1).nullish(),
	master: MediaMasterShape.nullish(),
	consent: MediaConsentShape.nullish(),
});
