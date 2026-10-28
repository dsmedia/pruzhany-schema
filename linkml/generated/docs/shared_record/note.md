---
search:
  boost: 5.0
---

# Slot: note 

<div data-search-exclude markdown="1">



URI: [pc:note](https://pruzhany.org/ns/sourced-entities#note)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Attribution](Attribution.md), [Citation](Citation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:note |
| native | pc:note |




## LinkML Source

<details>
```yaml
name: note
domain_of:
- Attribution
- Citation
range: string

```
</details></div>
