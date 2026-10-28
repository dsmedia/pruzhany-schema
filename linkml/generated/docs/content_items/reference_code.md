---
search:
  boost: 5.0
---

# Slot: reference_code 

<div data-search-exclude markdown="1">



URI: [pc:reference_code](https://pruzhany.org/ns/sourced-entities#reference_code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Source](Source.md), [Citation](Citation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:reference_code |
| native | pc:reference_code |




## LinkML Source

<details>
```yaml
name: reference_code
domain_of:
- Source
- Citation
range: string

```
</details></div>
