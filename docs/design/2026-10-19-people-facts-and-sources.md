# People, their facts and their sources: a proposal

**Status:** proposal; no schema type changes yet.
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
  `5d42d25` (5 March 2026), version 0.2.0;
- [RiC-O 1.1](https://github.com/ICA-EGAD/RiC-O) at `06912e1` (`ontology/current-version/RiC-O_1-1.rdf`);
- EHRI's report on its digital editions and standards (deliverable D11.6, July 2024);
- the [EHRI portal's authority sets](https://portal.ehri-project.eu/authorities).

What EHRI does:

- **Its data model is ICA's Records in Contexts ontology (RiC-O)**, extended. `ehri:Person` is a subclass
  of `rico:Person`, and EHRI reuses schema.org for addresses and opening hours. EHRI's own extensions concern
  archives and institutions. EHRI adds nothing of its own for people: a person is RiC-O's person.
- **RiC-O records a relation as a record of its own** (`rico:Relation` and its subclasses `FamilyRelation`,
  `AgentToAgentRelation`, `PerformanceRelation`, …). A relation has `relationHasSource`, `relationCertainty`,
  `relationHasDate` and `relationState`. The inverse property `rico:evidences` links a document to the
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
| `Relationship` with `citations`, `confidence`, `status` | `rico:Relation` + `relationHasSource`, `relationCertainty`, `relationState` | the same idea; keep our field names and map to these |
| `Fact` with `citations`, `confidence`, `date` | an n-ary `rico:Relation` or `rico:Event` with source and certainty | RiC-O has no general "fact"; a fact is exported as an event or a relation |
| `Name` with `kind`, `script` | `rico:AgentName` + `usedFromDate` | RiC-O's names are records of their own, as ours would be |
| `Citation.unit_id` (the paper's piece) | `rico:evidences` from a `RecordResource` | each piece of the paper is a `RecordResource` |
| `Fact.place_id` for a ghetto or camp | EHRI vocabulary URI (camps, ghettos) | the `dsmedia/arolsen` catalogue already loads EHRI's camp and ghetto lists |
| `Fact.type: occupation` | `rico:OccupationType` | |
| `Source` registry | EHRI institutions + archival descriptions | Yad Vashem and Arolsen are EHRI institutions with portal ids |
| `Person` ↔ archive records | `owl:sameAs` / `schema:sameAs` | the site already writes `sameAs` in its JSON-LD |

Two conclusions follow:

1. **Model in our own JSON, but keep it mappable to RiC-O.** No Holocaust project in these sources keeps
   its working data in RDF. EHRI publishes RiC-O from its portal's own database, and victims' databases keep
   their own shapes and are linked by `sameAs`. Every field in the proposal below has a RiC-O counterpart
   (the table), so an export to RiC-O / JSON-LD is a mapping, not a remodel.
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

## Privacy

The site's projection (`src/lib/privacy/projection.ts` in `pruzhany-svelte`) works field by field today. With
facts it can work fact by fact: publish an accepted fact whose citations are all on allowed hosts, about a
person not presumed living. `Source.host` gives the leak checks their list of hosts.

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
