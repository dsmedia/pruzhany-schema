import { withFieldOrder } from './shared.schema';
import {
	EditionShape,
	HolidayShape,
	HistoricalEventShape,
	EditionsCatalogShape,
} from './generated/editions';
import { z } from 'zod/v4';

/** ISO date string pattern (YYYY-MM-DD) */
const IsoDateString = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);

export const EditionSchema = withFieldOrder(
	EditionShape.extend({ holiday: z.string().optional() }),
	'date hebrewDate hebrewMonth hebrewYear holiday'
).strip();
export type Edition = z.infer<typeof EditionSchema>;

export const HolidaySchema = withFieldOrder(
	HolidayShape.extend({ hebrewName: z.string().optional() }),
	'date name hebrewName'
).strip();
export type Holiday = z.infer<typeof HolidaySchema>;

export const HistoricalEventSchema = withFieldOrder(
	HistoricalEventShape.extend({ endDate: IsoDateString.optional() }),
	'date endDate name description'
).strip();
export type HistoricalEvent = z.infer<typeof HistoricalEventSchema>;

export const EditionsCatalogSchema = withFieldOrder(
	EditionsCatalogShape.extend({
		editions: z.array(EditionSchema),
		holidays: z.array(HolidaySchema),
		historicalEvents: z.array(HistoricalEventSchema),
	}),
	'editions holidays historicalEvents availableDates'
).strip();
export type EditionsCatalog = z.infer<typeof EditionsCatalogSchema>;
