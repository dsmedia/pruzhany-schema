import requirements from '../vocabulary/citation-requirements.json' with { type: 'json' };
import type { Citation, Source } from './sourced-entities.schema';
import type { SharedRecord } from './shared-record.schema';

type Rule = {
	required: string[][];
	online?: string[][];
	by_source?: Record<string, string[][]>;
	host?: boolean;
	evidence?: boolean;
	family_transcript_requires_via?: boolean;
	// A source-specific override (the family's own register): its quote is cleared only when quoted.
	private_quote_clearance?: 'when_quoted';
};

/** Advisory shortfalls for a statement, never a schema refinement or publication permission. */
export function statementCitationShortfalls(
	citation: Citation,
	source: Source,
	via?: Source
): string[] {
	const kind = (requirements.kinds as Record<string, Rule>)[source.kind];
	if (!kind) return ['source.kind'];
	const overrides = (requirements as { source_overrides?: Record<string, Partial<Rule>> })
		.source_overrides;
	const rule: Rule = { ...kind, ...(overrides?.[source.id] ?? {}) };
	const values: Record<string, unknown> = { citation, source, via };
	const present = (field: string): boolean => {
		const [scope, key] = field.split('.');
		const value = (values[scope] as Record<string, unknown> | undefined)?.[key];
		return typeof value === 'string' ? !!value.trim() : !!value;
	};
	const groups = [
		...rule.required,
		...(rule.by_source?.[source.id] ?? []),
		...(citation.url ? (rule.online ?? []) : []),
	];
	const missing = groups.filter((group) => !group.some(present)).map((group) => group.join(' or '));
	if (rule.evidence === false) missing.push('source is provenance, not statement evidence');
	if (rule.host) {
		if (!source.host) missing.push('source.host');
		else if (citation.url) {
			const host = new URL(citation.url).hostname.replace(/^www\./, '');
			if (host !== source.host && !host.endsWith(`.${source.host}`))
				missing.push('citation.url on source.host');
		}
	}
	if (
		requirements.private_quote_clearance &&
		(citation.quote || rule.private_quote_clearance !== 'when_quoted')
	) {
		if (source.private && !source.quotes_cleared) missing.push('source.quotes_cleared');
		if (via?.private && !via.quotes_cleared) missing.push('via.quotes_cleared');
	}
	// A transcript cited directly is a declared reading of a derivative. No inference from locator text.
	if (
		rule.family_transcript_requires_via &&
		source.private &&
		source.derived_from?.some((d) => d.relation === 'transcription') &&
		!citation.via
	)
		missing.push('cite original with citation.via for family transcript');
	return [...new Set(missing)];
}

export function sharedRecordCitationShortfalls(record: SharedRecord) {
	const sources = new Map(record.sources.map((s) => [s.id, s]));
	const persons = new Set(record.persons.map((p) => p.id));
	return record.facts
		.filter(
			(f) =>
				f.status === 'accepted' &&
				persons.has(f.subject_id) &&
				requirements.statement_types.includes(f.type)
		)
		.flatMap((fact) =>
			fact.citations.flatMap((citation, index) => {
				const source = sources.get(citation.source_id);
				const shortfalls = source
					? statementCitationShortfalls(
							citation,
							source,
							citation.via ? sources.get(citation.via) : undefined
						)
					: ['unknown citation source'];
				return shortfalls.length
					? [{ fact_id: fact.id, citation_index: index, source_id: citation.source_id, shortfalls }]
					: [];
			})
		);
}
