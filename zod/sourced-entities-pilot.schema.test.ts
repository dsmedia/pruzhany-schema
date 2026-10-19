import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { SourcedEntitiesPilotSchema, PilotDateSchema, PilotFactSchema, PilotReviewSchema } from './sourced-entities-pilot.schema';

const fixtures = JSON.parse(execFileSync('uv', [
	'run', '--no-project', '--python', '3.11', '--with', 'pydantic==2.12.5',
	'python', '-P', 'pilots/sourced-entities/contract_cases.py',
], { encoding: 'utf8', timeout: 120_000 }));
const models = { Pilot: SourcedEntitiesPilotSchema, DateValue: PilotDateSchema, Fact: PilotFactSchema, Review: PilotReviewSchema };

describe('issue-14 isolated pilot', () => {
	it('reads the generated real-person preview without changing the production contract', () => {
		const data = SourcedEntitiesPilotSchema.parse(JSON.parse(readFileSync('pilots/sourced-entities/generated/pilot.json', 'utf8')));
		expect([data.people.length, data.events.length, data.mentions.length, data.facts.length]).toEqual([12, 2, 22, 8]);
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
