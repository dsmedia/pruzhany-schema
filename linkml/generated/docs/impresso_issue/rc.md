---
search:
  boost: 5.0
---

# Slot: rc 


_Radio channel, if applicable (st=='radio_broadcast'). The field is present only when a meaningful value is available._



<div data-search-exclude markdown="1">



URI: [pc:rc](https://pruzhany.org/ns/sourced-entities#rc)
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
| impresso | issue.rc |
| json_min_length | 1 |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:rc |
| native | pc:rc |




## LinkML Source

<details>
```yaml
name: rc
annotations:
  impresso:
    tag: impresso
    value: issue.rc
  json_min_length:
    tag: json_min_length
    value: 1
description: Radio channel, if applicable (st=='radio_broadcast'). The field is present
  only when a meaningful value is available.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string

```
</details></div>
