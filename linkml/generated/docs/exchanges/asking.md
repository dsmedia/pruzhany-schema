---
search:
  boost: 5.0
---

# Slot: asking 


_The asking served by these instructions, such as find_items, read_latin, write_english or join_people. Trial variants are registered by steps; this field is not a new controlled vocabulary._



<div data-search-exclude markdown="1">



URI: [pc:asking](https://pruzhany.org/ns/sourced-entities#asking)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
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
| self | pc:asking |
| native | pc:asking |




## LinkML Source

<details>
```yaml
name: asking
description: The asking served by these instructions, such as find_items, read_latin,
  write_english or join_people. Trial variants are registered by steps; this field
  is not a new controlled vocabulary.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: NonBlankText
required: true

```
</details></div>
