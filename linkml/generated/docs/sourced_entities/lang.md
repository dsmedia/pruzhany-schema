---
search:
  boost: 5.0
---

# Slot: lang 


_Its language, as a language tag such as yi or en._



<div data-search-exclude markdown="1">



URI: [pc:lang](https://pruzhany.org/ns/sourced-entities#lang)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SimpleLanguageTag](SimpleLanguageTag.md) |
| Domain Of | [Name](Name.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Name](Name.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lang |
| native | pc:lang |




## LinkML Source

<details>
```yaml
name: lang
description: Its language, as a language tag such as yi or en.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
owner: Name
domain_of:
- Name
range: SimpleLanguageTag

```
</details></div>
