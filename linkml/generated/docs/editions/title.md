---
search:
  boost: 5.0
---

# Slot: title 


_The paper's title as the site shows it._



<div data-search-exclude markdown="1">



URI: [rico:title](https://www.ica.org/standards/RiC/ontology#title)
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
| Slot URI | [rico:title](https://www.ica.org/standards/RiC/ontology#title) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Newspaper](Newspaper.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:title |
| native | pc:title |




## LinkML Source

<details>
```yaml
name: title
description: The paper's title as the site shows it.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: rico:title
owner: Newspaper
domain_of:
- Newspaper
range: NonBlankText
required: true

```
</details></div>
