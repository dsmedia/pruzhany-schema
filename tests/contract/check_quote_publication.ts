import { readFileSync } from 'node:fs';
import { CitationSchema, SourceSchema } from '../../zod/sourced-entities.schema';
import { quoteShown } from '../../zod/quote-publication';
const cases = JSON.parse(readFileSync(0, 'utf8'));
console.log(
	JSON.stringify(
		cases.map((c: { citation: unknown; source: unknown; via?: unknown; corroborated: boolean }) =>
			quoteShown(
				CitationSchema.parse(c.citation),
				SourceSchema.parse(c.source),
				c.via ? SourceSchema.parse(c.via) : undefined,
				c.corroborated
			)
		)
	)
);
