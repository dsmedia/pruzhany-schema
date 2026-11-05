import { describe, expect, it } from 'vitest';
import { PictureSourceSchema } from './picture-source.schema';
import { NewspaperSchema } from './editions.schema';
import { PageSchema, PagesDataSchema } from './page.schema';
import { NewspaperSchema as PreviousNewspaperSchema } from './tests/holder-url-baseline';
import { z } from 'zod/v4';

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

describe('picture rights and the holder image service', () => {
	const page = {
		id: 'page-2001-02-03-1',
		issue_date: '2001-02-03',
		page_number: 1,
		image_uri: 'fictional-page.jpg',
		dimensions: [1000, 1500],
		blocks: [],
		newspaper: 'fictional-paper',
	};
	const credit = {
		holder: 'Fictional Regional Library',
		rights: 'Fictional permission for these scans',
		rights_url: 'https://library.example.org/rights',
	};
	const image_service = 'https://library.example.org/iiif/3/fictional-page-1';

	it('keeps the newspaper wire contract unchanged when rights are inherited', () => {
		expect(z.toJSONSchema(NewspaperSchema)).toEqual(z.toJSONSchema(PreviousNewspaperSchema));
		const paper = { ...credit, id: 'fictional-paper', code: 'abc', title: 'Fictional Gazette' };
		expect(NewspaperSchema.parse(paper)).toEqual(PreviousNewspaperSchema.parse(paper));
	});

	it('preserves a page source with its own rights and its holder service', () => {
		const value = { ...page, picture_source: credit, image_service };
		expect(PageSchema.parse(value)).toEqual(value);
		expect(
			PagesDataSchema.parse({ edition_date: page.issue_date, pages: [value] }).pages[0]
		).toEqual(value);
		expect(PictureSourceSchema.parse(credit)).toEqual(credit);
	});

	it('keeps rights and the service optional without changing the displayed picture', () => {
		expect(PageSchema.parse(page)).toEqual(page);
		expect(PictureSourceSchema.parse({ holder: credit.holder })).toEqual({ holder: credit.holder });
		expect(PageSchema.parse({ ...page, image_service }).image_uri).toBe(page.image_uri);
	});

	it('refuses invalid service and rights URIs and blank rights statements', () => {
		for (const value of ['not a URI', '/relative/path', '', 42]) {
			expect(PageSchema.safeParse({ ...page, image_service: value }).success).toBe(false);
			expect(PictureSourceSchema.safeParse({ ...credit, rights_url: value }).success).toBe(false);
		}
		for (const rights of ['', ' \t\n'])
			expect(PageSchema.safeParse({ ...page, picture_source: { ...credit, rights } }).success).toBe(
				false
			);
	});
});
