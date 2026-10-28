---
search:
  boost: 5.0
---

# Slot: text 

<div data-search-exclude markdown="1">



URI: [pc:text](https://pruzhany.org/ns/sourced-entities#text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaText](MediaText.md) | Words about or on a medium (a caption, a description for screen readers, an inscription, a transcript), their language and their review. |  no  |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |  no  |
| [PrintedTitle](PrintedTitle.md) | A title as printed in the paper: its words and where each line of them stands. |  no  |
| [SuppliedTitle](SuppliedTitle.md) | A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check. |  no  |
| [Translation](Translation.md) | An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaText](MediaText.md), [PrintedAddress](PrintedAddress.md), [PrintedTitle](PrintedTitle.md), [SuppliedTitle](SuppliedTitle.md), [Translation](Translation.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:text |
| native | pc:text |




## LinkML Source

<details>
```yaml
name: text
domain_of:
- MediaText
- PrintedAddress
- PrintedTitle
- SuppliedTitle
- Translation
range: string

```
</details></div>
