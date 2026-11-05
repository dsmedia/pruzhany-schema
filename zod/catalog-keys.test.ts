import { expect, it } from 'vitest';
import { EditionsCatalogSchema, FatesListPieceSchema } from './index';

// Entirely fictional: an unprefixed first paper and abcd, a second, on one day and apart.
const edition = (date: string, newspaper: string, key: string) => ({
	date,
	hebrewDate: 'Fictional date',
	hebrewMonth: 1,
	hebrewYear: 5761,
	newspaper,
	key,
});
const catalog = {
	editions: [
		edition('2001-02-03', 'fictional-first-paper', '2001-02-03'),
		edition('2001-02-03', 'fictional-second-paper', 'abcd-2001-02-03'),
		edition('2001-02-10', 'fictional-second-paper', 'abcd-2001-02-10'),
		edition('2001-02-17', 'fictional-first-paper', '2001-02-17'),
	],
	holidays: [],
	historicalEvents: [],
	availableDates: ['2001-02-03'],
	availableKeys: ['2001-02-03', 'abcd-2001-02-03', 'abcd-2001-02-10'],
};
const refusal = (availableKeys: unknown, availableDates = catalog.availableDates) => {
	const parsed = EditionsCatalogSchema.safeParse({ ...catalog, availableKeys, availableDates });
	return parsed.success ? '' : parsed.error.issues.map((i) => i.message).join('; ');
};

it('accepts a catalog with and without availableKeys', () => {
	expect(EditionsCatalogSchema.safeParse(catalog).success).toBe(true);
	const { availableKeys: _keys, ...without } = catalog;
	expect(EditionsCatalogSchema.safeParse(without).success).toBe(true);
});

it('accepts two papers on one day and the second paper on a day of its own', () => {
	expect(refusal(['abcd-2001-02-10', 'abcd-2001-02-03', '2001-02-03'])).toBe('');
});

it('refuses a key twice and a key naming no edition', () => {
	expect(refusal(['2001-02-03', 'abcd-2001-02-03', 'abcd-2001-02-03'])).toBe(
		'duplicate available key'
	);
	expect(refusal(['2001-02-03', 'abcd-2001-02-17'])).toBe('available key names no edition');
});

it('holds the date-only keys to availableDates, and no other paper', () => {
	const unequal = 'date-only available keys must equal availableDates';
	expect(refusal(['2001-02-03', '2001-02-17'])).toBe(unequal);
	expect(refusal(['abcd-2001-02-03'])).toBe(unequal);
	expect(refusal(catalog.availableKeys, ['2001-02-03', '2001-02-10'])).toBe(unequal);
});

it('refuses a key that is not an edition key', () => {
	for (const key of ['2001-02-03-abcd', 'ABCD-2001-02-03', '2001-02-03\n'])
		expect(refusal(['2001-02-03', key])).not.toBe('');
});

it("accepts another paper's fates-list piece id and refuses a misplaced code", () => {
	const piece = { edition_date: '2001-02-03', content_item_id: 'cu-abcd-2001-02-03-i0101' };
	expect(FatesListPieceSchema.safeParse(piece).success).toBe(true);
	for (const id of [
		'cu-2001-02-03-abcd-i0101',
		'cu-ABCD-2001-02-03-i0101',
		'cu-2001-02-03-i0101\n',
	])
		expect(FatesListPieceSchema.safeParse({ ...piece, content_item_id: id }).success).toBe(false);
});
