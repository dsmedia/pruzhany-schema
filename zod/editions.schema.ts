import { z } from 'zod/v4';

/** ISO date string pattern (YYYY-MM-DD) */
const IsoDateString = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);

export const EditionSchema = z.object({
	date: IsoDateString,
	hebrewDate: z.string(),
	hebrewMonth: z.number().int().min(1).max(13),
	hebrewYear: z.number().int(),
	holiday: z.string().optional(),
});
export type Edition = z.infer<typeof EditionSchema>;

export const HolidaySchema = z.object({
	date: IsoDateString,
	name: z.string(),
	hebrewName: z.string().optional(),
});
export type Holiday = z.infer<typeof HolidaySchema>;

export const HistoricalEventSchema = z.object({
	date: IsoDateString,
	endDate: IsoDateString.optional(),
	name: z.string(),
	description: z.string(),
});
export type HistoricalEvent = z.infer<typeof HistoricalEventSchema>;

export const EditionsCatalogSchema = z.object({
	editions: z.array(EditionSchema),
	holidays: z.array(HolidaySchema),
	historicalEvents: z.array(HistoricalEventSchema),
	availableDates: z.array(IsoDateString),
});
export type EditionsCatalog = z.infer<typeof EditionsCatalogSchema>;
