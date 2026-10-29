---
search:
  boost: 5.0
---

# Slot: last_day 


_The day of last_commit. Agreement with history and first_day ordering are checked in steps, not by this single-document shape._



<div data-search-exclude markdown="1">



URI: [pc:last_day](https://pruzhany.org/ns/sourced-entities#last_day)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExchangeDay](ExchangeDay.md) |
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
| self | pc:last_day |
| native | pc:last_day |




## LinkML Source

<details>
```yaml
name: last_day
description: The day of last_commit. Agreement with history and first_day ordering
  are checked in steps, not by this single-document shape.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: ExchangeDay
required: true

```
</details></div>
