---
search:
  boost: 5.0
---

# Slot: sm 


_Source medium, format in which the media was originally produced. If `tp == radio_broadcast`, this is typically `typescript` or `audio`._



<div data-search-exclude markdown="1">



URI: [pc:sm](https://pruzhany.org/ns/sourced-entities#sm)
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


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** print, typescript, audio

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.sm |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:sm |
| native | pc:sm |




## LinkML Source

<details>
```yaml
name: sm
annotations:
  impresso:
    tag: impresso
    value: issue.sm
description: Source medium, format in which the media was originally produced. If
  `tp == radio_broadcast`, this is typically `typescript` or `audio`.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string
equals_string_in:
- print
- typescript
- audio

```
</details></div>
