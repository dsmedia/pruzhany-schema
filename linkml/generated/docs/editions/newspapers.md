---
search:
  boost: 5.0
---

# Slot: newspapers 


_The papers these editions belong to, one entry per source-register id, with their default picture credits. When present, every edition's newspaper must name one of these ids. The runtime twins enforce id uniqueness and membership; LinkML's generated JSON Schema cannot compare values across these lists._



<div data-search-exclude markdown="1">



URI: [pc:catalog_newspapers](https://pruzhany.org/ns/sourced-entities#catalog_newspapers)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Newspaper](Newspaper.md) |
| Domain Of | [EditionsCatalog](EditionsCatalog.md) |
| Slot URI | [pc:catalog_newspapers](https://pruzhany.org/ns/sourced-entities#catalog_newspapers) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EditionsCatalog](EditionsCatalog.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:catalog_newspapers |
| native | pc:newspapers |




## LinkML Source

<details>
```yaml
name: newspapers
description: The papers these editions belong to, one entry per source-register id,
  with their default picture credits. When present, every edition's newspaper must
  name one of these ids. The runtime twins enforce id uniqueness and membership; LinkML's
  generated JSON Schema cannot compare values across these lists.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: pc:catalog_newspapers
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: Newspaper
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
