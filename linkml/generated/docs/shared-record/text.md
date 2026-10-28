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
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture they are on, a box in that picture's own pixels, and the words read inside it. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaText](MediaText.md), [PrintedAddress](PrintedAddress.md) |










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
range: string

```
</details></div>
