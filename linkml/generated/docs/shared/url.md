---
search:
  boost: 5.0
---

# Slot: url 


_The record's address; null for a citation of evidence that was looked for and not found._



<div data-search-exclude markdown="1">



URI: [pc:url](https://pruzhany.org/ns/sourced-entities#url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalReference](ExternalReference.md) | A reference to a record in an outside database or resource, such as a page of testimony at Yad Vashem. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ExternalReference](ExternalReference.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ExternalReference](ExternalReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:url |
| native | pc:url |




## LinkML Source

<details>
```yaml
name: url
description: The record's address; null for a citation of evidence that was looked
  for and not found.
from_schema: https://pruzhany.org/ns/shared
rank: 1000
owner: ExternalReference
domain_of:
- ExternalReference
range: string

```
</details></div>
