---
search:
  boost: 10.0
---

# Class: CitedTextBasis 


_The exact source words of a citation or source title. The containing citation's locator or source description locates them; printed addresses are optional, and when supplied remain nonempty real image-and-box witnesses._



<div data-search-exclude markdown="1">



URI: [pc:CitedTextBasis](https://pruzhany.org/ns/sourced-entities#CitedTextBasis)





```mermaid
 classDiagram
    class CitedTextBasis
    click CitedTextBasis href "../CitedTextBasis/"
      TextBasis <|-- CitedTextBasis
        click TextBasis href "../TextBasis/"
      
      CitedTextBasis : addresses
        
          
    
        
        
        CitedTextBasis --> "1..*" PrintedAddress : addresses
        click PrintedAddress href "../PrintedAddress/"
    

        
      CitedTextBasis : source_text
        
      
```





## Inheritance
* [TextBasis](TextBasis.md)
    * **CitedTextBasis**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [source_text](source_text.md) | 1 <br/> [String](String.md) | The text used, exactly, never normalised or replaced by a later reading. | [TextBasis](TextBasis.md) |
| [addresses](addresses.md) | 1..* <br/> [PrintedAddress](PrintedAddress.md) | Where that text is printed, one address a line or patch. | [TextBasis](TextBasis.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CitedTranslation](CitedTranslation.md) | [based_on](based_on.md) | range | [CitedTextBasis](CitedTextBasis.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:CitedTextBasis |
| native | pc:CitedTextBasis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CitedTextBasis
description: The exact source words of a citation or source title. The containing
  citation's locator or source description locates them; printed addresses are optional,
  and when supplied remain nonempty real image-and-box witnesses.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
is_a: TextBasis
slot_usage:
  addresses:
    name: addresses
    required: false

```
</details>

### Induced

<details>
```yaml
name: CitedTextBasis
description: The exact source words of a citation or source title. The containing
  citation's locator or source description locates them; printed addresses are optional,
  and when supplied remain nonempty real image-and-box witnesses.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
is_a: TextBasis
slot_usage:
  addresses:
    name: addresses
    required: false
attributes:
  source_text:
    name: source_text
    description: The text used, exactly, never normalised or replaced by a later reading.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: CitedTextBasis
    domain_of:
    - TextBasis
    range: string
    required: true
  addresses:
    name: addresses
    description: Where that text is printed, one address a line or patch.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: CitedTextBasis
    domain_of:
    - TextBasis
    - PrintedTitle
    range: PrintedAddress
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1

```
</details></div>
