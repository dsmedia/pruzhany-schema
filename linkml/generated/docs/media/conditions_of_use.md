---
search:
  boost: 5.0
---

# Slot: conditions_of_use 


_The holder's terms of use, as written, with no permission inferred from them._



<div data-search-exclude markdown="1">



URI: [rico:conditionsOfUse](https://www.ica.org/standards/RiC/ontology#conditionsOfUse)
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
| Range | [NonBlankText](NonBlankText.md) |
| Domain Of | [PublicMedia](PublicMedia.md) |
| Slot URI | [rico:conditionsOfUse](https://www.ica.org/standards/RiC/ontology#conditionsOfUse) |
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
| self | rico:conditionsOfUse |
| native | pc:conditions_of_use |




## LinkML Source

<details>
```yaml
name: conditions_of_use
description: The holder's terms of use, as written, with no permission inferred from
  them.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: rico:conditionsOfUse
owner: PublicMedia
domain_of:
- PublicMedia
range: NonBlankText

```
</details></div>
