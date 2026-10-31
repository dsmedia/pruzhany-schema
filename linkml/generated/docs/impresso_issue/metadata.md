---
search:
  boost: 5.0
---

# Slot: metadata 


_Metadata about the content item._



<div data-search-exclude markdown="1">



URI: [pc:metadata](https://pruzhany.org/ns/sourced-entities#metadata)
Alias: m

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoMetadata](ImpressoMetadata.md) |
| Domain Of | [ImpressoIssueItem](ImpressoIssueItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueItem](ImpressoIssueItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].m |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:metadata |
| native | pc:metadata |




## LinkML Source

<details>
```yaml
name: metadata
annotations:
  impresso:
    tag: impresso
    value: issue.i[].m
description: Metadata about the content item.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: m
owner: ImpressoIssueItem
domain_of:
- ImpressoIssueItem
range: ImpressoMetadata
inlined: true

```
</details></div>
