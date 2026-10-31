---
search:
  boost: 5.0
---

# Slot: section_id 


_A section title grouping content items, with its original OCR components.section_id._



<div data-search-exclude markdown="1">



URI: [pc:section_id](https://pruzhany.org/ns/sourced-entities#section_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueSection](ImpressoIssueSection.md) | A section title grouping content items, with its original OCR components. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ImpressoIssueSection](ImpressoIssueSection.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueSection](ImpressoIssueSection.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].section_title.section_id |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:section_id |
| native | pc:section_id |




## LinkML Source

<details>
```yaml
name: section_id
annotations:
  impresso:
    tag: impresso
    value: issue.i[].section_title.section_id
description: A section title grouping content items, with its original OCR components.section_id.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssueSection
domain_of:
- ImpressoIssueSection
range: string
required: true

```
</details></div>
