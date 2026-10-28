---
search:
  boost: 5.0
---

# Slot: available_dates 


_The dates of the editions whose pages are on the site._



<div data-search-exclude markdown="1">



URI: [pc:available_dates](https://pruzhany.org/ns/sourced-entities#available_dates)
Alias: availableDates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IsoDay](IsoDay.md) |
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
| self | pc:available_dates |
| native | pc:available_dates |




## LinkML Source

<details>
```yaml
name: available_dates
description: The dates of the editions whose pages are on the site.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: availableDates
owner: EditionsCatalog
domain_of:
- EditionsCatalog
range: IsoDay
required: true
multivalued: true

```
</details></div>
