---
search:
  boost: 5.0
---

# Slot: code 


_The sixteen-character code naming this stored version and its directory. Some historical codes cover an expanded whole request rather than only instructions; the steps registry must establish the recipe and scope._



<div data-search-exclude markdown="1">



URI: [pc:code](https://pruzhany.org/ns/sourced-entities#code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExchangeCode](ExchangeCode.md) |
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
| self | pc:code |
| native | pc:code |




## LinkML Source

<details>
```yaml
name: code
description: The sixteen-character code naming this stored version and its directory.
  Some historical codes cover an expanded whole request rather than only instructions;
  the steps registry must establish the recipe and scope.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: ExchangeCode
required: true

```
</details></div>
