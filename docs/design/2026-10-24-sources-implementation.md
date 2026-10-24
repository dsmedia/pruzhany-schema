# Sources, holders and citations: the implemented contract

24 October 2026. Implements the agreed sources design, including its later two
refusals. The design note is retained unchanged; the implementation records its
wire choices here. The owner's proposed source kinds remain unreleased.

## Holders and source ancestry

`SharedRecord.holders` is optional when reading an older record (empty by default
in Pydantic). A holder has `id`, `name`, `kind` (`institution`, `family`, `private`),
and optional `short_name`, `host` and `identifiers`. A private holder's name never
needs to be public. No consumer may infer publication permission from a name.

Holder identifiers reuse `PlaceIdentifier` exactly: `source_id`, `value`, optional
HTTPS `url`, `accessed`, and `attribution: {by, on, note?}`. They require a registered
authority source, an address on that source's host, uniqueness within the holder,
and no sharing of the same identifier between two holders. Holder ids share the
record's id namespace. They are identifiers on evidence, not equivalence claims.

Sources gain `short_name`, `holder_id`, `reference_code`, `language` (a nonempty
list of BCP 47 language tags), `derived_from` (a nonempty list of
`{source_id, relation: copy | transcription}`), `dated`, `quotes_cleared` and
`private`. `dated` uses the existing `SourcedDate`, including partial dates and
printed words. `quotes_cleared` uses the existing `Attribution`: the owner's word
and its day, never a boolean guessed from possession of a document. Language tags
are checked against RFC 5646's syntax, not against a changing language registry.

Every `holder_id` and derived source must resolve. An ancestry cycle is refused.
The shared record checks every citation's `via`: it must be registered and have a
direct `derived_from` link to that citation's original. A fact cannot cite a source
both as `via` and as another original on the same statement. Separate statements
may cite that source for what it says in its own right.

`ehri_institution_id` is removed: neither the registry nor the site's current
record used it. `repository` remains readable for one release. The site's
`src/lib/privacy/projection.ts` still carries it, and steps' retained
`handmade_research.py` still reads it. New registry entries use `holder_id`;
the writer removes the obsolete text when a registered holder replaces it.

## Citations and the advisory table

New citation fields are `via`, `reference_code`, `record_type`, `quote_language`,
`public_note` and `locator`. Both `reference_code` and `locator` satisfy the existing
minimum locator refinement. The archive's own number stays in `record_id`. Folios,
chapters, named parts and photograph sides use `page`. Internal paths and register
entry pointers use `locator`, which is private like `note`. `public_note` is our
reviewed explanation; `quote` remains the record's own words.

`vocabulary/citation-requirements.json` is the single §3.4 table. Zod's
`statementCitationShortfalls` and Pydantic's `statement_citation_shortfalls` read
it, returning missing requirements. Whole-record helpers report accepted facts
about a person's life, with the fact id and citation index. These reports do not
reject incomplete evidence or grant publication permission. Existing refinements
and the reference refusals still apply. A private original or `via` needs its own
quote clearance. A directly cited private oral-history transcript is reported as
needing the original with `via`; the checker never guesses this from locator text.
A research letter may cite other records and also state findings of its own.

The table includes the proposed `archival_record` and `provenance` rows to record
the complete design. Neither value is accepted by the released `SourceKinds`.
Until approval, a source kept as `archive_database` is measured against that row,
even when its eventual archival-record row would have fewer shortfalls. Steps
excludes known provenance producers from its evidence counts by their registered
identity, never by the shape of a citation value.

## Standards and consumers

Mappings in `vocabulary/site-content.json` use only the pinned `standards/`:
EHRI 0.2.0's `Institution`, `Family`, `isCopyOf`; RiC-O 1.1's `Person`,
`hasOrHadHolder`, `hasOrHadIdentifier`, `hasOrHadLanguage`,
`hasDocumentaryFormType`, `hasCreationDate` and `describesOrDescribed`.
Display and privacy fields have explained local profile terms. A transcription
describes its original; it is not asserted to be a copy.

Fictional fixtures cover the new shapes, references, cycles, host and identifier
rules, language tags and advisory gaps in both runtimes. `bin/verify` runs these
alongside all existing checks and the standards alignment gate. Steps exports the
table and holder shape through `site_shapes refresh`, after this schema has a
clean committed HEAD. Preview exports cannot advance that recorded pin.
