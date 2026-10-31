---
search:
  boost: 5.0
---

# Slot: speakers 


_List of speakers (names or IDs based on availabilities) within boradcast._



<div data-search-exclude markdown="1">



URI: [pc:speakers](https://pruzhany.org/ns/sourced-entities#speakers)
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
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoMetadata](ImpressoMetadata.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.metadata.speakers |
| json_item_types | object,string |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:speakers |
| native | pc:speakers |




## LinkML Source

<details>
```yaml
name: speakers
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.speakers
  json_item_types:
    tag: json_item_types
    value: object,string
description: List of speakers (names or IDs based on availabilities) within boradcast.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string
multivalued: true

```
</details></div>
