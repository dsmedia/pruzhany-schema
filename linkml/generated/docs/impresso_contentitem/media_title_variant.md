---
search:
  boost: 5.0
---

# Slot: media_title_variant 


_Variant title of the media title this CI is from (mainly in the case of BL newspapers). The field is present only when a meaningful variant title is available._



<div data-search-exclude markdown="1">



URI: [pc:media_title_variant](https://pruzhany.org/ns/sourced-entities#media_title_variant)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoContentItem](ImpressoContentItem.md) | This schema defines the JSON representation of a paper-based content item — either printed or typewritten. A content item corresponds to any logical segmentation unit of a digitised media production, at or below the page level for printed documents. In newspapers, for example, an article is a typical type of content item. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoContentItem](ImpressoContentItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoContentItem](ImpressoContentItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.media_title_variant |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_title_variant |
| native | pc:media_title_variant |




## LinkML Source

<details>
```yaml
name: media_title_variant
annotations:
  impresso:
    tag: impresso
    value: content.media_title_variant
  json_min_length:
    tag: json_min_length
    value: 1
description: Variant title of the media title this CI is from (mainly in the case
  of BL newspapers). The field is present only when a meaningful variant title is
  available.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string

```
</details></div>
