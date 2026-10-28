---
search:
  boost: 5.0
---

# Slot: quote_language 


_The quote's language, where it is not the source's (a translation)._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadLanguage](https://www.ica.org/standards/RiC/ontology#hasOrHadLanguage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LanguageTag](LanguageTag.md) |
| Domain Of | [Citation](Citation.md) |
| Slot URI | [rico:hasOrHadLanguage](https://www.ica.org/standards/RiC/ontology#hasOrHadLanguage) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadLanguage |
| native | pc:quote_language |




## LinkML Source

<details>
```yaml
name: quote_language
description: The quote's language, where it is not the source's (a translation).
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: rico:hasOrHadLanguage
owner: Citation
domain_of:
- Citation
range: LanguageTag

```
</details></div>
