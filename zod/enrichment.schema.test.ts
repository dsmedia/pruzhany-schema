import { describe, it, expect } from 'vitest';
import {
	EnrichedPersonSchema,
	EnrichedLocationSchema,
	EnrichedEventSchema,
	TopicSchema,
	EnrichmentDataSchema,
	LocationTypeSchema,
} from './enrichment.schema';
import { ExternalReferenceSchema } from './shared.schema';

describe('Enrichment Schemas', () => {
	describe('EnrichedPersonSchema', () => {
		it('accepts valid person with all fields', () => {
			const person = {
				id: 'person-1',
				name: 'Jacob Perlstein',
				yiddish_name: 'יעקב פערלשטיין',
				aliases: ['Yankel'],
				gender: 'male',
				birth_year: 1900,
				holocaust_fate: 'perished',
				unit_ids: ['cu-5746'],
				relationships: [{ person_id: 'person-2', type: 'spouse' }],
				external_references: [{ source: 'Yad Vashem', url: 'https://example.com' }],
			};
			expect(() => EnrichedPersonSchema.parse(person)).not.toThrow();
		});

		it('accepts person with optional fields omitted', () => {
			const person = {
				id: 'person-1',
				name: 'Unknown Person',
				aliases: [],
				gender: 'unknown',
				holocaust_fate: 'unknown',
				unit_ids: [],
				relationships: [],
				external_references: [],
			};
			expect(() => EnrichedPersonSchema.parse(person)).not.toThrow();
		});

		it('rejects person with invalid gender', () => {
			const person = {
				id: 'person-1',
				name: 'Test',
				aliases: [],
				gender: 'other', // invalid
				holocaust_fate: 'unknown',
				unit_ids: [],
				relationships: [],
				external_references: [],
			};
			expect(() => EnrichedPersonSchema.parse(person)).toThrow();
		});

		it('accepts person with biographical_narratives and proposed_relationships', () => {
			const person = {
				id: 'person-aaron-yurevitch',
				name: 'Aron Judewicz',
				aliases: [],
				gender: 'male',
				holocaust_fate: 'perished',
				unit_ids: ['cu-1'],
				relationships: [],
				external_references: [],
				biographical_narratives: [
					{
						source: 'deep_research',
						markdown: '**Aron Judewicz** was deeply embedded in the smuggling networks…',
					},
					{ source: 'flash', markdown: 'Yizkor plaque notes his role as gabbai.' },
				],
				proposed_relationships: [
					{
						type: 'sibling_of',
						person_id_hint: 'Salomon Judewicz (brother, perished Auschwitz 1943)',
						evidence: 'Both named as resident brothers in 1939 deportation list.',
						source: 'deep_research',
					},
				],
			};
			expect(() => EnrichedPersonSchema.parse(person)).not.toThrow();
		});

		it('rejects biographical_narratives entry with invalid source', () => {
			const person = {
				id: 'person-1',
				name: 'Test',
				aliases: [],
				gender: 'unknown',
				holocaust_fate: 'unknown',
				unit_ids: [],
				relationships: [],
				external_references: [],
				biographical_narratives: [{ source: 'gpt', markdown: '...' }], // invalid source
			};
			expect(() => EnrichedPersonSchema.parse(person)).toThrow();
		});
	});

	describe('ExternalReferenceSchema', () => {
		it('accepts url: null for negative-evidence citations', () => {
			const ref = {
				source: 'yad-vashem',
				url: null,
				notes: 'Negative evidence: no record found under any spelling',
				verified: false,
			};
			expect(() => ExternalReferenceSchema.parse(ref)).not.toThrow();
		});

		it('accepts verified: true', () => {
			const ref = {
				source: 'jri-poland',
				url: 'https://example.com/record/123',
				record_id: 'JRI-12345',
				verified: true,
			};
			expect(() => ExternalReferenceSchema.parse(ref)).not.toThrow();
		});

		it('accepts omitted verified and url (backward compat)', () => {
			const ref = { source: 'Yad Vashem' };
			expect(() => ExternalReferenceSchema.parse(ref)).not.toThrow();
		});
	});

	describe('LocationTypeSchema', () => {
		it('includes address and landmark', () => {
			const options = LocationTypeSchema.options;
			expect(options).toContain('address');
			expect(options).toContain('landmark');
		});

		it('.options is the single source of truth (returns string array)', () => {
			const options = LocationTypeSchema.options;
			expect(Array.isArray(options)).toBe(true);
			expect(options.length).toBeGreaterThan(0);
			for (const opt of options) {
				expect(typeof opt).toBe('string');
			}
		});
	});

	describe('EnrichmentDataSchema', () => {
		it('accepts valid enrichment data structure', () => {
			const data = {
				version: '1.0',
				edition_date: '1938-12-16',
				last_updated: '2026-01-20',
				people: [],
				locations: [],
				events: [],
				topics: [],
			};
			expect(() => EnrichmentDataSchema.parse(data)).not.toThrow();
		});
	});
});
