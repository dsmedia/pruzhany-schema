---
search:
  boost: 5.0
---

# Slot: state 


_Pending, or approved by a reviewer._



<div data-search-exclude markdown="1">



URI: [pc:state](https://pruzhany.org/ns/sourced-entities#state)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Review](Review.md) | Whether a person has reviewed a statement, who and on what day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReviewStates](ReviewStates.md) |
| Domain Of | [Review](Review.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Review](Review.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:state |
| native | pc:state |




## LinkML Source

<details>
```yaml
name: state
description: Pending, or approved by a reviewer.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: Review
domain_of:
- Review
range: ReviewStates
required: true

```
</details></div>
