"""Whether a citation's quote may be shown; the twin of zod/quote-publication.ts."""
from .sourced_entities import Citation, Source


def _private(source: Source | None) -> bool:
    return bool(source and source.private)


def quote_shown(citation: Citation, source: Source, via: Source | None, corroborated: bool) -> bool:
    """The owner's word of 24 October 2026: "Yes they may if unique information"."""
    if not citation.quote:
        return False
    guards = [s for s in (source, via) if _private(s)]
    if any(not s.quotes_cleared for s in guards):
        return False
    if any(s.quote_condition == 'unique_information' for s in guards) and corroborated:
        return False
    return True


def corroborated(record, fact) -> bool:
    """Another accepted statement of the same kind about the same subject rests on a public source."""
    sources = {s.id: s for s in record.sources}
    return any(
        other.id != fact.id and other.status == 'accepted' and other.subject_id == fact.subject_id
        and other.type == fact.type
        and any(c.source_id in sources and not _private(sources[c.source_id])
                and not (c.via and _private(sources.get(c.via))) for c in other.citations)
        for other in record.facts)
