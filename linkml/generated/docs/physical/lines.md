---
search:
  boost: 5.0
---

# Slot: lines 


_Lines in paragraph order, including an empty list if stored that way._



<div data-search-exclude markdown="1">



URI: [pc:lines](https://pruzhany.org/ns/sourced-entities#lines)
Alias: l

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalParagraph](PhysicalParagraph.md) | One ordered group of lines in a region, optionally with its own box; no computed id is assigned to paragraphs by this contract. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalLine](PhysicalLine.md) |
| Domain Of | [PhysicalParagraph](PhysicalParagraph.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalParagraph](PhysicalParagraph.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json r[].p[].l. |
| alto | TextBlock/TextLine in the paragraphs' combined order. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:lines |
| native | pc:lines |




## LinkML Source

<details>
```yaml
name: lines
annotations:
  impresso:
    tag: impresso
    value: page.schema.json r[].p[].l.
  alto:
    tag: alto
    value: TextBlock/TextLine in the paragraphs' combined order.
description: Lines in paragraph order, including an empty list if stored that way.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: l
owner: PhysicalParagraph
domain_of:
- PhysicalParagraph
range: PhysicalLine
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>
