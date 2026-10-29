---
search:
  boost: 5.0
---

# Slot: shape_recovered 


_Whether the exact answer JSON Schema was recovered reproducibly and kept beside the prompt. False explicitly records the limit on answer validation; a shape name by itself is not recovery._



<div data-search-exclude markdown="1">



URI: [pc:shape_recovered](https://pruzhany.org/ns/sourced-entities#shape_recovered)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [PromptVersion](PromptVersion.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PromptVersion](PromptVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/exchanges




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:shape_recovered |
| native | pc:shape_recovered |




## LinkML Source

<details>
```yaml
name: shape_recovered
description: Whether the exact answer JSON Schema was recovered reproducibly and kept
  beside the prompt. False explicitly records the limit on answer validation; a shape
  name by itself is not recovery.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: boolean
required: true

```
</details></div>
