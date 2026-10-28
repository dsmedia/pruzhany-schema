---
search:
  boost: 5.0
---

# Slot: kind 


_What the medium is: image, audio, video or document._



<div data-search-exclude markdown="1">



URI: [rico:hasRepresentationType](https://www.ica.org/standards/RiC/ontology#hasRepresentationType)
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
| Range | [MediaKind](MediaKind.md) |
| Domain Of | [PublicMedia](PublicMedia.md) |
| Slot URI | [rico:hasRepresentationType](https://www.ica.org/standards/RiC/ontology#hasRepresentationType) |
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
| self | rico:hasRepresentationType |
| native | pc:kind |




## LinkML Source

<details>
```yaml
name: kind
description: 'What the medium is: image, audio, video or document.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: rico:hasRepresentationType
owner: PublicMedia
domain_of:
- PublicMedia
range: MediaKind
required: true

```
</details></div>
