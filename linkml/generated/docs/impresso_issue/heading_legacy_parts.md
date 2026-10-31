---
search:
  boost: 5.0
---

# Slot: heading_legacy_parts 


_A section title grouping content items, with its original OCR components.heading_legacy_parts._



<div data-search-exclude markdown="1">



URI: [pc:heading_legacy_parts](https://pruzhany.org/ns/sourced-entities#heading_legacy_parts)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueSection](ImpressoIssueSection.md) | A section title grouping content items, with its original OCR components. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoLegacyPart](ImpressoLegacyPart.md) |
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
| impresso | issue.i[].section_title.heading_legacy_parts |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:heading_legacy_parts |
| native | pc:heading_legacy_parts |




## LinkML Source

<details>
```yaml
name: heading_legacy_parts
annotations:
  impresso:
    tag: impresso
    value: issue.i[].section_title.heading_legacy_parts
description: A section title grouping content items, with its original OCR components.heading_legacy_parts.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
owner: ImpressoIssueSection
domain_of:
- ImpressoIssueSection
range: ImpressoLegacyPart
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
