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
	description: z.string(),
	endDate: z.string().regex(pattern1).nullish(),
	name: z.string(),
});

export const HolidayShape = z.strictObject({
	date: z.string().regex(pattern1),
	hebrewName: z.string().nullish(),
	name: z.string(),
});

export const EditionsCatalogShape = z.strictObject({
	availableDates: z.array(z.string().regex(pattern1)),
	editions: z.array(EditionShape),
	historicalEvents: z.array(HistoricalEventShape),
	holidays: z.array(HolidayShape),
});
