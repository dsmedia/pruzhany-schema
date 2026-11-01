<!-- Keep a Changelog 1.1.0, https://keepachangelog.com/en/1.1.0/, read 1 November 2026. -->
<!-- Sources: git log --merges and first-parent PR titles, read 1 November 2026;
the site-switch removal c835099 is an ancestor of merge 77c1b9e. -->
# Changelog

Notable merged changes follow Keep a Changelog 1.1.0. This repository has made no release
yet. The vocabularies are versioned on their own; their releases are recorded in the
[approval record](docs/vocabulary-approvals.md).

## [Unreleased]

### Added

- LinkML definitions, generated contracts, data dictionary and public RDF view ([#29](https://github.com/dsmedia/pruzhany-schema/pull/29), [#32](https://github.com/dsmedia/pruzhany-schema/pull/32)).
- Physical pages, model exchanges and structured answers in LinkML ([#36](https://github.com/dsmedia/pruzhany-schema/pull/36), [#39](https://github.com/dsmedia/pruzhany-schema/pull/39), [#44](https://github.com/dsmedia/pruzhany-schema/pull/44)).
- Person/organisation identifiers and retained merged identifiers; content-item language ([#47](https://github.com/dsmedia/pruzhany-schema/pull/47), [#57](https://github.com/dsmedia/pruzhany-schema/pull/57)).

### Changed

- Generate Python and Zod fields from LinkML, retaining runtime validation rules ([#30](https://github.com/dsmedia/pruzhany-schema/pull/30), [#42](https://github.com/dsmedia/pruzhany-schema/pull/42)).
- Require English renderings of non-English citation quotes; check public JSON-LD with an offline processor ([#55](https://github.com/dsmedia/pruzhany-schema/pull/55), [#59](https://github.com/dsmedia/pruzhany-schema/pull/59)).

### Removed

- Old persisted article, content-unit, life-event, enrichment and edition-bundle contracts after the [site switch](https://github.com/dsmedia/pruzhany-schema/commit/c835099807cd9979e4113b66ff3ea2cb932f41ce).
