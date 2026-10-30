# Shared rule cases

These cases define the common behavior of the Python publisher and the TypeScript
site where both languages must keep an implementation. All identifiers, labels,
people, sources and evidence here are fictional. Nothing was taken from a real
record. Expected values are kept data, never calculated by the tests under test.

- `record-shards.json`: 40 ids and their integer shard numbers. FNV-1a starts at
  `0x811c9dc5`, XORs each UTF-8 byte, multiplies by `0x01000193` with unsigned
  32-bit wraparound, and takes the low eight bits (256 shards). Values were
  computed with the site's `shardNumber` and checked against Python's `number`.
  Includes multi-byte characters, a supplementary-plane character, distinct
  composed/decomposed strings, a long id, and shards 00, 01, 0f, 10, 7f, 80, fe,
  ff. Both hash functions allow the empty string; record writers separately
  reject empty entity ids. Strings are hashed as supplied, without normalization.
- `presumption-core.json`: 56 minimal raw shared-record fragments. `person_id`
  selects the subject, `current_year` freezes the clock, and `expected.living`
  says whether the living-person presumption holds. Death evidence, births at
  109/110/111 years, and printed names at 84/85/86 source years are covered,
  including accepted versus proposed facts and preserved legacy evidence.
  Reviewed incoming death evidence is included. Every record explicitly supplies
  persons, facts, sources and relations; omitted full-record fields are irrelevant
  to these functions. The malformed-date cases intentionally bypass document
  validation. They check the raw rule, not whether an archive accepts such dates.

The site runs `presumeRecord(record, [], current_year)` and reads the target's
`living` result. Python runs `presumed_living(person, record, current_year=...)`.
No case supplies issue mentions, a family's `shown` permission, or media consent.
Consequently the implementations' separate additions cannot affect these cases.
Tests compare booleans only; site reason precedence is outside this shared core.

## Recorded differences

`sides_differ: true` requires separate `expected.site` and `expected.steps`
booleans, plus a recommendation. These are active assertions, never skips or
expected failures. Common cases explicitly use `sides_differ: false`.

| Case                    | Raw date   | Site living | Steps living | Recommendation |
| ----------------------- | ---------- | ----------- | ------------ | -------------- |
| malformed-birth-suffix  | `1916x`    | false       | true         | Steps          |
| malformed-birth-compact | `19160101` | false       | true         | Steps          |
| malformed-print-suffix  | `1941x`    | false       | true         | Steps          |
| malformed-print-compact | `19410101` | false       | true         | Steps          |

Recommend requiring the year to end or be followed by a hyphen, as Python does.
An arbitrary four-digit prefix in malformed input should not lift privacy.
This recommendation changes neither implementation. Both currently still read
the year in `1916-not-a-date` and `1941-99-99`; those common malformed cases are
also pinned. Neither function is a complete calendar-date validator.

The corpus structure is checked by `zod/conformance.test.ts`, using only the
repository's Bun toolchain (no Python or sibling checkout). Consumers must run
every case and select their own recorded answer on a difference. A deliberate
rule change updates this corpus and both consumers together.

Documentation read 30 October 2026: [Vitest Test API](https://vitest.dev/api/test)
(`it.each`), [Zod Defining schemas](https://zod.dev/api) (strict objects and
discriminated unions), and [Bun Runtime](https://bun.sh/docs/runtime). Tool
versions stay at the repository's existing pins.
