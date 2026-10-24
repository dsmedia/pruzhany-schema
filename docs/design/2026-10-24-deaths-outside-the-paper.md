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
- **A record-only death stays a fact** (constraint (a) of the council: every life event so far comes from the paper).
  Its `event_id` stays empty, so that one death event can later gather the facts unchanged. Whether a death event may
  rest on records alone is the owner's to decide, as an amendment to ADR 0001.

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

## Not done here

- The register's structured statements and the writer: pruzhany-steps.
- The site's wording and its `ARCHIVE_HOSTS` copy: the redesign session.
- The crosswalk rows for death and place of death from the fan-out: the owner's next vocabulary batch.
