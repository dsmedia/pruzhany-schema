---
search:
  boost: 10.0
---

# Class: Authorship 


_Who wrote a supplied title, a translation or a check of one, a person or a model, and on which day._



<div data-search-exclude markdown="1">



URI: [pc:Authorship](https://pruzhany.org/ns/sourced-entities#Authorship)





```mermaid
 classDiagram
    class Authorship
    click Authorship href "../Authorship/"
      Attribution <|-- Authorship
        click Attribution href "../Attribution/"
      
      Authorship : by
        
      Authorship : kind
        
          
    
        
        
        Authorship --> "1" AuthorshipKind : kind
        click AuthorshipKind href "../AuthorshipKind/"
    

        
      Authorship : note
        
      Authorship : on
        
      
```





## Inheritance
* [Attribution](Attribution.md)
    * **Authorship**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [kind](kind.md) | 1 <br/> [AuthorshipKind](AuthorshipKind.md) | Whether a person or a model wrote it. | direct |
| [by](by.md) | 1 <br/> [NonBlankText](NonBlankText.md) | Who made it or allowed it: a person, a session or a program. | [Attribution](Attribution.md) |
| [on](on.md) | 1 <br/> [IsoDay](IsoDay.md) | The day it was made or allowed. | [Attribution](Attribution.md) |
| [note](note.md) | 0..1 <br/> [String](String.md) | A note on how or why. | [Attribution](Attribution.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EnglishCheck](EnglishCheck.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |
| [TitleCheck](TitleCheck.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |
| [TranslationCheck](TranslationCheck.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |
| [SuppliedTitle](SuppliedTitle.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |
| [Translation](Translation.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |
| [CitedTranslation](CitedTranslation.md) | [attribution](attribution.md) | range | [Authorship](Authorship.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/mentions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:Authorship |
| native | pc:Authorship |
| exact | pc:site_authorship |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Authorship
description: Who wrote a supplied title, a translation or a check of one, a person
  or a model, and on which day.
from_schema: https://pruzhany.org/ns/mentions
exact_mappings:
- pc:site_authorship
rank: 1000
is_a: Attribution
attributes:
  kind:
    name: kind
    description: Whether a person or a model wrote it.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - Authorship
    range: AuthorshipKind
    required: true

```
</details>

### Induced

<details>
```yaml
name: Authorship
description: Who wrote a supplied title, a translation or a check of one, a person
  or a model, and on which day.
from_schema: https://pruzhany.org/ns/mentions
exact_mappings:
- pc:site_authorship
rank: 1000
is_a: Attribution
attributes:
  kind:
    name: kind
    description: Whether a person or a model wrote it.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Authorship
    domain_of:
    - Authorship
    range: AuthorshipKind
    required: true
  by:
    name: by
    description: 'Who made it or allowed it: a person, a session or a program.'
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Authorship
    domain_of:
    - Attribution
    range: NonBlankText
    required: true
  'on':
    name: 'on'
    description: The day it was made or allowed.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Authorship
    domain_of:
    - Attribution
    range: IsoDay
    required: true
  note:
    name: note
    description: A note on how or why.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Authorship
    domain_of:
    - Attribution
    range: string

```
</details></div>
