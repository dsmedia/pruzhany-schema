---
search:
  boost: 5.0
---

# Slot: composing_ci_ids 


_A section title grouping content items, with its original OCR components.composing_ci_ids._



<div data-search-exclude markdown="1">



URI: [pc:composing_ci_ids](https://pruzhany.org/ns/sourced-entities#composing_ci_ids)
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
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueSection](ImpressoIssueSection.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].section_title.composing_ci_ids |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:composing_ci_ids |
| native | pc:composing_ci_ids |




## LinkML Source

<details>
```yaml
name: composing_ci_ids
annotations:
  impresso:
    tag: impresso
    value: issue.i[].section_title.composing_ci_ids
description: A section title grouping content items, with its original OCR components.composing_ci_ids.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssueSection
domain_of:
- ImpressoIssueSection
range: string
required: true
multivalued: true

```
</details></div>
