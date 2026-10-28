---
search:
  boost: 5.0
---

# Slot: addresses 


_Where on the page pictures the quoted words are printed._



<div data-search-exclude markdown="1">



URI: [pc:addresses](https://pruzhany.org/ns/sourced-entities#addresses)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SiteCitation](SiteCitation.md) | A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrintedAddress](PrintedAddress.md) |
| Domain Of | [SiteCitation](SiteCitation.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
| Minimum Cardinality | 1 |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SiteCitation](SiteCitation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:addresses |
| native | pc:addresses |




## LinkML Source

<details>
```yaml
name: addresses
description: Where on the page pictures the quoted words are printed.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: SiteCitation
domain_of:
- SiteCitation
range: PrintedAddress
multivalued: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details></div>
