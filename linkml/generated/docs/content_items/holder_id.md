---
search:
  boost: 5.0
---

# Slot: holder_id 


_Who holds the source, by its id in the record's holders._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadHolder](https://www.ica.org/standards/RiC/ontology#hasOrHadHolder)
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
| Slot URI | [rico:hasOrHadHolder](https://www.ica.org/standards/RiC/ontology#hasOrHadHolder) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadHolder |
| native | pc:holder_id |




## LinkML Source

<details>
```yaml
name: holder_id
description: Who holds the source, by its id in the record's holders.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: rico:hasOrHadHolder
owner: Source
domain_of:
- Source
range: NonBlankText

```
</details></div>
