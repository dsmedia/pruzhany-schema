---
search:
  boost: 10.0
---

# Class: Answer (ReadLatinAnswer) 


_The model's answer to one message: a line for each picture, empty where it saw no text._



<div data-search-exclude markdown="1">



URI: [pc:ReadLatinAnswer](https://pruzhany.org/ns/sourced-entities#ReadLatinAnswer)





```mermaid
 classDiagram
    class ReadLatinAnswer
    click ReadLatinAnswer href "../ReadLatinAnswer/"
      ReadLatinAnswer : lines
        
          
    
        
        
        ReadLatinAnswer --> "1..*" ReadLatinLine : lines
        click ReadLatinLine href "../ReadLatinLine/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [lines](lines.md) | 1..* <br/> [ReadLatinLine](ReadLatinLine.md) | The lines field in the Answer response. | direct |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| asking | read_latin |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:ReadLatinAnswer |
| native | pc:ReadLatinAnswer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReadLatinAnswer
annotations:
  asking:
    tag: asking
    value: read_latin
description: 'The model''s answer to one message: a line for each picture, empty where
  it saw no text.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  lines:
    name: lines
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The lines field in the Answer response.
    title: Lines
    from_schema: https://pruzhany.org/ns/answers
    domain_of:
    - FindItemsAnswerHeading
    - ReadLatinAnswer
    range: ReadLatinLine
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: ReadLatinAnswer
annotations:
  asking:
    tag: asking
    value: read_latin
description: 'The model''s answer to one message: a line for each picture, empty where
  it saw no text.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  lines:
    name: lines
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The lines field in the Answer response.
    title: Lines
    from_schema: https://pruzhany.org/ns/answers
    owner: ReadLatinAnswer
    domain_of:
    - FindItemsAnswerHeading
    - ReadLatinAnswer
    range: ReadLatinLine
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>
