---
search:
  boost: 10.0
---

# Class: Attribution 


_Who made or allowed something, on what day, with an optional note._



<div data-search-exclude markdown="1">



URI: [pc:Attribution](https://pruzhany.org/ns/sourced-entities#Attribution)





```mermaid
 classDiagram
    class Attribution
    click Attribution href "../Attribution/"
      Attribution <|-- Authorship
        click Authorship href "../Authorship/"
      
      Attribution : by
        
      Attribution : note
        
      Attribution : on
        
      
```





## Inheritance
* **Attribution**
    * [Authorship](Authorship.md)


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [by](by.md) | 1 <br/> [NonBlankText](NonBlankText.md) | Who made it or allowed it: a person, a session or a program. | direct |
| [on](on.md) | 1 <br/> [IsoDay](IsoDay.md) | The day it was made or allowed. | direct |
| [note](note.md) | 0..1 <br/> [String](String.md) | A note on how or why. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:Attribution |
| native | pc:Attribution |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Attribution
description: Who made or allowed something, on what day, with an optional note.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
attributes:
  by:
    name: by
    description: 'Who made it or allowed it: a person, a session or a program.'
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - Attribution
    range: NonBlankText
    required: true
  'on':
    name: 'on'
    description: The day it was made or allowed.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - Attribution
    range: IsoDay
    required: true
  note:
    name: note
    description: A note on how or why.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    domain_of:
    - Attribution
    range: string

```
</details>

### Induced

<details>
```yaml
name: Attribution
description: Who made or allowed something, on what day, with an optional note.
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
attributes:
  by:
    name: by
    description: 'Who made it or allowed it: a person, a session or a program.'
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Attribution
    domain_of:
    - Attribution
    range: NonBlankText
    required: true
  'on':
    name: 'on'
    description: The day it was made or allowed.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Attribution
    domain_of:
    - Attribution
    range: IsoDay
    required: true
  note:
    name: note
    description: A note on how or why.
    from_schema: https://pruzhany.org/ns/site_common
    rank: 1000
    owner: Attribution
    domain_of:
    - Attribution
    range: string

```
</details></div>
