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
	IdentifierTypesEnum,
	LocationTypesEnum,
	NameKindsEnum,
	PrintedCalendarEnum,
	RelationshipTypesEnum,
	SharedFactRepresentationEnum,
	SourcedRelationTypeEnum,
} from './enums';
import { MediaPortraitShape, MediaShape } from './media';
import { AttributionShape, CitedTranslationShape, PrintedAddressShape } from './site_common';
import {
	FactQualifiersShape,
	FateShape,
	NameShape,
	ReviewShape,
	SourceShape,
	SourcedDateShape,
} from './sourced_entities';

const pattern1 = /\S/;
const pattern2 = /^\d{4}(-\d{2}(-\d{2})?)?$/;
const pattern3 = /^\d{4}-\d{2}-\d{2}$/;
const pattern4 = /^https:\/\/[^\s/?#]+[^\s]*$/;
const pattern5 = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$/;
const pattern6 =
	/^(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[A-Za-z]{4,8}(?:-[A-Za-z]{4})?(?:-(?:[A-Za-z]{2}|[0-9]{3}))?(?:-(?:[A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(?:-[0-9A-WY-Za-wy-z](?:-[A-Za-z0-9]{2,8})+)*(?:-[xX](?:-[A-Za-z0-9]{1,8})+)?|[xX](?:-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-(?:[aA][mM][iI]|[bB][nN][nN]|[dD][eE][fF][aA][uU][lL][tT]|[eE][nN][oO][cC][hH][iI][aA][nN]|[hH][aA][kK]|[kK][lL][iI][nN][gG][oO][nN]|[lL][uU][xX]|[mM][iI][nN][gG][oO]|[nN][aA][vV][aA][jJ][oO]|[pP][wW][nN]|[tT][aA][oO]|[tT][aA][yY]|[tT][sS][uU])|[sS][gG][nN]-(?:[bB][eE]-[fF][rR]|[bB][eE]-[nN][lL]|[cC][hH]-[dD][eE])|[aA][rR][tT]-[lL][oO][jJ][bB][aA][nN]|[cC][eE][lL]-[gG][aA][uU][lL][iI][sS][hH]|[nN][oO]-[bB][oO][kK]|[nN][oO]-[nN][yY][nN]|[zZ][hH]-[gG][uU][oO][yY][uU]|[zZ][hH]-[hH][aA][kK][kK][aA]|[zZ][hH]-[mM][iI][nN]|[zZ][hH]-[mM][iI][nN]-[nN][aA][nN]|[zZ][hH]-[xX][iI][aA][nN][gG])$/;
const pattern7 = /^[A-Za-z]{4}$/;
const pattern8 = /^[A-Za-z]{2,8}(-[A-Za-z0-9]{1,8})*$/;

export const LifeEventDateShape = z.strictObject({
	record_fact_id: z.string().regex(pattern1).nullish(),
	printed: z.string().regex(pattern1).nullish(),
	printed_calendar: PrintedCalendarEnum.nullish(),
	start: z.string().regex(pattern2).nullish(),
	qualifier: z.literal('reported_in').optional(),
	reported_in: z.string().regex(pattern3).nullish(),
});

export const LifeEventMainPersonShape = z.strictObject({
	person_id: z.string().regex(pattern1),
	part: EventPartsEnum,
});

export const PlaceIdentifierShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	value: z.string().regex(pattern1),
	url: z.url().regex(pattern4).meta({ format: 'uri' }).nullish(),
	accessed: z.string().regex(pattern3),
	attribution: AttributionShape,
	type: IdentifierTypesEnum.nullish(),
});

export const SharedEventShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	type: EventTypesEnum,
	proposed_type: z.string().regex(pattern1).nullish(),
	main_people: z.array(LifeEventMainPersonShape),
	evidence_basis: z.literal('records_only').optional(),
	dates: z.array(LifeEventDateShape).min(1),
	location_id: z.string().regex(pattern1).nullish(),
	description: z.string().nullish(),
});

export const HolderShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	short_name: z.string().regex(pattern1).nullish(),
	kind: HolderKindEnum,
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
	host: z.string().regex(pattern5).nullish(),
});

export const SiteCitationShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	via: z.string().regex(pattern1).nullish(),
	reference_code: z.string().regex(pattern1).nullish(),
	record_type: z.string().regex(pattern1).nullish(),
	quote_language: z.string().regex(pattern6).nullish(),
	public_note: z.string().regex(pattern1).nullish(),
	locator: z.string().regex(pattern1).nullish(),
	record_id: z.string().nullish(),
	page: z.string().nullish(),
	scan: z.string().nullish(),
	time: z.string().nullish(),
	edition_date: z.string().nullish(),
	unit_id: z.string().nullish(),
	url: z.url().regex(pattern4).meta({ format: 'uri' }).nullish(),
	quote: z.string().nullish(),
	note: z.string().nullish(),
	accessed: z.string().regex(pattern3).nullish(),
	quote_english: CitedTranslationShape.nullish(),
	addresses: z.array(PrintedAddressShape).min(1).nullish(),
});

export const SourcedRelationShape = z.strictObject({
	id: z.string().regex(pattern1),
	type: SourcedRelationTypeEnum,
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
	citations: z.array(SiteCitationShape).min(1),
	evidence_confidence: ConfidenceEnum,
	identity_confidence: ConfidenceEnum,
	status: ClaimStatusEnum,
	review: ReviewShape,
	attribution: AttributionShape,
	subject_id: z.string().regex(pattern1),
	family_id: z.string().regex(pattern1).nullish(),
	shown: AttributionShape.nullish(),
});

export const SharedFactShape = z.strictObject({
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
	citations: z.array(SiteCitationShape).min(1),
	evidence_confidence: ConfidenceEnum,
	identity_confidence: ConfidenceEnum,
	status: ClaimStatusEnum,
	review: ReviewShape,
	attribution: AttributionShape,
	subject_id: z.string().regex(pattern1),
	family_id: z.string().regex(pattern1).nullish(),
	representation: SharedFactRepresentationEnum,
});

export const SharedFamilyShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
});

export const SharedNameShape = z.strictObject({
	value: z.string().regex(pattern1),
	kind: NameKindsEnum,
	script: z.string().regex(pattern7),
	lang: z.string().regex(pattern8).nullish(),
	citations: z.array(SiteCitationShape).nullish(),
	attribution: AttributionShape.nullish(),
});

export const SharedOrganizationShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
});

export const SharedPersonShape = z.strictObject({
	portrait: MediaPortraitShape.nullish(),
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(SharedNameShape),
	gender: GenderEnum,
	fate: FateShape.nullish(),
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
});

export const SharedPlaceShape = z.strictObject({
	id: z.string().regex(pattern1),
	name: z.string().regex(pattern1),
	names: z.array(NameShape),
	type: LocationTypesEnum,
	parent_id: z.string().regex(pattern1).nullish(),
	coordinates: z.array(z.number().min(-180).max(180)).min(2).max(2).nullish(),
	identifiers: z.array(PlaceIdentifierShape).min(1).nullish(),
});

export const SharedRecordShape = z.strictObject({
	version: z.literal('1'),
	vocabulary_version: z.literal('1.3.0'),
	persons: z.array(SharedPersonShape),
	families: z.array(SharedFamilyShape),
	places: z.array(SharedPlaceShape),
	organizations: z.array(SharedOrganizationShape),
	events: z.array(SharedEventShape),
	sources: z.array(SourceShape),
	holders: z.array(HolderShape).nullish(),
	facts: z.array(SharedFactShape),
	relations: z.array(SourcedRelationShape),
	media: z.array(MediaShape).nullish(),
});
