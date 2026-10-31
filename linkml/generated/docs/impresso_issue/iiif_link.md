---
search:
  boost: 5.0
---

# Slot: iiif_link 


_IIIF image link, depending on content item type (if `tp == image`). The field is present only when a meaningful link is available. It should follow the format: '{scheme}://{server}/{prefix}/{identifier}/info.json'._



<div data-search-exclude markdown="1">



URI: [pc:iiif_link](https://pruzhany.org/ns/sourced-entities#iiif_link)
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
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.iiif_link |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:iiif_link |
| native | pc:iiif_link |




## LinkML Source

<details>
```yaml
name: iiif_link
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.iiif_link
  json_min_length:
    tag: json_min_length
    value: 1
description: 'IIIF image link, depending on content item type (if `tp == image`).
  The field is present only when a meaningful link is available. It should follow
  the format: ''{scheme}://{server}/{prefix}/{identifier}/info.json''.'
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
