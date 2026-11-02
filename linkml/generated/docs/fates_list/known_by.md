---
search:
  boost: 5.0
---

# Slot: known_by 


_How the age is known: one year of birth, a birth the paper announced, or years that disagree._



<div data-search-exclude markdown="1">



URI: [pc:known_by](https://pruzhany.org/ns/sourced-entities#known_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListAge](FatesListAge.md) | How a person's age is known, and whether it marks a child. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AgeKnownBy](AgeKnownBy.md) |
| Domain Of | [FatesListAge](FatesListAge.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


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
| self | pc:known_by |
| native | pc:known_by |




## LinkML Source

<details>
```yaml
name: known_by
description: 'How the age is known: one year of birth, a birth the paper announced,
  or years that disagree.'
from_schema: https://pruzhany.org/ns/fates_list
rank: 1000
owner: FatesListAge
domain_of:
- FatesListAge
range: AgeKnownBy
required: true

```
</details></div>
