// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import {
	ClaimStatusEnum,
	ConfidenceEnum,
	FactTypesEnum,
	FateOutcomesEnum,
	MentionRolesEnum,
	NameKindsEnum,
	PrintedCalendarEnum,
	RelationshipTypesEnum,
	ReviewStatesEnum,
	SourceDerivationRelationEnum,
	SourceKindsEnum,
	SourceMadeByEnum,
	SourceQuoteConditionEnum,
	SourcedDatePrecisionEnum,
} from './enums';
import { AttributionShape, CitedTranslationShape } from './site_common';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 = /^\d{4}(-\d{2}(-\d{2})?)?$/;
const pattern4 =
	/^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$/;
const pattern5 = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/;
const pattern6 = /^https:\/\/[^\s/?#]+[^\s]*$/;
const pattern7 = /^[A-Za-z]{4}$/;
const pattern8 = /^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/;

export const FactQualifiersShape = z.record(z.string(), z.string());

export const MentionShape = z.strictObject({
	id: z.string().regex(pattern1),
	person_id: z.string().regex(pattern1),
	unit_id: z.string().regex(pattern1),
	printed_name: z.string().regex(pattern1),
	role: MentionRolesEnum.nullish(),
	title: z.string().nullish(),
	function: z.string().nullish(),
	wkd_id: z.string().nullish(),
});

export const ReviewShape = z.strictObject({
	state: ReviewStatesEnum,
	by: z.string().regex(pattern1).nullish(),
	on: z.string().regex(pattern2).nullish(),
});

export const SourceDerivationShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	relation: SourceDerivationRelationEnum,
});

export const SourcedDateShape = z.strictObject({
	start: z.string().regex(pattern3).nullish(),
	end: z.string().regex(pattern3).nullish(),
	precision: SourcedDatePrecisionEnum.nullish(),
	printed: z.string().regex(pattern1).nullish(),
	printed_calendar: PrintedCalendarEnum.nullish(),
	inferred: z.boolean().nullish(),
});

export const FateShape = z.strictObject({
	outcome: FateOutcomesEnum,
	confidence: ConfidenceEnum,
	rests_on: z.array(z.string()),
	review: ReviewShape,
	summary: z.string().nullish(),
});

export const SourceShape = z.strictObject({
	made_by: SourceMadeByEnum.nullish(),
	id: z.string().regex(pattern1),
	kind: SourceKindsEnum,
	title: z.string().regex(pattern1),
	short_name: z.string().regex(pattern1).nullish(),
	holder_id: z.string().regex(pattern1).nullish(),
	reference_code: z.string().regex(pattern1).nullish(),
	language: z.array(z.string().regex(pattern4)).min(1).nullish(),
	derived_from: z.array(SourceDerivationShape).min(1).nullish(),
	dated: SourcedDateShape.nullish(),
	quotes_cleared: AttributionShape.nullish(),
	quote_condition: SourceQuoteConditionEnum.nullish(),
	private: z.boolean().nullish(),
	work_id: z.string().nullish(),
	author: z.string().nullish(),
	editor: z.string().nullish(),
	published: z.string().nullish(),
	repository: z.string().nullish(),
	url_pattern: z.string().nullish(),
	host: z.string().regex(pattern5).nullish(),
	subjects: z.array(z.string().regex(pattern1)).min(1).nullish(),
	title_english: CitedTranslationShape.nullish(),
});

export const CitationShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	via: z.string().regex(pattern1).nullish(),
	reference_code: z.string().regex(pattern1).nullish(),
	record_type: z.string().regex(pattern1).nullish(),
	quote_language: z.string().regex(pattern4).nullish(),
	public_note: z.string().regex(pattern1).nullish(),
	locator: z.string().regex(pattern1).nullish(),
	record_id: z.string().nullish(),
	page: z.string().nullish(),
	scan: z.string().nullish(),
	time: z.string().nullish(),
	edition_date: z.string().nullish(),
	unit_id: z.string().nullish(),
	url: z.url().regex(pattern6).meta({ format: 'uri' }).nullish(),
	quote: z.string().nullish(),
	note: z.string().nullish(),
	accessed: z.string().regex(pattern2).nullish(),
	quote_english: CitedTranslationShape.nullish(),
});

export const FactShape = z.strictObject({
	id: z.string().regex(pattern1),
	type: FactTypesEnum,
	proposed_type: z.string().regex(pattern1).nullish(),
	value: z.string().regex(pattern1).nullish(),
	date: SourcedDateShape.nullish(),
	place_id: z.string().regex(pattern1).nullish(),
	organization_id: z.string().regex(pattern1).nullish(),
	event_id: z.string().regex(pattern1).nullish(),
	related_person_id: z.string().regex(pattern1).nullish(),
	relationship_type: RelationshipTypesEnum.nullish(),
	related_name: z.string().regex(pattern1).nullish(),
	qualifiers: FactQualifiersShape.nullish(),
	holocaust_related: z.boolean().nullish(),
	citations: z.array(CitationShape).min(1),
	evidence_confidence: ConfidenceEnum,
	identity_confidence: ConfidenceEnum,
	status: ClaimStatusEnum,
	review: ReviewShape,
	attribution: AttributionShape,
});

export const NameShape = z.strictObject({
	value: z.string().regex(pattern1),
	kind: NameKindsEnum,
	script: z.string().regex(pattern7),
	lang: z.string().regex(pattern8).nullish(),
	citations: z.array(CitationShape).nullish(),
	attribution: AttributionShape.nullish(),
});
