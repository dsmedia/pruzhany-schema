---
search:
  boost: 5.0
---

# Slot: birth_years 


_The years of birth that disagree, in order._



<div data-search-exclude markdown="1">



URI: [pc:birth_years](https://pruzhany.org/ns/sourced-entities#birth_years)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListAge](FatesListAge.md) | How a person's age is known, and whether it marks a child. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BirthYear](BirthYear.md) |
| Domain Of | [FatesListAge](FatesListAge.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 2 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FatesListAge](FatesListAge.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/fates_list




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:birth_years |
| native | pc:birth_years |




## LinkML Source

<details>
```yaml
name: birth_years
description: The years of birth that disagree, in order.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListAge
domain_of:
- FatesListAge
range: BirthYear
multivalued: true
minimum_cardinality: 2

```
</details></div>
