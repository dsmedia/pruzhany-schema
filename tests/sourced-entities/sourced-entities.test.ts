import { readFileSync } from 'node:fs';
import { expect, it } from 'vitest';
import { z } from 'zod/v4';
import * as entities from '../../zod/sourced-entities.schema';
import { SharedPersonSchema } from '../../zod/shared-record.schema';
import { SiteArchiveSchema } from '../../zod/site-issue.schema';
const path = process.env.ENTITIES_CONTRACT_FIXTURES;
if (!path) throw new Error('Run through bin/verify entities');
const fixtures = JSON.parse(readFileSync(path, 'utf8'));
const models = { ...entities, SharedPersonSchema, SiteArchiveSchema };
for (const c of fixtures.cases)
	it(c.name, () => {
		const model = models[`${c.model}Schema` as keyof typeof models] as z.ZodType;
		expect(model.safeParse(c.value).success).toBe(c.valid);
	});
for (const c of fixtures.legacy)
	it(`legacy ${c.value.outcome}/${c.value.confidence}`, () => {
		expect(entities.legacyHolocaustFate(c.value)).toBe(c.expected);
	});
it('preserves the current archive fixture', () => {
	expect(SiteArchiveSchema.parse(fixtures.baseline)).toEqual(fixtures.baseline);
});
it('exports sources and facts in the shared record, with closed people and issue mentions', () => {
	const schema = z.toJSONSchema(SiteArchiveSchema);
	const record = schema.properties!.shared_record as any;
	for (const field of ['sources', 'facts', 'vocabulary_version'])
		expect(record.properties).toHaveProperty(field);
	const person = record.properties.persons.items;
	for (const field of ['names', 'fate']) expect(person.properties).toHaveProperty(field);
	expect(person.additionalProperties).toBe(false);
	const issue = (schema.properties!.issues as any).items;
	expect(issue.properties.mentions.properties).toHaveProperty('mentions');
	// JSON Schema omits semantic refinements: cross-references, payload rules,
	// date/range consistency, locator presence and approval. Steps must check these in code.
	// Python's JSON Schema validator checks the actual exported artifact in bin/verify.
});
