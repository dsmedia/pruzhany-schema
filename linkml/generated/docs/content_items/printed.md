---
search:
  boost: 5.0
---

# Slot: printed 


_The date's words as the source prints or writes them._



<div data-search-exclude markdown="1">



URI: [rico:expressedDate](https://www.ica.org/standards/RiC/ontology#expressedDate)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourcedDate](SourcedDate.md) | A date a source gives: a normalized start (and end, for a range) with how precise it is, or the words as printed with their calendar, or both. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [SourcedDate](SourcedDate.md) |
| Slot URI | [rico:expressedDate](https://www.ica.org/standards/RiC/ontology#expressedDate) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SourcedDate](SourcedDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:expressedDate |
| native | pc:printed |




## LinkML Source

<details>
```yaml
name: printed
description: The date's words as the source prints or writes them.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
slot_uri: rico:expressedDate
owner: SourcedDate
domain_of:
- SourcedDate
range: NonBlankText

```
</details></div>
