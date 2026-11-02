---
search:
  boost: 5.0
---

# Slot: name 


_The person's name as the site shows it._



<div data-search-exclude markdown="1">



URI: [pc:name](https://pruzhany.org/ns/sourced-entities#name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListPerson](FatesListPerson.md) | One person on the list: who, the fate, where the paper first prints them, where and when the fate is placed, the archives' records about them and how their age is known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [FatesListPerson](FatesListPerson.md) |
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
| self | pc:name |
| native | pc:name |




## LinkML Source

<details>
```yaml
name: name
description: The person's name as the site shows it.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListPerson
domain_of:
- FatesListPerson
range: NonBlankText
required: true

```
</details></div>
