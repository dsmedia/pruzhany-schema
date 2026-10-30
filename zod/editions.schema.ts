import {
	EditionShape,
	HolidayShape,
	HistoricalEventShape,
	EditionsCatalogShape,
} from './generated/editions';
import { z } from 'zod/v4';

// known-looser: these optional keys reject null; retain their generated constraints.
// Today's documents carry extensions; the old shape stripped unknown keys.
export const EditionSchema = z.object({
	...EditionShape.shape,
	holiday: EditionShape.shape.holiday.unwrap().unwrap().optional(),
});
export type Edition = z.infer<typeof EditionSchema>;

// Today's documents carry extensions; the old shape stripped unknown keys.
export const HolidaySchema = z.object({
	...HolidayShape.shape,
	hebrewName: HolidayShape.shape.hebrewName.unwrap().unwrap().optional(),
});
export type Holiday = z.infer<typeof HolidaySchema>;

// Today's documents carry extensions; the old shape stripped unknown keys.
export const HistoricalEventSchema = z.object({
	...HistoricalEventShape.shape,
	endDate: HistoricalEventShape.shape.endDate.unwrap().unwrap().optional(),
});
export type HistoricalEvent = z.infer<typeof HistoricalEventSchema>;

// Today's documents carry extensions; the old shape stripped unknown keys.
export const EditionsCatalogSchema = z.object({
	...EditionsCatalogShape.shape,
	editions: z.array(EditionSchema),
	holidays: z.array(HolidaySchema),
	historicalEvents: z.array(HistoricalEventSchema),
});
export type EditionsCatalog = z.infer<typeof EditionsCatalogSchema>;
