import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { SourcedEntitiesPilotSchema, PilotDateSchema, PilotFactSchema, PilotReviewSchema } from '../../zod/sourced-entities-pilot.schema';

const fixturePath = process.env.PILOT_CONTRACT_FIXTURES;
if (!fixturePath) throw new Error('Run this test through bin/verify pilot to generate the Python parity fixtures.');
const fixtures = JSON.parse(readFileSync(fixturePath, 'utf8'));
const models = { Pilot: SourcedEntitiesPilotSchema, DateValue: PilotDateSchema, Fact: PilotFactSchema, Review: PilotReviewSchema };

describe('issue-14 isolated pilot', () => {
	it('reads the generated real-person preview without changing the production contract', () => {
		const data = SourcedEntitiesPilotSchema.parse(JSON.parse(readFileSync(new URL('./generated/pilot.json', import.meta.url), 'utf8')));
		expect([data.people.length, data.events.length, data.mentions.length, data.facts.length, data.relationships.length]).toEqual([12, 2, 22, 6, 1]);
		expect(data.people.every(p => p.fate === undefined)).toBe(true);
		expect(data.facts.every(f => f.review.state === 'pending')).toBe(true);
	});
	for (const fixture of fixtures) {
		it(`agrees with Pydantic on ${fixture.name}`, () => {
			const model = models[fixture.model as keyof typeof models];
			expect(model.safeParse(fixture.value).success).toBe(fixture.valid);
		});
	}
});
