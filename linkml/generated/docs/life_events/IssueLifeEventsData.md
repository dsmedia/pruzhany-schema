---
search:
  boost: 10.0
---

# Class: IssueLifeEventsData 


_One issue's life events document: the issue's date and the life events it prints._



<div data-search-exclude markdown="1">



URI: [pc:IssueLifeEventsData](https://pruzhany.org/ns/sourced-entities#IssueLifeEventsData)





```mermaid
 classDiagram
    class IssueLifeEventsData
    click IssueLifeEventsData href "../IssueLifeEventsData/"
      IssueLifeEventsData : issue_date
        
      IssueLifeEventsData : life_events
        
          
    
        
        
        IssueLifeEventsData --> "1..*" IssueLifeEvent : life_events
        click IssueLifeEvent href "../IssueLifeEvent/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [issue_date](issue_date.md) | 1 <br/> [IsoDay](IsoDay.md) | The issue's date, written YYYY-MM-DD. | direct |
| [life_events](life_events.md) | 1..* <br/> [IssueLifeEvent](IssueLifeEvent.md) | The life events the issue prints. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/life_events




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:IssueLifeEventsData |
| native | pc:IssueLifeEventsData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IssueLifeEventsData
description: 'One issue''s life events document: the issue''s date and the life events
  it prints.'
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
attributes:
  issue_date:
    name: issue_date
    description: The issue's date, written YYYY-MM-DD.
    from_schema: https://pruzhany.org/ns/life_events
    rank: 1000
    domain_of:
    - IssueLifeEventsData
    range: IsoDay
    required: true
  life_events:
    name: life_events
    description: The life events the issue prints.
    from_schema: https://pruzhany.org/ns/life_events
    rank: 1000
    domain_of:
    - IssueLifeEventsData
    range: IssueLifeEvent
    required: true
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: IssueLifeEventsData
description: 'One issue''s life events document: the issue''s date and the life events
  it prints.'
from_schema: https://pruzhany.org/ns/life_events
rank: 1000
attributes:
  issue_date:
    name: issue_date
    description: The issue's date, written YYYY-MM-DD.
    from_schema: https://pruzhany.org/ns/life_events
    rank: 1000
    owner: IssueLifeEventsData
    domain_of:
    - IssueLifeEventsData
    range: IsoDay
    required: true
  life_events:
    name: life_events
    description: The life events the issue prints.
    from_schema: https://pruzhany.org/ns/life_events
    rank: 1000
    owner: IssueLifeEventsData
    domain_of:
    - IssueLifeEventsData
    range: IssueLifeEvent
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>
