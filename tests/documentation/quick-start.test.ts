import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { describe, expect, test } from 'vitest';
import { extractQuickStart } from '../../bin/extract-quick-start';

const begin = '<!-- quick-start:begin -->';
const end = '<!-- quick-start:end -->';
const readme = (commands: string) => [begin, '```sh', commands, '```', end].join('\n');
const extractor = fileURLToPath(new URL('../../bin/extract-quick-start.ts', import.meta.url));

describe('README quick start (bin/verify zod)', () => {
	test('extracts the repository commands', () => {
		const commands = extractQuickStart(
			readFileSync(new URL('../../README.md', import.meta.url), 'utf8')
		);
		expect(commands.trim()).not.toBe('');
	});
	test('preserves shell text verbatim', () => {
		const commands = '# comment\nprintf "hello\\n"\n\n  true';
		expect(extractQuickStart(readme(commands))).toBe(commands + '\n');
	});
	test.each([
		['no markers', '```sh\ntrue\n```'],
		['no end marker', [begin, '```sh', 'true', '```'].join('\n')],
		['duplicate markers', readme('true') + readme('false')],
		['reversed markers', [end, '```sh', 'true', '```', begin].join('\n')],
		['no block', `${begin}\ntrue\n${end}`],
		['wrong language', readme('true').replace('```sh', '```bash')],
		['unclosed block', readme('true').replace('\n```\n', '\n')],
		['two blocks', readme('true\n```\n```sh\nfalse')],
		['empty block', readme('')],
		['too many command lines', readme(Array(6).fill('true').join('\n'))],
	])('refuses planted fault: %s', (_, markdown) => {
		expect(() => extractQuickStart(markdown)).toThrow();
	});
	test('the CLI refuses a planted README lacking markers, emitting no commands', () => {
		const directory = mkdtempSync(join(tmpdir(), 'schema-quick-start-'));
		try {
			const path = join(directory, 'README.md');
			writeFileSync(path, '```sh\ntrue\n```\n');
			const result = spawnSync('bun', [extractor, path], { encoding: 'utf8' });
			expect(result.status).toBe(1);
			expect(result.stdout).toBe('');
			expect(result.stderr).toContain('markers');
		} finally {
			rmSync(directory, { recursive: true, force: true });
		}
	});
	test.each(['false', 'false | cat', 'echo "$QUICK_START_UNSET_TEST_VARIABLE"'])(
		'a failing README command fails the workflow shell: %s',
		(command) => {
			const directory = mkdtempSync(join(tmpdir(), 'schema-quick-start-'));
			try {
				const path = join(directory, 'README.md');
				const script = join(directory, 'quick-start.sh');
				writeFileSync(path, readme(command + '\nprintf unexpected'));
				const extracted = spawnSync('bun', [extractor, path], { encoding: 'utf8' });
				expect(extracted.status).toBe(0);
				writeFileSync(script, extracted.stdout);
				const result = spawnSync('bash', ['-euo', 'pipefail', script], { encoding: 'utf8' });
				expect(result.status).not.toBe(0);
				expect(result.stdout).not.toContain('unexpected');
			} finally {
				rmSync(directory, { recursive: true, force: true });
			}
		}
	);
});
