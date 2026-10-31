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
| impresso | issue.media_title_variant |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




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
    value: issue.media_title_variant
  json_min_length:
    tag: json_min_length
    value: 1
description: Variant title of the media title this CI is from (mainly in the case
  of BL newspapers). The field is present only when a meaningful variant title is
  available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
