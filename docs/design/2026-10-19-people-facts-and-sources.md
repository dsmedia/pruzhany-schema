# People, places, organisations and events, with their facts and sources: a proposal

**Status:** proposal of 19 October 2026, reconciled on 20 October; the decisions since are at the end and win where they differ.
**Date:** 2026-10-19
**Builds on:** [`2026-04-25-cross-edition-entities.md`](2026-04-25-cross-edition-entities.md) (Impresso mentions, NIL clustering).

---

## Where this comes from

The data behind this proposal is the 98 people of the hand-made edition of 16 December 1938, followed through all
238 editions in `dsmedia/pruzhany-svelte`'s `static/data/` at `35cccf9`. Each person was traced through the
person records of every enrichment file and through every content unit and life event that names them. The
people with the most kinds of material are:

| person | editions | pieces | what the pieces are |
|---|---|---|---|
| Eliyahu Pomeranetz | 63 | 112 | 40 greetings, 29 articles, 22 death notices, 17 notices, 4 ads |
| Mordechai Epstein | 76 | 89 | 46 greetings, 19 death notices, 15 notices, 8 articles, 1 ad |
| Moshe Makransky | 52 | 81 | 38 death notices, 38 greetings, 3 notices, 2 articles |
| Ephraim-Michel Pruzhansky | 50 | 72 | 42 greetings, 18 notices, 6 articles, 6 death notices |
| Shmuel Spector | 51 | 58 | 26 greetings, 15 ads, 8 death notices, 5 notices, 4 articles |
| Moshe Judewicz | 23 | 47 | 40 greetings, 4 notices, 2 articles, 1 ad; also a memoir, oral histories and partisan service |


These people show what the current `EnrichedPerson` cannot say, and where its free-text fields have absorbed
the overflow.

## What the data shows

### 1. One person, many copies that disagree

A person is copied whole into every edition's enrichment file. 53 of the 98 have copies that differ, with up
to 19 different versions of one person. Across the copies, these fields differ: `residence_at_publication`
422 times, `aliases` 280, `external_references` 37, `holocaust_fate_notes` 37, `biographical_narratives` 23,
`proposed_relationships` 14, `birth_location` 10, `relationships` 9. The copies happen not to disagree on
fate or occupation, but nothing stops them from doing so.

### 2. A person's link to a piece has no role

`EnrichedPerson.unit_ids` and `ContentUnit.person_ids` only say *that* a piece names a person. Take Mordechai
Epstein's 19 death notices. The link cannot say whether he is the one who died, a mourner, or the one who
signed the condolence. In the same way, `LifeEvent.principal_ids` for "Death of Rabbi Chaim Feldman" lists the
rabbi together with three of the people who mourn him. `LifeEventUnit.role` (`primary_announcement`,
`congratulation`, …) is the role of the *piece*, not of the person.

### 3. Sources are free text

The 98 people's `external_references` use **more than 100 distinct `source` strings**. The 1958 memorial book
alone appears under five of them: `pinkas-five-towns-1958`, `Pinkas fun finf fartilikte kehilos (Bernstein,
ed., Buenos Aires 1958)`, `Pinkus Pruzhany Memorial Book (Bernstein, Buenos Aires 1958)`, `Pinkas Pruzhany
(1958)` and `Pinkas Pruzhany`. Several more add a page or a chapter to the name. The page number lives in
`notes` (`"printed p. 240 — index entry: …"`). A reference's status is written into its name: `"(HELD AS
RESEARCH LEAD ONLY)"`, `"(UNVERIFIED)"`. The edition file already carries a registry of sources,
`externalSourceTypes`, with an `id` and a `baseUrl`, but no reference points into it. `verified` is a yes/no
value, so the pipeline's "probable" record link is written as `verified: false` and is then never published.

### 4. Facts are collapsed into single fields or into prose

- `occupation: "Teacher, Principal, Partisan Commander"`: three roles held at different times, with no date
  and no source for any of them.
- `residence_at_publication` holds one place per edition, which is why it differs 422 times. Emigration, moves
  and the ghetto have no field.
- `partisan_activity` and `ghetto_role` are one-off shapes for what are facts like any other.
- `additional_details` is label/value prose that holds facts, people and research gaps all together:
  `"Wife": "Leah Pomerantz (d. 18 Oct 1934 Pruzhany, natural causes)"`, `"Surviving children": "Itzhak
  (Argentina), Rachel Pomerantz-Shur (Argentina)"`, `"YV PoT": "None filed — gap"`.

### 5. The fate mixes outcome with certainty, and is cut off from its evidence

`HolocaustFate` holds an outcome and a certainty in one value (`perished`, `likely_perished`). The date, place
and manner of a death go in `death_year` or in `holocaust_fate_notes` prose. One fate note says that a death
year is "inferential and intentionally not encoded in the structured death_year field", because there is no
field for a date that is only inferred. The record a fate rests on is somewhere among the references, and
nothing says which one. (In the pipeline's register it *is* said, as `archives[].strength`, and it is lost on
the way to the site.)

### 6. Names of different kinds are all lumped into `aliases`

Moshe Judewicz's `aliases` hold all of these together: spellings (`Moshe Yudewitz`), his name in Polish
(`Mojżesz Judewicz`), his later American name (`Morris Sorid`), his nickname (`Mitia`) and his partisan name
(`Dmitri`). A married name is written inside `name` itself (`"Sarah Epstein (née Rendel)"`). The pipeline's
`not_aliases` (names that look like his but are other people) has nowhere to go.

### 7. A relationship's evidence is prose, and only one side carries it

`relationships[].evidence` mixes quotations, citations and reasoning in one string. A relationship is stored on
one of the two people and inverted by the reader. `proposed_relationships` names the other person in prose
(`person_id_hint: "Salomon Judewicz (brother, perished Auschwitz-Birkenau 1943)"`) and uses its own type names
(`sibling_of` where `relationships` has `sibling`).

### 8. Narratives are unsourced prose

`biographical_narratives[].source` is `"deep_research"` or `"flash"`: it names the tool that wrote the text,
not where the facts in it come from.

## What existing standards do

Two current models were read on 2026-10-19 for this proposal:

- **GEDCOM X** (FamilySearch, [conceptual model](https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md))
  separates a *persona* (a person as one source describes them, `extracted: true`, citing exactly one source)
  from a *conclusion person* (the researcher's belief, linked to its personas by `evidence`). A `Fact` has a
  `type`, `date`, `place`, `value` and `qualifiers`. A `SourceReference` points at a `SourceDescription`, and
  locator qualifiers say where in it (`Page`, `RectangleRegion`, `TimeRegion`). Every conclusion may carry
  `confidence` (`High`/`Medium`/`Low`), `attribution` (who, when, why) and an `analysis`.
- **Wikidata** ([Help:Statements](https://www.wikidata.org/wiki/Help:Statements)) records "what a source
  says" as a statement: a value, qualifiers (such as time) and references, with a *rank* that marks the
  preferred value where sources disagree.

Both describe a person as a list of sourced statements, not as a set of flat fields. That is the shape the data
above needs. The pipeline's OKF person files (`pruzhany-steps`, `src/pruzsteps/person_files.py`) and the
Impresso mention IDs of the earlier design both fit inside it.

### EHRI (European Holocaust Research Infrastructure)

Read on 2026-10-19:

- the EHRI Knowledge Graph ontology, [`EHRI/ehri-kg-ontology`](https://github.com/EHRI/ehri-kg-ontology) at
  `5d42d25` (5 March 2026), version 0.1.1, latest tag `v0.1.1` [corrected 2026-10-20: the pinned EHRI metadata says 0.1.1, not 0.2.0] [2026-10-22: 0.2.0 is on branch `develop` at `4b275a7`, untagged, and imports RiC-O 1.1; the gate now checks against it and RiC-O 1.1, at the owner's word];
- [RiC-O 1.0.2](https://github.com/ICA-EGAD/RiC-O) at `06912e1` (`ontology/previous-versions/RiC-O_v-1-0-2_release/RiC-O_1-0-2.rdf`) [corrected 2026-10-20: EHRI imports 1.0.2; 1.1 is checked separately, not its base];
- EHRI's report on its digital editions and standards (deliverable D11.6, July 2024);
- the [EHRI portal's authority sets](https://portal.ehri-project.eu/authorities).

[corrected 2026-10-20: the pinned term lists and their provenance now live in [`standards/`](../../standards/README.md); use them before mapping.]

What EHRI does:

- **Its data model is ICA's Records in Contexts ontology (RiC-O)**, extended. `ehri:Person` is a subclass
  of `rico:Person`, and EHRI reuses schema.org for addresses and opening hours. EHRI's own extensions concern
  archives and institutions. EHRI adds nothing of its own for people: a person is RiC-O's person.
- **RiC-O records a relation as a record of its own** (`rico:Relation` and its subclasses `FamilyRelation`,
  `AgentToAgentRelation`, `PerformanceRelation`, …). A relation has `isEvidencedBy` [corrected 2026-10-23: evidence, not `relationHasSource`, the first endpoint], `relationCertainty`,
  `isAssociatedWithDate` and `relationState` [corrected 2026-10-20: `relationHasDate` is absent from RiC-O 1.0.2; `relationState` describes temporal state, not editorial approval]. The inverse property `rico:evidences` links a document to the
  relation it proves. Names are records of their own too (`rico:AgentName`, with `usedFromDate`), not strings.
  A person has `hasBirthDate`/`hasDeathDate`, `hasBirthPlace`/`hasDeathPlace`, `hasOrHadOccupationOfType`
  (`rico:OccupationType`), `hasOrHadDemographicGroup`, and links to `rico:Event`.
- **EHRI links its entities to shared lists** rather than writing names out. Its editions tag people, places
  and organisations in TEI (`persName`, `placeName`, `orgName`), and each tag carries the address of an entry
  in EHRI's controlled vocabularies (terms, camps, ghettos) or in GeoNames. Its person authority records
  (the "EHRI Persons" set) hold name variants and transliterations, years and a short note, in the shape of
  ISAAR(CPF) / EAC-CPF.
- **EHRI links to other databases with `owl:sameAs`.** The paper on its knowledge graph (*The Holocaust
  Archival Material Knowledge Graph*, ISWC 2023) links EHRI persons to the Italian victims database (CDEC)
  this way, and to DBpedia. Victims' data is kept in the victims' databases, not copied into EHRI.

What this means for us:

| our proposal | RiC-O / EHRI | note |
|---|---|---|
| `Relationship` with `citations`, `confidence`, `status` | `rico:Relation` + `isEvidencedBy`, `relationCertainty`, `relationState` | evidence and certainty map; editorial status is local [corrected 2026-10-20: `relationState` is temporal state; corrected 2026-10-23: `isEvidencedBy` connects Relation → RecordResource; `relationHasSource` is the first endpoint] |
| `Fact` with `citations`, `confidence`, `date` | a qualified `rico:Relation` with `isEvidencedBy` and certainty | RiC-O has no general "fact"; use a qualified assertion and map where justified [corrected 2026-10-20: pending/disputed assertions must not become unqualified historical triples; see the pilot; corrected 2026-10-23: fact citations use `isEvidencedBy` on the qualified Relation] |
| `Name` with `kind`, `script` | `rico:AgentName` + `usedFromDate` | RiC-O's names are records of their own, as ours would be |
| `Citation.unit_id` (the paper's piece) | `rico:evidences` from a `RecordResource` | each piece of the paper is a `RecordResource` |
| `Fact.place_id` for a ghetto or camp | EHRI vocabulary URI (camps, ghettos) | the `dsmedia/arolsen` catalogue already loads EHRI's camp and ghetto lists |
| `Fact.type: occupation` | `rico:OccupationType` | |
| `Source` registry | EHRI institutions + archival descriptions | Yad Vashem and Arolsen are EHRI institutions with portal ids |
| `Person` ↔ archive records | source/evidence links | [corrected 2026-10-20: a record describing a person is not that person; reserve `sameAs` for separately adjudicated identity equivalence]. |

Two conclusions follow:

1. **Model in our own JSON, but keep it mappable to RiC-O.** No Holocaust project in these sources keeps
   its working data in RDF. EHRI publishes RiC-O from its portal's own database, and victims' databases keep
   their own shapes and are linked by `sameAs`. Some fields have a RiC-O counterpart; the rest need declared local terms with reasons [corrected 2026-10-20: the pilot uses local terms for fate, review and identity proposals; emigration has no RiC-O term, and `MigrationRelation` concerns digital instantiations, not people's migration].
2. **Use shared lists wherever one exists.** Give places, ghettos and camps their EHRI vocabulary id (and
   their GeoNames id) beside our own `location-*` id. Give a person who is in Wikidata or EHRI's persons
   set that id as well (the Impresso `wkd_id` of the earlier design). Give each `Source` that is an archive
   its EHRI institution id.

What was not read: the CDEC Shoah ontology, which the knowledge-graph paper describes as reusing FOAF and BIO.
It may hold victim-specific terms (deportation, transport) worth borrowing for `Fact.type`.

### The factoid model (prosopography)

The prosopographies of the Byzantine world and of medieval Scotland use the *factoid* model of Bradley and
Short (King's College London; [overview](https://www.kcl.ac.uk/factoid-prosopography/about)). A factoid is
"a statement by a modern scholar of a thing a source says about a person". It links a source, a person and an
assertion, and it allows factoids to contradict each other. Our `Fact` is a factoid that also carries a
`status` and a `confidence`. Those two fields answer the model's known weakness: it cannot easily record
negative findings or a scholar's own inference.

## The proposal

### A. One person record for the whole paper; editions hold only mentions

A **`Person`** record lives once, in a corpus-wide `people/` collection (one file per person, or one file
sharded by id). An edition's enrichment file no longer copies the person. It holds the person's
**mentions**:

```ts
Mention = {
  id,                    // Impresso mention id where there is a span; else `${unit_id}:${person_id}`
  person_id,             // or "NIL" while not yet clustered (earlier design, #1)
  unit_id,
  role,                  // see below
  printed_name,          // the name as the piece prints it: "ה' מענדל גאלדמאן"
  title?, function?,     // the earlier design's person components
  bbox?, offsets?,
}
```

`role` is a closed list, made from the piece kinds above: `subject` (the article is about them),
`deceased`, `honoree` (the one greeted: wedding, birth, engagement), `signer` (signs a greeting or
condolence), `mourner`, `advertiser`, `author` (byline), `office_holder` (named as chair, secretary, board),
`donor`, `named` (anything else). `LifeEvent.principal_ids` becomes `participants: {person_id, role}[]` with
the same list. Fixes 1 and 2.

The edition bundle (`edition-bundle.schema.ts`) can still embed a *projection* of each person it mentions, so
that an edition stays self-contained for the site. That projection is generated, never edited, so it cannot
drift.

### B. A registry of sources, and citations into it

```ts
Source = {
  id,                    // "pinkas-pruzhany-1958", "yad-vashem-names", "arolsen", "the-paper", "sorid-memoir-2007"
  kind,                  // archive_database | book | memorial_book | oral_history | memoir | photograph |
                         // press | family_document | web_page | the_paper
  title, author?, editor?, published?, repository?,
  url_pattern?,          // "https://collections.yadvashem.org/en/names/{record_id}"
  host?,                 // the host a link must be on to be published (the site's leak checks)
}

Citation = {
  source_id,
  record_id?, page?, scan?, time?, unit_id?,   // the locator; unit_id for the paper itself
  url?,                  // derivable from url_pattern; stored when it is not
  quote?,                // the source's own words supporting the claim
  accessed?,             // ISO date
}
```

`externalSourceTypes` becomes this registry. The 100+ strings become about 40 sources plus locators.
Fixes 3.

### C. Facts, each with its own citations

```ts
Fact = {
  id,
  type,                  // birth | death | name | occupation | office | membership | residence |
                         // emigration | marriage | education | ghetto | camp | deportation | partisan_service |
                         // survival | burial | commemoration
  value?,                // "Pharmacist", "Chapayev Partisan Brigade, Malenkov Otriad"
  date?: { value?, from?, to?, precision: day|month|year|decade, calendar?: gregorian|hebrew, inferred?: bool },
  place_id?,
  qualifiers?,           // cause, rank, alias used, age at event
  citations: Citation[],
  confidence: confirmed | probable | possible,
  status: accepted | disputed | rejected,     // a rejected fact is kept so it is not made again
  attribution: { by, on, note? },             // "the owner", "process:people-fanout round 6"
}
```

A person's `occupation`, `residence_at_publication`, `birth_*`, `death_*`, `partisan_activity`, `ghetto_role` and
most of `additional_details` become facts. Their current fields stay readable as **derived** values (the
accepted fact of that type with the highest confidence), so existing readers keep working. Fixes 4.

### D. The fate: a conclusion that names what it rests on

```ts
Fate = {
  outcome: perished | survived | died_before | left_before | unknown | not_applicable,
  confidence: confirmed | probable | possible,
  rests_on: Fact["id"][],        // the death/survival facts and their citations
  summary?,                      // one reviewed sentence, publishable
}
```

`holocaust_fate` is then derived: `perished` + `probable` gives `likely_perished`, as today. The site can show
*why* ("Yad Vashem, record 611275: names his wife Chana née Nukhimovski, as the paper does") and can show
"probable" differently from "confirmed". `left_before` is added because the pipeline already counts 85 people
who emigrated before the war, and they are currently written as `not_applicable` or `unknown`. Fixes 5.

### E. Names with a kind

```ts
Name = { value, script: latin|hebrew, kind: birth | married | later | nickname | alias | religious |
         spelling, lang?, sources?: Citation[] }
distinct_from: { person_id?, printed_name, reason }[]     // the pipeline's not_aliases
```

`name` stays as the display name, with nothing in brackets. `aliases` is derived from `names`. Fixes 6.

### F. Relationships as records of their own

```ts
Relationship = {
  id, person1, person2,          // GEDCOM X direction: person1 is the parent in parent_child
  type,                          // the existing relationshipTypes, with one spelling
  citations: Citation[],         // the paper's units with their quote; a memoir page; a tree
  confidence, status: accepted | proposed | rejected,
  confirmed?: { by, on }, shown?: { by, on },
}
```

Each relationship is stored once and read from both sides. `proposed_relationships` becomes
`status: proposed`, with `person2` set to `"NIL"` plus a `printed_name` until the other person exists. Fixes 7.

### G. Narratives keep their facts' citations

`biographical_narratives` gains `cites: Fact["id"][]`, `attribution` and `reviewed?: {by, on}`. The privacy
projection can then publish a narrative once someone has reviewed it, instead of dropping every narrative.
Fixes 8.

### What stays out of the schema

The research trail stays in the pipeline's OKF person files and is not published: the searches made, the
records turned down, and the leads ("YV PoT: none filed — gap"). The schema carries the conclusions and what
they cite. A rejected fact or a `distinct_from` entry is the trail's only footprint, kept so the same mistake
is not made twice.

## Places, organisations, events and topics

The same pattern applies to every kind of thing the paper names. It was measured the same way: across the 238
enrichment files of `pruzhany-svelte` at `35cccf9`.

### What the data shows

| | records in the files | distinct ids | ids whose copies differ | joined to a shared list |
|---|---|---|---|---|
| places | 9,308 | 2,048 | 593 | 6 with a GeoNames id, 6 with Wikidata |
| organisations | 8,801 | 2,713 | 757 | none |
| events | 1,618 | 1,618 | — | none |
| topics | 5 | 5 | — | none |

- **One thing under many ids.** 225 place ids end in `-2`, `-3` and so on (`location-krakow` and
  `location-krakow-2`; `location-usa` and `location-united-states`). One school, Yavneh, is spread over about
  a dozen organisation ids (`org-tarbut-school-yavne`, `org-tarbut-school-yavneh`, `org-hebrew-folk-school-yavneh`,
  `org-hebrew-public-school-yavneh`, …). Another forty-odd ids are its committees, for the parents and for its
  poor pupils, which are bodies of the school and say so nowhere.
- **Events are not joined across editions.** An engagement announced on 2 February and greeted again on
  9 February 1934 is two events (`event-19340202-engagement-of-esther-cherchevski-…` and
  `event-19340209-engagement-of-esther-cherechevsky-…`), spelled two ways. There are two event systems besides:
  the enrichment `events` and the `life-events` file. Each has its own ids and its own participants.
- **Places have no time.** Pruzhany is Prużana, Pruzhene, פרוזשענע and Пружаны, in Poland's Polesie
  voivodeship in 1939, the USSR's in 1940 and the Bezirk Bialystok in 1942. Its streets were renamed (the
  "3rd of May street" is held under two ids). `parent_id` is a single parent with no date.
- **Organisations have only a name, a type and a description.** They have no place, no dates, no parent body
  and no officers. The officers are in the paper ("the board of the Small Traders' Association"), and the
  people work already reads them: the fan-out's `other` facts include "Member of the five-person Bund
  committee after the Kultur-Lige was reorganized in 1934".

How far the tagging reaches: all 233 machine-written editions have places and organisations, and 229 have
events. They were tagged by the model that writes each piece's English (`pruzhany-steps`' `write_english`).
About half their pieces name a place (51%), 42% an organisation and 48% an event; 80% name a person. The
five hand-made editions have the places and events, but only one of them has any organisations (3% of their
pieces). Every tag is on the piece as a whole. None says where in the text the name stands, or in what
role.

### The same model, kind by kind

Each kind gets one record for the whole paper, mentions with a role in each edition, names with a kind and a
time, facts with citations, and ids in the shared lists. Each maps to RiC-O:

- **Place** (`rico:Place`): `names` with language, script and the years each name was used. `part_of` with
  dates (the town in the voivodeship, the street in the town, the ghetto in the town). `type` from the
  vocabulary. Coordinates. Ids in shared lists: **GeoNames** for modern places, **Wikidata**, **EHRI's
  camps and ghettos** for those, and JewishGen's town list for the communities. The `dsmedia/arolsen` catalogue
  already loads EHRI's camps and ghettos and USHMM's town-to-region gazetteer, whose name variants (e.g.
  "Pruzhany" finds the ghetto EHRI labels "Prużana") can propose these links. A street or an address is a
  place of the town's own local list, with its old and new names.
- **Organisation** (`rico:CorporateBody`): names, `type`, `part_of` with dates (a parents' committee of the
  Yavneh school; the school in the Tarbut network; a branch of the Bund or of TOZ), place, years active.
  Ids: Wikidata for national bodies (Tarbut, the Bund, Keren Hayesod, the JNF, TOZ, ORT, Hitachdut). People's
  offices and memberships are *person facts* (`type: office` or `membership`) that point at the organisation,
  so the organisation's page lists its officers by year without holding them itself.
- **Event** (`rico:Event`): one record for the event, however many editions announce, greet or mourn it.
  `type` from the vocabulary, a date (Hebrew as printed and Gregorian), a place, `participants` with the same
  roles as mentions (the deceased, the couple, the mourners, the signers). The two event systems become one:
  `life-events` is the family events among them. A person's `marriage` or `death` fact cites its event. Events
  of the wider world (Kristallnacht, the outbreak of war) carry a Wikidata id.
- **Topic**: a term of **EHRI's thesaurus** (the controlled vocabulary of terms its portal and editions use)
  wherever one fits, and our own term where none does, so that the paper's subjects are searchable with the
  same words as the archives'.

### How they are joined

Joining is the people's problem again (issue #1, NIL clustering), but most of it is cheaper:

- **By code first.** Names folded (spelling, script, the `-2` suffix), then matched against the shared lists:
  GeoNames, EHRI and the arolsen gazetteer for places; Wikidata for national bodies and world events. An event
  is joined across editions when its type and principal people agree. This needs no model, and is checked
  the way the people's records are, against the printed words.
- **A fan-out only for what code cannot settle.** A judge and a checker, as for people, over the residue: the
  committees of one school, two towns of one name, an organisation renamed. The fan-out's
  `other_metadata` already corrects a piece's places, organisations and events, and becomes the input here.
- **The vocabulary and the harvest are shared.** Place types, organisation types, event types and mention
  roles are in the same vocabulary file. A judge's `proposed_type` for any of them goes through the same
  harvest after each round.

### On the site

The four stages of the rollout apply unchanged. A place page with its map, its names over time and the
pieces that name it; an organisation page with its officers by year; an event page gathering every greeting
and notice of one wedding; all three come at stage 4, with the person page.

## Working with the fan-out: information with no home yet

### How often it happens

It is common. The fan-out's judges (`pruzhany-steps`, `.scratch/people-fanout/judged/`, 152 batches,
844 people written) state each fact a source gives in `fate.facts`. Their `fact_kind` is one of ten, and
**312 of the 771 facts are `other`**. Of the rest, `parent_name` has 112 and `birth_year_or_age` 69. The
`other` facts are of three different sorts:

- **About the person, with no field yet:** "Moshe and Leibl in Argentina; Kalman in Israel", "Resident in
  Tel Aviv before the war", "Born in Telechany", "Wife's maiden surname Zolotnitzki", "Member of the
  five-person Bund committee after the Kultur-Lige was reorganized in 1934", "Meir Motil and Lipe Zakheim
  headed the Jewish ghetto police", "Murdered at Auschwitz … no death date stated".
- **About the source, not the person:** "Second testimony: fourth child-table row has age 8 and no name",
  "Maiden name indexed Lobental, but the original submitter declaration explicitly identifies the victim as
  Weinsztok".
- **Already in another field:** "Female", "Gender: Female".

The rest goes into `why`, one paragraph per person with a median of 1,283 characters. The examples in this
proposal (emigration, office held, a death place without a date) all came from there.

New kinds will keep appearing as the work reaches later editions, new sources (oral histories, ghetto
records) and new sorts of people (rabbis, writers, office holders). The schema must take them in without
being redesigned every round.

### Three homes, so nothing is lost

1. **A fact about the person** with a type from the list, or `type: "other"` with a short `proposed_type`
   (`"emigration"`, `"office"`, `"ghetto_police"`). It is checked, cited and kept like any other fact. It is
   simply not yet given a field of its own on the site.
2. **A note about a source** goes on the `Citation` (`Citation.note`): how a record reads, an indexing error,
   a missing row. It belongs with the source and travels with every fact that cites it.
3. **Research notes** stay in the pipeline's trail and OKF person files: searches made, records turned down,
   leads. They are never written into the schema.

### The list of types is a file, and it grows between rounds

- **One vocabulary file** in this repo lists the fact types, name kinds, mention roles and relationship types.
  Each entry has a label, a one-line definition, its RiC-O counterpart and the version that added it. Zod,
  Pydantic, the pipeline's `check.py` and the judges' instructions are all generated from it. A judge
  always sees the current list, and a check never refuses a type the schema accepts.
- **After each round, a harvest** (code, free) counts the `proposed_type`s across the round's answers and
  groups the near-duplicates. A label that recurs, say in five or more people across two or more batches, is
  proposed for the list. It goes in when a session or the owner agrees, as a minor version, with its RiC-O
  counterpart.
- **Re-typing old facts** is a pass over the kept answers. Facts whose `proposed_type` maps directly are
  re-typed by code. The rest are re-typed by a cheap model reading only the fact's own words, never the whole
  person again. A fact is never lost on the way: until it is re-typed it stays `other`, cited, and shown on
  the person's page as a plain line with its source.
- **Only additions.** A type is never renamed or removed. A type that turns out to be wrong is deprecated with
  a mapping to its replacement, so old answers stay valid. Each answer records the vocabulary version it was
  written under.

### What changes for the fan-out

- `fate.facts` becomes `facts` (a person's facts, not only the fate's), in the shape of `Fact`. `fact_kind`
  is the vocabulary's type. `paper_unit` and `paper_words` become a `Citation` to the paper.
- `why` stays as the human-readable paragraph, but `check.py` warns when it states a dated or placed event
  (a year, a town, a country) that no fact carries. That is how the paragraph is kept from becoming the
  overflow again.
- `other_metadata` (corrections to a piece) is unchanged. It is about pieces, not people.

## Privacy

The site's projection (`src/lib/privacy/projection.ts` in `pruzhany-svelte`) works field by field today. With
facts it can work fact by fact: publish an accepted fact whose citations are all on allowed hosts, about a
person not presumed living. [corrected 2026-10-20: accepted is not editorially approved; publication also needs identity and review checks.] `Source.host` supplies source metadata, not publication authorization [corrected 2026-10-20: stage 1 publishes none of these fields; the site retains its explicit privacy allowlists].

## How it reaches the live site today, and what changes

Today a person travels like this:

1. **`pruzhany-steps`**: the fan-out's judged answers become the register (`corrections/people/*.toml`,
   written by `.scratch/people-fanout/write_register.py`). The owner's family register is kept by hand.
2. **`lay_people`** (and `write_site`, which calls it on every write) writes each register person into every
   edition's `enrichment` and `content-units` in a checkout of the site. It checks each file against
   `schemas/site/*.schema.json`, a copy of this repo's Zod shapes made with `z.toJSONSchema`.
3. **`pruzhany-svelte`**: a pull request carries the changed `static/data/` files, recorded in
   `MANUAL_OVERLAYS.md`. CI validates them against this repo's schemas, through the submodule. On merge to
   `master` the site deploys, and the privacy projection decides which fields are served.

The design keeps that road and changes what travels on it, in this order. Each stage can be deployed alone:

| stage | `pruzhany-schema` | `pruzhany-steps` | `pruzhany-svelte` | what a visitor sees |
|---|---|---|---|---|
| 1 | the vocabulary file and the new optional fields (`facts`, `names`, `fate`, `citations`, `mentions[].role`, the source registry), Zod and Pydantic | copies the new JSON Schema and the vocabulary into `schemas/site/`, by commit | bumps the submodule; the projection still drops the new fields | nothing changes |
| 2 | — | the register gains `facts`, `names`, `fate` and `distinct_from` from the judged answers, which already hold most of them. `lay_people` writes the new fields **and** the old ones derived from them; the fan-out's answer format and `check.py` follow the vocabulary | a data pull request as today | nothing changes; the files now carry the evidence |
| 3 | — | — | the projection publishes accepted facts whose citations are on allowed hosts; the person view shows a fate's source and its confidence, and a fact list; leak tests for the new fields | "probable" shown as such, with its record; dated facts (emigration, offices) |
| 4 | a corpus-wide `people` file and the edition bundle's people as a projection of it | `write_site` writes `people/` once and mentions per edition | loads people once; a page per person across editions (`/people/[id]`) | following a person through the paper |

[corrected 2026-10-20: person pages already exist downstream according to #16; stage 4 adds the corpus storage/loading architecture, not the first person page.]

The vocabulary reaches `pruzhany-steps` as a copy by commit, as the site's shapes already do: steps never
imports another checkout. A new type harvested after a round therefore goes through three steps: a
schema PR, the copy in steps, then the submodule bump on the site. Until all three are done, the fact stays
`other` with its `proposed_type`, which every stage already accepts.

## Migration (additive first, as the earlier design says)

1. Add `Source`, `Citation`, `Fact`, `Name`, `Fate` and `Mention` as optional fields beside the current ones.
   Pydantic twins and the parity test go in the same PR.
2. `pruzhany-steps`' `lay_people` writes them from the register. The register already has `archives[].strength`,
   ties with quoted evidence, `not_aliases` and fact-by-fact fate evidence, so it needs no new research.
3. Generate the old fields from the new ones, and make the generated fields read-only.
4. Move people out of the edition files into the corpus-wide collection, and make the edition bundle's people a
   projection.
5. Let the site show a fate's sources, its confidence, and a page that follows one person across editions.

## Open questions

- One file per person, or one file for all? 884 people today; up to tens of thousands if every name in the
  paper is clustered (#1).
- Should `role` follow HIPE's `pers.ind.articleauthor` and be a sub-type, or stay a separate field?
- Hebrew-calendar dates: should `Fact.date` keep the printed Hebrew date as given, beside its Gregorian
  conversion?
- Should every edition's people carry EHRI and GeoNames ids from the start, or only once a person or place is
  confirmed?

## Decisions and changes since (20 October 2026)

The [pilot, #15](https://github.com/dsmedia/pruzhany-schema/pull/15), merged as
`96fa579`, is an isolated executable slice, not stage 1 or a production migration.
Its [review and limits](../../pilots/sourced-entities/README.md) distinguish evidence,
identity confidence and editorial approval; all real assertions and joins remain pending.
The [stage-1 plan, #16](https://github.com/dsmedia/pruzhany-schema/issues/16), its
[review](https://github.com/dsmedia/pruzhany-schema/issues/16#issuecomment-6281076205)
and the owner's [decisions](https://github.com/dsmedia/pruzhany-schema/issues/16#issuecomment-6281227920)
supersede the rollout details above where they differ.
[#17](https://github.com/dsmedia/pruzhany-schema/pull/17) brings the pinned standards
and alignment gate onto this branch; this document is ticket 1 of #16.

The owner's decisions are to stay close to EHRI and RiC-O, enforced by
[`standards/check_alignment.py`](../../standards/check_alignment.py): prefer an EHRI
class, then a term in EHRI's RiC-O base, then a declared local term with a reason.
Keep existing site IDs. The living-person presumption belongs to the site,
`pruzhany-svelte/src/lib/privacy/presumption.ts`: anyone printed in the paper is
presumed deceased by now for display. That is permission to display, never evidence
of a death or fate. The owner approves vocabulary additions in batches, each with
two or three real examples and its mapping; until approval, keep `other` and
`proposed_type`. On 20 October the owner approved in advance the types of vocabulary 1.0.0 as
recommended, and allowed merging under the gates recorded on #16.

The review's four changes are accepted:

1. Stage 1 attaches optional fields only to `EnrichedPerson` and `EnrichmentData`,
   with no attachments to `EditionPerson` or `EditionBundle`. Public bundle fields
   wait for stage 3's publication decisions.
2. The fan-out's `fact_kind`s are a crosswalk, not fact types. `parent_name`,
   `spouse_name`, `sibling_name` and `child_name` are relationships;
   `giver_of_record` describes a source and stays private. `birth_year_or_age`
   becomes `birth` with `inferred`; `street_or_address` becomes `residence`;
   `schooling_or_pupil` becomes `education`, mapped to RiC-O `TeachingRelation`.
3. Use one corpus-wide source register, referenced by `Citation.source_id`, rather
   than per-edition copies. The authoring location of that register is still to be chosen.
4. Each citation requires at least one nonempty locator among `record_id`, `page`,
   `scan`, `time`, `unit_id`, `url`, with the same rule and parity cases in Zod and
   Pydantic. A quote or a source ID alone does not meet it.

The [pinned RiC-O 1.0.2 list](../../standards/rico-1.0.2.json) contains the planned
terms: membership `hasOrHadMember` / `MembershipRelation`; office `Position` /
`PositionHoldingRelation`; parent/child `hasChild` / `isChildOf`; sibling
`hasSibling`; spouse `hasOrHadSpouse` / `SpouseRelation`; teaching `hasOrHadTeacher` /
`TeachingRelation`. Emigration has no RiC-O term: keep it local with a reason, or
model an `Event` with participation. `MigrationRelation` connects digital
instantiations. Use EHRI's `ehri:Person`, `ehri:City` / `ehri:Region` /
`ehri:Country`, and `ehri:CorporateBody` where applicable, in its pinned
`http://lod.ehri-project-test.eu/ontology#` namespace.

Of the four open questions above, two are settled: `role` stays a separate field,
not a HIPE subtype, and dates retain the printed Hebrew date without inventing a
Gregorian conversion. Two remain deferred: one file per person versus a sharded
collection, and the timing of EHRI/GeoNames authority links. The plan proposes
confirmed authority links only, with candidates private; stage 1 does not settle
that storage or reconciliation policy.

Other changes in #16: `left_before` stays out of `Fate.outcome`; dated emigration
facts establish neither survival nor death. Evidence confidence, identity confidence
and editorial approval are separate. Stage 1 adds only the contract and publishes
nothing new; relationships, narrative citations, positional mentions and corpus
identity collections remain later work. The pilot does not certify production fate
criteria or replace the site's privacy policy.
