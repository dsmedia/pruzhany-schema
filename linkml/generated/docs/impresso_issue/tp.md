---
search:
  boost: 5.0
---

# Slot: tp 


_Type of the content item._



<div data-search-exclude markdown="1">



URI: [pc:tp](https://pruzhany.org/ns/sourced-entities#tp)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoMetadata](ImpressoMetadata.md) | Metadata for an entry in the canonical issue, including its page or audio references. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoMetadata](ImpressoMetadata.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** article, ad, image, table, death_notice, weather, page, radio_bulletin, radio_broadcast_episode, chronicle, chapter, discussion, entertainment

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.tp |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:tp |
| native | pc:tp |




## LinkML Source

<details>
```yaml
name: tp
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.tp
description: Type of the content item.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string
required: true
equals_string_in:
- article
- ad
- image
- table
- death_notice
- weather
- page
- radio_bulletin
- radio_broadcast_episode
- chronicle
- chapter
- discussion
- entertainment

```
</details></div>
