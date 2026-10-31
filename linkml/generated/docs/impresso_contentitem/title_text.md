---
search:
  boost: 5.0
---

# Slot: title_text 

<div data-search-exclude markdown="1">



URI: [pc:title_text](https://pruzhany.org/ns/sourced-entities#title_text)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |
| [ImpressoContentSection](ImpressoContentSection.md) | A section title grouping this content item with others. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md), [ImpressoContentSection](ImpressoContentSection.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:title_text |
| native | pc:title_text |




## LinkML Source

<details>
```yaml
name: title_text
domain_of:
- ImpressoContentItem
- ImpressoContentSection
range: string

```
</details></div>
