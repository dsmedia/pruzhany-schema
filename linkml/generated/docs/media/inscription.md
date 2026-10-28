---
search:
  boost: 5.0
---

# Slot: inscription 


_The object's own words, such as writing on the back of a photograph._



<div data-search-exclude markdown="1">



URI: [pc:media_inscription](https://pruzhany.org/ns/sourced-entities#media_inscription)
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
| Range | [MediaText](MediaText.md) |
| Domain Of | [PublicMedia](PublicMedia.md) |
| Slot URI | [pc:media_inscription](https://pruzhany.org/ns/sourced-entities#media_inscription) |
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
| self | pc:media_inscription |
| native | pc:inscription |




## LinkML Source

<details>
```yaml
name: inscription
description: The object's own words, such as writing on the back of a photograph.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:media_inscription
owner: PublicMedia
domain_of:
- PublicMedia
range: MediaText
inlined: true

```
</details></div>
