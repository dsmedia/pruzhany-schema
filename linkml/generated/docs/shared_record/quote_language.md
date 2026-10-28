---
search:
  boost: 5.0
---

# Slot: quote_language 

<div data-search-exclude markdown="1">



URI: [pc:quote_language](https://pruzhany.org/ns/sourced-entities#quote_language)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |
| [MediaFamilyWords](MediaFamilyWords.md) | The family's own words about a medium, quoted from a registered source with the page or part they are on: a public part of a citation, with no private note. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Citation](Citation.md), [MediaFamilyWords](MediaFamilyWords.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:quote_language |
| native | pc:quote_language |




## LinkML Source

<details>
```yaml
name: quote_language
domain_of:
- Citation
- MediaFamilyWords
range: string

```
</details></div>
