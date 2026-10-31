---
search:
  boost: 5.0
---

# Slot: source_id 

<div data-search-exclude markdown="1">



URI: [pc:source_id](https://pruzhany.org/ns/sourced-entities#source_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [PlaceIdentifier](PlaceIdentifier.md) | One identifier of a person, organisation, place or holder, carried only on evidence, never from a match of names. Outside ids are read on their authority's own pages; merged local ids cite the registered source of the adjudicated merge. |  no  |
| [SourceDerivation](SourceDerivation.md) | The record a source we hold was made from, and how: a copy or a transcription of it. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |
| [MediaFamilyWords](MediaFamilyWords.md) | The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note. |  no  |
| [PublicMedia](PublicMedia.md) | One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies. |  no  |
| [Media](Media.md) | One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PlaceIdentifier](PlaceIdentifier.md), [SourceDerivation](SourceDerivation.md), [Citation](Citation.md), [MediaFamilyWords](MediaFamilyWords.md), [PublicMedia](PublicMedia.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:source_id |
| native | pc:source_id |




## LinkML Source

<details>
```yaml
name: source_id
domain_of:
- PlaceIdentifier
- SourceDerivation
- Citation
- MediaFamilyWords
- PublicMedia
range: string

```
</details></div>
