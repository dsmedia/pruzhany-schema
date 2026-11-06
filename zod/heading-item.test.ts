import { describe, expect, it } from 'vitest';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { ContentItemsDataSchema, PrintedSectionSchema } from './content-item.schema';
import { SiteArchiveSchema, SiteIssueSchema } from './site-issue.schema';

const schemas = {
	ContentItemsData: ContentItemsDataSchema,
	PrintedSection: PrintedSectionSchema,
	SiteIssue: SiteIssueSchema,
	SiteArchive: SiteArchiveSchema,
};
type Path = (string | number)[];
type Change = { path: Path; value?: unknown; remove?: boolean };
type Container = Record<string | number, unknown>;
const fixtures = JSON.parse(
	readFileSync(
		join(dirname(fileURLToPath(import.meta.url)), 'tests/heading-item.fixtures.json'),
		'utf8'
	)
) as {
	example: unknown;
	models: Record<string, Path>;
	cases: { name: string; model: string; changes: Change[]; valid: boolean; error?: string }[];
};

function caseValue(model: string, changes: Change[]): unknown {
	let value: unknown = structuredClone(fixtures.example);
	for (const part of fixtures.models[model as keyof typeof fixtures.models])
		value = (value as Container)[part];
	for (const change of changes) {
		if (!change.path.length) {
			value = structuredClone(change.value);
			continue;
		}
		let target = value as Container;
		for (const part of change.path.slice(0, -1)) target = target[part] as Container;
		const key = change.path[change.path.length - 1];
		if (change.remove) delete target[key];
		else target[key] = structuredClone(change.value);
	}
	return value;
}

describe('a content item supplying a printed section heading', () => {
	for (const c of fixtures.cases) {
		it(c.name, () => {
			const result = schemas[c.model as keyof typeof schemas].safeParse(
				caseValue(c.model, c.changes)
			);
			expect(result.success).toBe(c.valid);
			if ('error' in c && c.error) {
				expect(result.success).toBe(false);
				if (!result.success)
					expect(result.error.issues.map((i) => i.message).join('; ')).toContain(c.error);
			}
		});
	}

	it('preserves the heading link, displayed title and blocks, and the greeting membership', () => {
		const issue = SiteIssueSchema.parse(fixtures.example);
		const [heading, greeting] = issue.content_items.content_items;
		const [section] = issue.content_items.sections;
		expect(section.heading_item_id).toBe(heading.id);
		expect(section.heading_blocks).toEqual(heading.page_blocks);
		expect(section.printed_title).toEqual(heading.printed_title);
		expect(section.content_item_ids).toEqual([greeting.id]);
		expect(greeting.section_id).toBe(section.id);
		expect(issue.pages.pages[0].blocks.slice(0, 2).map((b) => b.unit_id)).toEqual([
			heading.id,
			heading.id,
		]);
	});
});
