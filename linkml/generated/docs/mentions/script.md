---
search:
  boost: 5.0
---

# Slot: script 


_The script it is written in, as a four-letter ISO 15924 code such as Hebr or Latn._



<div data-search-exclude markdown="1">



URI: [pc:script](https://pruzhany.org/ns/sourced-entities#script)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Name](Name.md) | One name of a person, a family, an organisation or a place, of one kind (printed, birth, married, supplied and so on), in one script. A person's, a family's and an organisation's names are agent names and a place's are place names (vocabulary/ site-content.json, bindings agent_name and place_name), so the class itself names no single term. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScriptCode](ScriptCode.md) |
| Domain Of | [Name](Name.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Name](Name.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:script |
| native | pc:script |




## LinkML Source

<details>
```yaml
name: script
description: The script it is written in, as a four-letter ISO 15924 code such as
  Hebr or Latn.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: Name
domain_of:
- Name
range: ScriptCode
required: true

```
</details></div>
