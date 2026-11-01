# linkml/: the record's data, defined once in LinkML

This folder is the written definition of the record's data in [LinkML](https://linkml.io), from
which the project generates a JSON Schema for each document, Python and Zod field declarations,
and a data dictionary. **The retained Zod refinements and Python rules still validate.**
What LinkML cannot say about the shapes is listed in
`known-looser.yaml`, each with what enforces it instead.

| File | What it is |
| --- | --- |
| `schema/*.yaml` | The definition: `types.yaml` (the shared types), `vocabulary.yaml` (the vocabulary's enums, generated), `site_common.yaml`, `pages.yaml`, `content_items.yaml`, `mentions.yaml`, `life_events.yaml`, `editions.yaml` (the issue documents and the catalog), `sourced_entities.yaml`, `media.yaml`, `shared.yaml`, `shared_record.yaml` (the shared record). Imports run types/vocabulary <- site_common <- sourced_entities <- shared_record; media imports site_common. |
| `schema/vocabulary.yaml` | Written by `vocabulary/generate.py` from `vocabulary/*.json`, one enum a group, never edited by hand: change the JSON, run that generator, then `linkml/generate.py` for its docs. That generator's `--check` (`bin/verify vocabulary`) fails on a hand edit. |
| `modules.json` | The manifest: each schema file, its top class (or `null`) and the name its outputs take. |
| `generated/` | What `generate.py` makes from the manifest, committed: `json-schema/<name>.schema.json` for a module with a top class, `docs/<name>/` (gen-doc) for every module. Never edited by hand. |
| `generate.py` | Makes `generated/` afresh, or with `--check` compares it byte for byte. |
| `zod_generator.py`, `../zod/generated/` | Static Zod shapes adapted from the pinned JSON Schema class index; generated, never edited by hand. |
| `lint.py` | The house lint (below). |
| `linkml-lint.yaml` | How `linkml lint` is run: every recommended rule, no warning allowed. |
| `known-looser.yaml` | What the Zod exports refuse that the definition cannot: kind, places, why, and what refuses it. |
| `export_zod.ts` | Makes the six Zod exports again from this checkout, as pruzhany-steps' `site_shapes refresh` does. |
| `model-map.json`, `generated/contract.json` | Explicit model mapping and generated class inventory used by the LinkML–Zod contract gate. |
| `generated/docs/data-dictionary.md` | One readable page of classes, fields, descriptions, requirements, vocabulary, mappings and remaining validator duties. |
| `planned.yaml` | Source-cited future requirements for the dictionary only; never imported by document schemas. |
| `requirements.in`, `requirements.lock` | The locked environment: LinkML and everything it brings, by hash. |
| `build-constraints.in`, `build-constraints.txt` | The one build tool, setuptools, by hash. |
| `checks/documents.yaml` | Each check the twins of the issue documents and the catalog make beyond their shapes (every Zod refinement and Pydantic validator), and how the definition holds it: a LinkML rule, a rule of pruzhany-steps' `record/rules.yaml` (cited or proposed), or the twins alone; `tests/test_documents_checks.py` counts them. |
| `checks/record.yaml` | The same for the twins of the shared record, the sourced entities and media; `tests/test_record_checks.py` counts them. |
| `schema/physical.yaml` | Impresso's stored physical page contract, separate from the website's pages: page, region, paragraph, line, word and the shared array-valued box slot, with the computed identifier rule. |
| `external_schema.py`, `generated/external/physical/` | Explicit-null JSON Schema adapter and the physical contract's own class inventory and learning index. The external contract is checked against Impresso rather than the site's Zod/Pydantic twins. |
| `schema/exchanges.yaml`, `generated/external/exchanges/` | Prompt-version metadata and references to kept answers in steps, with their own external inventory and learning index; prompt text and answer payloads stay outside this repository. |
| `schema/answers.yaml`, `answer_generator.py`, `generated/external/answers/` | The four current structured-answer contracts and their exact request JSON Schema strings, plus an external class inventory and learning index. These procedural contracts have no EHRI/RiC-O mapping; the module explains why. |
| `tests/` | The canaries (`canary_*.py`), the tests (`test_*.py`) and their planted files (`fixtures/`). |

## Running it

### Structured answers

The `model-answers` manifest entry has no single top class: each class annotated
with `asking` defines one independent response document. `generate.py` and its
`--check` include all four `external/answers/<asking>.schema.json` files. Unlike
the readable generated files, these contain the exact `json.dumps` request string,
with no final newline. Their titles, descriptions, property/required/enum order,
closedness and defaults reproduce the released Pydantic **2.13.5** serialization
layout. The emitter needs no Pydantic runtime. The schema gate records all four
baseline byte counts and SHA-256 values; steps also compares the actual bytes.

`answer_generator.py` accepts only inline attributes, string/integer/boolean
ranges, literal string alternatives, inlined objects and lists, requiredness,
titles and descriptions. Unsupported constructs fail, including inheritance,
recursive classes and unknown constraints or annotations. `nullable` explicitly
allows JSON null independently of requiredness; `default_empty_list` preserves the
existing serialized default without making a required key optional.
`description_in_wire: false` distinguishes documentation for fields whose paid
schema has no description. Existing wire descriptions are retained verbatim.
These annotations are bounded wire adaptations, not claims that native LinkML
validation enforces required nullable keys. No archival entities or released
vocabulary values are added. New shapes are made here first; steps copies the
generated file into a new prompt version, never edits the generated file.

Read **30 October 2026**: LinkML [Slots](https://linkml.io/linkml/schemas/slots.html)
and [Annotations](https://linkml.io/linkml/schemas/annotations.html), Pydantic
[JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/), and Python
3.13 [json](https://docs.python.org/3.13/library/json.html). The exact released
layout is witnessed by the byte tests rather than presumed from current defaults.

### Generated Python and retained rules

`pydantic/generated/models.py` is one canonical class graph. The previous Python modules re-export
those classes and retain their validation functions and public helpers. `SiteIssue` and `SiteArchive`
remain hand-written carriers for cross-document checks. Extraction models and the isolated pilot
remain separate. The catalog now has Python models as well.

The pinned LinkML JSON Schema generator supplies the complete class index. `python_generator.py`
adapts that index to Pydantic: the native LinkML Python generator drops inherited type bounds,
uses lists for tuples, and cannot preserve the released null and coercion behavior. This backend
handles only the supported field constructs and refuses unknown ones. It normalizes equivalent
schema spellings, including absolute regex endings, without dropping constraints. A change to
class conditions requires explicit review of the retained Python enforcement.

`python-compatibility.json` maps every owned class, preserves public field order/configuration and
binds retained validators. Its exact field adjustments preserve the released Python API, including
tuple positions, null/absence and serialization. Each adjustment names its immutable source and
has synthetic witnesses in `tests/fixtures/python-adjustments.json`; duplicates, stale and untested
entries fail. The migration baseline is the merged stage-one commit recorded in that manifest.
These adjustments are distinct from `known-looser.yaml`, which compares the generated JSON Schemas
with the production Zod exports. Neither list grants a general exemption.

Generation emits no LinkML runtime dependency. The Python gate uses Pydantic **2.13.5**, matching
the private steps environment; LinkML keeps its separate locked environment. The generation check
covers `linkml/generated/`, `pydantic/generated/` and `zod/generated/`. Regenerate through `linkml/generate.py`,
never by editing emitted classes. `bin/verify pydantic` visits generated subpackages as well.

The original behavior corpus remains in the contract gate. The Python generation tests additionally
compare every previous field contract and public import, exercise every retained validator with a
rejecting example, and check the new catalog. The private `record compare linkml` now runs Python
on every original JSON document and on the complete archive assembled from every shard. It does
not treat an individual shard as a self-contained record with complete references.

### Generated Zod and retained refinements

`zod_generator.py` consumes that same resolved class index and emits all owned site classes into
`zod/generated/<module>.ts`. Field order comes from the definition, not the alphabetized JSON
Schema index: `SchemaView.class_ancestors` is reversed (ancestors first), `class_slots(direct=True)`
keeps declared slots/attributes in order, and `induced_slot` supplies aliases in the final class
context. Repeated inherited slots keep their first position. The pinned **linkml-runtime 1.12.1**
source, `linkml_runtime/utils/schemaview.py`, those three methods, and LinkML's
[SchemaView](https://linkml.io/linkml/developers/schemaview.html) page were read **30 October 2026**.
A test compares every emitted class's order with an independent traversal of the schema YAML,
including inherited fields and wire aliases; mismatched field inventories fail generation.
Objects use `z.strictObject`; the named text map uses `z.record`. Shared enums are declared once in
`enums.ts`; references between modules are imports. The backend supports the house style's scalar
types, patterns, URI format, numeric bounds, array item types/cardinality, maps, literals, enum
intersections and nullable fields. Optional nullable fields become `.nullish()`. Unknown field or
class constructs, unresolved references and reference/import cycles fail by name. It emits the
repository's Prettier form directly, without a JavaScript runtime or formatter at generation time.
`generate.py` writes and byte-checks `zod/generated/` alongside the existing outputs.

The public `zod/*.schema.ts` modules keep their schema/type/function exports. They adapt generated
shapes before refining them and use the retained child validators
where calendar, host, evidence and other checks are needed. Refined ancestor schemas use
`.safeExtend`; `.pick`, `.omit` and ordinary `.extend` operate on unrefined shapes. Zod's
[Defining schemas](https://zod.dev/api), including those four object APIs, was read **30 October
2026**; `.extend` throws on a refined object, while `.safeExtend` retains its refinements.
The code names that page/date beside the retained ancestor composition. Formatting follows Prettier's
[Options](https://prettier.io/docs/options), read **30 October 2026**: tabs, single quotes,
ES5 trailing commas and width 100.

Class conditions are recognized but deliberately not generated into Zod. Their enforcement stays
in the existing refinements and cross-document checks inventoried by `checks/documents.yaml` and
`checks/record.yaml`; the generated JSON Schemas also enforce them at the document boundaries.
The Python backend's condition inventory continues to require review when those conditions change.

The hand layer preserves all 40 places in `known-looser.yaml` (24 original locations plus
16 locations introduced by reusing CitedTranslation): required nullable keys, optional
non-null keys, positional box/coordinate bounds and positive duration. Type compatibility keeps
box/dimension/coordinate tuples, external-reference optional non-null scalars, the supported
content vocabulary version union, and nullable event-date qualifier/evidence-basis literals.
Page tuples reuse the generated element validators, so integer ranges and box bounds govern.
All generated objects keep their closedness; page numbers keep their integer range. Hashes and
HTTPS URLs use the generated patterns. Zod **4.3.5** lets a regex hide a URL's `format: uri` during
JSON Schema export; the generator preserves that format with metadata alongside both runtime
checks (read **30 October 2026**, installed `zod/src/v4/core/json-schema-processors.ts`,
`stringProcessor`). A regression test checks the pattern, URI format and runtime rejections.
The retained child rebindings propagate tuple/null adjustments, calendar and host refinements,
text/evidence/consent checks and defaults through parents; array rebindings retain cardinality.
Media rights retain their released default. The legacy `ContentType` and object-valued `Bbox`, plus
the isolated pilot, have no owned site class to replace and remain hand-written.
Two public enum declarations (`HolocaustFateSchema`, `ReadingStatusValueSchema`) retain their
literal spelling because the existing vocabulary tests inspect those declarations directly;
the migration comparison also holds their exported values and types to the frozen baseline.
The record's version literal and the non-document `EnglishCheck` base's judgement regex likewise
stay explicit for existing source-inspecting gates.

`zod/tests/frozen/` holds test-only shapes from `main` **e3e80c1**. Strict `tsc` compares every
exported inferred schema type with that baseline, including all six documents, and repeats the
site's `.pick`, `.extend`, `.shape`, `.safeExtend` and `.omit` projections. The bun-only tests compare
each public schema's kind and verify its JSON contract against those frozen shapes,
allowing only the measured tightenings and equivalent integer/digest spellings. The owner's
31 October 2026 site-content 1.1.0 release adds exactly that document-version literal to the
three affected type and JSON comparisons; the frozen files stay unchanged. Negative controls
reject weakened types, patterns, bounds, URI formats and required keys. Round one's obsolete
byte-identity/stripping assertions follow ticket 20's revised measure. Existing behavior tests
continue to exercise retained refinements.
Backend tests plant unknown constructs, drift, missing/extra
files and cycles. `bin/verify zod` typechecks imported generated/test subfolders and checks their
formatting recursively; `bin/verify linkml` checks generation and runs the backend tests.

### Source words and English

Citation, MediaFamilyWords and Source title English use `CitedTranslation is_a Translation`
from `site_common.yaml`. Its `CitedTextBasis is_a TextBasis` makes addresses optional;
piece Translation and TextBasis still require them.
The [slot audit](../docs/design/2026-10-31-words-and-their-english.md) lists every source-word
slot, existing English coverage, the three optional additions and remaining approval candidates.
The `english_of` annotation records each exact sibling-text binding; generation exports its
inventory for both twins. Attribution lives in site_common so the dependency stays acyclic;
the existing public imports remain available.

The single switch is the `deactivated: false` flag on Citation's
`require_non_english_quote_english` rule in `schema/sourced_entities.yaml`. Generation derives
the runtime constants in `zod/generated/words_policy.ts` and
`pydantic/generated/words_policy.py`, both now true. It was switched on **1 November 2026**
after pruzhany-steps decision 268 reported **0 quotes not marked English without English**.
Nonblank quotes now require English unless explicitly marked `en` or an `en-*` tag.
Present English is always bound to the exact original; source metadata binding runs at SharedRecord so the site's
`SourceSchema.pick()` API remains usable. The Python condition inventory has been reviewed;
the retained `validate_english` enforces coverage. Fictional tests cover the active rule and
generation of both switch states.

Read **31 October 2026**: LinkML [Advanced features, Rules](https://linkml.io/linkml/schemas/advanced.html#rules),
[Slots](https://linkml.io/linkml/schemas/slots.html),
[Annotations](https://linkml.io/linkml/schemas/annotations.html),
[JSON Schema](https://linkml.io/linkml/generators/json-schema.html) and
[deactivated](https://linkml.io/linkml-model/latest/docs/deactivated/).
Pinned 1.12.1's emitter ignores `deactivated` and omits anonymous slot range types;
`external_schema.ReleaseGenerator` honors the switch and only restores explicit condition
ranges carrying `json_schema_typed_range: true`. Existing unannotated rules retain their
measured behavior. `test_words_english.py` checks missing/null values, inherited Citation
rules, emitted policy and both runtime validators against the actual activated LinkML rule.

### Commands

`bin/verify linkml` runs everything, in this order: `linkml lint` on every schema file, the house
lint, every generated file made again in a temporary folder and compared byte for byte with
`generated/` (it fails naming each file that differs, is missing or is extra), the canaries, then
the tests. CI runs it on every push to `main` and every pull request (`.github/workflows/ci.yml`).

To regenerate after changing a schema file or the manifest, make the same environment and run
the generator (from the checkout's root; `-I` keeps the checkout off Python's path, where the
folder `pydantic/` would hide the library of that name):

```sh
env=$(mktemp -d)
uv venv --python 3.11 "$env"
uv pip sync --python "$env/bin/python" --require-hashes \
	--build-constraints linkml/build-constraints.txt linkml/requirements.lock
"$env/bin/python" -I linkml/generate.py           # make linkml/generated/ afresh
"$env/bin/python" -I linkml/generate.py --check   # what bin/verify runs
```

On Windows the environment's Python is `"$env/Scripts/python.exe"`. Generated files are UTF-8
with `\n` line ends; readable outputs have one at the end, while the exact answer request
strings have none. `.gitattributes` checks this folder out with `\n` too.

To add a module: write `schema/<module>.yaml` (importing `types` where it needs a shared type), add
it to `modules.json` with its top class, run the generator and commit what it makes with the
schema. A document's JSON Schema is made with that one top class: one JSON Schema with several
roots merges their top-level rules.

`bin/verify contract` retains the Zod–Pydantic checks and compares LinkML with Zod for every
mapped model's fields, requiredness and enum values. Mapping coverage is checked in both
directions; the two runtime archive carriers are explicitly excluded. Required-null
exceptions must be exact, still differ, and name a live place in `known-looser.yaml`.

In the private steps checkout, run `record compare linkml --root schema=<candidate> --root
site=<site>` for all real documents, all shards, the bundled Zod archive and catalog validators,
and bounded constraint mutations. Every exception needs a witness. Missing categories,
unsupported coverage, undocumented differences and newly rejected real files fail the check.
URI formats are enabled. This complements the contract gate; it is not a general proof of
schema equivalence. Keep real-data diagnostics private and synthetic fixtures here.

The check inventories' former proposals are adopted into the private rule catalog. The
record gate checks their source citations and inventory, but does not claim to execute this
repository's tests. The source-backed planned list stays exclusively in documentation, and
its private source quotations are checked by `record check --catalog` with both roots present.

## The locked environment

| | |
| --- | --- |
| Python | 3.11, as `bin/verify`'s other Python steps (`PYTHON_VERSION`) |
| linkml, linkml-runtime | 1.12.1 (released 13 October 2026) |
| LinkML metamodel the schema targets | **1.12.0** (`metamodel_version` in linkml-runtime 1.12.1's `meta.yaml`; every generated JSON Schema states it) |
| pydantic | 2.14.1 (pydantic-core 2.50.1) |
| jsonschema | 4.26.0 |
| PyYAML | 6.0.3 |

`requirements.lock` holds 90 packages (95 entries: a few differ by Python version), each pinned
and with the hash of every file PyPI has for it, resolved once for every platform (`--universal`)
and Python 3.11 or later. It is made from `requirements.in` by the command at its top:

```sh
uv pip compile linkml/requirements.in --universal --python-version 3.11 --generate-hashes --output-file linkml/requirements.lock
uv pip compile linkml/build-constraints.in --universal --python-version 3.11 --generate-hashes --output-file linkml/build-constraints.txt
```

It is an environment of its own: linkml 1.12.1 needs pydantic 2.13.5 or later, and the other
Python steps pin `PYDANTIC_VERSION` (2.13.5). `bin/verify linkml` makes it afresh in a temporary
folder each run with `uv pip sync --require-hashes` (a fraction of a second from uv's cache).
Measured on 28 October 2026 with uv 0.11.32: `uv pip sync --require-hashes` refuses a lock with a
planted wrong hash, and refuses a wrong hash in `--build-constraints`; `uv run --with-requirements`
installed the same wrong-hash lock without complaint, even with `--no-cache`, so it is not used.
uv 0.11.13, the version CI installs, has the same flags and syncs the same lock.

Three packages are on PyPI only as source (antlr4-python3-runtime 4.9.3, cfgraph 0.2.1,
pytest-logging 2015.11.4), so installing them builds them, with setuptools; `build-constraints.txt`
pins setuptools by hash. uv's `pip sync` has no switch that requires a hash for every build tool:
a build tool these packages took up later, and that is not in that file, would be installed
without one.

## The physical page contract

`schema/physical.yaml` defines the page file as Impresso writes it, including every
legacy field. `modules.json` registers its `PhysicalPage` root and names its external
contract, `impresso-page`. Generation writes `generated/json-schema/physical.schema.json`,
the usual gen-doc pages, and `generated/external/physical/contract.json` with every owned
physical class. Its resolved learning index is under that folder's `docs/model-index.json`.
All physical classes also appear in the combined data dictionary. The site's twin contract,
Python models and public RDF view keep their own inventory: they do not consume these
stored files. This is an explicit external contract, not an exception to site field parity.
The generator refuses an unknown external contract or a physical/exchanges contract without
a document root. The answers contract instead declares a separate root for each asking.

Impresso's objects are open (`extra_slots: allowed: true`). Its optional fields generally
refuse null, except `pOf` and `section_pOf`; the latter permits null members too. The schema
annotation `json_schema_nulls: explicit` selects `external_schema.py`, which calls the pinned
native generator with `include_null=False` and implements the boolean slot annotations
`nullable` and `nullable_items` through its `after_generate_class_slot` lifecycle hook.
Unsupported annotation values or shapes fail generation. The native generator still handles
aliases, requiredness, integer boxes, openness, enums and class conditions. LinkML rules
express the paired fields; `exactly_one_of` expresses the image keys, and `any_of` the timestamps.
No generated JSON is maintained by hand. No URI, timestamp format, numeric bound, nonempty
list or 999-element limit is invented where Impresso imposes none. The positional-id producer
must enforce 999, across all paragraphs for lines, as the module description specifies.

`test_physical.py` compares both validators on the invented two-region page and mutations
of every field, absent/null values, extra keys, boxes, nullable section members, all source
type/medium pairs and all image/timestamp presence combinations. The oracle is the unmodified
Impresso schema, pinned with its SHA-256, attribution and license in `standards/impresso-329323c/`.
Both validators use their own declared JSON Schema draft. The test also reads **every**
`editions/*/*-pNNNN.json` when `$PRUZHANY_STEPS` names a checkout, or `pruzhany-steps/editions`
exists beside this checkout or any of its parents. An explicit path with missing data fails;
without any sibling the optional real-data test reports a skip. Real-page diagnostics print
only ordinal numbers and schema paths, and the success report prints aggregate counts.

Impresso and ALTO correspondences are documented on every class and slot as `impresso` and
`alto` annotations with source `see_also` links and a read date. The physical box is the shared
`physical_box` slot (wire alias `c`), an array of exactly four integers; making it an object
class would change the file. ALTO has no paragraph wrapper, so an export flattens the paragraphs'
lines in order into a TextBlock. Semantic links, source classifications, conversion flags and
JSON timestamps have no automatic ALTO equivalent; their annotations say so. These are
documented export correspondences, not ontology equivalences. No prefix, EHRI/RiC-O version,
ontology mapping or owner-approved vocabulary value is added; the alignment gate is unchanged.

Pages read **29 October 2026** for this module and its generation settings:

- Impresso, [canonical page schema](https://impresso.github.io/impresso-schemas/json/canonical/page.schema.json),
  master `329323c` (13 August 2026), compared byte for byte with the steps copy;
  SHA-256 `b6a6ca37167b30d318eb175a844dc50c80d245f9753ddc279a5e198b47f53b2c`.
- Library of Congress, [ALTO home and version list](https://www.loc.gov/standards/alto/) and
  [ALTO 4.4 XSD](https://www.loc.gov/standards/alto/v4/alto-4-4.xsd): PageType, BlockType,
  TextBlockType/TextLine, StringType, MeasurementUnitType, sourceImageInformationType and
  processingStepType. Measurements are HPOS, VPOS, WIDTH, HEIGHT, in the source picture's pixels
  when MeasurementUnit is `pixel`. ALTO's floating-point coordinates are broader than Impresso's
  integer boxes. XSD SHA-256 as downloaded with CRLF:
  `5564fd29d2dd090d8102b8a0aa081906afd677cd5ecc632312e56f21ea14702b`.
- LinkML, [JSON Schema generator](https://linkml.io/linkml/generators/json-schema.html),
  [constraints](https://linkml.io/linkml/schemas/constraints.html),
  [slots](https://linkml.io/linkml/schemas/slots.html) and
  [advanced features](https://linkml.io/linkml/schemas/advanced.html).
  The installed locked LinkML **1.12.1** `generators/jsonschemagen.py` was also read for
  `include_null`, `extra_slots.allowed`, `handle_class_slot`, `after_generate_class_slot`,
  and anonymous class expressions; the generated behavior is tested here.

## The exchanges contract

`schema/exchanges.yaml` is the external contract `model-exchanges` in `modules.json`.
`generated/json-schema/exchanges.schema.json` has **PromptVersion as its one document
root**, so the steps check can validate a prompt metadata file directly, without a
wrapper. The same document's `$defs/KeptAsking` describes an index entry referencing
a kept answer; it does not replace the heterogeneous readings payloads. To validate
such an entry, use the same `$schema` and `$defs` with `$ref: '#/$defs/KeptAsking'`,
as `tests/test_exchanges.py` does. Select the validator using `$schema` and enable its
format checker, including `date`. Generated external inventory and learning metadata
live under `generated/external/exchanges/`; both classes also appear in the data
dictionary. The site twins, generated Python classes and public RDF view have their
own inventory.

Prompt metadata fields are `code`, `asking`, `model`, optional `effort`, `budget_usd`,
`shape_name`, `first_commit`, `first_day`, `last_commit`, `last_day` and
`shape_recovered`. All except effort are required. Commit ids are full forty-character
lowercase Git SHA-1 ids in steps; days refer to presence in code history, not dates
of calls. The shape name can be known while its exact JSON Schema is unrecoverable:
`shape_recovered: false` records that distinction. Effort is omitted when no explicit
setting is known. Names and selectors are nonblank strings, not new controlled
vocabularies. A budget is a nonnegative number in US dollars.

Kept-answer entries require `prompt_code`, `model` and `answer_file`; `day`,
`input_fingerprint` and `cost_usd` are optional. Unknown fields are omitted, never
filled with a fabricated day, digest or cost. Both classes are closed; optional
fields reject explicit null, using the same `json_schema_nulls: explicit` adapter
as the physical module. Prompt codes and input fingerprints are sixteen lowercase
hexadecimal characters, including English's **xxh3_64** input digests, not full
SHA-256 values. A code's lexical form does not establish its algorithm or scope.
Some historical codes cover expanded whole requests. Such a code may identify a
recovered stored version, but the registry must establish that association from
the exact text and its recipe; an index must not assume an instructions-only hash.

The stored formats were inspected on **29 October 2026**, taking several examples
of each form and reading their writers. Only field names and types are recorded here;
no private answer, personal data or real prompt text was copied. This table is a
projection guide for the steps index, not an assertion that these payloads share
one root schema:

| Kept form | Prompt association | Input fingerprint | Day and accounting scope |
| --- | --- | --- | --- |
| `readings/pruzst*/english-*.json` (`english_kept.Kept`, `write_english`) | `prompt` is the prompt code | Each `pieces` key is an xxh3_64 digest of that piece's input text | `answered_on` has some individual days; older entries omit them. `cost_usd` sums calls for the page. |
| `readings/pruzst*/structure-*.json` (`find_items.Asked`) | Recover the associated stored version from history; `request` covers the whole request | `request` fingerprints the instructions and page request | No asking day field; cost can include a faulty answer and its retry. |
| `readings/pruzst*/latin-*.json` (`read_latin.Looked`) | `request` is the prompt code | No separate input digest | No asking day field; cost accumulates calls for the page. |
| `readings/issues/*/` (`english_kept.KeptGroups`, `join_people`) | Recover the prompt from history | `request` fingerprints the system text and whole joining request | No asking day field; recorded file cost. |
| Structure trial answers (`measures/trial_structure.PageAsked`) | Companion `setting.json` keeps system, instructions, model, effort and shape | `request` fingerprints the page input; `sent` fingerprints the candidate's sent text; the index must specify which scope it uses | Day is in the trial directory name; cost includes retries. |
| Row trial answers (`measures/trial_rows.Asked`) | Companion `setting.json` keeps the prompt, shape and model | No separate stored digest; `pictures` holds the inputs and answers | Day is in the trial directory name; recorded asking cost. |

`answer_file` names the existing file relative to steps. Multiple entries for inputs
in one accumulated file must not count that file's cost more than once. A first Git
commit date is not an observed asking day. The steps check owns prompt byte hashing,
matching codes and histories, resolving the `PromptVersion.code` reference, date
ordering, existence of the text/shape/answer files, and answer validation against
the associated recovered shape. Unresolved histories must be reported rather than
filled with invented commits. Answer shape generation from LinkML is a later slice.

PROV-O correspondences use `see_also` and explanatory comments only. Versioned
instructions correspond to [Plan](https://www.w3.org/TR/prov-o/#Plan); an asking
to [Activity](https://www.w3.org/TR/prov-o/#Activity), and its kept file to
[Entity](https://www.w3.org/TR/prov-o/#Entity). Model association, input use and
answer generation have see-also links on the relevant fields. A plan link would
use a qualified association; `hadPlan` is not a direct Activity property. A day
does not supply a PROV timestamp. Costs, effort, hashes and code-history bounds
remain application metadata. PROV-O is unpinned, so these are documented
correspondences, not ontology bindings. The existing EHRI 0.2.0 and RiC-O 1.1
term lists were read; no prefix, ontology pin or vocabulary value was added.

`test_exchanges.py` validates invented metadata and references, including missing
and null fields, short digests, full commits, calendar dates, costs, shape recovery,
unknown properties, the external inventory and the learning reference. It needs
neither private data nor prompt text. The steps implementation owns its separate
`record exchanges` and `measures asking` checks.

Pages read **29 October 2026** for this module and its generation settings:

- W3C, [PROV-O Recommendation, 30 April 2013](https://www.w3.org/TR/prov-o/),
  sections 3.1 and 4.3, especially Plan and hadPlan.
- LinkML, [JSON Schema generator](https://linkml.io/linkml/generators/json-schema.html),
  [slots](https://linkml.io/linkml/schemas/slots.html) and
  [constraints and rules](https://linkml.io/linkml/schemas/constraints.html).
  The installed locked LinkML **1.12.1** `generators/jsonschemagen.py` was read for
  type formats, `include_null` and slot constraints; date behavior is tested here.
- uv, [CLI reference](https://docs.astral.sh/uv/reference/cli/), `uv venv --python`
  and `uv pip sync --python --require-hashes --build-constraints`, used with the
  existing lock and build constraints. Local uv is **0.11.32**; CI pins **0.11.13**.

## House style

Each construct the Zod exports use, written the one way it is written here, and the JSON Schema
gen-json-schema 1.12.1 makes of it (observed on 28 October 2026; `tests/test_house_style.py`, `tests/test_documents_house_style.py`, `tests/test_record_shape.py` and `tests/test_record_rules.py`
checks every row against `tests/fixtures/house-style.yaml`, which uses the real shared types).

| The shape says | Write | Generated JSON Schema |
| --- | --- | --- |
| a key that must be there, never null | `required: true` | the key in `required`; `"type": "string"` |
| a key that may be absent or null (248 of the 254 optional keys in the exports) | no `required` | `"type": ["string", "null"]`; an object: `"anyOf": [{"$ref": ...}, {"type": "null"}]` |
| text that is not blank (`\S`), a day, a digest, a language tag... | `range:` a type of `schema/types.yaml` | `"pattern"` on the property, as written |
| a pattern used once | `pattern:` on the slot, in single quotes, copied from the export once JSON's escapes are undone | `"pattern"` as written |
| exactly 64 hexadecimal digits (pattern with `minLength`/`maxLength` 64) | `range: Sha256Hex`, whose pattern ends `$(?![\s\S])` | `"pattern": "^[0-9a-f]{64}$(?![\\s\\S])"` |
| `const` | `equals_string:` | `"const"`; it refuses null by itself, even on an optional slot |
| `format: uri` | `range: uri` | `"format": "uri"` |
| `enum` | an enum with `permissible_values` | `"$ref"` to a `$defs` entry with `"type": "string", "enum": [...]` |
| `minItems: 1` | `multivalued: true`, `minimum_cardinality: 1` | `"minItems": 1` |
| a box `[x, y, w, h]` (`prefixItems`) | `range: NonNegativeNumber`, `multivalued: true`, `minimum_cardinality: 4`, `maximum_cardinality: 4` | `"items": {"minimum": 0, "type": "number"}, "minItems": 4, "maxItems": 4`; width and height above 0 are lost (known-looser) |
| bounds on each item of a list of numbers | a bounded type as the `range` (`NonNegativeInteger`) | `"items": {"minimum": 0, "maximum": 9007199254740991, ...}` |
| a whole number above 0 (`exclusiveMinimum: 0`) | `range: PositiveInteger` (`minimum_value: 1`) | `"minimum": 1`, the same for whole numbers |
| `maximum: 9007199254740991` (Zod's safe integer) | `maximum_value: 9007199254740991`, as the integer types have | `"maximum": 9007199254740991` |
| a map of text to text (`additionalProperties` and `propertyNames` of type string) | a class with no slots and `extra_slots: {range_expression: {range: string, required: true}}`, written in block style | `"additionalProperties": {"type": "string"}`; without `required: true` the values would also accept null |
| `additionalProperties: false` | nothing: classes are closed by default | `"additionalProperties": false` on every class |
| `number` / `integer` / `boolean` | `range: float` / `integer` / `boolean` | `"number"` / `"integer"` / `"boolean"` |
| one object inside another (`z.strictObject` as a field) | `range:` its class, `inlined: true` | `"$ref"` to its `$defs` entry; when optional, `"anyOf": [{"$ref": ...}, {"type": "null"}]` |
| a list of objects | `range:` their class, `multivalued: true`, `inlined_as_list: true` | `"type": "array", "items": {"$ref": ...}` |
| an object's `id` | a required slot (`range: NonBlankText` where the export has `\S`), never `identifier: true` | the key in `required`; `identifier: true` would make the id the object's IRI under `pc:`, a namespace choice left to stage 3, and claim a uniqueness no generator enforces |
| a key written in camelCase (the editions catalog) | a slot in snake_case with `alias:` the key, which `linkml lint`'s naming rule accepts | the property is named by the alias, as the file writes it |
| a subclass that narrows one field (`TitleCheck` extends `EnglishCheck` with its own pattern) | `is_a:` the parent, the field again under `slot_usage:` | the subclass's own `$defs` entry, with every inherited property and the narrowed one |
| a version stamp from a short list (`z.enum(['0.1.0', '1.0.0'])`) | `pattern:` of the exact values, `'^(0\.1\.0\|1\.0\.0)$(?![\s\S])'`; `linkml lint` refuses `1.0.0` as an enum value | `"pattern"` as written; a test holds its alternatives to the generated Pydantic `Literal` |
| a check of two fields of one object (`superRefine`) that LinkML can say | `rules:` on the class, `preconditions` and `postconditions` with `equals_string` or `equals_string_in` | `"allOf"` of `"if"`/`"then"`; the `if` puts the key in `required`, so a left-out or null value does not trigger it; every slot of the `postconditions` goes in the `then`'s `required` unless its condition says `required: false` |
| no value, in a rule's postconditions | `required: false` and `pattern: '^$'` on a slot whose range refuses empty text | `"then": {"properties": {"x": {"pattern": "^$"}}}`: null and absence pass, any text fails; `value_presence: ABSENT` gives `"not": {"required": [...]}`, which refuses the null the files hold |
| items of a list that must all differ (Zod's `uniqueIds`) | nothing: the check goes to the rule catalog (`checks/documents.yaml`) | `list_elements_unique: true` gives no `uniqueItems` (measured), so it is not written |
| the meaning of a class or a field | `class_uri` or `slot_uri`: the RiC-O or EHRI term a vocabulary binding names; `exact_mappings`: a `pc:` term a profile declares as a placeholder; `related_mappings`: one that covers several fields; `annotations: {impresso: ...}`: Impresso's field, in words, written in block style | nothing: a JSON Schema carries no mapping; `tests/test_documents.py` checks each term against `standards/` and `vocabulary/*.ttl` |
| a list of allowed texts (`enum`) of a vocabulary group, or whose values `linkml lint`'s naming rule accepts | a LinkML enum; a value with a standard term takes it as `meaning` | `"$ref"` to the enum; an optional key keeps its null branch |
| a list whose values the naming rule refuses (`site+download`, `institution-terms`) or that are addresses (media rights) | the slot's `equals_string_in` | `"enum": [...]` on the property, which refuses null even on an optional key (media `rights` is then not looser than the export) |
| a vocabulary enum narrowed to some of its values (a relation's `type`: kinship or other) | `range:` the enum and `equals_string_in` | `"$ref"` and `"enum"` together |
| a slot of one letter (MediaRegion's `x`, `y`, `w`, `h`) | the key as it is; `linkml-lint.yaml` excepts the four from the naming rule's two-letter floor | the key |
| an address that must begin `https://` (Zod's `z.url({protocol})`, Pydantic's pattern) | `range: HttpsUri`, `typeof: uri` with the Pydantic twin's pattern | `"format": "uri"` and `"pattern"` together; stricter than the export, which keeps only the format |
| coordinates, latitude then longitude | `range: Coordinate` (-180 to 180), `minimum_cardinality: 2`, `maximum_cardinality: 2` | `"items"` bounded -180 to 180, `"minItems": 2, "maxItems": 2`; the latitude's ±90 is lost (known-looser) |
| a twin's check "if this, then that" within one object | a `rules:` entry with `preconditions`, `postconditions` (and `elseconditions`), whose conditions use only `required`, `value_presence`, `equals_string`, `equals_string_in` and `pattern`, at most one `value_presence: ABSENT` a condition | `"if"`/`"then"`/`"else"`, gathered in `"allOf"` when a class has several; a present null counts as present, except for a list; a child class takes its ancestors' rules |
| a twin's check "at least one of these" | the class's `any_of`, each branch `required: true` | `"anyOf"` on the class; a child class does not take it, so it is written again there |
| a twin's check "never this", or "none of these" in a rule | the class's `none_of`, or `none_of` in a rule's condition | `"not": {"anyOf": [...]}`; never two `value_presence: ABSENT` in one condition, which come out as "not both" |
| a twin's check on a list's length or items, a range, or a nested object's field, inside a condition | nothing in LinkML: a rule for pruzhany-steps `record/rules.yaml` (`checks/record.yaml` names it) | the generator drops `range`, `minimum_cardinality`, `maximum_cardinality`, `has_member` and `all_members` in a condition without a word (`tests/test_record_rules.py`) |
| a standard term for a class, a slot or a value | `class_uri`, `slot_uri`, a permissible value's `meaning`; a term naming a whole made of several fields as `related_mappings` on each; a qualification as `annotations: {via: rico:...Relation}` | nothing: meaning does not reach the JSON Schema |

Also:

- **The output is draft 2019-09** (`"$schema": "https://json-schema.org/draft/2019-09/schema"`),
  the exports draft 2020-12; validate each with the validator its `$schema` names.
- **Some of it is stricter than the exports.** The exports' `prefixItems` bound no length
  (`items: false` is absent), so a box of three or five numbers passes them; the definition's
  cardinality of 4 refuses it. Where the exports say `number` and the definition `integer`, the
  definition refuses a fraction. Neither is listed in `known-looser.yaml`, which lists only what is
  looser; the comparison of real files (ticket 05) shows whether any real file is refused.
- **Never** `exact_cardinality`, `unique_keys`, or `minimum_value`/`maximum_value` on a
  multivalued slot: the house lint refuses them (below).
- **Never `value_presence`** to make a key required and nullable, and **never `none_of` with
  `equals_number`** to make a number above 0: each changes the generated JSON Schema in a way
  LinkML's own meaning does not (known-looser.yaml says how), so the next release may undo it.
- **Prose in block style** (`description: >-` and an indented paragraph, `comments:` as an
  indented list), and every YAML word that YAML 1.1 reads as a boolean quoted (`'on'`, `'no'`).
- **Every term the definition names is pinned or declared.** `standards/check_alignment.py`
  (`bin/verify standards`) reads `linkml/**/*.yaml` but `linkml/tests/`: every `rico:` or `ehri:` term
  and namespace IRI must be in the pinned lists, every `pc:` term used as a `meaning`, `class_uri`,
  `slot_uri`, mapping or `via` must be declared in a `vocabulary/*.ttl`, and every `via` must be a
  RiC-O Relation class.
- **No new prefix or namespace.** `pc` (`https://pruzhany.org/ns/sourced-entities#`, as in
  `vocabulary/profile.ttl`) is the default prefix, and a schema's `id` lies under
  `https://pruzhany.org/ns/`. `linkml lint`'s canonical-prefix rule reads a prefix list without
  `pc`, because its default list gives `pc` to the Public Contracts Ontology
  (`linkml-lint.yaml` says so).

## The house lint and the traps

`lint.py` refuses, naming the file, the line and what to write instead, each with a planted file
in `tests/fixtures/lint/` that it must refuse on the marked line:

| Rule | Why |
| --- | --- |
| `exact-cardinality` | gen-json-schema drops it: no `minItems`, no `maxItems` (plan section 3, item 1). |
| `bound-on-a-list` | gen-pydantic puts `minimum_value`/`maximum_value` of a multivalued slot on the whole list, so the trial's real page is refused (item 2). Found after inheritance and `slot_usage`. |
| `unique-keys` | Enforced by neither gen-json-schema nor linkml-validate (item 3). A rule that compares records lives in pruzhany-steps `record/rules.yaml`. |
| `yaml-boolean` | YAML 1.1, as PyYAML and so LinkML read it, turns a bare `on`, `off`, `yes` or `no` into a boolean, and a key `true` or `false` into one. `y` and `n` are not refused: PyYAML reads them as text, and `y` is a box's coordinate. |
| `flow-prose` | A comma inside `{...}` or `[...]` splits prose silently into another key or item. |

The traps the plan carries (its section 9, from the review package's section 9), each with its
guard here:

- **`exact_cardinality` is dropped.** Write `minimum_cardinality` with `maximum_cardinality`.
  Guard: the house lint, and `canary_linkml.ExactCardinalityIsDropped`.
- **Native generated Pydantic bounds the whole list.** Bound the items through a type. Guard: the
  house lint and `canary_linkml.PydanticBoundsTheWholeList`. The native generator also drops a bound
  on a type altogether (`list[int]` with no bound); the project's Python backend retains those
  item bounds from the JSON Schema class index, with rejecting fixtures in its generation tests.
- **`unique_keys` is not enforced.** Guard: the house lint, and
  `canary_linkml.UniqueKeysAreNotEnforced`.
- **Null is not absence, and LinkML has only absence.** A required slot refuses null and an
  optional one accepts it. Guard: the definition never marks required a key the files hold null
  in; `known-looser.yaml` lists every key where the exports say otherwise, and its test finds
  them afresh in the exports.
- **No bound by position in a list** (`prefixItems`). Guard: `known-looser.yaml`; pruzhany-steps'
  comparison is to plant these bounds (ticket 05).
- **A slot in a subset is still a property** of the JSON Schema. Guard: what is planned and not yet
  in any file stays out of the documents' schemas (plan section 4.2).
- **YAML 1.1 booleans and commas in flow style.** Guard: the house lint; `linkml lint` also reports
  a slot named `True`.
- **Flat RDF loses the order of a list, and an RDF export needs IRIs.** Guard (stage 3):
  `rdf_generator.py` writes a list as a JSON-LD `@list`, checked for order, length and position
  (`generated/rdf/coverage.md`); predicates are in the `https://pruzhany.org/ns/` namespace.
- **Several roots in one JSON Schema merge their rules.** Guard: one `top_class` a module in
  `modules.json`.
- **Windows writes `\r\n`.** Guard: `generate.py` writes `\n`; `.gitattributes` checks out `\n`;
  the byte comparison would fail on anything else.
- **A check that cannot fail proves nothing.** Guard: every rule and canary has a planted case or a
  control that fails; `tests/test_generate.py` plants a one-byte change, a missing file and an
  extra one; `tests/test_known_looser.py` plants one place of each kind for its finders.

When a canary fails after an upgrade, LinkML's behaviour changed: read the canary's docstring,
measure again, and change the canary, the house lint rule it guards, this README and
`known-looser.yaml` together.

## Not read, not measured

- LinkML's GitHub issues (whether the faults above are reported upstream): GitHub outside
  `dsmedia` is not reachable from the cloud session that built this.
- gen-pydantic's reading of `pattern` (whether `\S` means "contains" there, as in JSON Schema),
  and the TypeScript generator: not used. The linked-data generators were measured below.

## LinkML's own generators, measured (30 October 2026)

Read on **30 October 2026**: LinkML's [OWL](https://linkml.io/linkml/generators/owl.html),
[SHACL](https://linkml.io/linkml/generators/shacl.html),
[JSON-LD Contexts](https://linkml.io/linkml/generators/jsonld-context.html) and
[RDF](https://linkml.io/linkml/generators/rdf.html) pages; checked against installed
**linkml/linkml-runtime 1.12.1**, rdflib **7.6.0**, pySHACL **0.30.1**, from the
hashed lock on Python **3.11.17**. A scratch import wrapper covers all 12 site
modules in `modules.json`; physical and exchanges are outside the public RDF view.
Native defaults were used, with generation dates disabled.

Unmodified `gen-shacl`, `gen-jsonld-context` and `gen-rdf` each fail on
`SourcedRelation.type`: `equals_string_in` with range `FactTypes` requires range
`string` in these generators. Each also succeeds on 11/12 modules individually;
`shared_record` fails. To measure beyond that blocker, a **scratch-only enum
intersection adapter** replaces that one field's range with an enum containing
`kinship` and `other`, copying their meanings and removing `equals_string_in`.
The original/adapted field validators agree on all 22 witnesses (all enum values
plus invalid controls). No source definition or production generator was changed.

OWL and context comparisons use canonical N-Triples and rdflib graph isomorphism;
blank-node labels are canonicalized, not compared as run-local identifiers.
A context alone has no RDF triples: both contexts were applied to the identical
eight-record synthetic export from `tests/test_rdf_export.py`. An additional
probe exercises all 16 public type contexts and 102 field entries.

| Output | Measured result (ours / native) | Recommendation and deciding differences |
| --- | --- | --- |
| OWL, unadapted | 356 / 8,758 triples; 9 shared, 347 only ours, 8,749 only native; not isomorphic. | **Keep ours.** Native describes the storage schema with restrictions, global properties and enum classes; ours declares the selected public classes/fields, source-scoped assertions and approved role/type vocabulary. For example, only ours has `pc:export_SharedPerson rdfs:subClassOf ehri:Person`; only native has `pc:SharedPerson a owl:Class`. Native makes `pc:event_types_birth` an OWL class; ours preserves its approved named-individual/EventType declarations. |
| JSON-LD context, adapted | Export: 102 / 78 triples; 10 shared, 92 only ours, 68 only native. All-term probe: 142 / 118; 3 shared, 139 only ours, 115 only native. Neither is isomorphic. | **Keep ours.** Native loses the public type-scoped predicates, ordered/repeated list values, reference coercions and derived reification/evidence/role terms. For the same event, only ours emits `rdfs:label "Fictional event"`; native emits `pc:name "Fictional event"`. |
| SHACL, adapted | 1,287 / 4,547 shape triples. Same two good controls: 2 / 0 accepted; same 19 faults: 12 / 16 rejected by shapes alone. Our complete runtime accepts 2/2 and rejects 19/19. | **Keep ours.** Native rejects both the full fixture and the place with optional coordinates absent (closed-property and required-field violations); its bad-case rejections therefore do not establish working validation. It targets storage classes/predicates and requiredness rather than the public profile, and does not model its RDF lists or Reference alternatives. |
| RDF records | `gen-rdf` emits schema metadata (8,456 triples after adaptation), not records. The native Python loader/RDFLib dumper behind `linkml-convert`, with the same adapter, converts only 3/8 exported records. For those same three inputs: 41 / 21 triples, none shared; not isomorphic. | **Keep ours.** Both persons and the place require stored `names`; the fact requires `representation`; the relation requires `type`. The successful Source, SharedEvent and PrintedAddress become blank-node identities, omit our derived edges and flatten lists: `[1, 1, 2, 2]` becomes just two bbox values. Ours exports all eight records in 102 triples. |

SHACL outcome differences, individually: native rejects both good controls and
also rejects the malformed `Citation.url`, mismatched `SharedFact.assertion_predicate`,
`SharedEvent.event_type` and `SharedEvent.role_deceased` that our shapes alone
accept. Our runtime refuses all four through format/derived-edge checks. Both
shape sets accept the standalone cyclic list, list with two rest edges, and list
with missing rest; our runtime refuses each through list-structure checks. All
other 12 planted faults are refused by both shape sets. Namespace, stale-input
and generator-configuration checks remain outside SHACL.

[Measurements, triple samples from each side, and every case's result](trials/2026-10-30-own-generators.json)
retain only synthetic evidence. These are bounded replacement trials, not a claim
that the full storage schema and the public view should be equivalent. No output
is replaced, no consumer dependency is added, and no check is loosened.

## Pages read, 28 October 2026

- LinkML, "JSON Schema" generator: https://linkml.io/linkml/generators/json-schema.html (closed by
  default, optional slots accept null, `--no-include-null` for the whole schema, unique keys not
  supported, no generation date unless asked)
- LinkML, "Constraints and rules": https://linkml.io/linkml/schemas/constraints.html
- LinkML, "Slots": https://linkml.io/linkml/schemas/slots.html
- LinkML, "Advanced features": https://linkml.io/linkml/schemas/advanced.html
- LinkML, "Validating data": https://linkml.io/linkml/data/validating-data.html (the JSON Schema
  and Pydantic validation plugins)
- LinkML, "Schema Linter": https://linkml.io/linkml/schemas/linter.html (recommended rules,
  configuration, exit status on warnings)
- LinkML, "Documentation" generator: https://linkml.io/linkml/generators/docgen.html
- LinkML metamodel, `value_presence` and `extra_slots`: linkml-runtime 1.12.1's `meta.yaml`, as
  installed in the locked environment
- uv, "Locking environments": https://docs.astral.sh/uv/pip/compile/ (build constraints with
  hashes) and the command reference https://docs.astral.sh/uv/reference/cli/ (`--require-hashes`;
  `uv run` has no such switch)

## Metadata for learning tools

`generated/docs/model-index.json` is a reproducible documentation index of every owned
class, its resolved inherited fields, field constraints, descriptions, vocabulary values,
standard mappings and exact class YAML. It includes source hashes and the generated
contract hash so a consumer can refuse stale metadata. It contains no archive records.

A field may have the documentation-only annotation `references: TargetClass.field`
(or comma-separated targets). The generator checks that each target exists and is unique.
This describes an identifier link; containment is derived separately from the field range.
These annotations currently cover the notice-to-evidence learning trail. Unannotated
identifier fields must not be interpreted as proof that no reference exists. An annotation
does not add a validation rule or change the document's wire format.

The private steps repository uses this index with `docs/learn/notice-to-evidence/lesson.yaml`
to build its offline guided journey. Questions and source selectors live in that private
teaching layer; definitions and vocabulary continue to come from this repository. Historical
examples, crops, personal notes and real-data diagnostics must stay out of this public tree.

### Public RDF view (stage three)

The manifest now also generates `generated/rdf/`: an inline JSON-LD 1.1 context,
OWL vocabulary declarations, SHACL Core shapes, a machine-readable profile and
[a field-by-field coverage report](generated/rdf/coverage.md). The sources remain
LinkML; `rdf-profile.yaml` selects the public view and records every omitted model
and field. Adding a field requires an explicit decision. Planned requirements do
not enter this export. `rdf_generator.py` refuses unsupported scalar constraints,
ambiguous scalar unions and stale field selections. Tuple position bounds are
checked against live Zod exports, since LinkML JSON Schema loses those bounds.

`rdf_runtime.py` encodes already-projected public records; it never reads archive
storage. The private steps command `record export rdf` first validates all shards
and invokes the website's final `buildPublicAssets` in a disposable root. It does
**not** serialize `projectRecord`: its intermediate maps contain private data.
The final public files determine both which identities and which evidence appear.
Printed-only person displays, derived biography, navigation, images, families,
holders and media without this public representation remain outside this view.
PrintedAddress list support is tested with fictional boxes; public citations do
not expose the private stored address lists.

Persons use `ehri:Person`, events `rico:Event`, and approved event kinds and roles
use the existing declared vocabulary (`rico:hasEventType`, `pc:part_*`). Ordered
participant and citation records also remain available as RDF lists. A fact is a
source-scoped `rdf:Statement` and `rico:Relation`, retaining its status, review,
confidence, attribution and exact locators. `rico:isEvidencedBy` points to its
Source resources, not to an RDF list or citation locator. The encoder cross-checks
these derived edges against the preserved fields. It never asserts the underlying
person–birth/death/kinship triple. Public confirmed relationships are separately
reified and retain subject-to-object direction; their derived node IDs do not
pretend to be the private stored relation IDs. They cannot supply citations that
the website did not publish.

Stored identifiers remain unchanged literals. The caller supplies an explicit
HTTPS base; entity IRIs append `id/` and percent-encode the complete original ID.
Nested objects use deterministic hashes under `node/`. A public reference without
a description is marked `Reference` with its expected model and no private label.
This does not establish identity, resolve names or mint an ARK. No `owl:sameAs`
edges are inferred. The lasting public namespace is still an owner decision.

Validation combines enabled JSON Schema format checking, generated closed SHACL,
strict RDF-list structure checks and checks of the derived evidence/type/role
edges. Unsupported formats fail. Source and generated artifact hashes are checked
before export; generated profile fields are recomputed from their sources.
SHACL verifies this project's bounded export profile. Private-object conditions,
archive joins, evidence eligibility and publication remain with the authoritative
Zod/Python gates and the existing public-assets builder. This is neither EHRI's
ingestion SHACL nor an assertion of RiC-O conformance or EHRI acceptance.

`bin/verify standards` checks mappings against the existing EHRI 0.2.0 / RiC-O 1.1
pins and requires a declaration and reason for each new local export term.
`bin/verify linkml` regenerates these files byte for byte and runs synthetic faults
for values, formats, fixed values, tuple order/bounds, list cycles, references,
reification, omitted/unknown fields, stale inputs and reproducibility. It installs
pySHACL from the same hashed lock; the website gains no RDF dependency. Historical
examples and export diagnostics belong only in private pruzhany-steps.

### The other Impresso edition contracts

`schema/impresso_issue.yaml` and `schema/impresso_contentitem.yaml` describe every
field of the canonical issue and rebuilt paper content-item contracts beside
`physical.yaml`. Their manifest entries are external contracts; they generate
JSON Schemas, documentation and separate inventories under `generated/external/`.
They add no stored field or site model, and do not enter the Zod/Pydantic twins.
All three upstream oracles now read `../standards/impresso-329323c/` only.

`external_schema.py` preserves optional versus nullable fields, including required
nullable scalars. Bounded `json_types` and `json_item_types` annotations describe
legacy unions whose array/object contents upstream leaves unconstrained; they
replace only an unconstrained string placeholder, refusing constrained inputs.
`json_min_length` preserves string length without adding a whitespace rule.
Nested region-coordinate arrays use LinkML's native `array.dimensions`. These
wire adaptations are not a claim that native LinkML instance validation alone
enforces the JSON contract. Unknown properties remain allowed.

The issue schema places `required: [m]` on the **array**, where JSON Schema ignores
it; metadata is consequently optional on an entry. Its metadata `tp` enum excludes
null even though its type lists null. The rebuilt item's radio reading-order
condition applies when `st` is absent too, as upstream's `if` does not require
it. Tests retain these behaviors rather than repairing the upstream files.

Read **31 October 2026**: Impresso's README and all three schemas at the pinned
commit; LinkML [JSON Schema](https://linkml.io/linkml/generators/json-schema.html),
[Slots](https://linkml.io/linkml/schemas/slots.html),
[Advanced features](https://linkml.io/linkml/schemas/advanced.html) and
[Arrays](https://linkml.io/linkml/schemas/arrays.html); uv
[Commands](https://docs.astral.sh/uv/reference/cli/) for the existing hashed
environment. `test_impresso.py` checks each field's normalized constraints,
requiredness and mapping, then compares both validators on planted type, null,
absence, numeric/array bounds and dependency faults. Fixtures are fictional.
