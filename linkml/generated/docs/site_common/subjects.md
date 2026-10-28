---
search:
  boost: 5.0
---

# Slot: subjects 


_The persons, places or events the source shows or speaks of, by their ids._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadSubject](https://www.ica.org/standards/RiC/ontology#hasOrHadSubject)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Source](Source.md) |
| Slot URI | [rico:hasOrHadSubject](https://www.ica.org/standards/RiC/ontology#hasOrHadSubject) |
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


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadSubject |
| native | pc:subjects |




## LinkML Source

<details>
```yaml
name: subjects
description: The persons, places or events the source shows or speaks of, by their
  ids.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
slot_uri: rico:hasOrHadSubject
owner: Source
domain_of:
- Source
range: NonBlankText
multivalued: true
minimum_cardinality: 1

```
</details></div>
