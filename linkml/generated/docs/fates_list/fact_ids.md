---
search:
  boost: 5.0
---

# Slot: fact_ids 


_The shared record's birth statements that give the year._



<div data-search-exclude markdown="1">



URI: [pc:fact_ids](https://pruzhany.org/ns/sourced-entities#fact_ids)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListAge](FatesListAge.md) | How a person's age is known, and whether it marks a child. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [FatesListAge](FatesListAge.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


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
| self | pc:fact_ids |
| native | pc:fact_ids |




## LinkML Source

<details>
```yaml
name: fact_ids
description: The shared record's birth statements that give the year.
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListAge
domain_of:
- FatesListAge
range: NonBlankText
multivalued: true
minimum_cardinality: 1

```
</details></div>
