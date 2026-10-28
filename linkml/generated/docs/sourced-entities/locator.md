---
search:
  boost: 5.0
---

# Slot: locator 


_An internal pointer into the project's files; never published and never a holder's record number._



<div data-search-exclude markdown="1">



URI: [pc:site_citation_locator](https://pruzhany.org/ns/sourced-entities#site_citation_locator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Citation](Citation.md) |
| Slot URI | [pc:site_citation_locator](https://pruzhany.org/ns/sourced-entities#site_citation_locator) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_citation_locator |
| native | pc:locator |




## LinkML Source

<details>
```yaml
name: locator
description: An internal pointer into the project's files; never published and never
  a holder's record number.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
slot_uri: pc:site_citation_locator
owner: Citation
domain_of:
- Citation
range: NonBlankText

```
</details></div>
