---
search:
  boost: 5.0
---

# Slot: st 


_Media source type; present together with sm. Newspaper requires print; radio_broadcast requires typescript._



<div data-search-exclude markdown="1">



URI: [pc:st](https://pruzhany.org/ns/sourced-entities#st)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicalPage](PhysicalPage.md) | One Impresso page file, with its picture metadata and physical text hierarchy. Impresso allows unknown properties at every object level; no such properties are defined here. Exactly one image key and at least one timestamp key must be present. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhysicalPage](PhysicalPage.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhysicalPage](PhysicalPage.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** newspaper, radio_broadcast, radio_magazine, radio_schedule, monograph, encyclopedia

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json st, SourceType values. |
| alto | No direct ALTO page attribute for this source classification. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:st |
| native | pc:st |




## LinkML Source

<details>
```yaml
name: st
annotations:
  impresso:
    tag: impresso
    value: page.schema.json st, SourceType values.
  alto:
    tag: alto
    value: No direct ALTO page attribute for this source classification.
description: Media source type; present together with sm. Newspaper requires print;
  radio_broadcast requires typescript.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string
equals_string_in:
- newspaper
- radio_broadcast
- radio_magazine
- radio_schedule
- monograph
- encyclopedia

```
</details></div>
