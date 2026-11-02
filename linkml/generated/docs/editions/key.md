---
search:
  boost: 5.0
---

# Slot: key 


_The edition's key: its date alone for the first paper, or the paper's code and a hyphen before that date for any other paper. Its date must equal date; the source register supplies the paper's code._



<div data-search-exclude markdown="1">



URI: [pc:key](https://pruzhany.org/ns/sourced-entities#key)
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


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:key |
| native | pc:key |




## LinkML Source

<details>
```yaml
name: key
description: 'The edition''s key: its date alone for the first paper, or the paper''s
  code and a hyphen before that date for any other paper. Its date must equal date;
  the source register supplies the paper''s code.'
from_schema: https://pruzhany.org/ns/editions
rank: 1000
owner: Edition
domain_of:
- Edition
range: string
required: true
pattern: ^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])

```
</details></div>
