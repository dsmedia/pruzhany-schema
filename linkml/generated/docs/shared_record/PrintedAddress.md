---
search:
  boost: 10.0
---

# Class: PrintedAddress 


_Where some printed words stand: the page picture, a box on it in the picture's own pixels, and the words read in that box._



<div data-search-exclude markdown="1">



URI: [pc:PrintedAddress](https://pruzhany.org/ns/sourced-entities#PrintedAddress)





```mermaid
 classDiagram
    class PrintedAddress
    click PrintedAddress href "../PrintedAddress/"
      PrintedAddress : bbox
        
      PrintedAddress : image_uri
        
      PrintedAddress : text
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [image_uri](image_uri.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The page picture the box is on, by its name or address. | direct |
| [bbox](bbox.md) | 1..* <br/> [NonNegativeNumber](NonNegativeNumber.md) | The box on the picture: left, top, width and height, in the picture's pixels. | direct |
| [text](text.md) | 1 <br/> [String](String.md) | The words read in the box, exactly as read; empty for a patch with no readable line. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SiteCitation](SiteCitation.md) | [addresses](addresses.md) | range | [PrintedAddress](PrintedAddress.md) |
| [TextBasis](TextBasis.md) | [addresses](addresses.md) | range | [PrintedAddress](PrintedAddress.md) |
| [PrintedTitle](PrintedTitle.md) | [addresses](addresses.md) | range | [PrintedAddress](PrintedAddress.md) |
| [CitedTextBasis](CitedTextBasis.md) | [addresses](addresses.md) | range | [PrintedAddress](PrintedAddress.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:PrintedAddress |
| native | pc:PrintedAddress |
| exact | pc:site_printed_address |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PrintedAddress
description: 'Where some printed words stand: the page picture, a box on it in the
  picture''s own pixels, and the words read in that box.'
from_schema: https://pruzhany.org/ns/shared_record
exact_mappings:
- pc:site_printed_address
rank: 1000
attributes:
  image_uri:
    name: image_uri
    description: The page picture the box is on, by its name or address.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - PrintedAddress
    range: NonBlankText
    required: true
  bbox:
    name: bbox
    description: 'The box on the picture: left, top, width and height, in the picture''s
      pixels.'
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - PrintedAddress
    range: NonNegativeNumber
    required: true
    multivalued: true
    minimum_cardinality: 4
    maximum_cardinality: 4
  text:
    name: text
    description: The words read in the box, exactly as read; empty for a patch with
      no readable line.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    - MediaText
    required: true

```
</details>

### Induced

<details>
```yaml
name: PrintedAddress
description: 'Where some printed words stand: the page picture, a box on it in the
  picture''s own pixels, and the words read in that box.'
from_schema: https://pruzhany.org/ns/shared_record
exact_mappings:
- pc:site_printed_address
rank: 1000
attributes:
  image_uri:
    name: image_uri
    description: The page picture the box is on, by its name or address.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: PrintedAddress
    domain_of:
    - PrintedAddress
    range: NonBlankText
    required: true
  bbox:
    name: bbox
    description: 'The box on the picture: left, top, width and height, in the picture''s
      pixels.'
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: PrintedAddress
    domain_of:
    - PrintedAddress
    range: NonNegativeNumber
    required: true
    multivalued: true
    minimum_cardinality: 4
    maximum_cardinality: 4
  text:
    name: text
    description: The words read in the box, exactly as read; empty for a patch with
      no readable line.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: PrintedAddress
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    - MediaText
    range: string
    required: true

```
</details></div>
