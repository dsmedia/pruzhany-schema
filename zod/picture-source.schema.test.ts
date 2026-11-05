import { describe, expect, it } from 'vitest';
import { PictureSourceSchema } from './picture-source.schema';
import { NewspaperSchema } from './editions.schema';

describe('picture holder web address', () => {
	for (const [name, schema, credit] of [
		['PictureSource', PictureSourceSchema, { holder: 'Fictional Library' }],
		[
			'Newspaper',
			NewspaperSchema,
			{
				holder: 'Fictional Library',
				id: 'fictional-paper',
				code: 'abc',
				title: 'Fictional Gazette',
			},
		],
	] as const) {
		it(`${name} preserves a holder URL`, () => {
			const holder_url = 'https://LIBRARY.example.org/holdings/42%2F1';
			expect(schema.parse({ ...credit, holder_url }).holder_url).toBe(holder_url);
		});
		it(`${name} refuses a non-URI`, () => {
			for (const holder_url of ['not a URI', '/relative/path', '', 42])
				expect(schema.safeParse({ ...credit, holder_url }).success).toBe(false);
		});
		it(`${name} still accepts a credit without a holder URL`, () => {
			expect(schema.parse(credit)).toEqual(credit);
		});
	}
});
