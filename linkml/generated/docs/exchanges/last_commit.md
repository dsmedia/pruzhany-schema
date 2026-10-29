---
search:
  boost: 5.0
---

# Slot: last_commit 


_The last steps commit known to contain this prompt version in code, not necessarily the latest kept answer or the commit removing the version._



<div data-search-exclude markdown="1">



URI: [pc:last_commit](https://pruzhany.org/ns/sourced-entities#last_commit)
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
| self | pc:last_commit |
| native | pc:last_commit |




## LinkML Source

<details>
```yaml
name: last_commit
description: The last steps commit known to contain this prompt version in code, not
  necessarily the latest kept answer or the commit removing the version.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: ExchangeCommit
required: true

```
</details></div>
