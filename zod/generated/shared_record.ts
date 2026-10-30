// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import {
	ClaimStatusEnum,
	ConfidenceEnum,
	EventPartsEnum,
	EventTypesEnum,
	FactTypesEnum,
	GenderEnum,
	HolderKindEnum,
	LocationTypesEnum,
	NameKindsEnum,
	PrintedCalendarEnum,
	RelationshipTypesEnum,
	SharedFactRepresentationEnum,
	SourcedRelationTypeEnum,
} from './enums';
import { MediaPortraitShape, MediaShape } from './media';
import { PrintedAddressShape } from './site_common';
import {
	AttributionShape,
	FactQualifiersShape,
	FateShape,
	NameShape,
	ReviewShape,
	SourceShape,
	SourcedDateShape,
} from './sourced_entities';

const pattern1 = /\S/;
const pattern2 = /^\d{4}-\d{2}-\d{2}$/;
const pattern3 = /^\d{4}(-\d{2}(-\d{2})?)?$/;
const pattern4 = /^https:\/\/[^\s/?#]+[^\s]*$/;
const pattern5 =
	/^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$/;
const pattern6 = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/;
const pattern7 = /^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/;
const pattern8 = /^[A-Za-z]{4}$/;

export const LifeEventDateShape = z.strictObject({
	printed: z.string().regex(pattern1).nullish(),
	printed_calendar: PrintedCalendarEnum.nullish(),
	qualifier: z.literal('reported_in').optional(),
	record_fact_id: z.string().regex(pattern1).nullish(),
	reported_in: z.string().regex(pattern2).nullish(),
	start: z.string().regex(pattern3).nullish(),
});

export const LifeEventMainPersonShape = z.strictObject({
	part: EventPartsEnum,
	person_id: z.string().regex(pattern1),
});

export const PlaceIdentifierShape = z.strictObject({
	accessed: z.string().regex(pattern2),
	attribution: AttributionShape,
	source_id: z.string().regex(pattern1),
	url: z.url().regex(pattern4).nullish(),
	value: z.string().regex(pattern1),
});

export const SharedEventShape = z.strictObject({
	dates: z.array(LifeEventDateShape).min(1),
	description: z.string().nullish(),
	evidence_basis: z.literal('records_only').optional(),
	id: z.string().regex(pattern1),
	location_id: z.string().regex(pattern1).nullish(),
	main_people: z.array(LifeEventMainPersonShape),
	name: z.string().regex(pattern1),
	proposed_type: z.string().regex(pattern1).nullish(),
	type: EventTypesEnum,
});

export const SharedFamilyShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
});

export const SharedOrganizationShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
});

export const SharedPlaceShape = z.strictObject({
	coordinates: z.array(z.number().min(-180).max(180)).min(2).max(2).nullish(),
	id: z.string().regex(pattern1),
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
	parent_id: z.string().regex(pattern1).nullish(),
	type: LocationTypesEnum,
});

export const SiteCitationShape = z.strictObject({
	accessed: z.string().regex(pattern2).nullish(),
	addresses: z.array(PrintedAddressShape).min(1).nullish(),
	edition_date: z.string().nullish(),
	locator: z.string().regex(pattern1).nullish(),
	note: z.string().nullish(),
	page: z.string().nullish(),
	public_note: z.string().regex(pattern1).nullish(),
	quote: z.string().nullish(),
	quote_language: z.string().regex(pattern5).nullish(),
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

export const SourcedRelationShape = z.strictObject({
	attribution: AttributionShape,
	citations: z.array(SiteCitationShape).min(1),
	date: SourcedDateShape.nullish(),
	event_id: z.string().regex(pattern1).nullish(),
	evidence_confidence: ConfidenceEnum,
	family_id: z.string().regex(pattern1).nullish(),
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
	shown: AttributionShape.nullish(),
	status: ClaimStatusEnum,
	subject_id: z.string().regex(pattern1),
	type: SourcedRelationTypeEnum,
	value: z.string().regex(pattern1).nullish(),
});

export const HolderShape = z.strictObject({
	host: z.string().regex(pattern6).nullish(),
	id: z.string().regex(pattern1),
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
	kind: HolderKindEnum,
	name: z.string().regex(pattern1),
	short_name: z.string().regex(pattern1).nullish(),
});

export const SharedFactShape = z.strictObject({
	attribution: AttributionShape,
	citations: z.array(SiteCitationShape).min(1),
	date: SourcedDateShape.nullish(),
	event_id: z.string().regex(pattern1).nullish(),
	evidence_confidence: ConfidenceEnum,
	family_id: z.string().regex(pattern1).nullish(),
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
	representation: SharedFactRepresentationEnum,
	review: ReviewShape,
	status: ClaimStatusEnum,
	subject_id: z.string().regex(pattern1),
	type: FactTypesEnum,
	value: z.string().regex(pattern1).nullish(),
});

export const SharedNameShape = z.strictObject({
	attribution: AttributionShape.nullish(),
	citations: z.array(SiteCitationShape).nullish(),
	kind: NameKindsEnum,
	lang: z.string().regex(pattern7).nullish(),
	script: z.string().regex(pattern8),
	value: z.string().regex(pattern1),
});

export const SharedPersonShape = z.strictObject({
	fate: FateShape.nullish(),
	gender: GenderEnum,
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(SharedNameShape),
	portrait: MediaPortraitShape.nullish(),
});

export const SharedRecordShape = z.strictObject({
	events: z.array(SharedEventShape),
	facts: z.array(SharedFactShape),
	families: z.array(SharedFamilyShape),
	holders: z.array(HolderShape).nullish(),
	media: z.array(MediaShape).nullish(),
	organizations: z.array(SharedOrganizationShape),
	persons: z.array(SharedPersonShape),
	places: z.array(SharedPlaceShape),
	relations: z.array(SourcedRelationShape),
	sources: z.array(SourceShape),
	version: z.literal('1'),
	vocabulary_version: z.literal('1.3.0'),
});
