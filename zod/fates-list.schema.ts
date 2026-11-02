import {
	FatesListAgeShape,
	FatesListArchiveCountShape,
	FatesListCountsShape,
	FatesListDateShape,
	FatesListFateDetailShape,
	FatesListOutsideRecordShape,
	FatesListPersonShape,
	FatesListPieceShape,
	FatesListShape,
} from './generated/fates_list';
import { z } from 'zod/v4';

// The fates list (pruzhany-steps site_writer, static/data/fates-list.json). The generated shapes
// hold every field; the two refinements below are the LinkML rules of FatesListFateDetail and
// FatesListAge, as pydantic/fates_list.py checks them too.
export const FatesListPieceSchema = FatesListPieceShape;
export type FatesListPiece = z.infer<typeof FatesListPieceSchema>;

export const FatesListDateSchema = FatesListDateShape;
export type FatesListDate = z.infer<typeof FatesListDateSchema>;

export const FatesListFateDetailSchema = FatesListFateDetailShape.refine(
	(detail) => detail.place_id != null || detail.date != null,
	{ message: 'a fate detail needs a place_id or a date' }
);
export type FatesListFateDetail = z.infer<typeof FatesListFateDetailSchema>;

export const FatesListOutsideRecordSchema = FatesListOutsideRecordShape;
export type FatesListOutsideRecord = z.infer<typeof FatesListOutsideRecordSchema>;

// Each way of knowing an age, and the fields it needs.
const AGE_NEEDS = {
	birth_year: ['birth_year', 'fact_ids'],
	birth_announced: ['announced'],
	birth_years_disagree: ['birth_years'],
} as const;

export const FatesListAgeSchema = FatesListAgeShape.superRefine((age, context) => {
	for (const name of AGE_NEEDS[age.known_by]) {
		if (age[name] == null) {
			context.addIssue({
				code: 'custom',
				path: [name],
				message: `an age known by ${age.known_by} needs ${name}`,
			});
		}
	}
});
export type FatesListAge = z.infer<typeof FatesListAgeSchema>;

export const FatesListPersonSchema = z.strictObject({
	...FatesListPersonShape.shape,
	fate_details: z.array(FatesListFateDetailSchema).min(1).nullish(),
	age: FatesListAgeSchema.nullish(),
});
export type FatesListPerson = z.infer<typeof FatesListPersonSchema>;

export const FatesListArchiveCountSchema = FatesListArchiveCountShape;
export type FatesListArchiveCount = z.infer<typeof FatesListArchiveCountSchema>;

export const FatesListCountsSchema = FatesListCountsShape;
export type FatesListCounts = z.infer<typeof FatesListCountsSchema>;

export const FatesListSchema = z.strictObject({
	...FatesListShape.shape,
	people: z.array(FatesListPersonSchema),
});
export type FatesList = z.infer<typeof FatesListSchema>;
