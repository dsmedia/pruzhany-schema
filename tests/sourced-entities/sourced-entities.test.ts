import { readFileSync } from 'node:fs';
import { expect, it } from 'vitest';
import { z } from 'zod/v4';
import * as entities from '../../zod/sourced-entities.schema';
import { EnrichedPersonSchema, EnrichmentDataSchema } from '../../zod/enrichment.schema';
const path = process.env.ENTITIES_CONTRACT_FIXTURES;
if (!path) throw new Error('Run through bin/verify entities');
const fixtures = JSON.parse(readFileSync(path, 'utf8'));
const models = { ...entities, EnrichedPersonSchema, EnrichmentDataSchema };
for (const c of fixtures.cases)
	it(c.name, () => {
		const model = models[`${c.model}Schema` as keyof typeof models] as z.ZodType;
		expect(model.safeParse(c.value).success).toBe(c.valid);
	});
for (const c of fixtures.legacy)
	it(`legacy ${c.value.outcome}/${c.value.confidence}`, () => {
		expect(entities.legacyHolocaustFate(c.value)).toBe(c.expected);
	});
it('preserves a legacy edition with no new fields', () => {
	expect(EnrichmentDataSchema.parse(fixtures.baseline)).toEqual(fixtures.baseline);
});
it('exports every optional attachment in closed person JSON Schema', () => {
	const schema = z.toJSONSchema(EnrichmentDataSchema);
	expect(schema.properties).toHaveProperty('sources');
	expect(schema.properties).toHaveProperty('mentions');
	expect(schema.properties).toHaveProperty('vocabulary_version');
	const person = (schema.properties!.people as any).items;
	for (const field of ['facts', 'names', 'fate']) expect(person.properties).toHaveProperty(field);
	expect(person.additionalProperties).toBe(false);
	// JSON Schema omits semantic refinements: cross-references, payload rules,
	// date/range consistency, locator presence and approval. Steps must check these in code.
	// Python's JSON Schema validator checks the actual exported artifact in bin/verify.
});
