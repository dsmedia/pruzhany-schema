/**
 * Write the JSON Schema of the five site documents from this checkout's Zod, exactly as
 * pruzhany-steps' `site_shapes refresh` writes its copies (src/pruzsteps/site_shapes.ts):
 * same models, same options, tab-indented with a final newline. linkml/tests/test_known_looser.py
 * reads them, so every place known-looser.yaml names is checked against the shapes of today.
 *
 *   bun linkml/export_zod.ts <destination folder>
 */
import { mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { z } from 'zod/v4';
import { PagesDataSchema } from '../zod/page.schema';
import { ContentItemsDataSchema } from '../zod/content-item.schema';
import { IssueMentionsDataSchema, IssueLifeEventsDataSchema } from '../zod/site-issue.schema';
import { SharedRecordSchema } from '../zod/shared-record.schema';

const [destination] = Bun.argv.slice(2);
if (!destination) throw new Error('usage: bun linkml/export_zod.ts <destination folder>');

const exports: [string, z.ZodType][] = [
	['site/pages.schema.json', PagesDataSchema],
	['site-next/content-items.schema.json', ContentItemsDataSchema],
	['site-next/mentions.schema.json', IssueMentionsDataSchema],
	['site-next/life-events.schema.json', IssueLifeEventsDataSchema],
	['site-next/shared-record.schema.json', SharedRecordSchema],
];
for (const [path, schema] of exports) {
	// Zod "JSON Schema", https://zod.dev/json-schema: the options pruzhany-steps records.
	const shape = z.toJSONSchema(schema, { target: 'draft-2020-12', io: 'output' });
	await mkdir(join(destination, path, '..'), { recursive: true });
	await Bun.write(join(destination, path), JSON.stringify(shape, null, '\t') + '\n');
}
