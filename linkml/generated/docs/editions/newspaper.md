---
search:
  boost: 5.0
---

# Slot: newspaper 


_The paper this edition belongs to, by its id in the source register._



<div data-search-exclude markdown="1">



URI: [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Edition](Edition.md) |
| Slot URI | [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Edition](Edition.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| references | Newspaper.id |
| impresso | The media alias carried by Impresso's canonical id. The pinned schemas have no separate media-alias property; site_newspaper keeps the source register id. |




### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:site_newspaper |
| native | pc:newspaper |




## LinkML Source

<details>
```yaml
name: newspaper
annotations:
  references:
    tag: references
    value: Newspaper.id
  impresso:
    tag: impresso
    value: The media alias carried by Impresso's canonical id. The pinned schemas
      have no separate media-alias property; site_newspaper keeps the source register
      id.
description: The paper this edition belongs to, by its id in the source register.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: pc:site_newspaper
owner: Edition
domain_of:
- Edition
range: NonBlankText
required: true

```
</details></div>
