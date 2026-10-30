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

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 =
	/^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$/;
const pattern4 = /^https:\/\/[^\s/?#]+[^\s]*$/;
const pattern5 = /^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/;
const pattern6 = /^[A-Za-z]{4}$/;
const pattern7 = /^\d{4}(-\d{2}(-\d{2})?)?$/;
const pattern8 = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/;

export const AttributionShape = z.strictObject({
	by: z.string().regex(pattern1),
	note: z.string().nullish(),
	on: z.string().regex(pattern2),
});

export const CitationShape = z.strictObject({
	accessed: z.string().regex(pattern2).nullish(),
	edition_date: z.string().nullish(),
	locator: z.string().regex(pattern1).nullish(),
	note: z.string().nullish(),
	page: z.string().nullish(),
	public_note: z.string().regex(pattern1).nullish(),
	quote: z.string().nullish(),
	quote_language: z.string().regex(pattern3).nullish(),
	record_id: z.string().nullish(),
	record_type: z.string().regex(pattern1).nullish(),
	reference_code: z.string().regex(pattern1).nullish(),
	scan: z.string().nullish(),
	source_id: z.string().regex(pattern1),
	time: z.string().nullish(),
	unit_id: z.string().nullish(),
	url: z.url().regex(pattern4).nullish(),
	via: z.string().regex(pattern1).nullish(),
});

export const FactQualifiersShape = z.record(z.string(), z.string());

export const MentionShape = z.strictObject({
	function: z.string().nullish(),
	id: z.string().regex(pattern1),
	person_id: z.string().regex(pattern1),
	printed_name: z.string().regex(pattern1),
	role: MentionRolesEnum.nullish(),
	title: z.string().nullish(),
	unit_id: z.string().regex(pattern1),
	wkd_id: z.string().nullish(),
});

export const NameShape = z.strictObject({
	attribution: AttributionShape.nullish(),
	citations: z.array(CitationShape).nullish(),
	kind: NameKindsEnum,
	lang: z.string().regex(pattern5).nullish(),
	script: z.string().regex(pattern6),
	value: z.string().regex(pattern1),
});

export const ReviewShape = z.strictObject({
	by: z.string().regex(pattern1).nullish(),
	on: z.string().regex(pattern2).nullish(),
	state: ReviewStatesEnum,
});

export const SourceDerivationShape = z.strictObject({
	relation: SourceDerivationRelationEnum,
	source_id: z.string().regex(pattern1),
});

export const SourcedDateShape = z.strictObject({
	end: z.string().regex(pattern7).nullish(),
	inferred: z.boolean().nullish(),
	precision: SourcedDatePrecisionEnum.nullish(),
	printed: z.string().regex(pattern1).nullish(),
	printed_calendar: PrintedCalendarEnum.nullish(),
	start: z.string().regex(pattern7).nullish(),
});

export const FactShape = z.strictObject({
	attribution: AttributionShape,
	citations: z.array(CitationShape).min(1),
	date: SourcedDateShape.nullish(),
	event_id: z.string().regex(pattern1).nullish(),
	evidence_confidence: ConfidenceEnum,
	holocaust_related: z.boolean().nullish(),
	id: z.string().regex(pattern1),
	identity_confidence: ConfidenceEnum,
	organization_id: z.string().regex(pattern1).nullish(),
	place_id: z.string().regex(pattern1).nullish(),
	proposed_type: z.string().regex(pattern1).nullish(),
	qualifiers: FactQualifiersShape.nullish(),
	related_name: z.string().regex(pattern1).nullish(),
	related_person_id: z.string().regex(pattern1).nullish(),
	relationship_type: RelationshipTypesEnum.nullish(),
	review: ReviewShape,
	status: ClaimStatusEnum,
	type: FactTypesEnum,
	value: z.string().regex(pattern1).nullish(),
});

export const FateShape = z.strictObject({
	confidence: ConfidenceEnum,
	outcome: FateOutcomesEnum,
	rests_on: z.array(z.string()),
	review: ReviewShape,
	summary: z.string().nullish(),
});

export const SourceShape = z.strictObject({
	author: z.string().nullish(),
	dated: SourcedDateShape.nullish(),
	derived_from: z.array(SourceDerivationShape).min(1).nullish(),
	editor: z.string().nullish(),
	holder_id: z.string().regex(pattern1).nullish(),
	host: z.string().regex(pattern8).nullish(),
	id: z.string().regex(pattern1),
	kind: SourceKindsEnum,
	language: z.array(z.string().regex(pattern3)).min(1).nullish(),
	made_by: SourceMadeByEnum.nullish(),
	private: z.boolean().nullish(),
	published: z.string().nullish(),
	quote_condition: SourceQuoteConditionEnum.nullish(),
	quotes_cleared: AttributionShape.nullish(),
	reference_code: z.string().regex(pattern1).nullish(),
	repository: z.string().nullish(),
	short_name: z.string().regex(pattern1).nullish(),
	subjects: z.array(z.string().regex(pattern1)).min(1).nullish(),
	title: z.string().regex(pattern1),
	url_pattern: z.string().nullish(),
	work_id: z.string().nullish(),
});
