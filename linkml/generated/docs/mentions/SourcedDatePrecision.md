---
search:
  boost: 2.0
---


# Enum: SourcedDatePrecision 




_How much of a sourced date is known: its year, its month, its day, or a range._



<div data-search-exclude markdown="1">

URI: [pc:SourcedDatePrecision](https://pruzhany.org/ns/sourced-entities#SourcedDatePrecision)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| year | None | Only the year is known; the start is written YYYY. |
| month | None | The year and month are known; the start is written YYYY-MM. |
| day | None | The day is known; the start is written YYYY-MM-DD. |
| range | None | The date lies between a start and an end. |




## Slots

| Name | Description |
| ---  | --- |
| [precision](precision.md) | How much of the date is known: year, month, day or range. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: SourcedDatePrecision
description: 'How much of a sourced date is known: its year, its month, its day, or
  a range.'
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  year:
    text: year
    description: Only the year is known; the start is written YYYY.
  month:
    text: month
    description: The year and month are known; the start is written YYYY-MM.
  day:
    text: day
    description: The day is known; the start is written YYYY-MM-DD.
  range:
    text: range
    description: The date lies between a start and an end.

```
</details>

</div>
