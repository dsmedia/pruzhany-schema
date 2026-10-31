---
search:
  boost: 5.0
---

# Slot: ts 


_Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format). If consolidated==True, this is the consolidated timestamp (the original creation timestamp can be found in consolidated_timestamp_original); otherwise it is the original creation timestamp._



<div data-search-exclude markdown="1">



URI: [pc:ts](https://pruzhany.org/ns/sourced-entities#ts)
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
| impresso | issue.ts |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ts |
| native | pc:ts |




## LinkML Source

<details>
```yaml
name: ts
annotations:
  impresso:
    tag: impresso
    value: issue.ts
description: Creation date timestamp (in '%Y-%m-%dT%H:%M:%SZ' format). If consolidated==True,
  this is the consolidated timestamp (the original creation timestamp can be found
  in consolidated_timestamp_original); otherwise it is the original creation timestamp.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string
pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$

```
</details></div>
