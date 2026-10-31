---
search:
  boost: 5.0
---

# Slot: cdt 


_Creation date timestamp (of the JSON file)._



<div data-search-exclude markdown="1">



URI: [pc:cdt](https://pruzhany.org/ns/sourced-entities#cdt)
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
| impresso | issue.cdt |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:cdt |
| native | pc:cdt |




## LinkML Source

<details>
```yaml
name: cdt
annotations:
  impresso:
    tag: impresso
    value: issue.cdt
description: Creation date timestamp (of the JSON file).
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
