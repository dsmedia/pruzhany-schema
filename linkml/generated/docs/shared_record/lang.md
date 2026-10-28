---
search:
  boost: 5.0
---

# Slot: lang 

<div data-search-exclude markdown="1">



URI: [pc:lang](https://pruzhany.org/ns/sourced-entities#lang)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedName](SharedName.md) | One name of a person in the shared record, with its evidence located on the printed page where the site writer found it. |  no  |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |
| [MediaText](MediaText.md) | Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Name](Name.md), [MediaText](MediaText.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lang |
| native | pc:lang |




## LinkML Source

<details>
```yaml
name: lang
domain_of:
- Name
- MediaText
range: string

```
</details></div>
