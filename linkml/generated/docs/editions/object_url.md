---
search:
  boost: 5.0
---

# Slot: object_url 


_The holder's descriptive page for this one issue._



<div data-search-exclude markdown="1">



URI: [pc:holding_object_url](https://pruzhany.org/ns/sourced-entities#holding_object_url)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Edition](Edition.md) | One edition of the paper: its date in the common calendar and in the Hebrew one, and the holiday it falls on, if any. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Edition](Edition.md) |
| Slot URI | [pc:holding_object_url](https://pruzhany.org/ns/sourced-entities#holding_object_url) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Edition](Edition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:holding_object_url |
| native | pc:object_url |
| close | rdfs:seeAlso |




## LinkML Source

<details>
```yaml
name: object_url
description: The holder's descriptive page for this one issue.
from_schema: https://pruzhany.org/ns/editions
close_mappings:
- rdfs:seeAlso
rank: 1000
slot_uri: pc:holding_object_url
owner: Edition
domain_of:
- Edition
range: uri

```
</details></div>
