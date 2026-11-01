import { describe, expect, it } from 'vitest';
import { CitationSchema, SourceSchema } from './sourced-entities.schema';
import { statementCitationShortfalls } from './citation-requirements';

// The full cases are tests/contract/citation-requirements.fixtures.json, checked in both twins by
// bin/verify; these few stay inside zod/, which the site runs through a symlink to this folder alone.
const register = SourceSchema.parse({
	id: 'judewicz-kaplan',
	kind: 'family_document',
	title: 'Fictional register',
	private: true,
});
const paper = SourceSchema.parse({ id: 'paper', kind: 'the_paper', title: 'Fictional paper' });

describe('statement citation shortfalls are advisory', () => {
	it('the family register entry needs its locator, not a quote', () => {
		const citation = CitationSchema.parse({ source_id: 'judewicz-kaplan', locator: 'person-x' });
		expect(statementCitationShortfalls(citation, register)).toEqual([]);
	});
	it('a quote from the register still needs clearance', () => {
		const citation = CitationSchema.parse({
			source_id: 'judewicz-kaplan',
			locator: 'person-x',
			quote: 'Fictional words',
			quote_language: 'en',
		});
		expect(statementCitationShortfalls(citation, register)).toEqual(['source.quotes_cleared']);
	});
	it('the paper needs its printed words and address', () => {
		const citation = CitationSchema.parse({
			source_id: 'paper',
			unit_id: 'cu-x',
			edition_date: '1938-01-01',
		});
		const before = JSON.stringify(citation);
		expect(statementCitationShortfalls(citation, paper)).toEqual(['citation.quote']);
		expect(JSON.stringify(citation)).toBe(before);
	});
});
