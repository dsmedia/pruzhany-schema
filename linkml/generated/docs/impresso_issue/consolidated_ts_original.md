---
search:
  boost: 5.0
---

# Slot: consolidated_ts_original 


_Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format) of the original issue which was consolidated into this object. Only defined if `consolidated==True`._



<div data-search-exclude markdown="1">



URI: [pc:consolidated_ts_original](https://pruzhany.org/ns/sourced-entities#consolidated_ts_original)
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


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$` |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.consolidated_ts_original |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated_ts_original |
| native | pc:consolidated_ts_original |




## LinkML Source

<details>
```yaml
name: consolidated_ts_original
annotations:
  impresso:
    tag: impresso
    value: issue.consolidated_ts_original
description: Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format) of the original
  issue which was consolidated into this object. Only defined if `consolidated==True`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string
pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$

```
</details></div>
