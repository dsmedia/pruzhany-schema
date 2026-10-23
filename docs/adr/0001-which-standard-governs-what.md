# ADR 0001: Which standard governs which part of the data

**Status:** accepted by the owner on 23 October 2026 ("yes to all", the fourth grilling of brief 09). The direction was agreed as Q14 of brief 09 (pruzhany-steps `.scratch/site-files-keeper/briefs/09-round-4-one-event-across-issues.md`) and vetted in
[`docs/design/2026-10-23-standards-foundation-vetting.md`](../design/2026-10-23-standards-foundation-vetting.md), whose
sections are cited below as §n.

## Context

The owner's rule (`CLAUDE.md`): prefer an EHRI class, else a RiC-O term in EHRI's RiC-O version, else a local term with
a reason. That rule says how to pick a term; it does not say which standard is the authority for each part of the data,
and the data is labelled after the standards more than it is shaped by them: relations stored both ways, persons made
per issue, nothing that tests meaning (brief 09, "The standards foundation"). Three standards are in play, and the
vetting found that they cover different ground and leave one part to us:

- **Impresso** governs a historical newspaper as pages, regions, content items and their types, and the mentions of
  named entities with their Wikidata links. It does not cluster unlinked mentions across documents: an entity is a
  Wikidata QID or nothing (§4).
- **EHRI** (ontology 0.2.0, `ehri-0.2.0.json`) models persons and families as subclasses of RiC-O's, and has no event,
  role or kinship term; its live graph holds no events or family relations. Its namespace is a test domain that will
  move, with redirects (§1).
- **RiC-O** (1.1, `rico-1.1.json`, the version EHRI 0.2.0 imports) has events and their types, participants, family
  relations with their direction, evidence, dates and identifiers, and no role for a participant in an event (§2, §3).

## Decision

| part of the data | governed by | in practice |
|---|---|---|
| the physical and logical layers: pages, regions, lines, content items, types | **Impresso** | as `CONTEXT.md` in pruzhany-steps already says |
| mentions of people, places and organisations, and their Wikidata links | **Impresso** | Impresso-2's form is checked again before a Wikidata field is built (§4) |
| persons and families | **EHRI** (`ehri:Person`, `ehri:Family`) | no `ehri:` IRI is stored in the data; it is written only in an export, from the pinned list (§1) |
| life events and their kinds | **RiC-O** (`rico:Event`, `rico:EventType`) | one event per happening; a person's birth or death date is derived from it (§2) |
| a main person's part in a life event | **RiC-O**, extended | a local subproperty of `rico:affectsOrAffected` (the baby, the bride, the groom, the boy, the one who died) or of `rico:hasOrHadParticipant` (a parent at a birth), each declared in a profile with its reason (§2) |
| family relations | **RiC-O** (`ChildRelation`, `DescendanceRelation`, `SpouseRelation`, `SiblingRelation`, `FamilyRelation`) | stored once: in RiC-O's direction where it has one, once per pair where symmetric, in one local direction where RiC-O has no term (§3) |
| a relation's or a fact's evidence | **RiC-O** (`rico:isEvidencedBy` / `rico:evidences`) | not `rico:relationHasSource`, which is the relation's first end (§3) |
| dates | **RiC-O** (`rico:Date`: `expressedDate`, `normalizedDateValue`, `dateQualifier`) | the printed words and calendar kept; "reported in" a qualifier (§2) |
| identifiers, ours and others' | **RiC-O** (`rico:Identifier`, `rico:IdentifierType`) | a merged id kept as an "old identifier" that redirects (§4) |
| identity across issues of people not in Wikidata | **ours** | one id per person, after TAC-KBP's NIL clusters and Yad Vashem's personal files; resolved ids join first, then the full-printed-name rule; ids never renamed, reused or deleted (§4) |
| a mention's role, standing and review, the supplied name kind, uncle/aunt and in-law directions | **ours** (local terms) | each with its reason in a profile; a mention maps to RiC-O 1.2's `hasContentWhichRefersTo` once it is released and pinned (§1) |

What we claim is "mapped to RiC-O 1.1 as EHRI 0.2.0 imports it, with these rules tested", never "conformant": no
conformance notion exists for RiC-O (§6). The rules are those of §6, each labelled RiC-O, RiC-CM or local; a rule
labelled RiC-O cites the axiom in `standards/rico-1.1-axioms.json`, pinned at the owner's word of 23 October 2026.

## Consequences

- The cross-edition design of 2026-04-25 is amended where it says Impresso settles identity: Impresso settles the
  Wikidata-linked half; the NIL half (#1) is answered by this decision's identity row and §4's rule.
- Round 4 of ticket 09 (pruzhany-steps) builds events, parts and the described children to this table; storing
  relations once, and the evidence mapping, are their own tickets.
- Vocabulary changes it implies go to the owner's batch (#16): the parts, two event kinds, grandparents remapped to
  `hasDescendant`, the `supplied` name kind, `parenthood` deprecated.
- When EHRI moves its namespace, or RiC-O 1.2 or 2.0 is released and EHRI imports it, the owner is told; a new
  `standards/` file is added at the owner's word and every mapping re-checked. Stored data does not change.

## Considered and not chosen

- **Impresso for identity across issues** (Q14 as first worded): Impresso has no such thing to follow (§4).
- **EHRI for events**: EHRI has no event, and its data puts birth and death as dates on the person (§1); dates on the
  person alone cannot gather the pieces of one happening (§2).
- **`rico:eventRelation_role` or `rico:RoleType` for parts**: the first cannot carry a part, the second is attached only
  to creation relations; RiC's own guidance is a local subproperty (§2).
- **An RDF export validated by SHACL now**: declined by the owner on 23 October 2026 ("I don't [want] standards theater,
  but real proper tests if possible"); RiC-O publishes no shapes, and EHRI's describe only its own records (§1, §6).
