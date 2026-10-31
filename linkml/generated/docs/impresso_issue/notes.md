---
search:
  boost: 5.0
---

# Slot: notes 


_Notes._



<div data-search-exclude markdown="1">



URI: [pc:notes](https://pruzhany.org/ns/sourced-entities#notes)
Alias: n

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
| impresso | issue.n |
| json_types | string,array |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:notes |
| native | pc:notes |




## LinkML Source

<details>
```yaml
name: notes
annotations:
  impresso:
    tag: impresso
    value: issue.n
  json_types:
    tag: json_types
    value: string,array
description: Notes.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: n
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
