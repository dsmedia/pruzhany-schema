---
search:
  boost: 5.0
---

# Slot: hebrew_date 


_The edition's date in the Hebrew calendar, written in Hebrew letters._



<div data-search-exclude markdown="1">



URI: [pc:hebrew_date](https://pruzhany.org/ns/sourced-entities#hebrew_date)
Alias: hebrewDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Edition](Edition.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Edition](Edition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:hebrew_date |
| native | pc:hebrew_date |




## LinkML Source

<details>
```yaml
name: hebrew_date
description: The edition's date in the Hebrew calendar, written in Hebrew letters.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: hebrewDate
owner: Edition
domain_of:
- Edition
range: string
required: true

```
</details></div>
