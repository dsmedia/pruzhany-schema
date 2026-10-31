// Cross-language harness; no subprocess or Python dependency in zod/.
import { readFileSync } from 'node:fs';
import { CitationSchema, SiteCitationSchema } from '../../zod/index';
import { addEnglishIssues } from '../../zod/words-english';
const cases = JSON.parse(readFileSync(0, 'utf8')) as {
	model: 'Citation' | 'SiteCitation';
	value: unknown;
}[];
process.stdout.write(
	JSON.stringify(
		cases.map(
			({ model, value }) =>
				(model === 'Citation' ? CitationSchema : SiteCitationSchema)
					.superRefine((v, ctx) => addEnglishIssues(model, v, ctx, true))
					.safeParse(value).success
		)
	)
);
