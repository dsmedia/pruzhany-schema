---
search:
  boost: 10.0
---

# Class: EditionsCatalog 


_The catalog of editions: every edition, the holidays and historical events beside them, and the dates available on the site._



<div data-search-exclude markdown="1">



URI: [pc:EditionsCatalog](https://pruzhany.org/ns/sourced-entities#EditionsCatalog)





```mermaid
 classDiagram
    class EditionsCatalog
    click EditionsCatalog href "../EditionsCatalog/"
      EditionsCatalog : available_dates
        
      EditionsCatalog : available_keys
        
      EditionsCatalog : editions
        
          
    
        
        
        EditionsCatalog --> "1..*" Edition : editions
        click Edition href "../Edition/"
    

        
      EditionsCatalog : historical_events
        
          
    
        
        
        EditionsCatalog --> "1..*" HistoricalEvent : historical_events
        click HistoricalEvent href "../HistoricalEvent/"
    

        
      EditionsCatalog : holidays
        
          
    
        
        
        EditionsCatalog --> "1..*" Holiday : holidays
        click Holiday href "../Holiday/"
    

        
      EditionsCatalog : newspapers
        
          
    
        
        
        EditionsCatalog --> "*" Newspaper : newspapers
        click Newspaper href "../Newspaper/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [editions](editions.md) | 1..* <br/> [Edition](Edition.md) | Every edition of the paper, with its Hebrew date. | direct |
| [holidays](holidays.md) | 1..* <br/> [Holiday](Holiday.md) | The Jewish holidays of the paper's years. | direct |
| [historical_events](historical_events.md) | 1..* <br/> [HistoricalEvent](HistoricalEvent.md) | Events in the world outside the town that the calendar marks. | direct |
| [available_dates](available_dates.md) | 1..* <br/> [IsoDay](IsoDay.md) | The dates of the editions whose pages are on the site. | direct |
| [available_keys](available_keys.md) | * <br/> [String](String.md) | The keys of the editions whose pages are on the site, each an Edition key: the date alone for the first paper, or the paper's code and a hyphen before it for any other. Optional for now, because a site on an older schema pin refuses unknown fields and the catalogs written so far lack it: this schema comes first, then the site's pin, then the writer writes it, and later it becomes required. When present, no key appears twice and every key names an edition in editions. The writer publishes another paper's editions without reference to availableDates, which holds the first paper's dates, so the runtime twins check only that the date-only keys equal availableDates as a set. LinkML's generated JSON Schema cannot compare values within or across these lists. | direct |
| [newspapers](newspapers.md) | * <br/> [Newspaper](Newspaper.md) | The papers these editions belong to, one entry per source-register id, with their default picture credits. When present, every edition's newspaper must name one of these ids. The runtime twins enforce id uniqueness and membership; LinkML's generated JSON Schema cannot compare values across these lists. | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:EditionsCatalog |
| native | pc:EditionsCatalog |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EditionsCatalog
description: 'The catalog of editions: every edition, the holidays and historical
  events beside them, and the dates available on the site.'
from_schema: https://pruzhany.org/ns/editions
rank: 1000
attributes:
  editions:
    name: editions
    description: Every edition of the paper, with its Hebrew date.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    domain_of:
    - EditionsCatalog
    range: Edition
    required: true
    multivalued: true
    inlined_as_list: true
  holidays:
    name: holidays
    description: The Jewish holidays of the paper's years.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    domain_of:
    - EditionsCatalog
    range: Holiday
    required: true
    multivalued: true
    inlined_as_list: true
  historical_events:
    name: historical_events
    description: Events in the world outside the town that the calendar marks.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: historicalEvents
    domain_of:
    - EditionsCatalog
    range: HistoricalEvent
    required: true
    multivalued: true
    inlined_as_list: true
  available_dates:
    name: available_dates
    description: The dates of the editions whose pages are on the site.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: availableDates
    domain_of:
    - EditionsCatalog
    range: IsoDay
    required: true
    multivalued: true
  available_keys:
    name: available_keys
    description: 'The keys of the editions whose pages are on the site, each an Edition
      key: the date alone for the first paper, or the paper''s code and a hyphen before
      it for any other. Optional for now, because a site on an older schema pin refuses
      unknown fields and the catalogs written so far lack it: this schema comes first,
      then the site''s pin, then the writer writes it, and later it becomes required.
      When present, no key appears twice and every key names an edition in editions.
      The writer publishes another paper''s editions without reference to availableDates,
      which holds the first paper''s dates, so the runtime twins check only that the
      date-only keys equal availableDates as a set. LinkML''s generated JSON Schema
      cannot compare values within or across these lists.'
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: availableKeys
    domain_of:
    - EditionsCatalog
    multivalued: true
    pattern: ^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])
  newspapers:
    name: newspapers
    description: The papers these editions belong to, one entry per source-register
      id, with their default picture credits. When present, every edition's newspaper
      must name one of these ids. The runtime twins enforce id uniqueness and membership;
      LinkML's generated JSON Schema cannot compare values across these lists.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:catalog_newspapers
    domain_of:
    - EditionsCatalog
    range: Newspaper
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: EditionsCatalog
description: 'The catalog of editions: every edition, the holidays and historical
  events beside them, and the dates available on the site.'
from_schema: https://pruzhany.org/ns/editions
rank: 1000
attributes:
  editions:
    name: editions
    description: Every edition of the paper, with its Hebrew date.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: Edition
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  holidays:
    name: holidays
    description: The Jewish holidays of the paper's years.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: Holiday
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  historical_events:
    name: historical_events
    description: Events in the world outside the town that the calendar marks.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: historicalEvents
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: HistoricalEvent
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  available_dates:
    name: available_dates
    description: The dates of the editions whose pages are on the site.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: availableDates
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: IsoDay
    required: true
    multivalued: true
  available_keys:
    name: available_keys
    description: 'The keys of the editions whose pages are on the site, each an Edition
      key: the date alone for the first paper, or the paper''s code and a hyphen before
      it for any other. Optional for now, because a site on an older schema pin refuses
      unknown fields and the catalogs written so far lack it: this schema comes first,
      then the site''s pin, then the writer writes it, and later it becomes required.
      When present, no key appears twice and every key names an edition in editions.
      The writer publishes another paper''s editions without reference to availableDates,
      which holds the first paper''s dates, so the runtime twins check only that the
      date-only keys equal availableDates as a set. LinkML''s generated JSON Schema
      cannot compare values within or across these lists.'
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    alias: availableKeys
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: string
    multivalued: true
    pattern: ^(?:[a-z]+-)?\d{4}-\d{2}-\d{2}$(?![\s\S])
  newspapers:
    name: newspapers
    description: The papers these editions belong to, one entry per source-register
      id, with their default picture credits. When present, every edition's newspaper
      must name one of these ids. The runtime twins enforce id uniqueness and membership;
      LinkML's generated JSON Schema cannot compare values across these lists.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:catalog_newspapers
    owner: EditionsCatalog
    domain_of:
    - EditionsCatalog
    range: Newspaper
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>
