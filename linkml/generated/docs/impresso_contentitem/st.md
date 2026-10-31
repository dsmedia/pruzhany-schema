---
search:
  boost: 5.0
---

# Slot: st 


_The type of media source to which this content item belongs. Must be a value from the impresso-essentials.utils SourceType enum._



<div data-search-exclude markdown="1">



URI: [pc:st](https://pruzhany.org/ns/sourced-entities#st)
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


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** newspaper, radio_broadcast, radio_magazine, radio_schedule, monograph, encyclopedia

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | content.st |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_contentitem




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:st |
| native | pc:st |




## LinkML Source

<details>
```yaml
name: st
annotations:
  impresso:
    tag: impresso
    value: content.st
description: The type of media source to which this content item belongs. Must be
  a value from the impresso-essentials.utils SourceType enum.
from_schema: https://pruzhany.org/ns/impresso_contentitem
rank: 1000
owner: ImpressoContentItem
domain_of:
- ImpressoContentItem
range: string
equals_string_in:
- newspaper
- radio_broadcast
- radio_magazine
- radio_schedule
- monograph
- encyclopedia

```
</details></div>
