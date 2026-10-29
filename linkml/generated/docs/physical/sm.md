---
search:
  boost: 5.0
---

# Slot: sm 


_Original source medium; present together with st._



<div data-search-exclude markdown="1">



URI: [pc:sm](https://pruzhany.org/ns/sourced-entities#sm)
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
**Must Be One Of:** print, typescript

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| impresso | page.schema.json sm. |
| alto | No direct equivalent; Page/@PAGECLASS is user-defined, not this enumeration. |




### Schema Source


* from schema: https://pruzhany.org/ns/physical




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:sm |
| native | pc:sm |




## LinkML Source

<details>
```yaml
name: sm
annotations:
  impresso:
    tag: impresso
    value: page.schema.json sm.
  alto:
    tag: alto
    value: No direct equivalent; Page/@PAGECLASS is user-defined, not this enumeration.
description: Original source medium; present together with st.
from_schema: https://pruzhany.org/ns/physical
rank: 1000
owner: PhysicalPage
domain_of:
- PhysicalPage
range: string
equals_string_in:
- print
- typescript

```
</details></div>
