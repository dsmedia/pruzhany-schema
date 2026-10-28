---
search:
  boost: 5.0
---

# Slot: dated 


_The record's own date, apart from when it was published or consulted._



<div data-search-exclude markdown="1">



URI: [rico:hasCreationDate](https://www.ica.org/standards/RiC/ontology#hasCreationDate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SourcedDate](SourcedDate.md) |
| Domain Of | [Source](Source.md) |
| Slot URI | [rico:hasCreationDate](https://www.ica.org/standards/RiC/ontology#hasCreationDate) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasCreationDate |
| native | pc:dated |




## LinkML Source

<details>
```yaml
name: dated
description: The record's own date, apart from when it was published or consulted.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
slot_uri: rico:hasCreationDate
owner: Source
domain_of:
- Source
range: SourcedDate
inlined: true

```
</details></div>
