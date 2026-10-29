---
search:
  boost: 10.0
---

# Class: SiteCitation 


_A citation as the shared record keeps it: an older one as it was written, or one the site writer locates on the printed page, with the addresses of the words it quotes._



<div data-search-exclude markdown="1">



URI: [pc:SiteCitation](https://pruzhany.org/ns/sourced-entities#SiteCitation)





```mermaid
 classDiagram
    class SiteCitation
    click SiteCitation href "../SiteCitation/"
      Citation <|-- SiteCitation
        click Citation href "../Citation/"
      
      SiteCitation : accessed
        
      SiteCitation : addresses
        
          
    
        
        
        SiteCitation --> "1..*" PrintedAddress : addresses
        click PrintedAddress href "../PrintedAddress/"
    

        
      SiteCitation : edition_date
        
      SiteCitation : locator
        
      SiteCitation : note
        
      SiteCitation : page
        
      SiteCitation : public_note
        
      SiteCitation : quote
        
      SiteCitation : quote_language
        
      SiteCitation : record_id
        
      SiteCitation : record_type
        
      SiteCitation : reference_code
        
      SiteCitation : scan
        
      SiteCitation : source_id
        
      SiteCitation : time
        
      SiteCitation : unit_id
        
      SiteCitation : url
        
      SiteCitation : via
        
      
```





## Inheritance
* [Citation](Citation.md)
    * **SiteCitation**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [addresses](addresses.md) | 1..* <br/> [PrintedAddress](PrintedAddress.md) | Where on the page pictures the quoted words are printed. | direct |
| [source_id](source_id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The record the statement rests on (the original where it is known), by its id in the record's sources. | [Citation](Citation.md) |
| [via](via.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The one source actually read, a copy or a transcription of the original, by its id. | [Citation](Citation.md) |
| [reference_code](reference_code.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The holder's reference of the document cited, where the source is a set of many. | [Citation](Citation.md) |
| [record_type](record_type.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The holder's own type of the record, such as Page of Testimony. | [Citation](Citation.md) |
| [quote_language](quote_language.md) | 0..1 <br/> [LanguageTag](LanguageTag.md) | The quote's language, where it is not the source's (a translation). | [Citation](Citation.md) |
| [public_note](public_note.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | Our reviewed words for the page about this evidence, apart from the record's quote. | [Citation](Citation.md) |
| [locator](locator.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | An internal pointer into the project's files; never published and never a holder's record number. | [Citation](Citation.md) |
| [record_id](record_id.md) | 0..1 <br/> [String](String.md) | The holder's own number for the record, such as a Yad Vashem record number. | [Citation](Citation.md) |
| [page](page.md) | 0..1 <br/> [String](String.md) | The page, folio or entry cited. | [Citation](Citation.md) |
| [scan](scan.md) | 0..1 <br/> [String](String.md) | The scan or image cited. | [Citation](Citation.md) |
| [time](time.md) | 0..1 <br/> [String](String.md) | The time in a recording. | [Citation](Citation.md) |
| [edition_date](edition_date.md) | 0..1 <br/> [String](String.md) | The day of the paper's issue cited, written YYYY-MM-DD. | [Citation](Citation.md) |
| [unit_id](unit_id.md) | 0..1 <br/> [String](String.md) | The piece of the paper cited, by its content item id. | [Citation](Citation.md) |
| [url](url.md) | 0..1 <br/> [HttpsUri](HttpsUri.md) | The record's web address. | [Citation](Citation.md) |
| [quote](quote.md) | 0..1 <br/> [String](String.md) | The record's own words, exactly. | [Citation](Citation.md) |
| [note](note.md) | 0..1 <br/> [String](String.md) | Our private note on the evidence; never published. | [Citation](Citation.md) |
| [accessed](accessed.md) | 0..1 <br/> [IsoDay](IsoDay.md) | The day a person read the record. | [Citation](Citation.md) |

<details>
<summary>Expressions & Logic</summary>
#### Any Of

The class must satisfy at least one of:
- AnonymousClassExpression({
  'description': 'A citation names where in its source the evidence is.',
  'slot_conditions': {'record_id': SlotDefinition({'name': 'record_id', 'required': True, 'pattern': '\\S'})}
})
- AnonymousClassExpression({
  'slot_conditions': {'page': SlotDefinition({'name': 'page', 'required': True, 'pattern': '\\S'})}
})
- AnonymousClassExpression({
  'slot_conditions': {'scan': SlotDefinition({'name': 'scan', 'required': True, 'pattern': '\\S'})}
})
- AnonymousClassExpression({
  'slot_conditions': {'time': SlotDefinition({'name': 'time', 'required': True, 'pattern': '\\S'})}
})
- AnonymousClassExpression({
  'slot_conditions': {'unit_id': SlotDefinition({'name': 'unit_id', 'required': True, 'pattern': '\\S'})}
})
- AnonymousClassExpression({'slot_conditions': {'url': SlotDefinition({'name': 'url', 'required': True})}})
- AnonymousClassExpression({
  'slot_conditions': {'locator': SlotDefinition({'name': 'locator', 'required': True})}
})
- AnonymousClassExpression({
  'slot_conditions': {'reference_code': SlotDefinition({'name': 'reference_code', 'required': True})}
})

</details>





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SharedName](SharedName.md) | [citations](citations.md) | range | [SiteCitation](SiteCitation.md) |
| [SharedFact](SharedFact.md) | [citations](citations.md) | range | [SiteCitation](SiteCitation.md) |
| [SourcedRelation](SourcedRelation.md) | [citations](citations.md) | range | [SiteCitation](SiteCitation.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'addresses': {'value_presence': 'PRESENT'}}``` |```{'unit_id': {'required': True, 'pattern': '\\S'}, 'edition_date': {'required': True, 'pattern': '^\\d{4}-\\d{2}-\\d{2}$'}, 'quote': {'required': True, 'pattern': '\\S'}}``` | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:SiteCitation |
| native | pc:SiteCitation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SiteCitation
description: 'A citation as the shared record keeps it: an older one as it was written,
  or one the site writer locates on the printed page, with the addresses of the words
  it quotes.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
is_a: Citation
attributes:
  addresses:
    name: addresses
    description: Where on the page pictures the quoted words are printed.
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    domain_of:
    - SiteCitation
    - TextBasis
    - PrintedTitle
    range: PrintedAddress
    multivalued: true
    inlined_as_list: true
    minimum_cardinality: 1
rules:
- preconditions:
    slot_conditions:
      addresses:
        name: addresses
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      unit_id:
        name: unit_id
        required: true
        pattern: \S
      edition_date:
        name: edition_date
        required: true
        pattern: ^\d{4}-\d{2}-\d{2}$
      quote:
        name: quote
        required: true
        pattern: \S
  description: A located citation names its piece, its issue's day and its quote.
any_of:
- description: A citation names where in its source the evidence is.
  slot_conditions:
    record_id:
      name: record_id
      required: true
      pattern: \S
- slot_conditions:
    page:
      name: page
      required: true
      pattern: \S
- slot_conditions:
    scan:
      name: scan
      required: true
      pattern: \S
- slot_conditions:
    time:
      name: time
      required: true
      pattern: \S
- slot_conditions:
    unit_id:
      name: unit_id
      required: true
      pattern: \S
- slot_conditions:
    url:
      name: url
      required: true
- slot_conditions:
    locator:
      name: locator
      required: true
- slot_conditions:
    reference_code:
      name: reference_code
      required: true

```
</details>

### Induced

<details>
```yaml
name: SiteCitation
description: 'A citation as the shared record keeps it: an older one as it was written,
  or one the site writer locates on the printed page, with the addresses of the words
  it quotes.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
is_a: Citation
attributes:
  addresses:
    name: addresses
    description: Where on the page pictures the quoted words are printed.
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    owner: SiteCitation
    domain_of:
    - SiteCitation
    - TextBasis
    - PrintedTitle
    range: PrintedAddress
    multivalued: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
  source_id:
    name: source_id
    annotations:
      references:
        tag: references
        value: Source.id
    description: The record the statement rests on (the original where it is known),
      by its id in the record's sources.
    from_schema: https://pruzhany.org/ns/sourced_entities
    slot_uri: rico:isEvidencedBy
    owner: SiteCitation
    domain_of:
    - PlaceIdentifier
    - SourceDerivation
    - Citation
    - MediaFamilyWords
    - PublicMedia
    range: NonBlankText
    required: true
  via:
    name: via
    description: The one source actually read, a copy or a transcription of the original,
      by its id.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    range: NonBlankText
  reference_code:
    name: reference_code
    description: The holder's reference of the document cited, where the source is
      a set of many.
    from_schema: https://pruzhany.org/ns/sourced_entities
    slot_uri: rico:hasOrHadIdentifier
    owner: SiteCitation
    domain_of:
    - Source
    - Citation
    range: NonBlankText
  record_type:
    name: record_type
    description: The holder's own type of the record, such as Page of Testimony.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: rico:hasDocumentaryFormType
    owner: SiteCitation
    domain_of:
    - Citation
    range: NonBlankText
  quote_language:
    name: quote_language
    description: The quote's language, where it is not the source's (a translation).
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: rico:hasOrHadLanguage
    owner: SiteCitation
    domain_of:
    - Citation
    - MediaFamilyWords
    range: LanguageTag
  public_note:
    name: public_note
    description: Our reviewed words for the page about this evidence, apart from the
      record's quote.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: pc:site_citation_public_note
    owner: SiteCitation
    domain_of:
    - Citation
    range: NonBlankText
  locator:
    name: locator
    description: An internal pointer into the project's files; never published and
      never a holder's record number.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: pc:site_citation_locator
    owner: SiteCitation
    domain_of:
    - Citation
    range: NonBlankText
  record_id:
    name: record_id
    description: The holder's own number for the record, such as a Yad Vashem record
      number.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: rico:hasOrHadIdentifier
    owner: SiteCitation
    domain_of:
    - Citation
    range: string
  page:
    name: page
    description: The page, folio or entry cited.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    - MediaFamilyWords
    range: string
  scan:
    name: scan
    description: The scan or image cited.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    range: string
  time:
    name: time
    description: The time in a recording.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    range: string
  edition_date:
    name: edition_date
    description: The day of the paper's issue cited, written YYYY-MM-DD.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    range: string
  unit_id:
    name: unit_id
    description: The piece of the paper cited, by its content item id.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    - Mention
    range: string
  url:
    name: url
    description: The record's web address.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SiteCitation
    domain_of:
    - PlaceIdentifier
    - Citation
    - MediaDerivative
    range: HttpsUri
  quote:
    name: quote
    description: The record's own words, exactly.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SiteCitation
    domain_of:
    - Citation
    - MediaFamilyWords
    range: string
  note:
    name: note
    description: Our private note on the evidence; never published.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SiteCitation
    domain_of:
    - Attribution
    - Citation
    range: string
  accessed:
    name: accessed
    description: The day a person read the record.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SiteCitation
    domain_of:
    - PlaceIdentifier
    - Citation
    range: IsoDay
rules:
- preconditions:
    slot_conditions:
      addresses:
        name: addresses
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      unit_id:
        name: unit_id
        required: true
        pattern: \S
      edition_date:
        name: edition_date
        required: true
        pattern: ^\d{4}-\d{2}-\d{2}$
      quote:
        name: quote
        required: true
        pattern: \S
  description: A located citation names its piece, its issue's day and its quote.
any_of:
- description: A citation names where in its source the evidence is.
  slot_conditions:
    record_id:
      name: record_id
      required: true
      pattern: \S
- slot_conditions:
    page:
      name: page
      required: true
      pattern: \S
- slot_conditions:
    scan:
      name: scan
      required: true
      pattern: \S
- slot_conditions:
    time:
      name: time
      required: true
      pattern: \S
- slot_conditions:
    unit_id:
      name: unit_id
      required: true
      pattern: \S
- slot_conditions:
    url:
      name: url
      required: true
- slot_conditions:
    locator:
      name: locator
      required: true
- slot_conditions:
    reference_code:
      name: reference_code
      required: true

```
</details></div>
