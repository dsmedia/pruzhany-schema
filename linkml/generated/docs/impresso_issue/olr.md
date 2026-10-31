---
search:
  boost: 5.0
---

# Slot: olr 


_True if optical layout recognition was applied to the issue/bulletin this content item originates from._



<div data-search-exclude markdown="1">



URI: [pc:olr](https://pruzhany.org/ns/sourced-entities#olr)
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
| impresso | issue.olr |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:olr |
| native | pc:olr |




## LinkML Source

<details>
```yaml
name: olr
annotations:
  impresso:
    tag: impresso
    value: issue.olr
description: True if optical layout recognition was applied to the issue/bulletin
  this content item originates from.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: boolean

```
</details></div>
