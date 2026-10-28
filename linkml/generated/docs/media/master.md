---
search:
  boost: 5.0
---

# Slot: master 


_Where the private master file is kept; never public._



<div data-search-exclude markdown="1">



URI: [pc:media_master](https://pruzhany.org/ns/sourced-entities#media_master)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Media](Media.md) | One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MediaMaster](MediaMaster.md) |
| Domain Of | [Media](Media.md) |
| Slot URI | [pc:media_master](https://pruzhany.org/ns/sourced-entities#media_master) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Media](Media.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_master |
| native | pc:master |




## LinkML Source

<details>
```yaml
name: master
description: Where the private master file is kept; never public.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:media_master
owner: Media
domain_of:
- Media
range: MediaMaster
inlined: true

```
</details></div>
