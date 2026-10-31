---
search:
  boost: 5.0
---

# Slot: part_of 


_Article/content-item to which the image is attached (if `tp == image`)._



<div data-search-exclude markdown="1">



URI: [pc:part_of](https://pruzhany.org/ns/sourced-entities#part_of)
Alias: pOf

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoIssueItem](ImpressoIssueItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueItem](ImpressoIssueItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].pOf |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:part_of |
| native | pc:part_of |




## LinkML Source

<details>
```yaml
name: part_of
annotations:
  impresso:
    tag: impresso
    value: issue.i[].pOf
  nullable:
    tag: nullable
    value: true
description: Article/content-item to which the image is attached (if `tp == image`).
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: pOf
owner: ImpressoIssueItem
domain_of:
- ImpressoIssueItem
range: string

```
</details></div>
