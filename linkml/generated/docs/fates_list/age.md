---
search:
  boost: 5.0
---

# Slot: age 


_How the person's age is known; absent where the record gives no age._



<div data-search-exclude markdown="1">



URI: [pc:age](https://pruzhany.org/ns/sourced-entities#age)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FatesListAge](FatesListAge.md) |
| Domain Of | [FatesListPerson](FatesListPerson.md) |
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
| self | pc:age |
| native | pc:age |




## LinkML Source

<details>
```yaml
name: age
description: How the person's age is known; absent where the record gives no age.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListPerson
domain_of:
- FatesListPerson
range: FatesListAge
inlined: true

```
</details></div>
