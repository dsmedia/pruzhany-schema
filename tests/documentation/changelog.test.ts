import { readFileSync } from 'node:fs';
import { describe, expect, test } from 'vitest';

// Keep a Changelog 1.1.0, read 1 November 2026:
// https://keepachangelog.com/en/1.1.0/ (headings, dates, ordering and six change types).
function checkChangelog(markdown: string): void {
	const subsections = new Set(['Added', 'Changed', 'Deprecated', 'Removed', 'Fixed', 'Security']);
	let releases = 0;
	let previousDate = '9999-12-31';
	let previousVersion: number[] | undefined;
	let seen = new Set<string>();
	for (const line of markdown.split('\n')) {
		if (!/^\s*#/.test(line)) continue;
		if (line === '# Changelog' && !releases) continue;
		if (line.startsWith('### ')) {
			const name = line.slice(4);
			if (!releases || !subsections.has(name) || seen.has(name)) {
				throw new Error(`invalid or repeated subsection: ${line}`);
			}
			seen.add(name);
			continue;
		}
		if (!releases) {
			if (line !== '## [Unreleased]') throw new Error('first section must be ## [Unreleased]');
		} else {
			const release =
				/^## \[((?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*))\] - (\d{4}-\d{2}-\d{2})$/.exec(
					line
				);
			if (!release) throw new Error(`invalid release heading: ${line}`);
			const version = release[1].split('.').map(Number);
			const day = release[2];
			const date = new Date(`${day}T00:00:00Z`);
			if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== day) {
				throw new Error(`invalid release date: ${day}`);
			}
			if (day > previousDate) throw new Error('release dates must descend');
			if (previousVersion) {
				const order = version.findIndex((part, i) => part !== previousVersion![i]);
				if (order === -1 || version[order] > previousVersion[order]) {
					throw new Error('release versions must strictly descend');
				}
			}
			previousDate = day;
			previousVersion = version;
		}
		releases++;
		seen = new Set();
	}
	if (!releases) throw new Error('missing ## [Unreleased]');
}

describe('CHANGELOG form (bin/verify zod)', () => {
	test('the repository changelog follows the form', () => {
		checkChangelog(readFileSync(new URL('../../CHANGELOG.md', import.meta.url), 'utf8'));
	});
	test('accepts an empty Unreleased and all six change types', () => {
		checkChangelog('## [Unreleased]');
		checkChangelog(
			'## [Unreleased]\n## [1.1.0] - 2026-10-31\n' +
				['Added', 'Changed', 'Deprecated', 'Removed', 'Fixed', 'Security']
					.map((name) => `### ${name}\n- Example.\n`)
					.join('') +
				'## [1.0.0] - 2026-10-26'
		);
	});
	test.each([
		['missing Unreleased', '# Changelog'],
		['a release before Unreleased', '## [1.0.0] - 2026-10-20\n## [Unreleased]'],
		['duplicate Unreleased', '## [Unreleased]\n## [Unreleased]'],
		['unbracketed version', '## [Unreleased]\n## 1.0.0 - 2026-10-20'],
		['missing patch version', '## [Unreleased]\n## [1.0] - 2026-10-20'],
		['wrong release depth', '## [Unreleased]\n# [1.0.0] - 2026-10-20'],
		['missing date', '## [Unreleased]\n## [1.0.0]'],
		['non-ISO date', '## [Unreleased]\n## [1.0.0] - 20 October 2026'],
		['impossible date', '## [Unreleased]\n## [1.0.0] - 2026-02-30'],
		['ascending versions', '## [Unreleased]\n## [1.1.0] - 2026-10-31\n## [1.3.0] - 2026-10-26'],
		['repeated version', '## [Unreleased]\n## [1.0.0] - 2026-10-31\n## [1.0.0] - 2026-10-26'],
		['ascending dates', '## [Unreleased]\n## [1.0.1] - 2026-10-20\n## [1.0.0] - 2026-10-21'],
		['unknown subsection', '## [Unreleased]\n### Improved'],
		['wrong subsection depth', '## [Unreleased]\n#### Added'],
		['subsection before a release', '### Added\n## [Unreleased]'],
		['repeated subsection', '## [Unreleased]\n### Added\n### Added'],
	])('refuses planted fault: %s', (_, markdown) => {
		expect(() => checkChangelog(markdown)).toThrow();
	});
});
