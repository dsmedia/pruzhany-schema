---
search:
  boost: 5.0
---

# Slot: fate_details 


_Where and when the person's own death, survival and deportation statements place the fate, as the record holds them structured._



<div data-search-exclude markdown="1">



URI: [pc:fate_details](https://pruzhany.org/ns/sourced-entities#fate_details)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FatesListFateDetail](FatesListFateDetail.md) |
| Domain Of | [FatesListPerson](FatesListPerson.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


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
| self | pc:fate_details |
| native | pc:fate_details |




## LinkML Source

<details>
```yaml
name: fate_details
description: Where and when the person's own death, survival and deportation statements
  place the fate, as the record holds them structured.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListPerson
domain_of:
- FatesListPerson
range: FatesListFateDetail
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
