---
search:
  boost: 10.0
---

# Class: Newspaper 


_One newspaper in the source register, with its site title, code and default picture credit. A page may supply a different credit through picture_source._



<div data-search-exclude markdown="1">



URI: [ehri:RecordSet](http://lod.ehri-project-test.eu/ontology#RecordSet)





```mermaid
 classDiagram
    class Newspaper
    click Newspaper href "../Newspaper/"
      PictureSource <|-- Newspaper
        click PictureSource href "../PictureSource/"
      
      Newspaper : code
        
      Newspaper : holder
        
      Newspaper : holder_url
        
      Newspaper : id
        
      Newspaper : rights
        
      Newspaper : rights_url
        
      Newspaper : route
        
      Newspaper : shelf_mark
        
      Newspaper : title
        
      Newspaper : url
        
      
```





## Inheritance
* [PictureSource](PictureSource.md)
    * **Newspaper**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [ehri:RecordSet](http://lod.ehri-project-test.eu/ontology#RecordSet) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The paper's source-register id, the same value as Edition.newspaper. | direct |
| [code](code.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The paper's lowercase alphabetic code used in site keys and routes. | direct |
| [title](title.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The paper's title as the site shows it. | direct |
| [holder](holder.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The name of the institution holding the pages the pictures were made from. | [PictureSource](PictureSource.md) |
| [holder_url](holder_url.md) | 0..1 <br/> [Uri](Uri.md) | The web address of the institution named in holder: its page for the holding where the source register has one, otherwise its home page. | [PictureSource](PictureSource.md) |
| [route](route.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The name of the service or collection readers reach the pages through, when it differs from the holder itself. | [PictureSource](PictureSource.md) |
| [shelf_mark](shelf_mark.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The holder's shelf mark or call number for the pages. | [PictureSource](PictureSource.md) |
| [url](url.md) | 0..1 <br/> [Uri](Uri.md) | The pages' descriptive page at the holder or access route. | [PictureSource](PictureSource.md) |
| [rights](rights.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The rights statement for the pictures, as text. | [PictureSource](PictureSource.md) |
| [rights_url](rights_url.md) | 0..1 <br/> [Uri](Uri.md) | The address where the rights statement was read. | [PictureSource](PictureSource.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EditionsCatalog](EditionsCatalog.md) | [newspapers](newspapers.md) | range | [Newspaper](Newspaper.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/editions




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ehri:RecordSet |
| native | pc:Newspaper |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Newspaper
description: One newspaper in the source register, with its site title, code and default
  picture credit. A page may supply a different credit through picture_source.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
is_a: PictureSource
attributes:
  id:
    name: id
    description: The paper's source-register id, the same value as Edition.newspaper.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:site_newspaper
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
  code:
    name: code
    description: The paper's lowercase alphabetic code used in site keys and routes.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:newspaper_code
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
    pattern: ^[a-z]+$(?![\s\S])
  title:
    name: title
    description: The paper's title as the site shows it.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: rico:title
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
class_uri: ehri:RecordSet

```
</details>

### Induced

<details>
```yaml
name: Newspaper
description: One newspaper in the source register, with its site title, code and default
  picture credit. A page may supply a different credit through picture_source.
from_schema: https://pruzhany.org/ns/editions
rank: 1000
is_a: PictureSource
attributes:
  id:
    name: id
    description: The paper's source-register id, the same value as Edition.newspaper.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:site_newspaper
    owner: Newspaper
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
  code:
    name: code
    description: The paper's lowercase alphabetic code used in site keys and routes.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: pc:newspaper_code
    owner: Newspaper
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
    pattern: ^[a-z]+$(?![\s\S])
  title:
    name: title
    description: The paper's title as the site shows it.
    from_schema: https://pruzhany.org/ns/editions
    rank: 1000
    slot_uri: rico:title
    owner: Newspaper
    domain_of:
    - Newspaper
    range: NonBlankText
    required: true
  holder:
    name: holder
    description: The name of the institution holding the pages the pictures were made
      from.
    from_schema: https://pruzhany.org/ns/picture_source
    close_mappings:
    - rico:hasOrHadHolder
    rank: 1000
    slot_uri: pc:picture_holder_name
    owner: Newspaper
    domain_of:
    - PictureSource
    range: NonBlankText
    required: true
  holder_url:
    name: holder_url
    description: 'The web address of the institution named in holder: its page for
      the holding where the source register has one, otherwise its home page.'
    from_schema: https://pruzhany.org/ns/picture_source
    close_mappings:
    - rdfs:seeAlso
    rank: 1000
    slot_uri: pc:picture_holder_url
    owner: Newspaper
    domain_of:
    - PictureSource
    range: uri
  route:
    name: route
    description: The name of the service or collection readers reach the pages through,
      when it differs from the holder itself.
    from_schema: https://pruzhany.org/ns/picture_source
    rank: 1000
    slot_uri: pc:picture_access_route
    owner: Newspaper
    domain_of:
    - PictureSource
    range: NonBlankText
  shelf_mark:
    name: shelf_mark
    description: The holder's shelf mark or call number for the pages.
    from_schema: https://pruzhany.org/ns/picture_source
    rank: 1000
    slot_uri: rico:identifier
    owner: Newspaper
    domain_of:
    - PictureSource
    range: NonBlankText
  url:
    name: url
    description: The pages' descriptive page at the holder or access route.
    from_schema: https://pruzhany.org/ns/picture_source
    close_mappings:
    - rdfs:seeAlso
    rank: 1000
    slot_uri: pc:holding_object_url
    owner: Newspaper
    domain_of:
    - PictureSource
    range: uri
  rights:
    name: rights
    description: The rights statement for the pictures, as text.
    from_schema: https://pruzhany.org/ns/picture_source
    rank: 1000
    slot_uri: rico:conditionsOfUse
    owner: Newspaper
    domain_of:
    - PictureSource
    range: NonBlankText
  rights_url:
    name: rights_url
    description: The address where the rights statement was read.
    from_schema: https://pruzhany.org/ns/picture_source
    rank: 1000
    slot_uri: pc:picture_rights_url
    owner: Newspaper
    domain_of:
    - PictureSource
    range: uri
class_uri: ehri:RecordSet

```
</details></div>
