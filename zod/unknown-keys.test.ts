import { describe, expect, it } from 'vitest';
import * as current from './index';
import * as frozen from './tests/frozen';

const extension = { fictional: 'producer metadata' };
const block = {
	id: 'fictional-block',
	bbox: [0, 0, 20, 30],
	transcription: 'Fictional text',
	unit_id: 'fictional-item',
};
const page = {
	id: 'fictional-page',
	issue_date: '2000-01-01',
	page_number: 1,
	image_uri: 'fictional.png',
	dimensions: [100, 100],
	blocks: [block],
};
const pages = { edition_date: '2000-01-01', pages: [page] };
const crossReference = {
	target_id: 'fictional-item',
	confidence: 1,
	relationship: 'Fictional link',
	evidence: 'Fictional evidence',
};
const edition = {
	date: '2000-01-01',
	hebrewDate: 'Fictional date',
	hebrewMonth: 1,
	hebrewYear: 5760,
};
const holiday = { date: '2000-01-01', name: 'Fictional holiday' };
const historicalEvent = {
	date: '2000-01-01',
	name: 'Fictional event',
	description: 'An invented event for testing',
};
const catalog = {
	editions: [edition],
	holidays: [holiday],
	historicalEvents: [historicalEvent],
	availableDates: ['2000-01-01'],
};

describe('the nine formerly stripping schemas accept and strip extensions', () => {
	for (const [name, value] of [
		['BlockSchema', block],
		['PageSchema', page],
		['PagesDataSchema', pages],
		['ExternalReferenceSchema', { source: 'Fictional source' }],
		['CrossReferenceSchema', crossReference],
		['EditionSchema', edition],
		['HolidaySchema', holiday],
		['HistoricalEventSchema', historicalEvent],
		['EditionsCatalogSchema', catalog],
	] as const) {
		it(name, () => {
			const input = { ...value, extension };
			expect(current[name].parse(input)).toStrictEqual(value);
			expect(frozen[name].parse(input)).toStrictEqual(value);
		});
	}

	it('strips extensions from a pages document, its page and its block together', () => {
		const input = {
			...pages,
			extension,
			pages: [{ ...page, extension, blocks: [{ ...block, extension }] }],
		};
		expect(current.PagesDataSchema.parse(input)).toStrictEqual(pages);
		expect(frozen.PagesDataSchema.parse(input)).toStrictEqual(pages);
	});

	it('strips extensions from a catalog and all three child schemas together', () => {
		expect(
			current.EditionsCatalogSchema.parse({
				...catalog,
				extension,
				editions: [{ ...edition, extension }],
				holidays: [{ ...holiday, extension }],
				historicalEvents: [{ ...historicalEvent, extension }],
			})
		).toStrictEqual(catalog);
	});
});

const address = { image_uri: page.image_uri, bbox: block.bbox, text: block.transcription };
const contentItem = {
	id: 'fictional-item',
	type: 'article',
	supplied_title: {
		text: 'Fictional title',
		language: 'en',
		based_on: { source_text: block.transcription, addresses: [address] },
		attribution: { by: 'Fictional reviewer', on: '2000-01-01', kind: 'person' },
	},
	subject_ids: [],
	full_text: block.transcription,
	block_breaks: [0],
	page_blocks: [{ page_id: page.id, block_ids: [block.id] }],
	location_ids: [],
	organization_ids: [],
	cross_references: [crossReference],
};
const contentItemRef = { content_item_id: contentItem.id, role: 'primary_announcement' };
const lifeEvent = { id: 'fictional-event', content_items: [contentItemRef] };
const issue = {
	pages,
	content_items: {
		issue_date: '2000-01-01',
		vocabulary_version: '1.0.0',
		content_items: [contentItem],
		sections: [],
	},
	mentions: { issue_date: '2000-01-01', mentions: [] },
	life_events: { issue_date: '2000-01-01', life_events: [lifeEvent] },
};

it('uses the stripping cross-reference schema inside content items and issues', () => {
	const input = {
		...issue,
		content_items: {
			...issue.content_items,
			content_items: [{ ...contentItem, cross_references: [{ ...crossReference, extension }] }],
		},
	};
	expect(current.SiteIssueSchema.parse(input)).toStrictEqual(issue);
});

describe('formerly strict schemas still refuse extensions', () => {
	for (const [name, value] of [
		['ContentItemSchema', contentItem],
		['ContentItemRefSchema', contentItemRef],
		['PrintedAddressSchema', address],
		['SiteIssueSchema', issue],
	] as const) {
		it(name, () => {
			expect(current[name].parse(value)).toStrictEqual(value);
			expect(frozen[name].parse(value)).toStrictEqual(value);
			for (const schema of [current[name], frozen[name]]) {
				const result = schema.safeParse({ ...value, extension });
				expect(result.success).toBe(false);
				if (!result.success)
					expect(result.error.issues).toContainEqual({
						code: 'unrecognized_keys',
						keys: ['extension'],
						path: [],
						message: 'Unrecognized key: "extension"',
					});
			}
		});
	}

	it('refuses an extension on a content-item ref nested in a site issue', () => {
		const result = current.SiteIssueSchema.safeParse({
			...issue,
			life_events: {
				...issue.life_events,
				life_events: [{ ...lifeEvent, content_items: [{ ...contentItemRef, extension }] }],
			},
		});
		expect(result.success).toBe(false);
		if (!result.success)
			expect(result.error.issues).toContainEqual({
				code: 'unrecognized_keys',
				keys: ['extension'],
				path: ['life_events', 'life_events', 0, 'content_items', 0],
				message: 'Unrecognized key: "extension"',
			});
	});
});
