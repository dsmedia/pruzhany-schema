---
search:
  boost: 5.0
---

# Slot: newspaper 


_The paper this page belongs to, by its id in the source register._



<div data-search-exclude markdown="1">



URI: [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [Page](Page.md) |
| Slot URI | [pc:site_newspaper](https://pruzhany.org/ns/sourced-entities#site_newspaper) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | The media alias carried by Impresso's canonical id. The pinned schemas have no separate media-alias property; site_newspaper keeps the source register id. |




### Schema Source


* from schema: https://pruzhany.org/ns/pages




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
  impresso:
    tag: impresso
    value: The media alias carried by Impresso's canonical id. The pinned schemas
      have no separate media-alias property; site_newspaper keeps the source register
      id.
description: The paper this page belongs to, by its id in the source register.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
slot_uri: pc:site_newspaper
owner: Page
domain_of:
- Page
range: NonBlankText
required: true

```
</details></div>
