---
search:
  boost: 5.0
---

# Slot: language 


_The languages of the record, as BCP 47 tags._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadLanguage](https://www.ica.org/standards/RiC/ontology#hasOrHadLanguage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LanguageTag](LanguageTag.md) |
| Domain Of | [Source](Source.md) |
| Slot URI | [rico:hasOrHadLanguage](https://www.ica.org/standards/RiC/ontology#hasOrHadLanguage) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/sourced_entities




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadLanguage |
| native | pc:language |




## LinkML Source

<details>
```yaml
name: language
description: The languages of the record, as BCP 47 tags.
from_schema: https://pruzhany.org/ns/sourced_entities
rank: 1000
slot_uri: rico:hasOrHadLanguage
owner: Source
domain_of:
- Source
range: LanguageTag
multivalued: true
minimum_cardinality: 1

```
</details></div>
