import {
	EditionShape,
	HolidayShape,
	HistoricalEventShape,
	EditionsCatalogShape,
	NewspaperShape,
} from './generated/editions';
import { z } from 'zod/v4';

export const NewspaperSchema = NewspaperShape;
export type Newspaper = z.infer<typeof NewspaperSchema>;

// known-looser: these optional keys reject null; retain their generated constraints.
// Today's documents carry extensions; the old shape stripped unknown keys.
export const EditionSchema = z
	.object({
		...EditionShape.shape,
		holiday: EditionShape.shape.holiday.unwrap().unwrap().optional(),
	})
	.superRefine((v, ctx) => {
		// Zod, Defining schemas (https://zod.dev/api), read 2 November 2026.
		if (v.key.slice(-10) !== v.date)
			ctx.addIssue({ code: 'custom', path: ['key'], message: 'edition key must agree with date' });
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
export const EditionsCatalogSchema = z
	.object({
		...EditionsCatalogShape.shape,
		editions: z.array(EditionSchema),
		holidays: z.array(HolidaySchema),
		historicalEvents: z.array(HistoricalEventSchema),
	})
	.superRefine((v, ctx) => {
		// availableDates holds the first paper's dates; the writer publishes every other
		// paper's editions without it (pruzhany-steps publish/site_editions.published_keys),
		// so only the date-only keys are compared with it.
		if (v.availableKeys == null) return;
		const seen = new Set<string>();
		v.availableKeys.forEach((key, i) => {
			if (seen.has(key))
				ctx.addIssue({
					code: 'custom',
					path: ['availableKeys', i],
					message: 'duplicate available key',
				});
			seen.add(key);
		});
		const editions = new Set(v.editions.map((edition) => edition.key));
		v.availableKeys.forEach((key, i) => {
			if (!editions.has(key))
				ctx.addIssue({
					code: 'custom',
					path: ['availableKeys', i],
					message: 'available key names no edition',
				});
		});
		const firstPaper = new Set([...seen].filter((key) => key.length === 10));
		const dates = new Set(v.availableDates);
		if (firstPaper.size !== dates.size || [...dates].some((date) => !firstPaper.has(date)))
			ctx.addIssue({
				code: 'custom',
				path: ['availableKeys'],
				message: 'date-only available keys must equal availableDates',
			});
	})
	.superRefine((v, ctx) => {
		if (v.newspapers == null) return;
		const ids = new Set<string>();
		v.newspapers.forEach((paper, i) => {
			if (ids.has(paper.id))
				ctx.addIssue({
					code: 'custom',
					path: ['newspapers', i, 'id'],
					message: 'duplicate newspaper id',
				});
			ids.add(paper.id);
		});
		v.editions.forEach((edition, i) => {
			if (!ids.has(edition.newspaper))
				ctx.addIssue({
					code: 'custom',
					path: ['editions', i, 'newspaper'],
					message: 'edition newspaper is not listed in newspapers',
				});
		});
	});
export type EditionsCatalog = z.infer<typeof EditionsCatalogSchema>;
