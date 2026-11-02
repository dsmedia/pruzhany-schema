---
search:
  boost: 10.0
---

# Class: SentenceVerdict (JudgeOpeningSentenceVerdict) 


_Whether one sentence of the opening, by its number, is supported, and why._



<div data-search-exclude markdown="1">



URI: [pc:JudgeOpeningSentenceVerdict](https://pruzhany.org/ns/sourced-entities#JudgeOpeningSentenceVerdict)





```mermaid
 classDiagram
    class JudgeOpeningSentenceVerdict
    click JudgeOpeningSentenceVerdict href "../JudgeOpeningSentenceVerdict/"
      JudgeOpeningSentenceVerdict : number
        
      JudgeOpeningSentenceVerdict : supported
        
      JudgeOpeningSentenceVerdict : why
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [number](number.md) | 1 <br/> [Integer](Integer.md) | The number field in the SentenceVerdict response. | direct |
| [supported](supported.md) | 1 <br/> [Boolean](Boolean.md) | The supported field in the SentenceVerdict response. | direct |
| [why](why.md) | 1 <br/> [String](String.md) | One short sentence. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [JudgeOpeningAnswer](JudgeOpeningAnswer.md) | [sentences](sentences.md) | range | [JudgeOpeningSentenceVerdict](JudgeOpeningSentenceVerdict.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:JudgeOpeningSentenceVerdict |
| native | pc:JudgeOpeningSentenceVerdict |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JudgeOpeningSentenceVerdict
description: Whether one sentence of the opening, by its number, is supported, and
  why.
title: SentenceVerdict
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  number:
    name: number
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The number field in the SentenceVerdict response.
    title: Number
    from_schema: https://pruzhany.org/ns/answers
    domain_of:
    - WriteEnglishAnsweredPiece
    - QuoteEnglishQuotedEnglish
    - JudgeOpeningSentenceVerdict
    range: integer
    required: true
  supported:
    name: supported
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The supported field in the SentenceVerdict response.
    title: Supported
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    domain_of:
    - JudgeOpeningSentenceVerdict
    range: boolean
    required: true
  why:
    name: why
    description: One short sentence.
    title: Why
    from_schema: https://pruzhany.org/ns/answers
    domain_of:
    - WriteEnglishDoubt
    - JoinPeopleGroup
    - JudgeOpeningSentenceVerdict
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: JudgeOpeningSentenceVerdict
description: Whether one sentence of the opening, by its number, is supported, and
  why.
title: SentenceVerdict
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  number:
    name: number
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The number field in the SentenceVerdict response.
    title: Number
    from_schema: https://pruzhany.org/ns/answers
    owner: JudgeOpeningSentenceVerdict
    domain_of:
    - WriteEnglishAnsweredPiece
    - QuoteEnglishQuotedEnglish
    - JudgeOpeningSentenceVerdict
    range: integer
    required: true
  supported:
    name: supported
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The supported field in the SentenceVerdict response.
    title: Supported
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    owner: JudgeOpeningSentenceVerdict
    domain_of:
    - JudgeOpeningSentenceVerdict
    range: boolean
    required: true
  why:
    name: why
    description: One short sentence.
    title: Why
    from_schema: https://pruzhany.org/ns/answers
    owner: JudgeOpeningSentenceVerdict
    domain_of:
    - WriteEnglishDoubt
    - JoinPeopleGroup
    - JudgeOpeningSentenceVerdict
    range: string
    required: true

```
</details></div>
