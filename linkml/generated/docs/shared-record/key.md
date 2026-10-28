---
search:
  boost: 5.0
---

# Slot: key 


_The file's key in the bucket, whose last part is its SHA-256 digest._



<div data-search-exclude markdown="1">



URI: [pc:key](https://pruzhany.org/ns/sourced-entities#key)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaMaster](MediaMaster.md) | Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MediaMaster](MediaMaster.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MediaMaster](MediaMaster.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(?:[a-z0-9_-]+/)*[0-9a-f]{64}$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:key |
| native | pc:key |




## LinkML Source

<details>
```yaml
name: key
description: The file's key in the bucket, whose last part is its SHA-256 digest.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaMaster
domain_of:
- MediaMaster
range: string
required: true
pattern: ^(?:[a-z0-9_-]+/)*[0-9a-f]{64}$(?![\s\S])

```
</details></div>
