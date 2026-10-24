import type { Citation, Source } from './sourced-entities.schema';
import type { SharedFact, SharedRecord } from './shared-record.schema';

const isPrivate = (s?: Source) => !!s?.private;

/**
 * Whether a citation's quote may be shown. A private source's (or via's) words need the owner's
 * clearance; under the condition 'unique_information' (the owner's word of 24 October 2026:
 * "Yes they may if unique information") only where no other accepted statement of the same
 * kind about the same person rests on a source that is not private.
 */
export function quoteShown(
	citation: Citation,
	source: Source,
	via: Source | undefined,
	corroborated: boolean
): boolean {
	if (!citation.quote) return false;
	const guards = [source, via].filter(isPrivate) as Source[];
	if (guards.some((s) => !s.quotes_cleared)) return false;
	if (guards.some((s) => s.quote_condition === 'unique_information') && corroborated) return false;
	return true;
}

/** Another accepted statement of the same kind about the same subject rests on a public source. */
export function corroborated(record: SharedRecord, fact: SharedFact): boolean {
	const sources = new Map(record.sources.map((s) => [s.id, s]));
	return record.facts.some(
		(other) =>
			other.id !== fact.id &&
			other.status === 'accepted' &&
			other.subject_id === fact.subject_id &&
			other.type === fact.type &&
			other.citations.some(
				(c) =>
					sources.has(c.source_id) &&
					!isPrivate(sources.get(c.source_id)) &&
					!(c.via && isPrivate(sources.get(c.via)))
			)
	);
}
