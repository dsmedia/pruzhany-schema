---
search:
  boost: 5.0
---

# Slot: Over (over) 


_The over field in the AnswerHeading response._



<div data-search-exclude markdown="1">



URI: [pc:over](https://pruzhany.org/ns/sourced-entities#over)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FindItemsAnswerHeading](FindItemsAnswerHeading.md) | A heading over several items as the model gives it: its lines, and the items' numbers. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [FindItemsAnswerHeading](FindItemsAnswerHeading.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FindItemsAnswerHeading](FindItemsAnswerHeading.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| description_in_wire | False |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:over |
| native | pc:over |




## LinkML Source

<details>
```yaml
name: over
annotations:
  description_in_wire:
    tag: description_in_wire
    value: false
description: The over field in the AnswerHeading response.
title: Over
from_schema: https://pruzhany.org/ns/answers
rank: 1000
owner: FindItemsAnswerHeading
domain_of:
- FindItemsAnswerHeading
range: integer
required: true
multivalued: true

```
</details></div>
