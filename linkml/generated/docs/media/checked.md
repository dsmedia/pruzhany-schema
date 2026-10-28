---
search:
  boost: 5.0
---

# Slot: checked 


_The last dated check of the file's digest._



<div data-search-exclude markdown="1">



URI: [pc:checked](https://pruzhany.org/ns/sourced-entities#checked)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MediaMaster](MediaMaster.md) | Where a medium's private master file is kept: its bucket, its key named by its digest, its digest, its type, its size and its last check. Never public. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaFixity](MediaFixity.md) |
| Domain Of | [MediaMaster](MediaMaster.md) |
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
| self | pc:checked |
| native | pc:checked |




## LinkML Source

<details>
```yaml
name: checked
description: The last dated check of the file's digest.
from_schema: https://pruzhany.org/ns/media
rank: 1000
owner: MediaMaster
domain_of:
- MediaMaster
range: MediaFixity
inlined: true

```
</details></div>
