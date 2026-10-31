---
search:
  boost: 5.0
---

# Slot: archival_note 


_Plaintext archival note or description concerning the content item. In case of audio radio broadcasts, this corresponds to the content summary provided with the metadata. The field is present only when a meaningful note is available._



<div data-search-exclude markdown="1">



URI: [pc:archival_note](https://pruzhany.org/ns/sourced-entities#archival_note)
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
| impresso | issue.$defs.metadata.archival_note |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:archival_note |
| native | pc:archival_note |




## LinkML Source

<details>
```yaml
name: archival_note
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.archival_note
  json_min_length:
    tag: json_min_length
    value: 1
description: Plaintext archival note or description concerning the content item. In
  case of audio radio broadcasts, this corresponds to the content summary provided
  with the metadata. The field is present only when a meaningful note is available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
