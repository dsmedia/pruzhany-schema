---
search:
  boost: 5.0
---

# Slot: consolidated 


_True if this issue is consolidated, and contains additional language identification and ocrqa information._



<div data-search-exclude markdown="1">



URI: [pc:consolidated](https://pruzhany.org/ns/sourced-entities#consolidated)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [ImpressoIssue](ImpressoIssue.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssue](ImpressoIssue.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.consolidated |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:consolidated |
| native | pc:consolidated |




## LinkML Source

<details>
```yaml
name: consolidated
annotations:
  impresso:
    tag: impresso
    value: issue.consolidated
description: True if this issue is consolidated, and contains additional language
  identification and ocrqa information.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: boolean

```
</details></div>
