---
search:
  boost: 5.0
---

# Slot: hebrew_month 


_The Hebrew month, by its number from 1 to 13, counted from Nisan._



<div data-search-exclude markdown="1">



URI: [pc:hebrew_month](https://pruzhany.org/ns/sourced-entities#hebrew_month)
Alias: hebrewMonth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Edition](Edition.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Edition](Edition.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 1 |
| Maximum Value | 13 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:hebrew_month |
| native | pc:hebrew_month |




## LinkML Source

<details>
```yaml
name: hebrew_month
description: The Hebrew month, by its number from 1 to 13, counted from Nisan.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: hebrewMonth
owner: Edition
domain_of:
- Edition
range: integer
required: true
minimum_value: 1
maximum_value: 13

```
</details></div>
