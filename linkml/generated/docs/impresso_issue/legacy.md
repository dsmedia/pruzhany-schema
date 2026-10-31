---
search:
  boost: 5.0
---

# Slot: legacy 


_Legacy sections or components of the content item in the original OCR/OLR. They are meant to enable the reassignation of Impresso CIs (and enrichments) to the original OCR/OLR files._



<div data-search-exclude markdown="1">



URI: [pc:legacy](https://pruzhany.org/ns/sourced-entities#legacy)
Alias: l

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssueItem](ImpressoIssueItem.md) | A content item (e.g. article, advertisement, radio broadcast, etc.) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoLegacy](ImpressoLegacy.md) |
| Domain Of | [ImpressoIssueItem](ImpressoIssueItem.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssueItem](ImpressoIssueItem.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i[].l |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:legacy |
| native | pc:legacy |




## LinkML Source

<details>
```yaml
name: legacy
annotations:
  impresso:
    tag: impresso
    value: issue.i[].l
description: Legacy sections or components of the content item in the original OCR/OLR.
  They are meant to enable the reassignation of Impresso CIs (and enrichments) to
  the original OCR/OLR files.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: l
owner: ImpressoIssueItem
domain_of:
- ImpressoIssueItem
range: ImpressoLegacy
inlined: true

```
</details></div>
