import { readFileSync } from 'node:fs';
import { CitationSchema, SourceSchema } from '../../zod/sourced-entities.schema';
import { statementCitationShortfalls } from '../../zod/citation-requirements';
const cases = JSON.parse(readFileSync(0, 'utf8'));
console.log(
	JSON.stringify(
		cases.map((c: { citation: unknown; source: unknown; via?: unknown; valid?: boolean }) =>
			c.valid === false
				? { valid: CitationSchema.safeParse(c.citation).success }
				: statementCitationShortfalls(
						CitationSchema.parse(c.citation),
						SourceSchema.parse(c.source),
						c.via ? SourceSchema.parse(c.via) : undefined
					)
		)
	)
);
