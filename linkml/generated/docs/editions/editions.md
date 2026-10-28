---
search:
  boost: 5.0
---

# Slot: editions 


_Every edition of the paper, with its Hebrew date._



<div data-search-exclude markdown="1">



URI: [pc:editions](https://pruzhany.org/ns/sourced-entities#editions)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Edition](Edition.md) |
| Domain Of | [EditionsCatalog](EditionsCatalog.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | pc:editions |
| native | pc:editions |




## LinkML Source

<details>
```yaml
name: editions
description: Every edition of the paper, with its Hebrew date.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: Edition
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
