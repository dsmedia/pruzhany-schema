---
search:
  boost: 5.0
---

# Slot: title 


_Title of the content item. The field is present only when a meaningful title is available._



<div data-search-exclude markdown="1">



URI: [pc:title](https://pruzhany.org/ns/sourced-entities#title)
Alias: t

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
| impresso | issue.$defs.metadata.t |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:title |
| native | pc:title |




## LinkML Source

<details>
```yaml
name: title
annotations:
  impresso:
    tag: impresso
    value: issue.$defs.metadata.t
  json_min_length:
    tag: json_min_length
    value: 1
description: Title of the content item. The field is present only when a meaningful
  title is available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: t
owner: ImpressoMetadata
domain_of:
- ImpressoMetadata
range: string

```
</details></div>
