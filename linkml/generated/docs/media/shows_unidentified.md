---
search:
  boost: 5.0
---

# Slot: shows_unidentified 


_True when the picture shows people not identified._



<div data-search-exclude markdown="1">



URI: [pc:media_shows_unidentified](https://pruzhany.org/ns/sourced-entities#media_shows_unidentified)
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
| Range | [Boolean](Boolean.md) |
| Domain Of | [PublicMedia](PublicMedia.md) |
| Slot URI | [pc:media_shows_unidentified](https://pruzhany.org/ns/sourced-entities#media_shows_unidentified) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PublicMedia](PublicMedia.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_shows_unidentified |
| native | pc:shows_unidentified |




## LinkML Source

<details>
```yaml
name: shows_unidentified
description: True when the picture shows people not identified.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:media_shows_unidentified
owner: PublicMedia
domain_of:
- PublicMedia
range: boolean
required: true

```
</details></div>
