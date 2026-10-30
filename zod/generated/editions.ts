// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

const pattern1 = /^\d{4}-\d{2}-\d{2}$/;

export const EditionShape = z.strictObject({
	date: z.string().regex(pattern1),
	hebrewDate: z.string(),
	hebrewMonth: z.number().int().min(1).max(13),
	hebrewYear: z.number().int().min(-9007199254740991).max(9007199254740991),
	holiday: z.string().nullish(),
});

export const HistoricalEventShape = z.strictObject({
	date: z.string().regex(pattern1),
	endDate: z.string().regex(pattern1).nullish(),
	name: z.string(),
	description: z.string(),
});

export const HolidayShape = z.strictObject({
	date: z.string().regex(pattern1),
	name: z.string(),
	hebrewName: z.string().nullish(),
});

export const EditionsCatalogShape = z.strictObject({
	editions: z.array(EditionShape),
	holidays: z.array(HolidayShape),
	historicalEvents: z.array(HistoricalEventShape),
	availableDates: z.array(z.string().regex(pattern1)),
});
