---
search:
  boost: 10.0
---

# Class: SuppliedTitle 


_A title supplied in English for a content item or section, with what it was made from, who made it and, where one was made, its later check._



<div data-search-exclude markdown="1">



URI: [rico:Title](https://www.ica.org/standards/RiC/ontology#Title)





```mermaid
 classDiagram
    class SuppliedTitle
    click SuppliedTitle href "../SuppliedTitle/"
      SuppliedTitle : attribution
        
          
    
        
        
        SuppliedTitle --> "1" Authorship : attribution
        click Authorship href "../Authorship/"
    

        
      SuppliedTitle : based_on
        
          
    
        
        
        SuppliedTitle --> "1" TextBasis : based_on
        click TextBasis href "../TextBasis/"
    

        
      SuppliedTitle : checked_against
        
          
    
        
        
        SuppliedTitle --> "0..1" TitleCheck : checked_against
        click TitleCheck href "../TitleCheck/"
    

        
      SuppliedTitle : language
        
      SuppliedTitle : text
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [rico:Title](https://www.ica.org/standards/RiC/ontology#Title) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [text](text.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The English title. | direct |
| [language](language.md) | 1 <br/> [String](String.md) | The title's language, always English (en). | direct |
| [based_on](based_on.md) | 1 <br/> [TextBasis](TextBasis.md) | The exact printed text the title was made from, and where it is printed. | direct |
| [attribution](attribution.md) | 1 <br/> [Authorship](Authorship.md) | Who wrote the title, and on which day. | direct |
| [checked_against](checked_against.md) | 0..1 <br/> [TitleCheck](TitleCheck.md) | A later check of this title against the reading, where one was made. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/site_common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:Title |
| native | pc:SuppliedTitle |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SuppliedTitle
description: A title supplied in English for a content item or section, with what
  it was made from, who made it and, where one was made, its later check.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
attributes:
  text:
    name: text
    description: The English title.
    from_schema: https://pruzhany.org/ns/site_common
    slot_uri: rico:textualValue
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    range: NonBlankText
    required: true
  language:
    name: language
    description: The title's language, always English (en).
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - SuppliedTitle
    - Translation
    - Source
    required: true
    equals_string: en
  based_on:
    name: based_on
    description: The exact printed text the title was made from, and where it is printed.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - SuppliedTitle
    - Translation
    range: TextBasis
    required: true
    inlined: true
  attribution:
    name: attribution
    description: Who wrote the title, and on which day.
    from_schema: https://pruzhany.org/ns/site_common
    domain_of:
    - EnglishCheck
    - SuppliedTitle
    - Translation
    - Fact
    - Name
    range: Authorship
    required: true
    inlined: true
  checked_against:
    name: checked_against
    description: A later check of this title against the reading, where one was made.
    from_schema: https://pruzhany.org/ns/site_common
    exact_mappings:
    - pc:site_checked_against_text
    rank: 1000
    domain_of:
    - SuppliedTitle
    - Translation
    range: TitleCheck
    inlined: true
class_uri: rico:Title

```
</details>

### Induced

<details>
```yaml
name: SuppliedTitle
description: A title supplied in English for a content item or section, with what
  it was made from, who made it and, where one was made, its later check.
from_schema: https://pruzhany.org/ns/site_common
rank: 1000
attributes:
  text:
    name: text
    description: The English title.
    from_schema: https://pruzhany.org/ns/site_common
    slot_uri: rico:textualValue
    owner: SuppliedTitle
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    range: NonBlankText
    required: true
  language:
    name: language
    description: The title's language, always English (en).
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: SuppliedTitle
    domain_of:
    - SuppliedTitle
    - Translation
    - Source
    range: string
    required: true
    equals_string: en
  based_on:
    name: based_on
    description: The exact printed text the title was made from, and where it is printed.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: SuppliedTitle
    domain_of:
    - SuppliedTitle
    - Translation
    range: TextBasis
    required: true
    inlined: true
  attribution:
    name: attribution
    description: Who wrote the title, and on which day.
    from_schema: https://pruzhany.org/ns/site_common
    owner: SuppliedTitle
    domain_of:
    - EnglishCheck
    - SuppliedTitle
    - Translation
    - Fact
    - Name
    range: Authorship
    required: true
    inlined: true
  checked_against:
    name: checked_against
    description: A later check of this title against the reading, where one was made.
    from_schema: https://pruzhany.org/ns/site_common
    exact_mappings:
    - pc:site_checked_against_text
    rank: 1000
    owner: SuppliedTitle
    domain_of:
    - SuppliedTitle
    - Translation
    range: TitleCheck
    inlined: true
class_uri: rico:Title

```
</details></div>
