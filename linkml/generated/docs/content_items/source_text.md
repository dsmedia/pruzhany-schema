---
search:
  boost: 5.0
---

# Slot: source_text 


_The text used, exactly, never normalised or replaced by a later reading._



<div data-search-exclude markdown="1">



URI: [pc:source_text](https://pruzhany.org/ns/sourced-entities#source_text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextBasis](TextBasis.md) | The exact text a translation or supplied title was made from, and where it is printed, kept even after the text is read again. |  no  |
| [CitedTextBasis](CitedTextBasis.md) | The exact source words of a citation or source title. The containing citation's locator or source description locates them; printed addresses are optional, and when supplied remain nonempty real image-and-box witnesses. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [TextBasis](TextBasis.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TextBasis](TextBasis.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:source_text |
| native | pc:source_text |




## LinkML Source

<details>
```yaml
name: source_text
description: The text used, exactly, never normalised or replaced by a later reading.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
owner: TextBasis
domain_of:
- TextBasis
range: string
required: true

```
</details></div>
