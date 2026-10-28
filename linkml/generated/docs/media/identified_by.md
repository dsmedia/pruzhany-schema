---
search:
  boost: 5.0
---

# Slot: identified_by 


_What identifies the person: the family, a record, or the picture's inscription._



<div data-search-exclude markdown="1">



URI: [pc:identified_by](https://pruzhany.org/ns/sourced-entities#identified_by)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaDepicted](MediaDepicted.md) | One person a picture shows, identified or not, where in the picture, and on whose identification. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaIdentifiedBy](MediaIdentifiedBy.md) |
| Domain Of | [MediaDepicted](MediaDepicted.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaDepicted](MediaDepicted.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:identified_by |
| native | pc:identified_by |




## LinkML Source

<details>
```yaml
name: identified_by
description: 'What identifies the person: the family, a record, or the picture''s
  inscription.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaDepicted
domain_of:
- MediaDepicted
range: MediaIdentifiedBy
required: true

```
</details></div>
