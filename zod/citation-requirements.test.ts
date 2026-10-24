import { describe, expect, it } from 'vitest';
import fixtures from '../tests/contract/citation-requirements.fixtures.json';
import { CitationSchema, SourceSchema } from './sourced-entities.schema';
import { statementCitationShortfalls } from './citation-requirements';

describe('statement citation shortfalls are advisory', () => {
	for (const fixture of fixtures.cases)
		it(fixture.name, () => {
			const source = SourceSchema.parse(fixture.source);
			const citation = CitationSchema.parse(fixture.citation);
			const via = 'via' in fixture ? SourceSchema.parse(fixture.via) : undefined;
			const before = JSON.stringify({ source, citation, via });
			expect(statementCitationShortfalls(citation, source, via)).toEqual(fixture.shortfalls);
			expect(JSON.stringify({ source, citation, via })).toBe(before);
		});
});
