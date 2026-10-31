---
search:
  boost: 5.0
---

# Slot: iiif_manifest_uri 


_URI for the issue's manifest in the IIIF Presentation API. The field is present only when a meaningful URI is available._



<div data-search-exclude markdown="1">



URI: [pc:iiif_manifest_uri](https://pruzhany.org/ns/sourced-entities#iiif_manifest_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoIssue](ImpressoIssue.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssue](ImpressoIssue.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.iiif_manifest_uri |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:iiif_manifest_uri |
| native | pc:iiif_manifest_uri |




## LinkML Source

<details>
```yaml
name: iiif_manifest_uri
annotations:
  impresso:
    tag: impresso
    value: issue.iiif_manifest_uri
  json_min_length:
    tag: json_min_length
    value: 1
description: URI for the issue's manifest in the IIIF Presentation API. The field
  is present only when a meaningful URI is available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
