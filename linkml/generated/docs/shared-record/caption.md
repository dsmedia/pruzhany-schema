---
search:
  boost: 5.0
---

# Slot: caption 


_The caption the site shows, with its language and review._



<div data-search-exclude markdown="1">



URI: [pc:media_caption](https://pruzhany.org/ns/sourced-entities#media_caption)
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
| Slot URI | [pc:media_caption](https://pruzhany.org/ns/sourced-entities#media_caption) |
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


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_caption |
| native | pc:caption |




## LinkML Source

<details>
```yaml
name: caption
description: The caption the site shows, with its language and review.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: pc:media_caption
owner: PublicMedia
domain_of:
- PublicMedia
range: MediaText
required: true
inlined: true

```
</details></div>
