import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod/v4';

// __dirname also works when the site discovers this file through src/lib/schemas.
const read = (name: string): unknown =>
	JSON.parse(readFileSync(join(__dirname, '../conformance', name), 'utf8'));
const text = z.string().min(1);
const date = z.strictObject({ start: z.string().optional(), end: z.string().optional() });
const citation = z.strictObject({ source_id: text, edition_date: z.string().optional() });
const qualifiers = z.strictObject({ original_json: z.string(), original_field: text.optional() });
const record = z.strictObject({
	persons: z
		.array(
			z.strictObject({
				id: text,
				names: z.array(z.strictObject({ value: text, kind: text, citations: z.array(citation) })),
				fate: z.strictObject({ outcome: text, confidence: text }).optional(),
			})
		)
		.min(1),
	facts: z.array(
		z.strictObject({
			id: text,
			subject_id: text,
			representation: z.enum(['structured', 'prose', 'image']),
			type: text,
			status: z.enum(['proposed', 'accepted', 'disputed', 'rejected']),
			citations: z.array(citation),
			date: date.optional(),
			proposed_type: text.optional(),
			qualifiers: qualifiers.optional(),
		})
	),
	sources: z.array(z.strictObject({ id: text, work_id: text.optional(), dated: date.optional() })),
	relations: z.array(
		z.strictObject({
			id: text,
			person_id: text,
			related_person_id: text,
			status: text,
			review: z.strictObject({ state: text, by: text, on: text }),
			qualifiers,
		})
	),
});
const input = {
	id: text,
	description: text,
	current_year: z.number().int().positive(),
	person_id: text,
	record,
};
const coreCase = z.discriminatedUnion('sides_differ', [
	z.strictObject({
		...input,
		sides_differ: z.literal(false),
		expected: z.strictObject({ living: z.boolean() }),
	}),
	z.strictObject({
		...input,
		sides_differ: z.literal(true),
		expected: z.strictObject({ site: z.boolean(), steps: z.boolean() }),
		recommendation: z.strictObject({ side: z.enum(['site', 'steps']), why: text }),
	}),
]);
const coreFile = z.strictObject({ version: z.literal(1), cases: z.array(coreCase).min(1) });
const shardFile = z.strictObject({
	version: z.literal(1),
	cases: z
		.array(z.strictObject({ entity_id: z.string(), shard: z.number().int().min(0).max(255) }))
		.min(1),
});

describe('fictional cross-language conformance files', () => {
	it('has unique shard inputs, UTF-8 probes, the empty string and boundary shards', () => {
		const { cases } = shardFile.parse(read('record-shards.json'));
		expect(new Set(cases.map((c) => c.entity_id)).size).toBe(cases.length);
		expect(cases.some((c) => c.entity_id === '')).toBe(true);
		expect(cases.some((c) => /[^\x00-\x7f]/.test(c.entity_id))).toBe(true);
		for (const boundary of [0, 1, 15, 16, 127, 128, 254, 255])
			expect(cases.some((c) => c.shard === boundary)).toBe(true);
	});
	it('has unique core cases, a defined target, and explained real disagreements', () => {
		const { cases } = coreFile.parse(read('presumption-core.json'));
		expect(new Set(cases.map((c) => c.id)).size).toBe(cases.length);
		for (const c of cases) {
			expect(c.record.persons.filter((p) => p.id === c.person_id)).toHaveLength(1);
			if (c.sides_differ) expect(c.expected.site).not.toBe(c.expected.steps);
		}
	});
	it('rejects malformed envelopes, out-of-range shards and incomplete disagreements', () => {
		expect(shardFile.safeParse({ version: 1, cases: [] }).success).toBe(false);
		for (const shard of [-1, 256, 0.5, '00'])
			expect(shardFile.safeParse({ version: 1, cases: [{ entity_id: '', shard }] }).success).toBe(
				false
			);
		const c = coreFile.parse(read('presumption-core.json')).cases[0];
		for (const change of [
			{ current_year: '2026' },
			{ expected: { living: 'false' } },
			{ sides_differ: true, expected: { site: false, steps: true } },
			{ record: { ...c.record, issues: [] } },
		])
			expect(coreCase.safeParse({ ...c, ...change }).success).toBe(false);
	});
});
