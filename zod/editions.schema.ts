import {
	EditionShape,
	HolidayShape,
	HistoricalEventShape,
	EditionsCatalogShape,
} from './generated/editions';
import { z } from 'zod/v4';

// known-looser: these optional keys reject null; retain their generated constraints.
export const EditionSchema = EditionShape.extend({
	holiday: EditionShape.shape.holiday.unwrap().unwrap().optional(),
});
export type Edition = z.infer<typeof EditionSchema>;

export const HolidaySchema = HolidayShape.extend({
	hebrewName: HolidayShape.shape.hebrewName.unwrap().unwrap().optional(),
});
export type Holiday = z.infer<typeof HolidaySchema>;

export const HistoricalEventSchema = HistoricalEventShape.extend({
	endDate: HistoricalEventShape.shape.endDate.unwrap().unwrap().optional(),
});
export type HistoricalEvent = z.infer<typeof HistoricalEventSchema>;

export const EditionsCatalogSchema = EditionsCatalogShape.extend({
	editions: z.array(EditionSchema),
	holidays: z.array(HolidaySchema),
	historicalEvents: z.array(HistoricalEventSchema),
});
export type EditionsCatalog = z.infer<typeof EditionsCatalogSchema>;
