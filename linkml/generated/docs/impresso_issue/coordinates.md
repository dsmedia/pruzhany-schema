---
search:
  boost: 5.0
---

# Slot: coordinates 


_Coordinates (xywh format or [HPOS, VPOS, WIDTH, HEIGHT]) of image-region corresponding to the content-item depending on its type (if `tp == image`). NOTE: the 'null' option should be removed to prevent tables from having coordinates._



<div data-search-exclude markdown="1">



URI: [pc:coordinates](https://pruzhany.org/ns/sourced-entities#coordinates)
Alias: c

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [ImpressoIssueItem](ImpressoIssueItem.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 4 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueItem](ImpressoIssueItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].c |
| nullable | True |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:coordinates |
| native | pc:coordinates |




## LinkML Source

<details>
```yaml
name: coordinates
annotations:
  impresso:
    tag: impresso
    value: issue.i[].c
  nullable:
    tag: nullable
    value: true
description: 'Coordinates (xywh format or [HPOS, VPOS, WIDTH, HEIGHT]) of image-region
  corresponding to the content-item depending on its type (if `tp == image`). NOTE:
  the ''null'' option should be removed to prevent tables from having coordinates.'
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: c
owner: ImpressoIssueItem
domain_of:
- ImpressoIssueItem
range: integer
multivalued: true
minimum_cardinality: 4

```
</details></div>
