---
search:
  boost: 5.0
---

# Slot: role 


_Who decided, by role: the owner or the project; never a person's name._



<div data-search-exclude markdown="1">



URI: [pc:role](https://pruzhany.org/ns/sourced-entities#role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaDecision](MediaDecision.md) | A review or a clearance: whose role made it (the owner or the project) and on what day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaDecisionRole](MediaDecisionRole.md) |
| Domain Of | [MediaDecision](MediaDecision.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaDecision](MediaDecision.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:role |
| native | pc:role |




## LinkML Source

<details>
```yaml
name: role
description: 'Who decided, by role: the owner or the project; never a person''s name.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaDecision
domain_of:
- MediaDecision
range: MediaDecisionRole
required: true

```
</details></div>
