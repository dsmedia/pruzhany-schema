# Deaths the paper never printed: statements, places and their identifiers

**Status:** built on 24 October 2026, the schema half of the council run `2026-10-23-place-of-death` (pruzhany-svelte
`docs/council/runs/2026-10-23-place-of-death/decisions.md`), agreed with the redesign session and started at the
owner's "Yes after I clear" (pruzhany-steps `.scratch/place-of-death/handoff.md`).
**Builds on:** [`2026-10-19-people-facts-and-sources.md`](2026-10-19-people-facts-and-sources.md),
[`2026-10-23-standards-foundation-vetting.md`](2026-10-23-standards-foundation-vetting.md) (§4, outside ids),
[ADR 0001](../adr/0001-which-standard-governs-what.md).

## The case

Shulim Judewicz, born 5 April 1918. Five records speak to his end: an Arolsen card and the transport list Ohrdruf →
Bergen-Belsen of 13 March 1945 ("103878 Jodowicz Szymon"); the Buchenwald memorial's letter of 2022; his brother
Morris's testimony of 1998 ("He was among those that perished in this march"); and the Bergen-Belsen memorial's book of
the dead, entry 4695 ("Szulem Judewicz", died 1945 in Bergen-Belsen). Until now the shared record held one `death` fact
citing only the family's register, with no place and no date.

## What the contract already held, and uses as it is

- **One `death` fact per source's statement, never merged.** `Fact` has `value`, `place_id`, a `SourcedDate`
  (`precision: range` with `start` and `end` where a record gives only bounds, `inferred` where a bound is reasoned),
  `citations` with `record_id`, `url`, `quote` (the record's own words and spelling), `note` and `accessed`, and
  `evidence_confidence`. A statement another outweighs is `status: disputed`, never deleted. A record with no address of
  its own (the book of the dead) is cited by `record_id`, with the search page as `url` where one exists and a `note`.
- **Camp movements are `deportation` facts** (released in 1.0.0), each cited, `place_id` the camp reached.
- **The person's `death_year` and `holocaust_fate` are derived** from the preferred statement through `Fate.rests_on`
  and `legacyHolocaustFate`. The ranking, best first: a record made at the time, a memorial's book of the dead, a page
  of testimony, a later oral testimony. Confidence never rises above the best witness.
- **The council initially left a record-only death as facts** (constraint (a): every life event then came from the
  paper). The owner answered on 24 October 2026 that a death event may rest on records alone (ADR 0001's amendment).
  Ticket 03 below builds that amendment; the facts acquire `event_id` without changing their statements.

## What changed

1. **`SharedPlace.identifiers`**, a list of `PlaceIdentifier`: `source_id` (the authority list, a registered source),
   `value` (the id as the authority writes it), `url` (https, optional), `accessed` (the day it was read on the
   authority's own pages) and `attribution` (who added it). Not `same_as`: the vetting (§4) keeps `sameAs` for an
   adjudicated equivalence, and carries outside ids "only on evidence, with their source and standing". Naming the
   authority by a registered source needs no new vocabulary: its host and address form are described once, in the
   source. An export makes one `rico:IdentifierType` for each such source.
2. **Tests of meaning** in `SharedRecord`: an identifier's source must be registered; one identifier may sit on one
   place only; an identifier's address must be on its source's host.
3. **`Source.host` is a bare lowercase host name**, never with a scheme or `www.`, and **every cited address is on its
   source's host** (or a subdomain), where the source names one. Measured before it was made a rule, on the site's
   shared record of 24 October 2026: all 781 citations with an address already were. This makes the registry the one
   place a source's host is written; it replaces neither the site's privacy allowlist nor its review (the correction of
   20 October in the facts-and-sources design: a host is metadata, not permission to publish).

## Mappings (`vocabulary/site-content.json`, `bindings`; read in `standards/rico-1.1-axioms.json`, 24 October 2026)

| field | term | why |
|---|---|---|
| `identifiers` | `rico:hasOrHadIdentifier` | domain `rico:Thing`, range `rico:Identifier` |
| an identifier | `rico:Identifier` | a subclass of `rico:Appellation` |
| `value` | `rico:textualValue` | domain includes `rico:Appellation` |
| `source_id` | `rico:hasIdentifierType` | domain `rico:Identifier`, range `rico:IdentifierType` |
| `accessed`, `attribution` | local `pc:site_identifier_reading` | `rico:isEvidencedBy` has domain `rico:Relation`, and an Identifier is not one |
| `Source.host` | local `pc:site_source_host` | neither standard records where a source's records are served |
| a fact with a place | `rico:PlaceRelation` | exactly one Place as `relationHasSource`; carries `isEvidencedBy` and `relationCertainty` |
| `evidence_confidence` | `rico:relationCertainty` | domain `rico:Relation` |
| the preferred death statement | `rico:hasDeathPlace`, `rico:hasDeathDate` | written only in an export, never stored, never from a disputed or proposed statement |

The released definition of the `death` fact type ("a death place uses rico:hasDeathPlace independently") is unchanged:
the binding says how that shortcut is written, from the preferred statement only.

## The places of Shulim's records, read on the EHRI portal on 24 October 2026

| place | EHRI id | portal title | coordinates there |
|---|---|---|---|
| Bergen-Belsen | `ehri_camps-42` | Bergen-Belsen concentration camp | 52.7589, 9.9071 |
| Ohrdruf | `ehri_camps-137` | Ohrdruf concentration camp (under Buchenwald concentration camp) | 50.8260, 10.7356 |
| Sachsenhausen | `ehri_camps-803` | Sachsenhausen concentration camp | 52.7662, 13.2624 |
| the Pruzhany ghetto | `ehri_ghettos-824` | Prużana Ghetto | 52.5567, 24.4644 |

Each address is `https://portal.ehri-project.eu/keywords/<id>`. EHRI 0.2.0 has no camp class (City, Country, Region
only), so `location_types.camp` stays local. The portal's pages also give Wikidata ids; no Wikidata identifier is
written until Impresso-2's form is checked again (vetting §8, "Later").

## Death events from records (ticket 03, 24 October 2026)

`SharedEvent.evidence_basis: "records_only"` explicitly says that no issue selects this death. Absence of an issue
selection alone is insufficient: older research events also have no selection, and a shared event must remain
intelligible when read without every issue. The marker is optional on existing events and is removed if a newspaper
death later covers the same person. A records-only event has exactly one main person, with the released `deceased`
part, and one date entry: `{record_fact_id: "<preferred death fact id>"}`.

This new `LifeEventDate` form refers to the accepted record statement instead of copying its date. Read that fact's
`date` for the event and the person's derived death date. This preserves `SourcedDate` exactly, including ranges,
inferred bounds, words without normalization, and the absence of a known date. Shulim's `00.00.1945` remains the range
`1945-03-13` to `1945-12-31`, `inferred: true`; it gives 1945, never a death on 13 March. Where records disagree,
`Person.preferred_death()` selects the statement, with the existing witness/confidence ranking and register tie order;
the other dates stay in their facts. `location_id` must equal that same statement's `place_id`, including absence.
No date is added to `SharedPerson`. The site's consumer must resolve the date reference before projecting or displaying
the event or deriving the person's year/day; public projection remains the site session's work.

The writer gathers records after resolving the newspaper's events and people's identities. It reuses an existing
death for the same resolved deceased person, retaining its id and its actual printed dates after the preferred record
reference; an issue-date fallback is replaced. Otherwise it makes `event-death-<person id without person->`, independent
of the date, source, place and enumeration order. Every death fact of that person receives the event id, including
disputed and proposed facts and older family assertions. Facts retain their ids, payloads, standing and citations.
Deportations remain facts. A later newspaper death retires the record event through the writer's permanent redirects.

The prior distinction between a memorial and a death still holds (ADR 0001; the one-life-event design): an annual or
thirtieth-day commemoration keeps its own `memorial` event, `remembered` part and date. A memorial is not silently
retyped as the death. No eligible person in this measurement has only a newspaper memorial.

Both language contracts refuse a second death for one person, a death fact referencing another person's death or a
memorial, a missing/disputed/proposed/non-record preferred statement, a place different from that statement, or a
records-only event selected by an issue or by a content item's `event_id`. A date reference is first and unique; it
cannot also carry a printed or reported-in date. Existing printed-calendar, ISO-date and first-report rules remain.
`records_only` describes the event's basis and lack of selection, not the absence of all older assertions: the writer
must gather them unchanged. In particular, the input includes 70 accepted paper assertions on these people whose
citations alone do not identify them as the event's deceased. They cannot establish an event join. Their editorial
standing is preserved; no source or citation is corrected in this ticket.

Mappings checked in the pinned `standards/rico-1.1-axioms.json` and vocabulary:

| element | mapping |
|---|---|
| death event and kind | existing `rico:Event`, `rico:hasEventType`, released `pc:event_types_death` |
| person who died | released `pc:part_deceased` under `rico:affectsOrAffected` (Event → Thing, narrowed to Person) |
| evidence on the sourced statement | existing `rico:isEvidencedBy` (Relation → RecordResource); an export qualifies the event assertion through `rico:EventRelation`, never puts this property directly on Event |
| selected source date | existing `rico:Date` with `expressedDate`, `normalizedDateValue` and `dateQualifier`; no new date claim |
| `evidence_basis` and `record_fact_id` | local `pc:site_event_evidence_basis` and `pc:site_event_record_date`, declared with reasons in `vocabulary/site-content.profile.ttl`; neither pinned ontology chooses a preferred statement or records absence from this newspaper |

The 238-issue input gains **260** death events; **0** people join an existing newspaper death. **137** preferred
statements have dates and **123** do not. **2,491** death facts gain their person's event id, including facts joining
already existing newspaper deaths; all **25** deportation facts and every citation remain unchanged. The entire
candidate archive passes the schema, and repeating the gathering gives identical shared-record shard bytes.
The full Shulim event, its three record statements, counts and input digest are kept in pruzhany-steps
`decisions/159-death-events-from-records/measurement.json`; decision 159 records checks and refresh commands.

The site's wording, projection and `ARCHIVE_HOSTS` copy remain the redesign session's. The fan-out crosswalk rows for
death and place of death remain the owner's vocabulary batch; this ticket releases no new event kind or part.
