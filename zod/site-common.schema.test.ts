import { describe, expect, it } from 'vitest';
import { SuppliedTitleSchema, TranslationSchema } from './site-common.schema';

const check = {
	reading_id: 'fictional-item',
	reading_sha256: 'a'.repeat(64),
	english_sha256: 'b'.repeat(64),
	judgement_id: 'corrections/english-choice/1900-01-05.json#J0001:title',
	judgement_sha256: 'c'.repeat(64),
	attribution: { by: 'Fictional checker', on: '2026-01-03', kind: 'person' },
};
const title = {
	text: 'A fictional title',
	language: 'en',
	based_on: {
		source_text: 'Earlier reading',
		addresses: [{ image_uri: 'fiction.png', bbox: [0, 0, 1, 1], text: 'Earlier reading' }],
	},
	attribution: { by: 'Original translator', on: '2020-01-02', kind: 'person' },
};

describe('an independent check of one English field', () => {
	it('keeps the original basis and author with an optional complete check', () => {
		expect(SuppliedTitleSchema.parse(title)).toEqual(title);
		expect(SuppliedTitleSchema.parse({ ...title, checked_against: check })).toEqual({
			...title,
			checked_against: check,
		});
	});
	it.each(['J42', 'urn:archive:judgement/J42#review', 'בדיקה/42'])(
		'accepts the opaque identifier %s unchanged for either field',
		(identifier) => {
			for (const [schema, field] of [
				[SuppliedTitleSchema, 'title'],
				[TranslationSchema, 'text'],
			] as const) {
				const value = {
					...title,
					checked_against: { ...check, judgement_id: `${identifier}:${field}` },
				};
				expect(schema.parse(value)).toEqual(value);
			}
		}
	);
	it.each([' ', '\t', '\n', '\r', '\u00a0', '\u0085', '\ufeff', '\u2028', '\u2029'])(
		'rejects whitespace %j anywhere in a judgement identifier',
		(space) => {
			for (const [schema, field] of [
				[SuppliedTitleSchema, 'title'],
				[TranslationSchema, 'text'],
			] as const) {
				for (const judgement_id of [
					`${space}J42:${field}`,
					`J${space}42:${field}`,
					`J42:${field}${space}`,
				]) {
					expect(
						schema.safeParse({ ...title, checked_against: { ...check, judgement_id } }).success
					).toBe(false);
				}
			}
		}
	);
	it.each(['', ':title', ':text', 'J42', 'J42:summary', 'J42:title:extra'])(
		'rejects missing identifiers or unsupported suffixes: %j',
		(judgement_id) => {
			for (const schema of [SuppliedTitleSchema, TranslationSchema]) {
				expect(
					schema.safeParse({ ...title, checked_against: { ...check, judgement_id } }).success
				).toBe(false);
			}
		}
	);
	it.each(Object.keys(check))('rejects a check missing %s', (key) => {
		const incomplete: Record<string, unknown> = { ...check };
		delete incomplete[key];
		expect(SuppliedTitleSchema.safeParse({ ...title, checked_against: incomplete }).success).toBe(
			false
		);
	});
	it('does not accept a title judgement for a translation or vice versa', () => {
		const translationCheck = {
			...check,
			judgement_id: check.judgement_id.replace(':title', ':text'),
		};
		expect(
			TranslationSchema.safeParse({ ...title, checked_against: translationCheck }).success
		).toBe(true);
		expect(TranslationSchema.safeParse({ ...title, checked_against: check }).success).toBe(false);
		expect(
			SuppliedTitleSchema.safeParse({ ...title, checked_against: translationCheck }).success
		).toBe(false);
	});
});
