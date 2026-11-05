---
search:
  boost: 5.0
---

# Slot: available_keys 


_The keys of the editions whose pages are on the site, each an Edition key: the date alone for the first paper, or the paper's code and a hyphen before it for any other. Optional for now, because a site on an older schema pin refuses unknown fields and the catalogs written so far lack it: this schema comes first, then the site's pin, then the writer writes it, and later it becomes required. When present, no key appears twice and every key names an edition in editions. The writer publishes another paper's editions without reference to availableDates, which holds the first paper's dates, so the runtime twins check only that the date-only keys equal availableDates as a set. LinkML's generated JSON Schema cannot compare values within or across these lists._



<div data-search-exclude markdown="1">



URI: [pc:available_keys](https://pruzhany.org/ns/sourced-entities#available_keys)
Alias: availableKeys

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EditionsCatalog](EditionsCatalog.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EditionsCatalog](EditionsCatalog.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:available_keys |
| native | pc:available_keys |




## LinkML Source

<details>
```yaml
name: available_keys
description: 'The keys of the editions whose pages are on the site, each an Edition
  key: the date alone for the first paper, or the paper''s code and a hyphen before
  it for any other. Optional for now, because a site on an older schema pin refuses
  unknown fields and the catalogs written so far lack it: this schema comes first,
  then the site''s pin, then the writer writes it, and later it becomes required.
  When present, no key appears twice and every key names an edition in editions. The
  writer publishes another paper''s editions without reference to availableDates,
  which holds the first paper''s dates, so the runtime twins check only that the date-only
  keys equal availableDates as a set. LinkML''s generated JSON Schema cannot compare
  values within or across these lists.'
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: availableKeys
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: string
multivalued: true
pattern: ^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])

```
</details></div>
