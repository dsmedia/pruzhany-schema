---
search:
  boost: 5.0
---

# Slot: note 


_A note on how or why._



<div data-search-exclude markdown="1">



URI: [pc:note](https://pruzhany.org/ns/sourced-entities#note)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Attribution](Attribution.md) | Who made or allowed something, on what day, with an optional note. |  no  |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Attribution](Attribution.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Attribution](Attribution.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:note |
| native | pc:note |




## LinkML Source

<details>
```yaml
name: note
description: A note on how or why.
from_schema: https://pruzhany.org/ns/mentions
rank: 1000
owner: Attribution
domain_of:
- Attribution
range: string

```
</details></div>
