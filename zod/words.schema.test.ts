import { describe, it, expect } from 'vitest';
import { WordsDataSchema } from './words.schema';

const word = {
	bbox: [10, 20, 30, 12],
	transcription: 'אונזער',
	start: 0,
	length: 6,
};

function edition(blocks: unknown[]) {
	return {
		edition_date: '1934-06-22',
		pages: [{ page_id: 'page-1934-06-22-1', blocks }],
	};
}

describe('WordsDataSchema', () => {
	it('accepts a block of a unit whose words have spans', () => {
		const data = edition([
			{
				block_id: 'blk-1934-06-22-p1-r001',
				unit_id: 'cu-1934-06-22-i0101',
				lines: [
					{
						bbox: [10, 20, 80, 14],
						words: [word, { ...word, hyphenated: true }],
					},
				],
			},
		]);
		expect(WordsDataSchema.parse(data)).toEqual(data);
	});

	it('accepts a heading block with no unit and no spans', () => {
		const data = edition([
			{
				block_id: 'blk-1934-06-22-p1-r002',
				unit_id: null,
				lines: [
					{
						bbox: [0, 0, 5, 5],
						words: [{ bbox: [0, 0, 5, 5], transcription: 'א' }],
					},
				],
			},
		]);
		expect(WordsDataSchema.parse(data)).toEqual(data);
	});

	it('refuses a span on a word of a block with no unit', () => {
		const data = edition([
			{
				block_id: 'b',
				unit_id: null,
				lines: [{ bbox: [0, 0, 5, 5], words: [word] }],
			},
		]);
		expect(WordsDataSchema.safeParse(data).success).toBe(false);
	});

	it('refuses a start without a length', () => {
		const data = edition([
			{
				block_id: 'b',
				unit_id: 'u',
				lines: [
					{
						bbox: [0, 0, 5, 5],
						words: [{ bbox: [0, 0, 5, 5], transcription: 'א', start: 0 }],
					},
				],
			},
		]);
		expect(WordsDataSchema.safeParse(data).success).toBe(false);
	});

	it('refuses an empty word, a negative offset and a box of three numbers', () => {
		const bad = [
			{ ...word, transcription: '' },
			{ ...word, start: -1 },
			{ ...word, bbox: [1, 2, 3] },
		];
		for (const w of bad) {
			const data = edition([
				{
					block_id: 'b',
					unit_id: 'u',
					lines: [{ bbox: [0, 0, 5, 5], words: [w] }],
				},
			]);
			expect(WordsDataSchema.safeParse(data).success).toBe(false);
		}
	});
});
