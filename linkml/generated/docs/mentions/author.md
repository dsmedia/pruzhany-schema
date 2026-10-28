---
search:
  boost: 5.0
---

# Slot: author 


_Who wrote the source: an institution, never a member of its staff._



<div data-search-exclude markdown="1">



URI: [rico:hasCreator](https://www.ica.org/standards/RiC/ontology#hasCreator)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Source](Source.md) |
| Slot URI | [rico:hasCreator](https://www.ica.org/standards/RiC/ontology#hasCreator) |
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
| self | rico:hasCreator |
| native | pc:author |




## LinkML Source

<details>
```yaml
name: author
description: 'Who wrote the source: an institution, never a member of its staff.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
slot_uri: rico:hasCreator
owner: Source
domain_of:
- Source
range: string

```
</details></div>
