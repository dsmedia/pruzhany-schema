---
search:
  boost: 5.0
---

# Slot: comp_id 


_ID of the part._



<div data-search-exclude markdown="1">



URI: [pc:comp_id](https://pruzhany.org/ns/sourced-entities#comp_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoLegacyPart](ImpressoLegacyPart.md) | One original OCR component retained for tracing a content item back to its source. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoLegacyPart](ImpressoLegacyPart.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoLegacyPart](ImpressoLegacyPart.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.$defs.legacy_part_item.comp_id |
| json_types | string,array |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:comp_id |
| native | pc:comp_id |




## LinkML Source

<details>
```yaml
name: comp_id
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.legacy_part_item.comp_id
  json_types:
    tag: json_types
    value: string,array
description: ID of the part.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoLegacyPart
domain_of:
- ImpressoLegacyPart
range: string

```
</details></div>
