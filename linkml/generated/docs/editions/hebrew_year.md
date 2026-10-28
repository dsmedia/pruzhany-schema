---
search:
  boost: 5.0
---

# Slot: hebrew_year 


_The Hebrew year, such as 5699._



<div data-search-exclude markdown="1">



URI: [pc:hebrew_year](https://pruzhany.org/ns/sourced-entities#hebrew_year)
Alias: hebrewYear

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
| Minimum Value | -9007199254740991 |
| Maximum Value | 9007199254740991 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:hebrew_year |
| native | pc:hebrew_year |




## LinkML Source

<details>
```yaml
name: hebrew_year
description: The Hebrew year, such as 5699.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
alias: hebrewYear
owner: Edition
domain_of:
- Edition
range: integer
required: true
minimum_value: -9007199254740991
maximum_value: 9007199254740991

```
</details></div>
