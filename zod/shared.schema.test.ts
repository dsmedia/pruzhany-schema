import { describe, it, expect } from 'vitest';
import { ExternalReferenceSchema, HolocaustFateSchema } from './shared.schema';

describe('Shared Schemas', () => {
	describe('HolocaustFateSchema', () => {
		it('accepts valid fate values', () => {
			expect(HolocaustFateSchema.parse('perished')).toBe('perished');
			expect(HolocaustFateSchema.parse('survived')).toBe('survived');
			expect(HolocaustFateSchema.parse('unknown')).toBe('unknown');
		});

		it('rejects invalid fate values', () => {
			expect(() => HolocaustFateSchema.parse('invalid')).toThrow();
		});
	});

	describe('ExternalReferenceSchema', () => {
		it('accepts valid reference with url', () => {
			const ref = {
				source: 'Yad Vashem',
				url: 'https://yadvashem.org/123',
				notes: 'Page of testimony',
			};
			expect(ExternalReferenceSchema.parse(ref)).toEqual(ref);
		});

		it('accepts reference without optional url', () => {
			const ref = { source: 'Family records' };
			expect(ExternalReferenceSchema.parse(ref)).toEqual(ref);
		});

		it('rejects reference without source', () => {
			expect(() => ExternalReferenceSchema.parse({ url: 'https://example.com' })).toThrow();
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
});
