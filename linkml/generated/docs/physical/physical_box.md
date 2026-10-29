---
search:
  boost: 5.0
---

# Slot: physical_box 


_A box [x, y, width, height] in pixels of this page's picture, with origin at its upper left. Impresso requires exactly four integers, without a nonnegative or positive bound. It is an array, not an object with invented coordinate fields._



<div data-search-exclude markdown="1">



URI: [pc:physical_box](https://pruzhany.org/ns/sourced-entities#physical_box)
Alias: c

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalRegion](PhysicalRegion.md) | One region of the page, with a box, ordered paragraphs and optional semantic links. |  yes  |
| [PhysicalParagraph](PhysicalParagraph.md) | One ordered group of lines in a region, optionally with its own box; no computed id is assigned to paragraphs by this contract. |  no  |
| [PhysicalLine](PhysicalLine.md) | One line with a box and ordered OCR tokens. |  yes  |
| [PhysicalWord](PhysicalWord.md) | One OCR token (a word or word part), with its own box and surface text. |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [PhysicalRegion](PhysicalRegion.md), [PhysicalParagraph](PhysicalParagraph.md), [PhysicalLine](PhysicalLine.md), [PhysicalWord](PhysicalWord.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 4 |
| Maximum Cardinality | 4 |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json $defs/coordinates; c on region, paragraph, line and token. |
| alto | ALTO 4.4 HPOS, VPOS, WIDTH, HEIGHT respectively on TextBlock, TextLine or String; Description/MeasurementUnit must be pixel and the image frame must agree. ALTO accepts floating-point measurements; this Impresso contract requires integers. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:physical_box |
| native | pc:physical_box |




## LinkML Source

<details>
```yaml
name: physical_box
annotations:
  impresso:
    tag: impresso
    value: page.schema.json $defs/coordinates; c on region, paragraph, line and token.
  alto:
    tag: alto
    value: ALTO 4.4 HPOS, VPOS, WIDTH, HEIGHT respectively on TextBlock, TextLine
      or String; Description/MeasurementUnit must be pixel and the image frame must
      agree. ALTO accepts floating-point measurements; this Impresso contract requires
      integers.
description: A box [x, y, width, height] in pixels of this page's picture, with origin
  at its upper left. Impresso requires exactly four integers, without a nonnegative
  or positive bound. It is an array, not an object with invented coordinate fields.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
alias: c
domain_of:
- PhysicalRegion
- PhysicalParagraph
- PhysicalLine
- PhysicalWord
range: integer
multivalued: true
minimum_cardinality: 4
maximum_cardinality: 4

```
</details></div>
