---
search:
  boost: 5.0
---

# Slot: mime 


_The file's media type, such as image/tiff._



<div data-search-exclude markdown="1">



URI: [pc:mime](https://pruzhany.org/ns/sourced-entities#mime)
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
| Regex Pattern | `^(?:image|audio|video|application)/[a-z0-9][a-z0-9.+-]*$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:mime |
| native | pc:mime |




## LinkML Source

<details>
```yaml
name: mime
description: The file's media type, such as image/tiff.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaMaster
domain_of:
- MediaMaster
range: string
required: true
pattern: ^(?:image|audio|video|application)/[a-z0-9][a-z0-9.+-]*$(?![\s\S])

```
</details></div>
