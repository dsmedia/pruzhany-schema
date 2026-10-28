---
search:
  boost: 5.0
---

# Slot: record_type 


_The holder's own type of the record, such as Page of Testimony._



<div data-search-exclude markdown="1">



URI: [rico:hasDocumentaryFormType](https://www.ica.org/standards/RiC/ontology#hasDocumentaryFormType)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Citation](Citation.md) |
| Slot URI | [rico:hasDocumentaryFormType](https://www.ica.org/standards/RiC/ontology#hasDocumentaryFormType) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:hasDocumentaryFormType |
| native | pc:record_type |




## LinkML Source

<details>
```yaml
name: record_type
description: The holder's own type of the record, such as Page of Testimony.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:hasDocumentaryFormType
owner: Citation
domain_of:
- Citation
range: NonBlankText

```
</details></div>
