---
search:
  boost: 5.0
---

# Slot: first_commit 


_The first steps commit known to contain this prompt version in code._



<div data-search-exclude markdown="1">



URI: [pc:first_commit](https://pruzhany.org/ns/sourced-entities#first_commit)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExchangeCommit](ExchangeCommit.md) |
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
| self | pc:first_commit |
| native | pc:first_commit |




## LinkML Source

<details>
```yaml
name: first_commit
description: The first steps commit known to contain this prompt version in code.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: ExchangeCommit
required: true

```
</details></div>
