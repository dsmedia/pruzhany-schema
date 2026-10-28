---
search:
  boost: 5.0
---

# Slot: private 


_True when the document itself is never shown._



<div data-search-exclude markdown="1">



URI: [pc:private](https://pruzhany.org/ns/sourced-entities#private)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Source](Source.md) | A record the statements rest on: a book, an archive's database, a family document, the paper itself and the like, registered once and cited by its id. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Source](Source.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Source](Source.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:private |
| native | pc:private |
| related | pc:site_source_privacy |




## LinkML Source

<details>
```yaml
name: private
description: True when the document itself is never shown.
from_schema: https://pruzhany.org/ns/shared_record
related_mappings:
- pc:site_source_privacy
rank: 1000
owner: Source
domain_of:
- Source
range: boolean

```
</details></div>
