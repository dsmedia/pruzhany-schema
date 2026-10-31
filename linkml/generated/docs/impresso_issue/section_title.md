---
search:
  boost: 5.0
---

# Slot: section_title 


_A section title grouping content items, with its original OCR components._



<div data-search-exclude markdown="1">



URI: [pc:section_title](https://pruzhany.org/ns/sourced-entities#section_title)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoIssueSection](ImpressoIssueSection.md) |
| Domain Of | [ImpressoIssueItem](ImpressoIssueItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueItem](ImpressoIssueItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].section_title |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:section_title |
| native | pc:section_title |




## LinkML Source

<details>
```yaml
name: section_title
annotations:
  impresso:
    tag: impresso
    value: issue.i[].section_title
description: A section title grouping content items, with its original OCR components.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssueItem
domain_of:
- ImpressoIssueItem
range: ImpressoIssueSection
inlined: true

```
</details></div>
