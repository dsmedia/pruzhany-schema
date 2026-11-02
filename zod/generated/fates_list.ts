// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';
import {
	AgeKnownByEnum,
	FateDetailKindEnum,
	FatesListConfidenceEnum,
	FatesListOutcomeEnum,
	SourcedDatePrecisionEnum,
} from './enums';

const pattern1 = /\S/;
const pattern2 = /^\d{4}(-\d{2}(-\d{2})?)?$/;
const pattern3 = /^location-[A-Za-z0-9_-]+$/;
const pattern4 = /^https:\/\/[^\s/?#]+[^\s]*$/;
const pattern5 = /^\d{4}-\d{2}-\d{2}$/;
const pattern6 = /^cu-\d{4}-\d{2}-\d{2}-i\d{4}$/;
const pattern7 = /^person-[A-Za-z0-9_-]+$/;

export const FatesListArchiveCountShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	archive: z.string().regex(pattern1),
	people: z.number().int().min(0).max(9007199254740991),
	people_with_address: z.number().int().min(0).max(9007199254740991),
});

export const FatesListCountsShape = z.strictObject({
	people: z.number().int().min(0).max(9007199254740991),
	perished_confirmed: z.number().int().min(0).max(9007199254740991),
	perished_probable: z.number().int().min(0).max(9007199254740991),
	survived_confirmed: z.number().int().min(0).max(9007199254740991),
	survived_probable: z.number().int().min(0).max(9007199254740991),
	children: z.number().int().min(0).max(9007199254740991),
	children_by_birth_year: z.number().int().min(0).max(9007199254740991),
	children_by_announcement: z.number().int().min(0).max(9007199254740991),
	birth_year_known: z.number().int().min(0).max(9007199254740991),
	birth_years_disagree: z.number().int().min(0).max(9007199254740991),
	no_age: z.number().int().min(0).max(9007199254740991),
	with_place: z.number().int().min(0).max(9007199254740991),
	with_date: z.number().int().min(0).max(9007199254740991),
	outside_records: z.array(FatesListArchiveCountShape),
});

export const FatesListDateShape = z.strictObject({
	start: z.string().regex(pattern2),
	precision: SourcedDatePrecisionEnum.nullish(),
	end: z.string().regex(pattern2).nullish(),
});

export const FatesListFateDetailShape = z.strictObject({
	kind: FateDetailKindEnum,
	place_id: z.string().regex(pattern3).nullish(),
	place_name: z.string().regex(pattern1).nullish(),
	date: FatesListDateShape.nullish(),
});

export const FatesListOutsideRecordShape = z.strictObject({
	source_id: z.string().regex(pattern1),
	archive: z.string().regex(pattern1),
	collection: z.string().regex(pattern1),
	record_type: z.string().regex(pattern1).nullish(),
	record_id: z.string().regex(pattern1),
	url: z.string().regex(pattern4).nullish(),
});

export const FatesListPieceShape = z.strictObject({
	edition_date: z.string().regex(pattern5),
	content_item_id: z.string().regex(pattern6),
});

export const FatesListAgeShape = z.strictObject({
	known_by: AgeKnownByEnum,
	child: z.boolean(),
	birth_year: z.number().int().min(1800).max(2100).nullish(),
	birth_years: z.array(z.number().int().min(1800).max(2100)).min(2).nullish(),
	fact_ids: z.array(z.string().regex(pattern1)).min(1).nullish(),
	announced: FatesListPieceShape.nullish(),
});

export const FatesListPersonShape = z.strictObject({
	person_id: z.string().regex(pattern7),
	name: z.string().regex(pattern1),
	printed_name: z.string().regex(pattern1).nullish(),
	outcome: FatesListOutcomeEnum,
	confidence: FatesListConfidenceEnum,
	first_mention: FatesListPieceShape,
	fate_details: z.array(FatesListFateDetailShape).min(1).nullish(),
	outside_records: z.array(FatesListOutsideRecordShape).min(1).nullish(),
	age: FatesListAgeShape.nullish(),
});

export const FatesListShape = z.strictObject({
	people: z.array(FatesListPersonShape),
	counts: FatesListCountsShape,
	notes: z.array(z.string().regex(pattern1)),
});
