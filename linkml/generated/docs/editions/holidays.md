---
search:
  boost: 5.0
---

# Slot: holidays 


_The Jewish holidays of the paper's years._



<div data-search-exclude markdown="1">



URI: [pc:holidays](https://pruzhany.org/ns/sourced-entities#holidays)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Holiday](Holiday.md) |
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
| self | pc:holidays |
| native | pc:holidays |




## LinkML Source

<details>
```yaml
name: holidays
description: The Jewish holidays of the paper's years.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: Holiday
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
