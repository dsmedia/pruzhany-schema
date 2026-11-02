---
search:
  boost: 5.0
---

# Slot: code 


_The paper's lowercase alphabetic code used in site keys and routes._



<div data-search-exclude markdown="1">



URI: [pc:newspaper_code](https://pruzhany.org/ns/sourced-entities#newspaper_code)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Newspaper](Newspaper.md) | One newspaper in the source register, with its site title, code and default picture credit. A page may supply a different credit through picture_source. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Newspaper](Newspaper.md) |
| Slot URI | [pc:newspaper_code](https://pruzhany.org/ns/sourced-entities#newspaper_code) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Newspaper](Newspaper.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[a-z]+$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:newspaper_code |
| native | pc:code |




## LinkML Source

<details>
```yaml
name: code
description: The paper's lowercase alphabetic code used in site keys and routes.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: pc:newspaper_code
owner: Newspaper
domain_of:
- Newspaper
range: NonBlankText
required: true
pattern: ^[a-z]+$(?![\s\S])

```
</details></div>
