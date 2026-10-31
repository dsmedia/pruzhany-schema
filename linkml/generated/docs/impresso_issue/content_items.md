---
search:
  boost: 5.0
---

# Slot: content_items 


_The content item(s) contained in the newspaper/radio_broadcast issue. Upstream places required m on the array, where JSON Schema does not apply it; the entry metadata is therefore optional._



<div data-search-exclude markdown="1">



URI: [pc:content_items](https://pruzhany.org/ns/sourced-entities#content_items)
Alias: i

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImpressoIssue](ImpressoIssue.md) | Logical representation of the contents of a canonical issue (newspaper or broadcast). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImpressoIssueItem](ImpressoIssueItem.md) |
| Domain Of | [ImpressoIssue](ImpressoIssue.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ImpressoIssue](ImpressoIssue.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | issue.i |




### Schema Source


* from schema: https://pruzhany.org/ns/impresso_issue




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:content_items |
| native | pc:content_items |




## LinkML Source

<details>
```yaml
name: content_items
annotations:
  impresso:
    tag: impresso
    value: issue.i
description: The content item(s) contained in the newspaper/radio_broadcast issue.
  Upstream places required m on the array, where JSON Schema does not apply it; the
  entry metadata is therefore optional.
from_schema: https://pruzhany.org/ns/impresso_issue
rank: 1000
alias: i
owner: ImpressoIssue
domain_of:
- ImpressoIssue
range: ImpressoIssueItem
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
