# Sources and citations: what a source is, and what citing one must carry

**Status:** agreed by the steps and site-redesign sessions on 24 October 2026; built from that day at the owner's "Yes". The owner asked on 24 October
2026, in their own words, that the two sessions "coordinate … on data model of sources and sourcing". It folds in the
decisions of the council run `2026-10-24-sources` (pruzhany-svelte branch `ccr-059c2aef-b1kljr`, commit `d8f43f2e`,
`docs/council/runs/2026-10-24-sources/decisions.md`, with its four reports), cited below as "council".

## 1. Why

Today a source is one flat registry entry and a citation is any one locator out of six (`validateCitation`: record id,
page, scan, time, unit id or url). The council found the model sound for the paper and for databases cited by record
and quote, and not sound in three ways, each seen on Shulim Judewicz's page:

- **A copy stands in for its original.** `sachsenhausen-memorial-2022` is the memorial's letter of 2022, but what the
  family's statements rest on are the two documents it transcribes: the arrival list of 27.10.1944 (Russian State
  Military Archive, 1367/2/1a, Bl. 15) and the transport list of 13.11.1944 (FSB archive, N 19092/Tom 90, Bl. 107). The
  owner agreed on 24 October 2026 that the page shows each original with its reference (pruzhany-steps
  `.scratch/site-redesign/grilling.md`, "The memorials' letters on Shulim's page"), and recalls that the transport list
  may have reached the family from the National Archives or the USHMM through a researcher they paid.
- **The holder is free text.** `repository` has four meanings on 18 sources ("the family's papers", "USC Shoah
  Foundation; its transcript in the family's papers", "Yad Vashem"); `ehri_institution_id` is set on none. The site keeps
  a hand table (`record-words.ts`) to say "The Bergen-Belsen Memorial's book of the dead says:".
- **Public and internal values share fields.** `record_id` holds five kinds of value (a Yad Vashem number, a page, an
  internal path, a person's id, "the family's typed transcript"); the site decides what to publish from a string's shape.
- **Nothing says what a citation of a kind must carry.** A memorial-book death may cite a page with no words; a
  testimony may cite a transcript with no minute of the recording.

The council also corrected a count: of the 482 `web_page` sources, 476 or 477 are the project's own provenance entries
(`issue/<date>`, `static/data/<date>-enrichment.json`) carrying about 259,500 of 273,000 citations; two or three are web
pages.

## 2. What the standards say (read from `standards/`, 24 October 2026)

From `rico-1.1-axioms.json` (RiC-O 1.1, the version EHRI 0.2.0 imports):

- `rico:isEvidencedBy`: domain `Relation`, range `RecordResource`. A statement's evidence is a record resource
  (`Record`, `RecordPart`, `RecordSet`); a folio or entry inside it is a `RecordPart`.
- `rico:isCopyOf` / `rico:hasCopy`: domain and range `RecordResource`.
- `rico:describesOrDescribed`: domain `RecordResource`, range `Thing`. A transcription made by another hand describes
  its original; it is not a copy of it.
- `rico:hasOrHadHolder`: domain `RecordResource` or `Instantiation`, range `Agent`.
- `rico:hasOrHadIdentifier` → `rico:Identifier`: an archive's reference code (ISAD(G) 3.1.1) is one.
- `rico:hasOrHadLanguage`: domain `Agent`, `Record`, `RecordPart`.

From `ehri-0.2.0.json`: `ehri:isCopyOf` / `ehri:hasCopy` (subproperties of RiC-O's, with `ehri:IsCopyOfRelation`), new in
0.2.0 for exactly this case: Holocaust archives hold copies of originals held elsewhere. `ehri:Institution` (a
`CorporateBody` and a schema.org `ArchiveOrganization`) is an archive; `ehri:Family` a family. By the owner's rule
(prefer EHRI, then RiC-O in EHRI's version, then a local term with a reason): copies map to `ehri:isCopyOf`,
transcriptions to `rico:describesOrDescribed`, archive holders to `ehri:Institution`, the family to `ehri:Family`.

## 3. The model

Parts of the source registry (`corrections/people/sources.json` in pruzhany-steps, written into the shared record), and
the citation.

### 3.1 Holder (new): who holds a source

| field | meaning | maps to |
|---|---|---|
| `id` | stable, address-ready (`holder-arolsen-archives`) | — |
| `name`, `short_name` | "Arolsen Archives"; the site's display name | `rico:hasOrHadName` |
| `kind` | `institution`, `family`, `private` (a person or a researcher: never published by name) | `ehri:Institution`, `ehri:Family`, `rico:Person` |
| `identifiers` | as places have them (`source_id`, `value`, `url`, `accessed`, `by`): EHRI institution ids first | `rico:hasOrHadIdentifier` |
| `host` | its web host, the one gate for its addresses | — |

`Source.ehri_institution_id` is retired. Three kinds of identifier, in this order:

1. **EHRI's institution id** (the owner's rule: EHRI first). All nine were read on EHRI's portal
   (`portal.ehri-project.eu/institutions/<id>`) by this session on 24 October 2026, each page giving the institution's
   own name and a persistent ARK (`ark:/41045/…`): RGVA `ru-003203` (Российский государственный военный архив), the
   FSB's central archive `ru-003198`, the Arolsen Archives `de-002409`, the Sachsenhausen Memorial's archive
   `de-002649`, the Buchenwald Memorial's archive `de-002463`, the Bergen-Belsen Memorial `de-002598`, USHMM
   `us-005578`, the Yad Vashem Archives `il-002798`, the National Library of Israel's archives department `il-002794`.
   The ARK is kept beside the id as its `url`.
2. **ISIL** (ISO 15511, the international identifier for libraries and archives) where the institution has one. Read on
   Wikidata on 24 October 2026, not yet on the ISIL agencies' own registers: Arolsen `DE-2379`, the Sachsenhausen
   Memorial `DE-MUS-825314`, the National Library of Israel `IL-NNL`; none found for the others.
3. **Wikidata** later, after the vetting's Impresso-2 check. Today Wikidata links an EHRI id (P14900) for only three
   of the nine (Arolsen, USHMM, RGVA); VIAF and Library of Congress ids exist there for most, and are not used.

"The family's papers" is a `family` holder with no id.

### 3.2 Source: a record resource we cite

Kept: `id`, `kind`, `title`, `editor`, `published`, `work_id` (never published where it is a file name), `url_pattern`,
`host`. Changed and new:

| field | meaning | maps to |
|---|---|---|
| `author` | public: an institution, never a staff member of one (the Buchenwald letter is the Buchenwald Memorial's) | `rico:hasCreator` |
| `short_name` | the site's "who says it": "the Bergen-Belsen Memorial's book of the dead" | — (display) |
| `holder_id` | its holder (§3.1); replaces free-text `repository` | `rico:hasOrHadHolder` |
| `reference_code` | the holder's own reference for the record, as written: "1367/2/1a" | `rico:hasOrHadIdentifier` |
| `language` | the record's languages, BCP 47 (`de`, `yi`, `ru`) | `rico:hasOrHadLanguage` |
| `derived_from` | for a copy or transcription we hold: a list of `{source_id, relation}`, `relation` `copy` or `transcription` | `ehri:isCopyOf`; `rico:describesOrDescribed` |
| `dated` | a letter's or document's own date (a letter is not "consulted") | `rico:hasCreationDate` |
| `quotes_cleared` | quotes from a private document may be published (the owner's word, with its day) | — |
| `private` | the document itself is never shown (the family's papers, letters, privately obtained copies) | — |

**Kinds.** Two new kinds go to the owner's batch (#16), each with real examples and its mapping:
`archival_record`, a document held by an archive and cited by its reference code (the RGVA arrival list, the transport
list in the FSB archive, the Ohrdruf Nordlager list), mapped to `rico:Record`; and `provenance`, the project's own record
of where a value came from (the 476 or 477 `issue/<date>` and old-file entries), never exported as evidence nor named to
the public as a source. Until approved they stay as they are.

### 3.3 Citation: one statement's evidence

| field | meaning | public | maps to |
|---|---|---|---|
| `source_id` | the record the statement rests on: the **original** where known | yes | `rico:isEvidencedBy` |
| `via` (new) | the one source we actually read: a copy or a transcription; its own `derived_from` says which and of what | yes | (on the source) |
| `reference_code` (new) | the holder's reference of the document cited, where the source is a set of many (an Arolsen tree signature) | yes | `rico:hasOrHadIdentifier` |
| `record_id` | the holder's own number for the record: a Yad Vashem record, an Arolsen DocID, a book of the dead's entry; never an internal pointer | yes | `rico:hasOrHadIdentifier` |
| `record_type` (new) | the holder's type of the record: "Page of Testimony", "list" | yes | `rico:hasDocumentaryFormType` |
| `page`, `scan`, `time`, `unit_id`, `edition_date`, `url` | as today; a folio goes in `page` ("Bl. 15") | yes | `RecordPart` |
| `quote` | the record's own words | yes, unless the source is private and not cleared | — |
| `quote_language` (new) | where the quote's language is not the source's (a translation) | yes | `rico:hasOrHadLanguage` |
| `accessed` | the day a person read the record, never the day a line was written | yes | — |
| `public_note` (new) | ours, reviewed, for the page (how two prisoner numbers tie the papers to him) | yes | — |
| `note` | ours, private, as today (414 of 993 notes name a Page of Testimony's giver) | no | — |
| `locator` (new) | an internal pointer (a register entry, a provenance path) moved out of `record_id` | no | — |

Two refusals, so a page never fails to word a citation (the site-redesign session's asks): a citation whose `via`
source has no `derived_from` entry for that citation's `source_id` is refused; and a `via` source is never also cited
as an original for the same statement. Publication is decided by field and by the source's kind and `private` flag,
never by a value's shape. `via` is one
hop: a longer chain (the researcher's copy of the USHMM microfilm of the RGVA original) is followed through the sources'
own `derived_from`, each hop described once.

### 3.4 What each kind of source must carry when it is cited

Required for a **statement** (a fact about a person's life: death, removal, birth, marriage, residence, occupation). A
bare link to a record with no claim drawn from it needs only its locator.

| kind | locator | quote | accessed | url | other |
|---|---|---|---|---|---|
| `the_paper` | `unit_id`, `edition_date` | required | — | — | — |
| `archive_database` | `record_id` | required | required | required, on its host | `record_type` for Yad Vashem; Arolsen's permalink as `url` |
| `archival_record` | `page` (folio, entry) | required | when read online | if online | `via` when read from a copy or transcription; holder and `reference_code` on the source |
| `memorial_book` | `page` | required | when read online | optional | `scan` optional |
| `oral_history` | `time` (in the recording) or a transcript page | required | — | — | `via` when read from a family transcript |
| `memoir` | chapter or `page` | required | — | — | — |
| `family_document` | `page` or a part named | required, cleared | — | — | source `private`, `dated` |
| `web_page` | — | required | required | required, on its host | — |
| `book`, `press`, `photograph` | page / edition / side | required (a photograph: its inscription) | — | — | — |
| `provenance` | `locator` | — | — | — | never evidence for a statement |

Checked by the writer, in Zod and Pydantic both, from one table in the schema repository: first as a report, then as a
refusal once the gaps of §4 are closed.

## 4. Measured: today's accepted statements against §3.4

From the shared record as the site holds it (master `f34d4a57`), accepted facts about a person's life, provenance
entries aside:

| kind | statements | pass | what the rest lack |
|---|---|---|---|
| the paper | 2,243 | 2,243 | — |
| archive databases | 363 | 263 | 100 have no quote and no day read: older links to Yad Vashem and Arolsen |
| memorial books | 108 | 42 | 66: most have a page and no quote, 2 no page |
| spoken testimony | 33 | 14 | 19 cite "the family's typed transcript" with no minute |
| the family register | 32 | 5 | 27 are the register's own word, cited to the person's entry, no quote |
| memoir, web page, book | 21 | 21 | — |

The rule would refuse 212 of 2,800 today, before `record_type` (677 of 941 Yad Vashem citations lack one, council) and
the meaning of `accessed` (the council found all 371 statements' values to be the day the line was written; the 259 Yad
Vashem statements were in fact read again that day, the family's texts read from their copies that day; each is checked
before it stands) are counted. The gaps are read again or marked for what they are; the rule is never relaxed.

## 5. Shulim's records under the model

- **Arrival at Sachsenhausen.** `source_id` = the arrival list of 27.10.1944 (kind `archival_record`, holder RGVA,
  `reference_code` "1367/2/1a"), `page` "Bl. 15", the list's words as quote, `via` = `sachsenhausen-memorial-2022`,
  whose `derived_from` is `[{arrival list, transcription}, {transport list, transcription}]`: it gives 1908 where the
  list, as the Buchenwald Memorial reads it, gives 1918. The page says "as transcribed by the Sachsenhausen Memorial for
  the family, 2022".
- **Sachsenhausen to Ohrdruf.** `source_id` = the transport list of 13.11.1944 (holder the FSB's central archive,
  `reference_code` "N-19092, tom 90"; worded cautiously: the file is among the records of the Soviet war-crimes trial of
  Sachsenhausen, council, not verified), its entry "No. 668" (Szylan Judewicz, prisoner number 110849) as the locator.
  The family holds two derivatives of it, each a source of its own:
  - the USHMM's microfilm, RG-06.025*26 ("Sachsenhausen, 1939-1951"), item 2281 (`derived_from` `copy`, holder the
    USHMM), scanned at the USHMM's reading room on 28 February 2023 and sent to the family as two PDFs by an independent
    researcher the family paid (the owner's Gmail, read by the site-redesign session on 24 October 2026). The route is
    private: no public field names the researcher or the fee. This copy is the statement's `via`;
  - the Sachsenhausen Memorial archive's copy, "JSU 1, Bd. 90", sent to the family by the Buchenwald Memorial with its
    letter of 17 February 2022 (`derived_from` `copy`, holder the Sachsenhausen Memorial).
  The Sachsenhausen Memorial's answer of 31 March 2022 is a separate `transcription` of the same list (it gives 1908).
- **Ohrdruf.** `source_id` = the alphabetical list of the northern camp (Nordlager) of 24.12.1944 (holder the Arolsen
  Archives, its DocID as `record_id`, the permalink as `url`, the tree signature as `reference_code`), which the
  Buchenwald Memorial also sent the family on 23 May 2022. `public_note` = the Buchenwald Memorial's identification
  by the two prisoner numbers, 110849 and 103878; the letter is the `via`, its public `author` the Buchenwald Memorial.
- **Arolsen card and transport list** (DocIDs 6203612 to 6203614, today only in a note): `record_id` and `url` each.
- **"Possibly 26 October"**: stays accepted with evidence `possible`; it does not contradict the list (the day the
  transport left Auschwitz). The site does not show a possible removal a recorded one covers.

## 6. Order of work

1. **Schema**: `Holder`, the new `Source` and `Citation` fields, the per-kind table and its checks, Zod and Pydantic
   twins, the alignment mappings (`ehri:isCopyOf`, `rico:describesOrDescribed`, `rico:hasOrHadHolder`,
   `rico:hasOrHadIdentifier`, `rico:hasOrHadLanguage`, `rico:hasDocumentaryFormType`, `rico:hasCreationDate`),
   `bin/verify`.
2. **Steps**: the holders; the registry's sources moved onto them; Shulim's statements as in §5; internal pointers out
   of `record_id` into `locator`; the Buchenwald author; then the gaps of §4, read again where a record can be read.
3. **Site** (the redesign session): `record-words.ts` replaced by `short_name` and the holder's name; `reference_code`,
   `record_type`, `via` and `public_note` rendered; publication by field. Until the schema carries `reference_code`, the
   site narrows its rule with tests and withholds `work_id` file names (draft #212, today).
4. **The owner's batch**: `archival_record` and `provenance`, with real examples and their mappings.

## 7. Private, never published

Citation `note` and `locator`; a `private` source as a document, and its quotes until `quotes_cleared`; pictures of
letters or privately obtained copies; a `private` holder's name (a paid researcher) and fees; a staff member of an
institution named in private correspondence; a living submitter of a Page of Testimony; email and postal details in
letters; `work_id` values that are file names. The projection publishes `public_note`, `short_name`, `author` where it
is an institution, the holder's name where its kind is `institution` or `family`, `reference_code`, `record_id`,
`record_type`, `page`.

## 8. Not now

A page per source or per holder (ids are address-ready). Wikidata ids for institutions (Wikidata P14900 has no match for
several; after the vetting's Impresso-2 check). Instantiations (a scan of a photocopy) as their own entities. JSON-LD of
sources with EHRI ARKs, CSL-JSON "cite this", an EHRI micro-archive of the family's papers (council, "could").

## 9. Open

- Whether a `family` holder is shown by name ("the Sorid family") or as "the family": the owner's.
- The institution credit is the council's default; the owner may say otherwise.

## 10. The owner's rules of 24 October 2026, evening

- **Quotes from the family's papers** (Morris Sorid's testimonies and memoir, the memorials' letters to the family):
  "Yes they may if unique information". Such a source carries `quotes_cleared` (the owner, 24 October 2026) and
  `quote_condition: unique_information`: a quote is shown only where no other accepted statement of the same kind about
  the same person rests on a source that is not private (`quoteShown` and `corroborated`, Zod and Pydantic twins, with
  contract cases). Otherwise the record is still cited, by name and reference, without its words.
- **Find the archive, as a general rule**: "Morris testimonies are via other archives like USC shoah foundation. Find
  the archive as a general rule." A document or recording the family holds a copy of is cited as its original, held by
  the archive that holds it (with its holder, reference and catalogue address); the family's copy is the citation's
  `via`. Only what exists nowhere else (the family's own register, a letter to the family, a photograph never deposited)
  is cited as the family's.
