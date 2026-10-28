---
search:
  boost: 2.0
---


# Enum: PrintedCalendar 




_The calendar a date was printed or written in._



<div data-search-exclude markdown="1">

URI: [pc:PrintedCalendar](https://pruzhany.org/ns/sourced-entities#PrintedCalendar)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| gregorian | None | The Gregorian calendar. |
| hebrew | None | The Hebrew calendar; its words are kept as printed and never converted. |




## Slots

| Name | Description |
| ---  | --- |
| [printed_calendar](printed_calendar.md) | The calendar of the printed words. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions






## LinkML Source

<details>
```yaml
name: PrintedCalendar
description: The calendar a date was printed or written in.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
permissible_values:
  gregorian:
    text: gregorian
    description: The Gregorian calendar.
  hebrew:
    text: hebrew
    description: The Hebrew calendar; its words are kept as printed and never converted.

```
</details>

</div>
