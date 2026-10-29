---
search:
  boost: 5.0
---

# Slot: budget_usd 


_The configured maximum budget in US dollars, separate from an answer's recorded cost. Zero is allowed; no undocumented upper bound is imposed._



<div data-search-exclude markdown="1">



URI: [pc:budget_usd](https://pruzhany.org/ns/sourced-entities#budget_usd)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonNegativeNumber](NonNegativeNumber.md) |
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
| self | pc:budget_usd |
| native | pc:budget_usd |




## LinkML Source

<details>
```yaml
name: budget_usd
description: The configured maximum budget in US dollars, separate from an answer's
  recorded cost. Zero is allowed; no undocumented upper bound is imposed.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: NonNegativeNumber
required: true

```
</details></div>
