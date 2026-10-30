---
search:
  boost: 10.0
---

# Class: Answer (JoinPeopleAnswer) 


_The groups of names that are one person; a name in no group is a person of its own._



<div data-search-exclude markdown="1">



URI: [pc:JoinPeopleAnswer](https://pruzhany.org/ns/sourced-entities#JoinPeopleAnswer)





```mermaid
 classDiagram
    class JoinPeopleAnswer
    click JoinPeopleAnswer href "../JoinPeopleAnswer/"
      JoinPeopleAnswer : groups
        
          
    
        
        
        JoinPeopleAnswer --> "1..*" JoinPeopleGroup : groups
        click JoinPeopleGroup href "../JoinPeopleGroup/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [groups](groups.md) | 1..* <br/> [JoinPeopleGroup](JoinPeopleGroup.md) | The groups field in the Answer response. | direct |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| asking | join_people |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:JoinPeopleAnswer |
| native | pc:JoinPeopleAnswer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: JoinPeopleAnswer
annotations:
  asking:
    tag: asking
    value: join_people
description: The groups of names that are one person; a name in no group is a person
  of its own.
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  groups:
    name: groups
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The groups field in the Answer response.
    title: Groups
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    domain_of:
    - JoinPeopleAnswer
    range: JoinPeopleGroup
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: JoinPeopleAnswer
annotations:
  asking:
    tag: asking
    value: join_people
description: The groups of names that are one person; a name in no group is a person
  of its own.
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  groups:
    name: groups
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The groups field in the Answer response.
    title: Groups
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    owner: JoinPeopleAnswer
    domain_of:
    - JoinPeopleAnswer
    range: JoinPeopleGroup
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>
