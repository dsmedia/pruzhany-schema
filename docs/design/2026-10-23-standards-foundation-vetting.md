# The standards foundation of persons, life events and relations, vetted

**Status:** research of 23 October 2026; the owner's batch was answered and released in 1.2.0 that day (§8). The research and measurements below describe the pre-release state.
**Date:** 2026-10-23
**Asked by:** pruzhany-steps `.scratch/site-files-keeper/handoff-standards-foundation.md` (the owner's word of 23 October
2026: "this is worth some deeper research as it is foundational … vet the approach and consider how it should be done per
forward looking Ehri standards").
**Builds on:** [`2026-04-25-cross-edition-entities.md`](2026-04-25-cross-edition-entities.md),
[`2026-10-19-people-facts-and-sources.md`](2026-10-19-people-facts-and-sources.md),
[`2026-10-22-site-files.md`](2026-10-22-site-files.md).
**Decision drafted from it:** [`docs/adr/0001-which-standard-governs-what.md`](../adr/0001-which-standard-governs-what.md).

The full evidence, with every script that produced a number, is in five notes in pruzhany-steps,
`.scratch/standards-vetting/notes/` (branch `ccr-87f05bd4-47ulz3`, commits `075c8072` to `c211dfb1`):
`A-ehri.md` (EHRI now and next), `B-rico.md` (RiC-O on events, parts, relations, tests), `C-impresso-identity.md`
(Impresso and identity across issues, the join rule measured), `D-data.md` (the data the plan would change, measured),
`E-described-persons.md` (a person known only by description). This file keeps their conclusions and the primary source
each rests on. A claim marked *inference* is ours; everything else is quoted or counted.

## What was read, at which commit (all on 2026-10-23)

| key | source | commit or address |
|---|---|---|
| [R] | RiC-O 1.1, `ICA-EGAD/RiC-O`, `ontology/current-version/RiC-O_1-1.rdf` | `master` `06912e1` (the pin) |
| [Rn] | the same repository, unreleased | `next-version` `2c90fec` (2026-10-06) |
| [CM] | RiC-CM 1.0.1, `ICA-EGAD/RiC-CM`, `current-version/RiC-CM-1.0.1.pdf` | `dcd7c32` (2026-09-30) |
| [RAG] | RiC Application Guidelines (draft), `ICA-EGAD/RiC-AG`, `source/` | `8ee0244` (2026-10-09) |
| [E] | EHRI ontology 0.2.0, `EHRI/ehri-kg-ontology`, `ontology/ehri.owl` | `develop` `4b275a7` (the pin) |
| [EM] | EHRI's mappings and shapes, `EHRI/ehri-kg-mapping` | `develop` `1c2325f` (2026-08-13) |
| [EK] | EHRI-KG news and SPARQL | <https://ehri-kg.ehri-project.eu/news/alignment-rico-11-and-additional-services/> (2026-09-07); <https://lod.ehri-project-test.eu/sparql> |
| [EP] | EHRI portal | <https://portal.ehri-project.eu/authorities>, `/sets/ehri_pers`, `/api/graphql` |
| [I] | Impresso schemas, `impresso/impresso-schemas` | `master` `329323c`; `86-organize-json-schemas-by-data-phase` `21e40a0` (Impresso-2) |
| [IG] | *Impresso Named Entity Annotation Guidelines* v2.2.0 | <https://zenodo.org/records/3604227> |
| [H] | HIPE-2022 and HIPE-2026 overviews | <http://ceur-ws.org/Vol-3180/paper-83.pdf>; <https://ceur-ws.org/Vol-4283/paper212.pdf> |
| [TAC] | TAC 2011 KBP task definition | <https://tac.nist.gov/2011/KBP/KBP2011_TaskDefinition.pdf> §2.1 |
| [WD] | Wikidata help | <https://www.wikidata.org/wiki/Help:Merge>, `Help:Redirects`, `Help:Split_an_item`; items `Q75388852`, `Q75330048`, `Q90040312` |
| [GND] | DNB's GND change service | <https://dnb.de/gndchangeservice> |
| [YV] | Yad Vashem: collections' field strings; *Guidelines for Suggesting "Personal Files"* (copy) | <https://collections.yadvashem.org/assets/i18n/en.json>; <https://www.jgscv.org/pdf/handouts/Call_Clusters_eng.pdf> |
| [AA] | Arolsen Archives catalogue guides and glossary (through the ArolsenMCP tools) | guides `archive-guide`, `ousarchiv/cni-person-search`; glossary "N.N." |
| [G7] | GEDCOM 7, `FamilySearch/GEDCOM`; GEDCOM X, `FamilySearch/gedcomx` | `633ebf8`; `ab90040` |
| [D] | our data: pruzhany-svelte `static/data/` (the preview) and the shared record | `cbd2e94` |

Not read, and so not relied on: Yad Vashem's own help pages (403), ISAAR(CPF) (403), the EDTF specification, EHRI's
ISWC 2023 paper, RiC-CM and RiC-AG on ica.org (their GitHub copies were read).

## 1. EHRI, looking forward

- **Nothing newer than 0.2.0.** Every branch and pull-request head of `EHRI/ehri-kg-ontology` is an ancestor of
  `develop` `4b275a7`; no tag after `v0.1.1`; the ontology the namespace serves is 0.2.0 and the same graph as the pinned
  file; `/0.2.1`, `/0.3.0`, `/1.0.0` answer 404 ([E]; A-ehri §1). 0.2.0 is still not on `main` (issue #14 open). **No
  new pin to ask for.**
- **The address will change.** "Before the end of the project, the EHRI-KG will be moved to a production server and
  IRIs will be consolidated (no need to worry, we will implement the necessary redirections)" ([EK], 2026-09-07). No date,
  no production namespace yet. *Inference*: never store an `ehri:` IRI in our data; keep our vocabulary ids with
  mappings (as today) and write `ehri:` IRIs only in an export, so the move is one new `standards/` file and a re-check.
- **EHRI models persons and families and nothing of events, roles or kinship.** `ehri:Person ⊑ rico:Person`,
  `ehri:Family ⊑ rico:Family`; 21 `ehri:` classes, none an event; the only role properties belong to the two
  copy relations ([E] `ontology/ehri.owl`). The live graph holds 3,342 `ehri:Person`, 2 `ehri:Family` and **0**
  `rico:Event`, `rico:EventRelation`, `rico:FamilyRelation` or `rico:ChildRelation`; birth and death are
  `rico:hasBirthDate`/`hasDeathDate` to a `rico:Date`; family ties and deportations are prose (`rico:history`)
  ([EK] SPARQL, queries in A-ehri §4).
- **EHRI's persistent person id is a portal ARK** (`ark:41045/…` → `portal.ehri-project.eu/authorities/ehri_pers-N`);
  the graph's own person IRI is a test-domain IRI and already lags a portal merge (a merged id answers 301 on the portal
  and is still the old number in the graph) ([EP]; A-ehri §2).
- **EHRI's person set is mostly record creators and notable people**, "non-exhaustive"; a portal search for Pruzhany
  finds no authority ([EP]). Its outside links are few and made by exact name: 52 `owl:sameAs` to CDEC; an EHRI VIAF
  trial on victims' names gave 31 right and 37 false of 68 (A-ehri §2, §5).
- **EHRI publishes SHACL and ShEx shapes for its own exported records** (`src/shapes/1.1/people.shacl.ttl`,
  `people.shex`, [EM]). This corrects brief 09, which found no shapes because it looked only in the ontology repository.
  They describe persons as EHRI exports them, not events or relations.
- **RiC-O moves too.** The unreleased `next-version` adds `rico:hasContentWhichRefersTo`, "Introduced in RiC-O 1.2",
  for a record whose content refers to a thing, "explicit (e.g. a direct quotation or mention) or implicit" ([Rn]): the
  standard's word for our **Mention**, today the local `pc:site_mention`. RiC-O's roadmap for 2.0 says it will
  "articulate the Event and Activity classes, and the Relation system of classes" (B-rico §Summary). *Inference*: keep
  parts as local subterms that can be re-pointed when it does.

## 2. Events and their main people in RiC-O

- **A birth, a wedding, a death is a `rico:Event` typed by a `rico:EventType`.** `EventType`'s scope note: "Biographical
  event types include birth, marriage, death, etc." ([R] l. 25709). RiC-O allows a dated fact on the person as well:
  "The two methods may be used in parallel" ([R] l. 344). ICA's worked marriage models it as `rico:Activity` (a
  subclass of Event) with each spouse `rico:affectsOrAffected` and the register entry `rico:documents` it
  ([RAG] `faq--record_or_record_set.md` ll. 100–110). *Inference*: only the event gives the 23 greetings of 16 December
  1938 one thing to gather on; store the event and derive the person's birth or death date from it. EHRI's own data
  carries the date on the person, so an export writes both.
- **RiC-O has no participation-with-a-role for events.** `eventRelation_role` has domain and range `EventRelation`
  (a self-loop that "rolifies" the class; it cannot carry a part); `RoleType` is "the role an Agent plays in some context
  (usually in some creation relation)" and is attached only by `creationWithRole` ([R] ll. 2721, 29439). ICA's guidance:
  "RiC is not a model about wills, nor about the roles of the individuals involved", and a project that needs roles adds
  a subproperty (its example `my-onto:hasTestator ⊑ rico:hasAuthor`) ([RAG] `faq--how_to_extend_ric.md` ll. 67–159).
- **So each part is a local subproperty.** `rico:affectsOrAffected ⊑ rico:hasOrHadParticipant`, domain Event, range
  Thing, "Connects an Event to a Thing on which the Event has or had some impact" ([R] l. 1459). *Inference*: the parts
  whose person's life the event changes (baby, bride, groom, the boy, the one who died) are subproperties of
  `affectsOrAffected`; a parent at a birth is a subproperty of `hasOrHadParticipant`. Both stay inside RiC-O 1.1's domains
  and ranges and follow ICA's advice; the owner's Q10 ("mapped to `rico:hasOrHadParticipant`") holds, made exact. The
  n-ary `EventRelation` with `relationHasContext` and a `RoleType` is legal too, costs a node per person and infers only
  `isEventAssociatedWith`: kept for a participant whose part ever needs its own source (B-rico §A.7, §A.8).
- **Dates.** `rico:Date` with `expressedDate` (the printed words, with "the calendar used"), `normalizedDateValue`
  ("based on a public technical standard") and `dateQualifier` ([R] ll. 21391, 22247) fit Q3 (the printed date, else
  "reported in" the first issue's date). *Inference*: "reported in" is a qualifier, not a bound: a birth is on or before
  its notice, but a wedding may be greeted before it happens.
- **RiC-CM gives one test RiC-O does not:** a person has one birth and one death (R070, R072, "1 to M", [CM] pp.
  110–111). RiC-O declares no functional property.

## 3. Relations, once, in RiC-O's direction

- **RiC-O orients only two family relations.** `ChildRelation`: "The Relation is oriented from the parent to the child:
  the parent is the source of the relation, and the child(ren) is the target" ([R] l. 24691); `DescendanceRelation`,
  ascendant → descendant, transitive, with "zero to many intermediate persons" ([R] l. 25388, 4523). `hasOrHadSpouse`,
  `hasSibling` and `hasFamilyAssociationWith` are `owl:SymmetricProperty`, their n-ary classes "not oriented"
  ([R] ll. 8032, 9152, 5149). RiC-O has no term for uncle, aunt, cousin or in-law (B-rico §B.1).
- **What that means for our kinds** (vocabulary `relationship_types`): store `parent_of`, never `child_of`; store
  grandparent and great-grandparent, never their inverses, and map them to `rico:hasDescendant` instead of today's
  catch-all (a mapping change, for the owner's batch); store a symmetric kind (spouse, sibling, cousin, in-law) once per
  pair, with a fixed order so a duplicate is visible; uncle/aunt and parent-in-law have no RiC-O direction, so one is
  chosen locally (*inference*: the elder generation first, as `DescendanceRelation`) and a test says the choice is ours.
- **The data** ([D]; D-data §1): 1,596 relations; 1,483 kinship ones, of which 728 pairs are stored both ways and 27
  have no inverse. **Stored once they are 755 (868 with the 113 unresolved `other` ones).** The two readings never
  differ in standing, review or attribution, but their citations differ in 674 pairs (each carries its own person's
  issues), their evidence prose in 18, and `shown` in 47 (today "show this relative on this person's page"). So
  storing once is a merge: the union of the citations, both evidence texts kept, the dropped row's id kept as an alias,
  and `shown` given a meaning without direction (which person's page may show the tie). The 1,050 proposed relations
  keep their standing; the merge changes how they are stored, not what is believed.
- **A mapping to correct.** Our design and the pilot file a relation's citations under `rico:relationHasSource`
  (`2026-10-19-people-facts-and-sources.md` ll. 133, 151; `pilots/sourced-entities/build.py:331`;
  `vocabulary/site-content.json`, `fact_source`). In RiC-O 1.1 `relationHasSource ⊑ relationConnects`, inverse of
  `thingIsSourceOfRelation`: "Connects an n-ary Relation to a Thing that is its source", the oriented relation's first
  end, the parent of a `ChildRelation` ([R] l. 19351). The evidence is `rico:isEvidencedBy`, "Connects a Relation to a
  Record Resource that is used for proving is existence or describing it" (domain Relation, range RecordResource;
  inverse `rico:evidences`) ([R] ll. 11822, 2753). Found by E-described-persons and checked against [R] by the session.

## 4. One identity per person across issues

- **Impresso stops at NIL.** In every Impresso schema read, an entity is a Wikidata QID and nothing else: the entity
  document is "one document per non-null Wikidata QID" (Impresso-2 `sem.root.entities.v3.schema.json`, [I]); unlinked
  mentions are grouped only by exact surface string, which the schema itself does not treat as identity. The guidelines
  link to a QID or NIL ([IG] §4). No HIPE campaign has a NIL-clustering task; HIPE-2026 groups NILs only inside one
  document ([H]). So "Impresso for identity across issues" is not a fair description: Impresso governs mentions and
  their Wikidata links, and identity of everyone not in Wikidata is ours (C-impresso-identity §1).
- **Impresso-2 changed the field.** It marks an unlinked mention `wkdata_qid: null`; `wkd_id` survives only as a
  deprecated alias in the annotation API ([I] `entities-nel.v2.schema.json`, `annotation-api/entities/nel-entity.v1`).
  Our 2026-04-25 design adopts the legacy required literal `"NIL"`. No person carries any Wikidata id today ([D]: 0 of
  16,585; `wkd_id` empty on all 39,166 mentions), so nothing is built on it yet; it is to be decided before something is.
- **The models for clustering unlinked people across documents** are TAC-KBP's NIL clusters ("cluster together queries
  referring to the same non-KB (NIL) entities and provide a unique ID for each cluster", [TAC] §2.1) and, in our domain,
  Yad Vashem's "personal files": the name records stay as they are and are grouped into one file, proposed and approved
  by staff on several attributes ([YV] guidelines). Arolsen files differently spelt names together "based on identical
  dates of birth and prisoner numbers" ([AA] e-Guide). None joins on a name alone.
- **The Q16 rule measured** on the preview's 238 issues ([D]; C-impresso-identity §3, scripts in its appendix). As
  worded ("every main person's name printed identically in Yiddish", same kind, within 8 weeks) it joins 206 pairs of
  events; 11 of them have main people with clearly different surnames in the shared record, 6 certainly two people,
  every one through a **given name printed alone** ("Death of Esther Pribulsky" joined to "Death of Esther Kalbkopf",
  42 days apart, on "אסתר"). The paper often greets by first name only: 1,875 of 4,414 printed forms of main people are
  one word. Requiring every main person's **full** printed name (two words or more, honorifics and pointing removed)
  leaves 69 joins and no conflict. Without the window there are 96 more pairs, mostly the same people at a different
  happening (a second child, a yearly memorial): **the window protects the events, not the people.**
- **Recall is low.** Of 325 pairs whose English names look alike within 8 weeks, the rule as worded joins 170 and the
  full-name rule 69: the paper spells a name differently from week to week (גולדמן / גאלדמאן) and the reading adds
  letters. The owner's worked case does not join by printed names at all (16 December prints "ריבטשע" alone; 23 December
  "רבקה יודעוויטש"); it joins only through the family register's ids. So resolved ids must join first.
- **Stable ids.** Wikidata: "Under no circumstances should redirects be deleted or repurposed"; a split keeps the
  original item on one part and makes a new one ([WD]). GND keeps redirect records "permanently" and marks a split with
  or without redirect ([GND]). VIAF answers 301 for a merged id. GEDCOM X keeps a merged id as a `Deprecated` identifier;
  RiC-O's `IdentifierType` gives "old identifier" as its example ([G7]; [R]). *Inference*: an id of ours, once
  published, is never renamed, reused or deleted; a merge keeps one and redirects the other for ever (the round-2 maps
  already do this); a split keeps the old id on the person with the most of its evidence and mints a new one. Ids are
  never parsed for meaning, though today's `person-<slug>-<date>` form stays (the owner's "keep existing site IDs", #16).
- **Outside ids** (an EHRI ARK, Yad Vashem, Arolsen, Wikidata) are carried as identifiers only on evidence, with their
  source and standing, never from a name match (EHRI's own VIAF trial above). A record that describes a person is a
  source about them, not the same thing; `sameAs` is kept for an adjudicated equivalence (the correction of 20 October in
  `2026-10-19-people-facts-and-sources.md`).

## 5. The children known only by description

- **No standard requires a person to have a name.** `rico:Person` is "An individual human being" and `hasOrHadName` is
  optional ([R]); `ehri:Person` adds no restriction ([E]); RiC-CM lists Name as "Repeatable" with no obligation ([CM]);
  GEDCOM 7 gives `NAME {0:M}` and GEDCOM X makes a person's names optional ([G7]).
- **The practice is a person record.** Wikidata holds unnamed children as ordinary humans labelled "unnamed daughter
  …", given name "unknown value", with sourced parents and birth date ([WD] items above). Arolsen's glossary records
  "N.N." ("No Name") for children whose name was unknown, and its transcription help says the "Unknown" it shows for an
  empty name field is "due to technical reasons" ([AA]). Yad Vashem's lists carry such children with a placeholder
  ([YV] `names1.pdf`). *Inference*: a description is held as a **supplied** name, marked as ours, never as a printed one.
- **A later naming goes on the same person.** Wikidata merges into one item; GEDCOM X keeps the other id as
  `Deprecated`; Yad Vashem groups records into one personal file ([WD]; [G7]; [YV]). The evidence is never the name:
  for a child of the paper, the same resolved parents and a compatible birth, and no other child of those parents in the
  window (E-described-persons §4).
- **Our vocabulary contradicts this in one place.** `parenthood` was made for "Parenthood of an unnamed child without
  inventing a person node" (`vocabulary/sourced-entities.json` ll. 93–102; `vocabulary/profile.ttl` l. 12). RiC-O's
  `ChildRelation` needs a Person at the child's end, the owner's Q12 says every birth's child is a person, and no fact in
  the shared record uses it (0 of 60,318; the pilot uses it twice). It is released, so it is deprecated with
  `replaced_by` the `parent_of` relation to the described child, never removed.
- **Our site would drop such a child.** An issue's public life event keeps only principals mentioned in that issue
  (pruzhany-svelte `src/lib/privacy/shared-projection.ts` l. 415; `scripts/validate-data.ts`); 40 principal references are
  dropped so today ([D]). The child therefore needs a Mention pinned to the printed words that designate them ("זייער
  טעכטערל", their little daughter), which is also the printed evidence that they exist.
- **The worked example already exists.** The family register holds `person-judewicz-daughter-1938`, an id made from the
  description and later given the names Tsveeyah, Cywia and Tseskele from the paper of 14 April 1939, the 1939 house
  register and the family's papers, on the same id (pruzhany-steps `corrections/people/judewicz-kaplan.toml` ll.
  126–142). It lacks a mark that the names were found later and citations on them in the shared record.

## 6. Tests of meaning, and what may honestly be claimed

- **No conformance notion exists.** Neither ICA nor EHRI defines conformance levels, an application profile, a validator
  or shapes for RiC-O ([R], [Rn], [E], [RAG]; a web search on 2026-10-23 found none). RiC-AG speaks only of data "strictly
  compliant to RiC-O, i.e. not an extension, since the components you have defined are sub-properties or sub-classes of
  RiC-O" ([RAG] `faq--how_to_extend_ric.md` l. 159). EHRI's shapes ([EM]) cover its own records.
- **So the honest claim is**: "mapped to RiC-O 1.1 as EHRI 0.2.0 imports it; every kind, part and relation names a RiC-O
  term or a declared local subterm of one, with its reason; these rules are tested on every change". Never
  "RiC-O conformant". The day an export is made, RiC-AG's own test applies (dropping our subterms to their RiC-O parents
  leaves a dataset in RiC-O alone), EHRI's people shapes are the yardstick for persons, and a reasoner can check
  consistency.
- **The rules a test can check on our JSON**, each able to fail on a real mistake, labelled by where it comes from
  (B-rico §C.1 and E-described-persons §5 give each with its line in [R]):

  | # | rule | from | fails today on |
  |---|---|---|---|
  | 1 | no stored `child_of`, `grandchild_of`, `great_grandchild_of`; one is turned into its inverse or refused | RiC-O: ChildRelation, DescendanceRelation orientation | 218 + 49 + 1 rows |
  | 2 | a symmetric kind is one row per pair | RiC-O: `owl:SymmetricProperty` | 184 spouse, 141 sibling, 18 cousin pairs |
  | 3 | one stored direction for uncle/aunt and in-law kinds | local, after RiC-O | 118 + 1 pairs |
  | 4 | both ends of a kinship relation are persons | RiC-O: domain and range Person | 0 (exists in part) |
  | 5 | no id is both a person and a family; a family is never a main person | RiC-O: Group ⊥ Person (one of six disjointness axioms) | 0 |
  | 6 | every main person resolves to a person of the record | RiC-O: participant range | 0 (exists in part) |
  | 7 | an event has one released kind (or `other` with `proposed_type`), the same in every issue | RiC-O + RiC-CM: Event Type "Not repeatable" | 0 (exists) |
  | 8 | every part is a vocabulary term whose mapping names `affectsOrAffected` or `hasOrHadParticipant`, and fits the event's kind | local, mapped to RiC-O | the hand-made Judewicz birth's doctor, midwife and a greeter as principals |
  | 9 | a person is the baby of at most one birth and the one who died in at most one death | RiC-CM R070, R072 | `person-judewicz-daughter-1938` in two birth events |
  | 10 | a normalised date parses; a "reported in" date is never an exact date without its qualifier | RiC-O: `normalizedDateValue` | not measured |
  | 11 | a relation's evidence is a source of the registry, a cited piece exists; mapped to `isEvidencedBy` | RiC-O: `isEvidencedBy` | the `fact_source` mapping |
  | 12 | mapped terms exist and their kind matches | the existing `bin/verify standards` | 0 (exists) |
  | 13 | a described child: made only from a notice of one child, has a mention, and a supplied name never counts as printed in a join | local, from E | not yet applicable |
  | 14 | a join resting on a given name alone, or on a name only, is refused | local, from Q7 and §4 | 6 of the 206 joins of the rule as worded |

- **One gap, closed the same day.** `standards/rico-1.1.json` records only each term's IRI, kind and label, not its
  domain, range, `inverseOf`, `subPropertyOf`, symmetry or disjointness, so rules 1–9 and 11 could only cite RiC-O as
  "our rule, after RiC-O". At the owner's word ("yes, pin the rules", 23 October 2026) they are pinned as
  `standards/rico-1.1-axioms.json`, from the same file at the same commit, by the existing extractor (`--axioms`; rdflib
  at extraction only, no new dependency for the site or the program); the gate keeps it in step with the terms list, and
  its tests read the rules this note cites from it. A test of meaning cites that file, not this note.

## 7. The verdicts

Each of the owner's answers in brief 09 against what was read. "Holds" means confirmed with the source named above;
"changed" gives the change and its reason.

| answer | verdict |
|---|---|
| **Q14** which standard governs what | **Changed in wording.** Impresso governs the newspaper's layers and its mentions with their Wikidata links, not identity across issues (§4). EHRI governs persons and families (`ehri:Person`, `ehri:Family`), adds nothing for events, parts or kinship, and its namespace is not stored (§1). RiC-O 1.1 governs events, their kinds, participants, family relations, evidence, dates and identifiers (§2, §3). Identity of people not in Wikidata is ours, after TAC-KBP's NIL clusters and Yad Vashem's personal files (§4). Drafted as ADR 0001. |
| **Q15** shape as the standard shapes | **Holds, made exact.** Relations once: only parent → child and ascendant → descendant have a RiC-O direction; symmetric kinds once per pair; uncle/aunt and in-laws in a local direction; the merge unions citations (§3). Main people as participants: each part a local subproperty of `affectsOrAffected` or `hasOrHadParticipant` (§2). Evidence maps to `isEvidencedBy`, not `relationHasSource` (§3). |
| **Q16** one identity across issues | **Holds in shape, changed in the rule.** Resolved ids join first; the name test needs every main person's full printed name, never a given name alone; a letter's difference is listed; the 8 weeks are the event's window, measured from its first piece; the same full names further apart make a person proposal, never an event join; ids never renamed, reused or deleted, merges redirect for ever, a split keeps the old id on one side; outside ids only on evidence (§4). |
| **Q17** tests of meaning on our JSON, no export, no new library | **Holds.** Fourteen rules, each labelled RiC-O, RiC-CM or local, several failing on today's data (§6). "Conformant" is never claimed. RiC-O's own axioms are pinned (`standards/rico-1.1-axioms.json`) so the tests cite them. |
| first grilling Q1, one event per happening | holds: RiC-O's EventType, RiC-CM's one birth per person (§2) |
| Q2, 8 weeks | holds as the event's window, not as a person rule (§4) |
| Q3, engagement and wedding two events; Q4, a death and its memorial two | hold: two happenings, two Events |
| Q5, main people | holds; the hand-made Judewicz event's doctor, midwife and greeter are involved, not main (rule 8) |
| Q6, who sent greetings drawn from mentions | holds: a Mention, RiC-O 1.2's `hasContentWhichRefersTo` when pinned (§1) |
| Q7, never join on a name alone | holds, and is what changes Q9 (§4) |
| Q9, an unnamed baby a main person by description | holds: every standard and archive read (§5) |
| Q10, parts as local terms mapped to `hasOrHadParticipant` | holds, refined: `affectsOrAffected` (itself under `hasOrHadParticipant`) for those the event happens to (§2) |
| Q11, a stated relation recorded with the notice as its source | holds, with the notice as the relation's evidence (`isEvidencedBy`), not its RiC-O "source" (§3) |
| Q12, new kinds and parts in the owner's batch | holds; the batch also carries the grandparent remapping, the `supplied` name kind and the `parenthood` deprecation |
| second grilling Q2, evidence decides, hand-made is not magic | holds: Yad Vashem's and Arolsen's practice (§4) |
| Q3, printed date else "reported in" | holds: `rico:Date` with `expressedDate` and a qualifier; "reported in" is not a bound for a wedding (§2) |
| Q8, the five worked cases | hold, with corrected facts: the Judewicz birth is greeted in **three** issues (16, 23 and 30 December 1938), 13 events today; Yosef Vigotov is **three** person ids under three death events; only 1 of 337 births lists the child (D-data) |
| Q9, identical printed Yiddish names | **changed**: full printed names (§4) |
| Q10, the Yiddish, never the model's English | holds |
| Q11, engagements as engagement events | holds (289 by name of 296 "celebration" events, D-data) |
| Q12, every birth's child a person | holds; a supplied name, a mention on the describing words, `parenthood` deprecated (§5) |
| Q1, Q4, Q5, Q6, Q7, Q13 of the second grilling | hold; nothing read bears on them otherwise |

## 8. Open, and whose

- **The owner's, answered:** RiC-O 1.1's axioms are pinned (`standards/rico-1.1-axioms.json`, the owner's "yes, pin the
  rules" of 23 October 2026; §6).
- **The owner's batch (#16), answered and released in 1.2.0 on 2026-10-23:** after seeing two or three real printed
  notices and their English for each new term on the private batch page, the owner answered **"Yes"** to **"yes to all"**.
  The seven parts are released as §2 proposed them: `parent` under `rico:hasOrHadParticipant`; `baby`, `bride`,
  `groom`, `boy`, `deceased` and `remembered` under `rico:affectsOrAffected`. `memorial` covers annual and 30-day remembrance, never the death; `supplied` marks our attributed
  description of an unnamed person. `parenthood` is deprecated in favour of a `parent_of` relation to the child as
  a person. Grandparent and great-grandparent map to `hasDescendant` via `DescendanceRelation`; their inverses map to
  the pinned `hasAncestor`. The 1.0.0 and 1.1.0 snapshots retain their old mappings. Engagement was already released
  and used, so needed no change. The same **"Yes"** keeps a son's bris greeting in its birth's event, with no new word;
  `שלום זכר` is not a bris. ADR 0001 is unchanged.
- **Settled by the owner's existing words, so not asked:** a given name alone never joins (Q7); twins or "children" make
  no child, they are listed ("only where the notice makes clear there is one child", first grilling Q9); the description's
  wording is the owner's own example.
- **Later, when it comes:** EHRI's production namespace (a new `standards/` file at the owner's word); RiC-O 1.2's
  `hasContentWhichRefersTo` for mentions; RiC-O 2.0's events; Impresso-2's `wkdata_qid: null` against our legacy
  `wkd_id: "NIL"` (before any Wikidata field is built); EHRI ids for the few notable people who have one (a small piece of
  research of its own).
- **Measured next, before it may join anything:** a spelling fold for the paper's two orthographies, which would raise
  the name rule's recall (§4), with the scripts of C-impresso-identity and a hand-read sample.
