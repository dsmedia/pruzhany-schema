---
search:
  boost: 5.0
---

# Slot: paragraphs 


_Paragraphs in region order; Impresso permits zero, one or several._



<div data-search-exclude markdown="1">



URI: [pc:paragraphs](https://pruzhany.org/ns/sourced-entities#paragraphs)
Alias: p

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalRegion](PhysicalRegion.md) | One region of the page, with a box, ordered paragraphs and optional semantic links. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalParagraph](PhysicalParagraph.md) |
| Domain Of | [PhysicalRegion](PhysicalRegion.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalRegion](PhysicalRegion.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p. |
| alto | No intermediate paragraph element between TextBlock and TextLine; flatten the paragraphs' lines in order when exporting this region as a TextBlock. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:paragraphs |
| native | pc:paragraphs |




## LinkML Source

<details>
```yaml
name: paragraphs
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p.
  alto:
    tag: alto
    value: No intermediate paragraph element between TextBlock and TextLine; flatten
      the paragraphs' lines in order when exporting this region as a TextBlock.
description: Paragraphs in region order; Impresso permits zero, one or several.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: p
owner: PhysicalRegion
domain_of:
- PhysicalRegion
range: PhysicalParagraph
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
