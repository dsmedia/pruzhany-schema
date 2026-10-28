---
search:
  boost: 10.0
---

# Class: Translation 


_An English translation of a content item's printed text, with the exact text it was made from, who made it and, where one was made, its later check._



<div data-search-exclude markdown="1">



URI: [pc:Translation](https://pruzhany.org/ns/sourced-entities#Translation)





```mermaid
 classDiagram
    class Translation
    click Translation href "../Translation/"
      Translation : attribution
        
          
    
        
        
        Translation --> "1" Authorship : attribution
        click Authorship href "../Authorship/"
    

        
      Translation : based_on
        
          
    
        
        
        Translation --> "1" TextBasis : based_on
        click TextBasis href "../TextBasis/"
    

        
      Translation : checked_against
        
          
    
        
        
        Translation --> "0..1" TranslationCheck : checked_against
        click TranslationCheck href "../TranslationCheck/"
    

        
      Translation : language
        
      Translation : text
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [text](text.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The English text. | direct |
| [language](language.md) | 1 <br/> [String](String.md) | The translation's language, always English (en). | direct |
| [based_on](based_on.md) | 1 <br/> [TextBasis](TextBasis.md) | The exact printed text translated, and where it is printed. | direct |
| [attribution](attribution.md) | 1 <br/> [Authorship](Authorship.md) | Who translated it, and on which day. | direct |
| [checked_against](checked_against.md) | 0..1 <br/> [TranslationCheck](TranslationCheck.md) | A later check of this translation against the reading, where one was made. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:Translation |
| native | pc:Translation |
| exact | pc:site_translation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Translation
description: An English translation of a content item's printed text, with the exact
  text it was made from, who made it and, where one was made, its later check.
from_schema: https://pruzhany.org/ns/mentions
exact_mappings:
- pc:site_translation
rank: 1000
attributes:
  text:
    name: text
    description: The English text.
    from_schema: https://pruzhany.org/ns/site_common
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    range: NonBlankText
    required: true
  language:
    name: language
    description: The translation's language, always English (en).
    from_schema: https://pruzhany.org/ns/site_common
    domain_of:
    - SuppliedTitle
    - Translation
    required: true
    equals_string: en
  based_on:
    name: based_on
    description: The exact printed text translated, and where it is printed.
    from_schema: https://pruzhany.org/ns/site_common
    domain_of:
    - SuppliedTitle
    - Translation
    range: TextBasis
    required: true
    inlined: true
  attribution:
    name: attribution
    description: Who translated it, and on which day.
    from_schema: https://pruzhany.org/ns/site_common
    domain_of:
    - EnglishCheck
    - SuppliedTitle
    - Translation
    range: Authorship
    required: true
    inlined: true
  checked_against:
    name: checked_against
    description: A later check of this translation against the reading, where one
      was made.
    from_schema: https://pruzhany.org/ns/site_common
    exact_mappings:
    - pc:site_checked_against_text
    domain_of:
    - SuppliedTitle
    - Translation
    range: TranslationCheck
    inlined: true

```
</details>

### Induced

<details>
```yaml
name: Translation
description: An English translation of a content item's printed text, with the exact
  text it was made from, who made it and, where one was made, its later check.
from_schema: https://pruzhany.org/ns/mentions
exact_mappings:
- pc:site_translation
rank: 1000
attributes:
  text:
    name: text
    description: The English text.
    from_schema: https://pruzhany.org/ns/site_common
    owner: Translation
    domain_of:
    - PrintedAddress
    - PrintedTitle
    - SuppliedTitle
    - Translation
    range: NonBlankText
    required: true
  language:
    name: language
    description: The translation's language, always English (en).
    from_schema: https://pruzhany.org/ns/site_common
    owner: Translation
    domain_of:
    - SuppliedTitle
    - Translation
    range: string
    required: true
    equals_string: en
  based_on:
    name: based_on
    description: The exact printed text translated, and where it is printed.
    from_schema: https://pruzhany.org/ns/site_common
    owner: Translation
    domain_of:
    - SuppliedTitle
    - Translation
    range: TextBasis
    required: true
    inlined: true
  attribution:
    name: attribution
    description: Who translated it, and on which day.
    from_schema: https://pruzhany.org/ns/site_common
    owner: Translation
    domain_of:
    - EnglishCheck
    - SuppliedTitle
    - Translation
    range: Authorship
    required: true
    inlined: true
  checked_against:
    name: checked_against
    description: A later check of this translation against the reading, where one
      was made.
    from_schema: https://pruzhany.org/ns/site_common
    exact_mappings:
    - pc:site_checked_against_text
    owner: Translation
    domain_of:
    - SuppliedTitle
    - Translation
    range: TranslationCheck
    inlined: true

```
</details></div>
