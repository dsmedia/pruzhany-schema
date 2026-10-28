---
search:
  boost: 5.0
---

# Slot: record_id 


_The holder's own number for the record, such as a Yad Vashem record number._



<div data-search-exclude markdown="1">



URI: [rico:hasOrHadIdentifier](https://www.ica.org/standards/RiC/ontology#hasOrHadIdentifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Citation](Citation.md) |
| Slot URI | [rico:hasOrHadIdentifier](https://www.ica.org/standards/RiC/ontology#hasOrHadIdentifier) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasOrHadIdentifier |
| native | pc:record_id |




## LinkML Source

<details>
```yaml
name: record_id
description: The holder's own number for the record, such as a Yad Vashem record number.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
slot_uri: rico:hasOrHadIdentifier
owner: Citation
domain_of:
- Citation
range: string

```
</details></div>
