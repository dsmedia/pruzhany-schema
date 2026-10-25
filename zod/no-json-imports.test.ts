import { describe, expect, it } from 'vitest';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

// The site's Playwright tests load these modules through Node's ESM loader, which refuses a JSON
// import without an import attribute; a table is generated as a module instead
// (vocabulary/generate.py).
describe('the vendored Zod tree', () => {
	it('imports no JSON file', () => {
		// __dirname: Bun and Vitest both give it to a module, where the site's jsdom tests give
		// import.meta.url another scheme.
		const dir = __dirname;
		const offenders = readdirSync(dir)
			.filter((name) => name.endsWith('.ts'))
			.filter((name) => /from\s+['"][^'"]+\.json['"]/.test(readFileSync(join(dir, name), 'utf8')));
		expect(offenders).toEqual([]);
	});
});
