---
search:
  boost: 5.0
---

# Slot: image_uri 


_The page picture the box is on, by its name or address._



<div data-search-exclude markdown="1">



URI: [pc:image_uri](https://pruzhany.org/ns/sourced-entities#image_uri)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrintedAddress](PrintedAddress.md) | Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [PrintedAddress](PrintedAddress.md) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PrintedAddress](PrintedAddress.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:image_uri |
| native | pc:image_uri |




## LinkML Source

<details>
```yaml
name: image_uri
description: The page picture the box is on, by its name or address.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
owner: PrintedAddress
domain_of:
- PrintedAddress
range: NonBlankText
required: true

```
</details></div>
