---
search:
  boost: 5.0
---

# Slot: image_service 


_The base URI of the holder's IIIF Image API 3 service for this page's picture, without /info.json or a trailing slash. It is the holder's service, never ours; image_uri remains the picture shown on the page. A manifest may attach this service to that image so viewers can request further sizes and regions._



<div data-search-exclude markdown="1">



URI: [pc:image_service](https://pruzhany.org/ns/sourced-entities#image_service)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Page](Page.md) | One printed page of the issue: its picture, its size and its regions of print. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Page](Page.md) |
| Slot URI | [pc:image_service](https://pruzhany.org/ns/sourced-entities#image_service) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Page](Page.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/pages




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:image_service |
| native | pc:image_service |




## LinkML Source

<details>
```yaml
name: image_service
description: The base URI of the holder's IIIF Image API 3 service for this page's
  picture, without /info.json or a trailing slash. It is the holder's service, never
  ours; image_uri remains the picture shown on the page. A manifest may attach this
  service to that image so viewers can request further sizes and regions.
from_schema: https://pruzhany.org/ns/pages
rank: 1000
slot_uri: pc:image_service
owner: Page
domain_of:
- Page
range: uri

```
</details></div>
