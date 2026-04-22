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
});
