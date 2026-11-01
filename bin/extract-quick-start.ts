import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

/** Return the README's shell commands verbatim; never execute partial/missing input. */
export function extractQuickStart(markdown: string): string {
	const begin = '<!-- quick-start:begin -->';
	const end = '<!-- quick-start:end -->';
	if (markdown.split(begin).length !== 2 || markdown.split(end).length !== 2) {
		throw new Error('expected exactly one pair of quick-start markers');
	}
	const start = markdown.indexOf(begin) + begin.length;
	const finish = markdown.indexOf(end);
	if (finish < start) throw new Error('quick-start markers are reversed');
	const block = markdown.slice(start, finish).trim();
	const match = /^```sh\n([\s\S]*?)\n```$/.exec(block);
	if (!match || match[1].includes('```')) {
		throw new Error('quick start must contain exactly one fenced sh block');
	}
	const commands = match[1]
		.split('\n')
		.filter((line) => line.trim() && !line.trim().startsWith('#'));
	if (commands.length < 1 || commands.length > 5) {
		throw new Error('quick start must contain one to five command lines');
	}
	return match[1] + '\n';
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
	try {
		if (process.argv.length !== 3)
			throw new Error('usage: bun bin/extract-quick-start.ts README.md');
		process.stdout.write(extractQuickStart(readFileSync(process.argv[2], 'utf8')));
	} catch (error) {
		console.error(`quick start: ${(error as Error).message}`);
		process.exitCode = 1;
	}
}
