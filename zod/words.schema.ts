/**
 * Layer 1, word level: where every printed word of an edition stands.
 *
 * One optional file per edition, `{date}-words.json`, beside the pages file. It
 * holds each word's box on the page picture and its text, grouped by the block
 * and the printed line it stands in, in the pages file's order. A word's unit is
 * its block's: blocks of different units can lie one inside another, so where a
 * word lies cannot say which piece it is of.
 *
 * `start` / `length` place a word in its unit's `full_text` as published, in
 * UTF-16 code units (JavaScript string offsets), with no normalisation. Both
 * halves of a word broken over two lines point at the one joined word; the first
 * half carries `hyphenated: true`. A word of a block with no unit (a heading over
 * several pieces) has no span.
 */

import { z } from 'zod/v4';

/** [x, y, width, height] in the page picture's pixels, as a block's `bbox`. */
const WordBboxSchema = z.tuple([z.number(), z.number(), z.number(), z.number()]);

const OffsetSchema = z.number().int().nonnegative();

export const WordSchema = z
	.object({
		bbox: WordBboxSchema,
		transcription: z.string().min(1), // the word as printed
		start: OffsetSchema.optional(),
		length: OffsetSchema.optional(),
		hyphenated: z.boolean().optional(),
	})
	.refine((w) => (w.start === undefined) === (w.length === undefined), {
		message: 'start and length are given together or not at all',
	});

export const WordLineSchema = z.object({
	bbox: WordBboxSchema,
	words: z.array(WordSchema),
});

export const WordBlockSchema = z
	.object({
		block_id: z.string(), // FK to a block of the pages file
		unit_id: z.string().nullable(), // that block's unit_id
		lines: z.array(WordLineSchema),
	})
	.refine(
		(b) => b.unit_id !== null || b.lines.every((l) => l.words.every((w) => w.start === undefined)),
		{
			message: 'a word of a block with no unit has no span',
		}
	);

export const WordPageSchema = z.object({
	page_id: z.string(), // FK to a page of the pages file
	blocks: z.array(WordBlockSchema),
});

export const WordsDataSchema = z.object({
	edition_date: z.string(),
	pages: z.array(WordPageSchema),
});

export type Word = z.infer<typeof WordSchema>;
export type WordLine = z.infer<typeof WordLineSchema>;
export type WordBlock = z.infer<typeof WordBlockSchema>;
export type WordPage = z.infer<typeof WordPageSchema>;
export type WordsData = z.infer<typeof WordsDataSchema>;
