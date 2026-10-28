---
search:
  boost: 5.0
---

# Slot: rights 


_The rights statement or licence that applies, by its address; when absent, copyright not evaluated._



<div data-search-exclude markdown="1">



URI: [pc:media_rights](https://pruzhany.org/ns/sourced-entities#media_rights)
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
| Slot URI | [pc:media_rights](https://pruzhany.org/ns/sourced-entities#media_rights) |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PublicMedia](PublicMedia.md) |


<details>
<summary>Additional Constraints</summary>
**Must Be One Of:** http://rightsstatements.org/vocab/InC/1.0/, http://rightsstatements.org/vocab/InC-OW-EU/1.0/, http://rightsstatements.org/vocab/InC-EDU/1.0/, http://rightsstatements.org/vocab/InC-NC/1.0/, http://rightsstatements.org/vocab/InC-RUU/1.0/, http://rightsstatements.org/vocab/NoC-CR/1.0/, http://rightsstatements.org/vocab/NoC-NC/1.0/, http://rightsstatements.org/vocab/NoC-OKLR/1.0/, http://rightsstatements.org/vocab/NoC-US/1.0/, http://rightsstatements.org/vocab/CNE/1.0/, http://rightsstatements.org/vocab/UND/1.0/, http://rightsstatements.org/vocab/NKC/1.0/, https://creativecommons.org/licenses/by/4.0/, https://creativecommons.org/licenses/by-sa/4.0/, https://creativecommons.org/licenses/by-nd/4.0/, https://creativecommons.org/licenses/by-nc/4.0/, https://creativecommons.org/licenses/by-nc-sa/4.0/, https://creativecommons.org/licenses/by-nc-nd/4.0/, https://creativecommons.org/publicdomain/zero/1.0/, https://creativecommons.org/publicdomain/mark/1.0/

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:media_rights |
| native | pc:rights |




## LinkML Source

<details>
```yaml
name: rights
description: The rights statement or licence that applies, by its address; when absent,
  copyright not evaluated.
from_schema: https://pruzhany.org/ns/media
rank: 1000
slot_uri: pc:media_rights
owner: PublicMedia
domain_of:
- PublicMedia
range: string
equals_string_in:
- http://rightsstatements.org/vocab/InC/1.0/
- http://rightsstatements.org/vocab/InC-OW-EU/1.0/
- http://rightsstatements.org/vocab/InC-EDU/1.0/
- http://rightsstatements.org/vocab/InC-NC/1.0/
- http://rightsstatements.org/vocab/InC-RUU/1.0/
- http://rightsstatements.org/vocab/NoC-CR/1.0/
- http://rightsstatements.org/vocab/NoC-NC/1.0/
- http://rightsstatements.org/vocab/NoC-OKLR/1.0/
- http://rightsstatements.org/vocab/NoC-US/1.0/
- http://rightsstatements.org/vocab/CNE/1.0/
- http://rightsstatements.org/vocab/UND/1.0/
- http://rightsstatements.org/vocab/NKC/1.0/
- https://creativecommons.org/licenses/by/4.0/
- https://creativecommons.org/licenses/by-sa/4.0/
- https://creativecommons.org/licenses/by-nd/4.0/
- https://creativecommons.org/licenses/by-nc/4.0/
- https://creativecommons.org/licenses/by-nc-sa/4.0/
- https://creativecommons.org/licenses/by-nc-nd/4.0/
- https://creativecommons.org/publicdomain/zero/1.0/
- https://creativecommons.org/publicdomain/mark/1.0/

```
</details></div>
