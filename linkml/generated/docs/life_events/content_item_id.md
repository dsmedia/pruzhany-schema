---
search:
  boost: 5.0
---

# Slot: content_item_id 


_The content item, by its id in the content items document._



<div data-search-exclude markdown="1">



URI: [pc:content_item_id](https://pruzhany.org/ns/sourced-entities#content_item_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ContentItemRef](ContentItemRef.md) | A content item that prints a life event, and the part it plays: the announcement itself, a greeting, a condolence, a mention or an advertisement. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [ContentItemRef](ContentItemRef.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ContentItemRef](ContentItemRef.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:content_item_id |
| native | pc:content_item_id |




## LinkML Source

<details>
```yaml
name: content_item_id
description: The content item, by its id in the content items document.
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
owner: ContentItemRef
domain_of:
- ContentItemRef
range: NonBlankText
required: true

```
</details></div>
