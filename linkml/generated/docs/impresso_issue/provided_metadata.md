---
search:
  boost: 5.0
---

# Slot: provided_metadata 


_Minimally preprocessed issue-level metadata included by the provider institution, especially useful for radio data (sm=audio)._



<div data-search-exclude markdown="1">



URI: [pc:provided_metadata](https://pruzhany.org/ns/sourced-entities#provided_metadata)
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
| impresso | issue.provided_metadata |
| json_types | object,array |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:provided_metadata |
| native | pc:provided_metadata |




## LinkML Source

<details>
```yaml
name: provided_metadata
annotations:
  impresso:
    tag: impresso
    value: issue.provided_metadata
  json_types:
    tag: json_types
    value: object,array
description: Minimally preprocessed issue-level metadata included by the provider
  institution, especially useful for radio data (sm=audio).
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
