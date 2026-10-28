---
search:
  boost: 5.0
---

# Slot: accessed 

<div data-search-exclude markdown="1">



URI: [pc:accessed](https://pruzhany.org/ns/sourced-entities#accessed)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [PlaceIdentifier](PlaceIdentifier.md) | One outside identifier of a place or a holder, read on its authority's own pages and carried only on that evidence, never from a match of names. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlaceIdentifier](PlaceIdentifier.md), [Citation](Citation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:accessed |
| native | pc:accessed |




## LinkML Source

<details>
```yaml
name: accessed
domain_of:
- PlaceIdentifier
- Citation
range: string

```
</details></div>
