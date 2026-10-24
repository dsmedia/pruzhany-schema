"""Advisory statement citation shortfalls, from the same table as Zod; never a refusal."""
from urllib.parse import urlsplit
from .sourced_entities import CITATION_REQUIREMENTS, Citation, Source


def statement_citation_shortfalls(citation: Citation, source: Source, via: Source | None = None) -> list[str]:
    kind = CITATION_REQUIREMENTS['kinds'].get(source.kind)
    if kind is None:
        return ['source.kind']
    # A source-specific override (the family's own register), as the Zod twin applies it.
    rule = {**kind, **CITATION_REQUIREMENTS.get('source_overrides', {}).get(source.id, {})}
    values = {'citation': citation, 'source': source, 'via': via}
    def present(field):
        scope, key = field.split('.')
        value = getattr(values[scope], key, None)
        return bool(value.strip() if isinstance(value, str) else value)
    groups = [*rule['required'], *rule.get('by_source', {}).get(source.id, []),
              *(rule.get('online', []) if citation.url else [])]
    missing = [' or '.join(group) for group in groups if not any(present(field) for field in group)]
    if rule.get('evidence') is False:
        missing.append('source is provenance, not statement evidence')
    if rule.get('host'):
        if not source.host:
            missing.append('source.host')
        elif citation.url:
            host = (urlsplit(citation.url).hostname or '').removeprefix('www.')
            if host != source.host and not host.endswith('.' + source.host):
                missing.append('citation.url on source.host')
    if CITATION_REQUIREMENTS['private_quote_clearance'] and (
            citation.quote or rule.get('private_quote_clearance') != 'when_quoted'):
        if source.private and not source.quotes_cleared:
            missing.append('source.quotes_cleared')
        if via and via.private and not via.quotes_cleared:
            missing.append('via.quotes_cleared')
    if (rule.get('family_transcript_requires_via') and source.private and
            any(d.relation == 'transcription' for d in source.derived_from or []) and not citation.via):
        missing.append('cite original with citation.via for family transcript')
    return list(dict.fromkeys(missing))


def shared_record_citation_shortfalls(record) -> list[dict]:
    sources = {s.id: s for s in record.sources}
    persons = {p.id for p in record.persons}
    result = []
    for fact in record.facts:
        if (fact.status != 'accepted' or fact.subject_id not in persons or
                fact.type not in CITATION_REQUIREMENTS['statement_types']):
            continue
        for index, citation in enumerate(fact.citations):
            source = sources.get(citation.source_id)
            shortfalls = (statement_citation_shortfalls(citation, source, sources.get(citation.via))
                          if source else ['unknown citation source'])
            if shortfalls:
                result.append(dict(fact_id=fact.id, citation_index=index, source_id=citation.source_id,
                                   shortfalls=shortfalls))
    return result
