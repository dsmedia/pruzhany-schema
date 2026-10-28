---
search:
  boost: 5.0
---

# Slot: transcript 


_A document's full text; required for documents._



<div data-search-exclude markdown="1">



URI: [pc:media_transcript](https://pruzhany.org/ns/sourced-entities#media_transcript)
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
| Slot URI | [pc:media_transcript](https://pruzhany.org/ns/sourced-entities#media_transcript) |
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
| self | pc:media_transcript |
| native | pc:transcript |




## LinkML Source

<details>
```yaml
name: transcript
description: A document's full text; required for documents.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:media_transcript
owner: PublicMedia
domain_of:
- PublicMedia
range: MediaText
inlined: true

```
</details></div>
