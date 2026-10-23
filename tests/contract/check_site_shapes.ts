// The contract step supplies fictional JSON; this runner needs only bun.
import { readFileSync } from 'node:fs';
import { z } from 'zod/v4';
import * as schemas from '../../zod/index';

const cases = JSON.parse(readFileSync(0, 'utf8')) as {
	name: string;
	model: string;
	value: unknown;
}[];
const results = cases.map((c) => {
	const schema = schemas[`${c.model}Schema` as keyof typeof schemas] as z.ZodType;
	const parsed = schema.safeParse(c.value);
	return {
		name: c.name,
		valid: parsed.success,
		value: parsed.success ? parsed.data : null,
		error: parsed.success ? '' : parsed.error.issues.map((i) => i.message).join('; '),
	};
});

const basis = {
	source_text: 'Original text',
	addresses: [
		{
			image_uri: 'fictional.png',
			bbox: [0, 0, 1, 1] as [number, number, number, number],
			text: 'Original text',
		},
	],
};
if (
	!schemas.textBasisMatches(basis, 'Original text') ||
	schemas.textBasisMatches(basis, 'Changed text')
)
	throw new Error('text basis must detect a rereading');
const rich = cases.find((c) => c.name === 'all hand-written forms remain sourced and pending');
if (rich) {
	const record = schemas.SharedRecordSchema.parse(rich.value);
	const prose = record.facts.filter((f) => f.representation === 'prose');
	if (prose.length !== 3 || !prose.every(schemas.isUnreviewedProse))
		throw new Error('unreviewed prose must stay identifiable as unreviewed');
}
const laterNaming = cases.find(
	(c) => c.name === 'local 13: later naming on the same child id retains supplied description'
);
if (laterNaming) {
	const child = schemas.SiteArchiveSchema.parse(laterNaming.value).shared_record.persons[2];
	if (
		child.names
			.filter(schemas.isPrintedName)
			.map((n) => n.value)
			.join() !== 'צעסקעלע'
	)
		throw new Error('a supplied description must never enter the printed-name match set');
}
process.stdout.write(JSON.stringify(results));
