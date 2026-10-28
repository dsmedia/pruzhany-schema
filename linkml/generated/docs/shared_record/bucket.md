---
search:
  boost: 5.0
---

# Slot: bucket 


_The private storage bucket, apart from the page pictures' bucket._



<div data-search-exclude markdown="1">



URI: [pc:bucket](https://pruzhany.org/ns/sourced-entities#bucket)
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
| Regex Pattern | `^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:bucket |
| native | pc:bucket |




## LinkML Source

<details>
```yaml
name: bucket
description: The private storage bucket, apart from the page pictures' bucket.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
owner: MediaMaster
domain_of:
- MediaMaster
range: string
required: true
pattern: ^[a-z0-9][a-z0-9-]{1,61}[a-z0-9]$(?![\s\S])

```
</details></div>
