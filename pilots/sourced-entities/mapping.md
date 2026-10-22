# RiC-O / EHRI mapping exercised by the pilot

EHRI ontology 0.2.0 imports RiC-O 1.1, and the gate checks against both (the owner's word of 2026-10-22); the pilot’s terms also exist in RiC-O 1.0.2, which EHRI 0.1.1 imported. The pilot uses that RiC-O namespace directly and adds a small, explicit application profile for research workflow. It does not assume EHRI supplies a general historical-claims or Holocaust-fate ontology.

The upstream RDF files were read on 2026-10-19. [The checked component profile](ric-o-profile.json) records their SHA-256 hashes, versions and source links. This is a checked vocabulary subset, not an OWL conformance certification.

| Pilot concept | RDF representation | EHRI | Qualification |
|---|---|---|---|
| Person | `rico:Person` | `ehri:Person` | Local ID; no automatic Wikidata/EHRI equivalence. |
| Newspaper edition | `rico:RecordSet` | — | Individual cited content units are `rico:Record` nodes. |
| Other source | `rico:RecordResource` | — | Hosted copies retain their underlying bibliographic `work_id`. |
| Printed name | `rico:AgentName` | — | `rico:name` carries a language tag; `pc:recordedFor` records its proposed association with a person. |
| Event / place | `rico:Event` / `rico:Place` | `ehri:City`, `ehri:Region`, `ehri:Country` when known | Event identity proposals remain explicit. |
| Pending, disputed or rejected assertion | `rdf:Statement`, `pc:Claim` | — | `rdf:subject`, `rdf:predicate`, `rdf:object`; no corresponding base triple is emitted. |
| Approved assertion with confirmed identity | Base RiC-O property plus a qualified `rico:Relation` | — | `relationConnects`, `relationHasSource`, `relationCertainty`, and the source record's `evidences`. An unapproved identity join still blocks promotion. |
| Residence | `rico:hasOrHadLocation` | — | Dates remain attached to the qualified statement; the legacy scalar is resolved at the edition date. |
| Occupation | `rico:hasOrHadOccupationOfType` → `rico:OccupationType` | — | An occupation is not a free literal in an object-property position. |
| Birth/death date | `rico:hasBirthDate` / `hasDeathDate` → `rico:Date` | — | Printed date, calendar, normalized interval and inference flag survive as typed JSON extension data. |
| Birth/death place only | `rico:hasBirthPlace` / `hasDeathPlace` | — | Never masquerades as a date property. |
| Marriage | `rico:hasOrHadSpouse` | — | Engagement participation is separate and does not create a marriage. |
| Event participation | `rico:isOrWasParticipantIn` | — | `pc:role` records the participant's role. |
| Citation and attribution | `prov:wasDerivedFrom` plus bibliographic locator | — | A citation points at a source record, not an equivalent person. |
| Fate | `pc:FateConclusion` | — | Outcome, confidence, review and supporting claim IDs; no fabricated RiC-O counterpart. |
| Identity join | `pc:IdentityProposal` | — | Original IDs, proposed target, citations and preview/review state. |
| Editorial approval / disputed status | `pc:reviewState`, `pc:status` | — | **Not** `rico:relationState`: that property describes present/past/ongoing state. |

The real-person fixture has pending editorial review throughout. Its export therefore demonstrates reified assertions and uses actual RiC-O classes for people, names, records and events, while withholding unqualified historical claim triples. Tests use fictional people to exercise approved `rico:Relation` output, source/evidence links, date object ranges and disputed claims.

No `owl:sameAs` or `schema:sameAs` is emitted. A record describing a person is not the person. Proposed identity matches require separate adjudication before an identity equivalence could be exported. The `example.org` namespace deliberately marks every pilot URI as experimental rather than minting production identities.

`profile.ttl` declares the local terms. JSON-LD has an inline prefix context and is parsed in tests without fetching any remote context. The current checks validate RDF parsing, the actually used RiC-O IRIs and selected semantic invariants; they do not run a full OWL reasoner or claim compliance with an EHRI ingestion API.

EHRI’s Person class adds no person-specific properties. People’s names remain `rico:AgentName`: EHRI’s AlternateAgentName and ParallelAgentName are defined for institutions. EHRI’s namespace is the upstream test-domain namespace `http://lod.ehri-project-test.eu/ontology#`. Place kind (`city`, `region`, `country`) may be supplied to the RDF exporter; the current pilot Place contract carries no kind and real data has no places.
