---
search:
  boost: 5.0
---

# Slot: addresses 

<div data-search-exclude markdown="1">



URI: [pc:addresses](https://pruzhany.org/ns/sourced-entities#addresses)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |  no  |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SiteCitation](SiteCitation.md), [TextBasis](TextBasis.md), [PrintedTitle](PrintedTitle.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:addresses |
| native | pc:addresses |




## LinkML Source

<details>
```yaml
name: addresses
domain_of:
- SiteCitation
- TextBasis
- PrintedTitle
range: string

```
</details></div>
