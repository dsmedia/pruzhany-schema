---
search:
  boost: 5.0
---

# Slot: first_mention 


_The earliest published piece that prints the person._



<div data-search-exclude markdown="1">



URI: [pc:site_mention](https://pruzhany.org/ns/sourced-entities#site_mention)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FatesListPiece](FatesListPiece.md) |
| Domain Of | [FatesListPerson](FatesListPerson.md) |
| Slot URI | [pc:site_mention](https://pruzhany.org/ns/sourced-entities#site_mention) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListPerson](FatesListPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_mention |
| native | pc:first_mention |




## LinkML Source

<details>
```yaml
name: first_mention
description: The earliest published piece that prints the person.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
slot_uri: pc:site_mention
owner: FatesListPerson
domain_of:
- FatesListPerson
range: FatesListPiece
required: true
inlined: true

```
</details></div>
