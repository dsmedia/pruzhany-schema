// Generated from LinkML by linkml/generate.py (zod_generator.py). Do not edit.
import { z } from 'zod/v4';

const pattern1 = /^\d{4}-\d{2}-\d{2}$/;
const pattern2 = /\S/;
const pattern3 = /^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])/;
const pattern4 = /^[a-z]+$(?![\s\S])/;

export const EditionShape = z.strictObject({
	date: z.string().regex(pattern1),
	hebrewDate: z.string(),
	hebrewMonth: z.number().int().min(1).max(13),
	hebrewYear: z.number().int().min(-9007199254740991).max(9007199254740991),
	holiday: z.string().nullish(),
	newspaper: z.string().regex(pattern2),
	key: z.string().regex(pattern3),
	object_url: z.url().nullish(),
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

export const NewspaperShape = z.strictObject({
	holder: z.string().regex(pattern2),
	holder_url: z.url().nullish(),
	route: z.string().regex(pattern2).nullish(),
	shelf_mark: z.string().regex(pattern2).nullish(),
	url: z.url().nullish(),
	rights: z.string().regex(pattern2).nullish(),
	rights_url: z.url().nullish(),
	id: z.string().regex(pattern2),
	code: z.string().regex(pattern4),
	title: z.string().regex(pattern2),
});

export const EditionsCatalogShape = z.strictObject({
	editions: z.array(EditionShape),
	holidays: z.array(HolidayShape),
	historicalEvents: z.array(HistoricalEventShape),
	availableDates: z.array(z.string().regex(pattern1)),
	availableKeys: z.array(z.string().regex(pattern3)).nullish(),
	newspapers: z.array(NewspaperShape).nullish(),
});
