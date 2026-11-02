import { expect, it } from 'vitest';
import { EditionSchema } from './editions.schema';

const edition = {
	key: 'abcd-2001-02-03',
	newspaper: 'fictional-second-paper',
	date: '2001-02-03',
	hebrewDate: 'Fictional date',
	hebrewMonth: 1,
	hebrewYear: 5761,
};

it('requires the source register newspaper on an edition', () => {
	expect(EditionSchema.safeParse(edition).success).toBe(true);
	const { newspaper: _newspaper, ...missing } = edition;
	expect(EditionSchema.safeParse(missing).success).toBe(false);
});

it('accepts either edition key and refuses a different date or a misplaced code', () => {
	for (const key of ['2001-02-03', 'abcd-2001-02-03'])
		expect(EditionSchema.safeParse({ ...edition, key }).success).toBe(true);
	for (const key of ['2001-02-04', 'abcd-2001-02-04', '2001-02-03-abcd'])
		expect(EditionSchema.safeParse({ ...edition, key }).success).toBe(false);
});
