---
search:
  boost: 5.0
---

# Slot: is_exact_date 


_False if the date assigned to the issue is known to be inexact or approximated, True or undefined otherwise._



<div data-search-exclude markdown="1">



URI: [pc:is_exact_date](https://pruzhany.org/ns/sourced-entities#is_exact_date)
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
| impresso | issue.is_exact_date |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:is_exact_date |
| native | pc:is_exact_date |




## LinkML Source

<details>
```yaml
name: is_exact_date
annotations:
  impresso:
    tag: impresso
    value: issue.is_exact_date
description: False if the date assigned to the issue is known to be inexact or approximated,
  True or undefined otherwise.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: boolean

```
</details></div>
