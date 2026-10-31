---
search:
  boost: 5.0
---

# Slot: kind 


_Whether a person or a model wrote it._



<div data-search-exclude markdown="1">



URI: [pc:kind](https://pruzhany.org/ns/sourced-entities#kind)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Authorship](Authorship.md) | Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AuthorshipKind](AuthorshipKind.md) |
| Domain Of | [Authorship](Authorship.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Authorship](Authorship.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:kind |
| native | pc:kind |




## LinkML Source

<details>
```yaml
name: kind
description: Whether a person or a model wrote it.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: Authorship
domain_of:
- Authorship
range: AuthorshipKind
required: true

```
</details></div>
