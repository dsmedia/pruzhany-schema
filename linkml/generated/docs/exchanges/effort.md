---
search:
  boost: 5.0
---

# Slot: effort 


_The explicit effort setting when known; omit when no setting was supplied or recovered. Model-dependent effort values are not enumerated here._



<div data-search-exclude markdown="1">



URI: [pc:effort](https://pruzhany.org/ns/sourced-entities#effort)
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
| self | pc:effort |
| native | pc:effort |




## LinkML Source

<details>
```yaml
name: effort
description: The explicit effort setting when known; omit when no setting was supplied
  or recovered. Model-dependent effort values are not enumerated here.
from_schema: https://pruzhany.org/ns/exchanges
rank: 1000
owner: PromptVersion
domain_of:
- PromptVersion
range: NonBlankText

```
</details></div>
