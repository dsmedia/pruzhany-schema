---
search:
  boost: 5.0
---

# Slot: scan 


_The scan or image cited._



<div data-search-exclude markdown="1">



URI: [pc:scan](https://pruzhany.org/ns/sourced-entities#scan)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |
| [Citation](Citation.md) | Where in one source a statement's evidence lies: the source, and the record, page, scan, time, piece of the paper, address or pointer within it, with the quoted words. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Citation](Citation.md) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Citation](Citation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:scan |
| native | pc:scan |




## LinkML Source

<details>
```yaml
name: scan
description: The scan or image cited.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: Citation
domain_of:
- Citation
range: string

```
</details></div>
