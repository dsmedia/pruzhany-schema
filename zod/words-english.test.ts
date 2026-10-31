import { describe, expect, it } from 'vitest';
import { z } from 'zod/v4';
import * as schemas from './index';
import { addEnglishIssues } from './words-english';
import { REQUIRE_NON_ENGLISH_QUOTE_ENGLISH } from './generated/words_policy';
import { readFileSync, realpathSync } from 'node:fs';
import { join } from 'node:path';
const fixture = JSON.parse(
	readFileSync(
		join(realpathSync(__dirname), '../tests/contract/words-english.fixtures.json'),
		'utf8'
	)
) as {
	example: unknown;
	models: Record<string, string[]>;
	cases: {
		name: string;
		model: string;
		valid: boolean;
		error?: string;
		changes: { path: (string | number)[]; value?: unknown; remove?: boolean }[];
	}[];
};

// Shared fictional corpus: bun alone here; Python/LinkML run outside zod/.
describe('source words carry exact attributed English', () => {
	for (const test of fixture.cases) {
		it(test.name, () => {
			const paths = fixture.models[test.model as keyof typeof fixture.models];
			let source: unknown = fixture.example;
			for (const key of paths) source = (source as Record<string, unknown>)[key];
			const value = structuredClone(source) as Record<string, unknown>;
			for (const change of test.changes) {
				let object = value;
				for (const key of change.path.slice(0, -1)) object = object[key] as typeof object;
				if (change.remove) delete object[change.path.at(-1)!];
				else object[change.path.at(-1)!] = structuredClone(change.value);
			}
			const schema = schemas[`${test.model}Schema` as keyof typeof schemas] as z.ZodType;
			const parsed = schema.safeParse(value);
			expect(parsed.success).toBe(test.valid);
			if (test.error && !parsed.success)
				expect(parsed.error.issues.some((i) => i.message.includes(test.error!))).toBe(true);
		});
	}
});

const original = 'Di erd iz rund.';
const translation = {
	text: 'The earth is round.',
	language: 'en',
	based_on: {
		source_text: original,
		addresses: [{ image_uri: 'fictional.png', bbox: [0, 0, 10, 10], text: original }],
	},
	attribution: { kind: 'person', by: 'Fictional translator', on: '2000-01-01' },
};

describe('one staged quote-English switch', () => {
	it('leaves the released contract off', () => {
		expect(REQUIRE_NON_ENGLISH_QUOTE_ENGLISH).toBe(false);
		expect(
			schemas.CitationSchema.safeParse({ source_id: 's', page: '1', quote: original }).success
		).toBe(true);
	});
	for (const base of [schemas.CitationSchema, schemas.SiteCitationSchema]) {
		const enabled = base.superRefine((v, ctx) => addEnglishIssues('Citation', v, ctx, true));
		for (const language of [undefined, null, 'yi', 'de', 'und', 'en', 'en-US', 'EN-gb']) {
			for (const english of [undefined, null, translation]) {
				it(`${base === schemas.CitationSchema ? 'Citation' : 'SiteCitation'} ${language} ${english ? 'with English' : String(english)}`, () => {
					const value = {
						source_id: 's',
						page: '1',
						quote: original,
						quote_language: language,
						quote_english: english,
					};
					expect(enabled.safeParse(value).success).toBe(
						!!english || !!language?.toLowerCase().match(/^en(-|$)/)
					);
				});
			}
		}
		it('does not require English for an absent, null or blank quote', () => {
			for (const quote of [undefined, null, '', '  '])
				expect(enabled.safeParse({ source_id: 's', page: '1', quote }).success).toBe(true);
		});
	}
});
