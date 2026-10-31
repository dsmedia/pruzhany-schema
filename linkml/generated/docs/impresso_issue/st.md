---
search:
  boost: 5.0
---

# Slot: st 


_Type of media source. Should be a value the impresso-essentials.utils SourceType enum._



<div data-search-exclude markdown="1">



URI: [pc:st](https://pruzhany.org/ns/sourced-entities#st)
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
**Must Be One Of:** newspaper, radio_broadcast, radio_magazine, radio_schedule, monograph, encyclopedia

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.st |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:st |
| native | pc:st |




## LinkML Source

<details>
```yaml
name: st
annotations:
  impresso:
    tag: impresso
    value: issue.st
description: Type of media source. Should be a value the impresso-essentials.utils
  SourceType enum.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: string
equals_string_in:
- newspaper
- radio_broadcast
- radio_magazine
- radio_schedule
- monograph
- encyclopedia

```
</details></div>
