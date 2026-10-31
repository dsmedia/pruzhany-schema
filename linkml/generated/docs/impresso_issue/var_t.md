---
search:
  boost: 5.0
---

# Slot: var_t 


_Deprecated, replaced by `media_title_variant` at issue's top-level. Variant title of the media title this CI is from (only in the case of BL newspapers). The field is present only when a meaningful variant title is available._



<div data-search-exclude markdown="1">



URI: [pc:var_t](https://pruzhany.org/ns/sourced-entities#var_t)
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
| impresso | issue.$defs.metadata.var_t |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:var_t |
| native | pc:var_t |




## LinkML Source

<details>
```yaml
name: var_t
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.var_t
  json_min_length:
    tag: json_min_length
    value: 1
description: Deprecated, replaced by `media_title_variant` at issue's top-level. Variant
  title of the media title this CI is from (only in the case of BL newspapers). The
  field is present only when a meaningful variant title is available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
