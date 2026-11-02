---
search:
  boost: 5.0
---

# Slot: id 


_The paper's source-register id, the same value as Edition.newspaper._



<div data-search-exclude markdown="1">



URI: [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper)
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
| Slot URI | [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper) |
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
| self | pc:site_newspaper |
| native | pc:id |




## LinkML Source

<details>
```yaml
name: id
description: The paper's source-register id, the same value as Edition.newspaper.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: pc:site_newspaper
owner: Newspaper
domain_of:
- Newspaper
range: NonBlankText
required: true

```
</details></div>
