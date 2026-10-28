---
search:
  boost: 5.0
---

# Slot: link 


_For sound or film: the page on the holder's own host where it can be heard or seen._



<div data-search-exclude markdown="1">



URI: [pc:media_link](https://pruzhany.org/ns/sourced-entities#media_link)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PublicMedia](PublicMedia.md) | One held or linked copy of a registered source (a photograph, document, recording or film), as the public may see it: what it is, what it shows and says, its review, its terms and its served copies. |  no  |
| [Media](Media.md) | One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PublicMedia](PublicMedia.md) |
| Slot URI | [pc:media_link](https://pruzhany.org/ns/sourced-entities#media_link) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PublicMedia](PublicMedia.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$(?![\s\S])` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_link |
| native | pc:link |




## LinkML Source

<details>
```yaml
name: link
description: 'For sound or film: the page on the holder''s own host where it can be
  heard or seen.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:media_link
owner: PublicMedia
domain_of:
- PublicMedia
range: string
pattern: ^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$(?![\s\S])

```
</details></div>
