# linkml/: the record's data, defined once in LinkML

This folder is the written definition of the record's data in [LinkML](https://linkml.io), from
which the project generates a JSON Schema for each document and a data dictionary. It is stage 1
of the plan in pruzhany-steps `.scratch/linkml/plan.md`: **LinkML describes; `zod/` and
`pydantic/` still validate.** What LinkML cannot say about the shapes is listed in
`known-looser.yaml`, each with what enforces it instead.

| File | What it is |
| --- | --- |
| `schema/*.yaml` | The definition: `types.yaml` (the shared types), `vocabulary.yaml` (the vocabulary's enums, generated), `site_common.yaml`, `pages.yaml`, `content_items.yaml`, `mentions.yaml`, `life_events.yaml`, `editions.yaml` (the issue documents and the catalog), `sourced_entities.yaml`, `media.yaml`, `shared.yaml`, `shared_record.yaml` (the shared record). Imports run types and vocabulary <- sourced_entities <- site_common <- shared_record. |
| `schema/vocabulary.yaml` | Written by `vocabulary/generate.py` from `vocabulary/*.json`, one enum a group, never edited by hand: change the JSON, run that generator, then `linkml/generate.py` for its docs. That generator's `--check` (`bin/verify vocabulary`) fails on a hand edit. |
| `modules.json` | The manifest: each schema file, its top class (or `null`) and the name its outputs take. |
| `generated/` | What `generate.py` makes from the manifest, committed: `json-schema/<name>.schema.json` for a module with a top class, `docs/<name>/` (gen-doc) for every module. Never edited by hand. |
| `generate.py` | Makes `generated/` afresh, or with `--check` compares it byte for byte. |
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
| `tests/` | The canaries (`canary_*.py`), the tests (`test_*.py`) and their planted files (`fixtures/`). |

## Running it

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

On Windows the environment's Python is `"$env/Scripts/python.exe"`. Every generated file is UTF-8
with `\n` line ends and one at the end, whatever the machine; `.gitattributes` here checks every
file of this folder out with `\n` too.

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
Python steps pin `PYDANTIC_VERSION` (2.12.5). `bin/verify linkml` makes it afresh in a temporary
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
- **Generated Pydantic bounds the whole list.** Bound the items through a type. Guard: the house
  lint, and `canary_linkml.PydanticBoundsTheWholeList`. Also measured: gen-pydantic drops a bound
  on a type altogether (`list[int]` with no bound), which matters in stage 2 and not here.
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
- **Flat RDF loses the order of a list, and an RDF export needs IRIs.** Not generated in stage 1;
  the RDF outputs come in stage 3, with `@list` or `xywh=` and the ids' namespace.
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
  and the other generators (SHACL, OWL, JSON-LD context, TypeScript): not used in stage 1.

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
