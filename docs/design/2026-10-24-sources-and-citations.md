# Sources and citations: what a source is, and what citing one must carry

**Status:** draft for review by the site-redesign session (24 October 2026). Not built. The owner asked on 24 October
2026, in their own words, that the two sessions "coordinate … on data model of sources and sourcing". The council run
`docs/council/runs/2026-10-24-sources/` of pruzhany-svelte is out on the same question; its decisions are folded in
before this is final (§9).

## 1. Why

Today a source is one flat registry entry and a citation is any one locator out of six (`validateCitation`: record id,
page, scan, time, unit id or url). Three faults follow, each seen on Shulim Judewicz's page:

- **A copy stands in for its original.** `sachsenhausen-memorial-2022` is the memorial's letter of 2022, but what the
  family's statements rest on are the two documents it copies: the arrival list of 27.10.1944 (Russian State Military
  Archive, 1367/2/1a, Bl. 15) and the transport list of 13.11.1944 (FSB archive, N 19092/Tom 90, Bl. 107). The owner
  agreed on 24 October 2026 that the page shows each original with its signature, "as the Sachsenhausen Memorial copied
  it for the family, 2022" (pruzhany-steps `.scratch/site-redesign/grilling.md`, "The memorials' letters on Shulim's
  page"), and recalls that the transport list may have reached the family from the National Archives or the USHMM
  through a researcher they paid.
- **The holder is free text.** `repository` reads "the family's papers", "USC Shoah Foundation; its transcript in the
  family's papers", "Yad Vashem": an institution, a copy's whereabouts and a private holder in one field. The site keeps
  a hand table (`record-words.ts`) to say "The Bergen-Belsen Memorial's book of the dead says:".
- **Nothing says what a citation of a kind must carry.** A memorial-book death may cite a page with no words; a
  testimony may cite "the family's typed transcript" with no minute of the recording.

## 2. What the standards say (read from `standards/`, 24 October 2026)

From `rico-1.1-axioms.json` (RiC-O 1.1, the version EHRI 0.2.0 imports):

- `rico:isEvidencedBy`: domain `Relation`, range `RecordResource`. A statement's evidence is a record resource;
  `Record`, `RecordPart` and `RecordSet` are its subclasses. A citation therefore names a record resource, and a
  locator inside it is a `RecordPart` (a folio, a page, an entry).
- `rico:isCopyOf` / `rico:hasCopy`: domain and range `RecordResource`, subproperties of
  `hasGeneticLinkToRecordResource`. A copy is a record resource of its own, linked to its original.
- `rico:hasOrHadHolder`: domain `RecordResource` or `Instantiation`, range `Agent`.
- `rico:hasOrHadIdentifier` → `rico:Identifier`: an archive's signature is an identifier of the record.
- `rico:hasOrHadLanguage`: domain `Agent`, `Record`, `RecordPart`.
- `rico:isOrWasDerivedFromInstantiation`: Instantiation to Instantiation (a scan of a photocopy).

From `ehri-0.2.0.json`: `ehri:isCopyOf` / `ehri:hasCopy` (subproperties of RiC-O's) with `ehri:IsCopyOfRelation`, new in
0.2.0 for exactly this case: Holocaust archives hold copies of originals held elsewhere. `ehri:Institution` (a
`CorporateBody` and a schema.org `ArchiveOrganization`) is the holder of archival material; `ehri:locationOfOriginals`
and `ehri:locationOfCopies` describe it in prose. By the owner's rule (prefer EHRI, then RiC-O in EHRI's version, then
a local term with a reason), copies map to `ehri:isCopyOf` and archive holders to `ehri:Institution`.

## 3. The model

Three parts of the source registry (`corrections/people/sources.json` in pruzhany-steps, written into the shared record),
and one change to the citation.

### 3.1 Holder (new): who holds a source

| field | meaning | maps to |
|---|---|---|
| `id` | stable, address-ready (`holder-arolsen-archives`) | — |
| `name`, `short_name` | "Arolsen Archives"; the site's display name | `rico:hasOrHadName` |
| `kind` | `institution`, `family`, `private` (a person or researcher, never published by name) | `ehri:Institution`, `ehri:Family`, `rico:Person` |
| `ehri_institution_id` | where EHRI has one | `rico:hasOrHadIdentifier` |
| `host` | its web host, the one gate for its addresses | — |

`Source.ehri_institution_id` moves here; `Source.repository` becomes `holder_id`.

### 3.2 Source: a record resource we cite

Existing fields stay (`id`, `kind`, `title`, `author`, `editor`, `published`, `work_id`, `url_pattern`, `host`). New:

| field | meaning | maps to |
|---|---|---|
| `short_name` | the site's "who says it": "the Bergen-Belsen Memorial's book of the dead" | — (display) |
| `holder_id` | its holder (§3.1) | `rico:hasOrHadHolder` |
| `reference` | the archive's signature, as written: "1367/2/1a" | `rico:hasOrHadIdentifier` |
| `language` | the record's languages, BCP 47 (`de`, `yi`, `pl`) | `rico:hasOrHadLanguage` |
| `copy_of` | for a copy that is itself registered, its original | `ehri:isCopyOf` |
| `private` | the document itself is never shown (the family's papers); only quotes the owner allows | — |

A **new source kind** is proposed to the owner's batch (#16): `archival_record`, a document held by an archive and cited
by its signature (the arrival list, the transport list, the Ohrdruf Nordlager list), mapped to `rico:Record`. Until it is
approved such a document stays `archive_database` with a `proposed_type`-style note in the batch.

### 3.3 Citation: one statement's evidence

Existing locators stay. Changes:

| field | meaning | maps to |
|---|---|---|
| `source_id` | the record the statement rests on: the **original** where known | `rico:isEvidencedBy` |
| `via` (new) | the source through which we read it: the copy the family holds, the letter that enclosed it | the copy `ehri:isCopyOf` the original |
| `quote_language` (new) | where the quote's language is not the source's (a translation) | `rico:hasOrHadLanguage` |
| `note` | ours, private, as today | — |
| `public_note` (new) | ours, written for the page (how two prisoner numbers tie the papers to him) | — |

`via` names a registered source, so a letter that copies two documents is registered once and cited as `via` on both.
A chain (a researcher's copy of the NARA copy of an original) is one `via` to the source the family holds, and that
source's own `copy_of` and `holder_id` carry the rest.

### 3.4 What each kind of source must carry when it is cited

Required for a **statement** (a fact about a person's life: death, removal, birth, marriage, residence, occupation);
a bare link to a record (an archive reference with no claim drawn from it) needs only the first column's locator.

| kind | locator | quote | accessed | url | other |
|---|---|---|---|---|---|
| `the_paper` | `unit_id`, `edition_date` | required | — | — | — |
| `archive_database` | `record_id` | required | required | required, on its host | — |
| `archival_record` | `record_id` (folio, page, entry) | required | — | if online | `via` when read from a copy |
| `memorial_book` | page | required | when read online | optional | `scan` optional |
| `oral_history` | `time` (minute of the recording) or a transcript page | required | — | — | `via` when read from a family transcript |
| `memoir` | chapter or page | required | — | — | — |
| `family_document` | `record_id` | required | — | — | source `private` |
| `web_page` | — | required | required | required, on its host | — |
| `book`, `press`, `photograph` | page / edition / side | required (a photograph: its inscription) | — | — | — |

Checked by the writer, in Zod and Pydantic both, from one table in the schema repository.

## 4. Measured: today's accepted statements against §3.4

From the shared record as the site holds it (master `f34d4a57`), accepted facts about a person's life, preserved
witnesses aside:

| kind | statements | pass | what the rest lack |
|---|---|---|---|
| the paper | 2,243 | 2,243 | — |
| archive databases | 363 | 263 | 100 have no quote and no day read: older links to Yad Vashem and Arolsen made before 24 October |
| memorial books | 108 | 42 | 66: most have a page and no quote, 2 no page |
| spoken testimony | 33 | 14 | 19 cite "the family's typed transcript" with no minute |
| the family register | 32 | 5 | 27 are the register's own word, cited to the person's entry, no quote |
| memoir, web page, book | 21 | 21 | — |

The rule would refuse 212 of 2,800 today. The plan (§6) reads them again or marks them as what they are, never
relaxes the rule.

## 5. Shulim's records under the model

- Arrival at Sachsenhausen: `source_id` = the arrival list (kind `archival_record`, holder the Russian State Military
  Archive, reference `1367/2/1a`), `record_id` "Bl. 15", the list's words as quote, `via` = `sachsenhausen-memorial-2022`.
- Sachsenhausen to Ohrdruf: `source_id` = the transport list (holder the FSB archive, reference `N 19092/Tom 90`),
  `record_id` "Bl. 107", `via` = the copy the family's papers show it came from (the memorial's letter, or the
  researcher's NARA/USHMM copy, to be read before it is written).
- Ohrdruf: `source_id` = the Nordlager list of 24.12.1944 (holder the Arolsen Archives, its DocID), `public_note` = the
  Buchenwald letter's identification by the two prisoner numbers, 110849 and 103878; the letter is the `via`.
- "Possibly 26 October": stays accepted with evidence `possible`; it does not contradict the list (it is the day the
  transport left Auschwitz). The site does not show a possible removal a recorded one covers.

## 6. Order of work, once agreed

1. Schema: `Holder`, the new `Source` and `Citation` fields, the per-kind table and its checks, Zod and Pydantic twins,
   the alignment mappings (`ehri:isCopyOf`, `rico:hasOrHadHolder`, `rico:hasOrHadIdentifier`, `rico:hasOrHadLanguage`),
   `bin/verify`. The rule first reports, then refuses, once the gaps are closed.
2. Steps: the registry's holders and sources; Shulim's statements as in §5; then the gaps of §4, read again where a
   record can be read (the 66 memorial-book citations, the 100 archive links), marked where it cannot.
3. Site: `record-words.ts` replaced by `short_name` and the holder's name; signatures published; `via` and
   `public_note` rendered; `note` stays private.
4. The owner's batch: `archival_record`, with two or three real examples and its mapping.

## 7. Private, never published

Citation `note`; a `private` source as a document (only its quotes the owner allows); a `private` holder's name (a
paid researcher) and fees; a living submitter of a Page of Testimony; email and postal details in letters. The
projection publishes `public_note`, `short_name`, the holder's name where `kind` is `institution` or `family`, `reference`
and `record_id`.

## 8. Not now

A page per source or per holder (later; ids are address-ready). Wikidata ids for institutions (after the vetting's
Impresso-2 check). Instantiations (a scan of a photocopy) as their own entities: `via` and `copy_of` carry what the page
needs.

## 9. Open

- The council run's decisions (archives, historian, data, security), to be folded in.
- Whether `via` is the right name; the site reads it as "as <via's short name> copied it for the family".
- Whether a `family` holder is shown by name ("the Sorid family") or as "the family".
