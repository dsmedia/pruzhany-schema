---
search:
  boost: 10.0
---

# Class: Answer (JudgeOpeningAnswer) 


_The verdict on one opening: one for each of its sentences._



<div data-search-exclude markdown="1">



URI: [pc:JudgeOpeningAnswer](https://pruzhany.org/ns/sourced-entities#JudgeOpeningAnswer)





```mermaid
 classDiagram
    class JudgeOpeningAnswer
    click JudgeOpeningAnswer href "../JudgeOpeningAnswer/"
      JudgeOpeningAnswer : sentences
        
          
    
        
        
        JudgeOpeningAnswer --> "1..*" JudgeOpeningSentenceVerdict : sentences
        click JudgeOpeningSentenceVerdict href "../JudgeOpeningSentenceVerdict/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sentences](sentences.md) | 1..* <br/> [JudgeOpeningSentenceVerdict](JudgeOpeningSentenceVerdict.md) | The sentences field in the Answer response. | direct |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| asking | judge_opening |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:JudgeOpeningAnswer |
| native | pc:JudgeOpeningAnswer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JudgeOpeningAnswer
annotations:
  asking:
    tag: asking
    value: judge_opening
description: 'The verdict on one opening: one for each of its sentences.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  sentences:
    name: sentences
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The sentences field in the Answer response.
    title: Sentences
    from_schema: https://pruzhany.org/ns/answers
    domain_of:
    - WriteOpeningAnswer
    - JudgeOpeningAnswer
    range: JudgeOpeningSentenceVerdict
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: JudgeOpeningAnswer
annotations:
  asking:
    tag: asking
    value: judge_opening
description: 'The verdict on one opening: one for each of its sentences.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  sentences:
    name: sentences
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The sentences field in the Answer response.
    title: Sentences
    from_schema: https://pruzhany.org/ns/answers
    owner: JudgeOpeningAnswer
    domain_of:
    - WriteOpeningAnswer
    - JudgeOpeningAnswer
    range: JudgeOpeningSentenceVerdict
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>
