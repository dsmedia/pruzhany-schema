---
search:
  boost: 5.0
---

# Slot: bytes 


_The file's size in bytes._



<div data-search-exclude markdown="1">



URI: [pc:bytes](https://pruzhany.org/ns/sourced-entities#bytes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaMaster](MediaMaster.md) | Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PositiveInteger](PositiveInteger.md) |
| Domain Of | [MediaMaster](MediaMaster.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaMaster](MediaMaster.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:bytes |
| native | pc:bytes |




## LinkML Source

<details>
```yaml
name: bytes
description: The file's size in bytes.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaMaster
domain_of:
- MediaMaster
range: PositiveInteger
required: true

```
</details></div>
