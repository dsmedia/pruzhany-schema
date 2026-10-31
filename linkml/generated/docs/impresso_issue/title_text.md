---
search:
  boost: 5.0
---

# Slot: title_text 


_A section title grouping content items, with its original OCR components.title_text._



<div data-search-exclude markdown="1">



URI: [pc:title_text](https://pruzhany.org/ns/sourced-entities#title_text)
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
| impresso | issue.i[].section_title.title_text |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:title_text |
| native | pc:title_text |




## LinkML Source

<details>
```yaml
name: title_text
annotations:
  impresso:
    tag: impresso
    value: issue.i[].section_title.title_text
description: A section title grouping content items, with its original OCR components.title_text.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssueSection
domain_of:
- ImpressoIssueSection
range: string
required: true

```
</details></div>
