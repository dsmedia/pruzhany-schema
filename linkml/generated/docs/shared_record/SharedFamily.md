---
search:
  boost: 10.0
---

# Class: SharedFamily 


_One family of the record: its id, the name shown and its names._



<div data-search-exclude markdown="1">



URI: [ehri:Family](http://lod.ehri-project-test.eu/ontology#Family)





```mermaid
 classDiagram
    class SharedFamily
    click SharedFamily href "../SharedFamily/"
      SharedFamily : id
        
      SharedFamily : name
        
      SharedFamily : names
        
          
    
        
        
        SharedFamily --> "1..*" Name : names
        click Name href "../Name/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ehri:Family](http://lod.ehri-project-test.eu/ontology#Family) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The family's id. | direct |
| [name](name.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The name the site shows. | direct |
| [names](names.md) | 1..* <br/> [Name](Name.md) | The family's names. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SharedRecord](SharedRecord.md) | [families](families.md) | range | [SharedFamily](SharedFamily.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ehri:Family |
| native | pc:SharedFamily |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SharedFamily
description: 'One family of the record: its id, the name shown and its names.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
attributes:
  id:
    name: id
    description: The family's id.
    from_schema: https://pruzhany.org/ns/shared_record
    domain_of:
    - SharedPerson
    - SharedFamily
    - Holder
    - SharedPlace
    - SharedOrganization
    - SharedEvent
    - Source
    - Fact
    - Mention
    - PublicMedia
    range: NonBlankText
    required: true
  name:
    name: name
    description: The name the site shows.
    from_schema: https://pruzhany.org/ns/shared_record
    domain_of:
    - SharedPerson
    - SharedFamily
    - Holder
    - SharedPlace
    - SharedOrganization
    - SharedEvent
    range: NonBlankText
    required: true
  names:
    name: names
    description: The family's names.
    from_schema: https://pruzhany.org/ns/shared_record
    domain_of:
    - SharedPerson
    - SharedFamily
    - SharedPlace
    - SharedOrganization
    range: Name
    required: true
    multivalued: true
    inlined_as_list: true
class_uri: ehri:Family

```
</details>

### Induced

<details>
```yaml
name: SharedFamily
description: 'One family of the record: its id, the name shown and its names.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
attributes:
  id:
    name: id
    description: The family's id.
    from_schema: https://pruzhany.org/ns/shared_record
    owner: SharedFamily
    domain_of:
    - SharedPerson
    - SharedFamily
    - Holder
    - SharedPlace
    - SharedOrganization
    - SharedEvent
    - Source
    - Fact
    - Mention
    - PublicMedia
    range: NonBlankText
    required: true
  name:
    name: name
    description: The name the site shows.
    from_schema: https://pruzhany.org/ns/shared_record
    owner: SharedFamily
    domain_of:
    - SharedPerson
    - SharedFamily
    - Holder
    - SharedPlace
    - SharedOrganization
    - SharedEvent
    range: NonBlankText
    required: true
  names:
    name: names
    description: The family's names.
    from_schema: https://pruzhany.org/ns/shared_record
    owner: SharedFamily
    domain_of:
    - SharedPerson
    - SharedFamily
    - SharedPlace
    - SharedOrganization
    range: Name
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: ehri:Family

```
</details></div>
