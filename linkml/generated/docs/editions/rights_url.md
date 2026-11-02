---
search:
  boost: 5.0
---

# Slot: rights_url 


_The address where the rights statement was read._



<div data-search-exclude markdown="1">



URI: [pc:picture_rights_url](https://pruzhany.org/ns/sourced-entities#picture_rights_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Newspaper](Newspaper.md) | One newspaper in the source register, with its site title, code and default picture credit. A page may supply a different credit through picture_source. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Newspaper](Newspaper.md) |
| Slot URI | [pc:picture_rights_url](https://pruzhany.org/ns/sourced-entities#picture_rights_url) |
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
| self | pc:picture_rights_url |
| native | pc:rights_url |




## LinkML Source

<details>
```yaml
name: rights_url
description: The address where the rights statement was read.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
slot_uri: pc:picture_rights_url
owner: Newspaper
domain_of:
- Newspaper
range: uri

```
</details></div>
