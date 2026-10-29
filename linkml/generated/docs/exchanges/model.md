---
search:
  boost: 5.0
---

# Slot: model 

<div data-search-exclude markdown="1">



URI: [pc:model](https://pruzhany.org/ns/sourced-entities#model)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PromptVersion](PromptVersion.md) | One prompt version's metadata, kept beside its exact text and recovered answer shape. First and last refer to its presence in code history, not paid-call dates. A shape may be unrecoverable even when the prompt text and its history are known. |  no  |
| [KeptAsking](KeptAsking.md) | A reference to a kept answer file or an identified input within an accumulated file. Model and prompt metadata can come from a companion trial setting or history; fields absent from storage are not invented. This is not a promise that one file is one paid call. Payloads retain their existing steps formats. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PromptVersion](PromptVersion.md), [KeptAsking](KeptAsking.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:model |
| native | pc:model |




## LinkML Source

<details>
```yaml
name: model
domain_of:
- PromptVersion
- KeptAsking
range: string

```
</details></div>
