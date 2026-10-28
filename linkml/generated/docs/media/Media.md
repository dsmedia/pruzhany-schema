---
search:
  boost: 10.0
---

# Class: Media 


_One held or linked copy of a registered source, as the shared record keeps it: all that the public may see, with the private master file and the private permission besides._



<div data-search-exclude markdown="1">



URI: [rico:Instantiation](https://www.ica.org/standards/RiC/ontology#Instantiation)





```mermaid
 classDiagram
    class Media
    click Media href "../Media/"
      PublicMedia <|-- Media
        click PublicMedia href "../PublicMedia/"
      
      Media : alt
        
          
    
        
        
        Media --> "0..1" MediaText : alt
        click MediaText href "../MediaText/"
    

        
      Media : caption
        
          
    
        
        
        Media --> "1" MediaText : caption
        click MediaText href "../MediaText/"
    

        
      Media : cleared
        
          
    
        
        
        Media --> "0..1" MediaDecision : cleared
        click MediaDecision href "../MediaDecision/"
    

        
      Media : conditions_of_access
        
      Media : conditions_of_use
        
      Media : consent
        
          
    
        
        
        Media --> "0..1" MediaConsent : consent
        click MediaConsent href "../MediaConsent/"
    

        
      Media : credit
        
      Media : depicted
        
          
    
        
        
        Media --> "1..*" MediaDepicted : depicted
        click MediaDepicted href "../MediaDepicted/"
    

        
      Media : derived
        
          
    
        
        
        Media --> "1..*" MediaDerivative : derived
        click MediaDerivative href "../MediaDerivative/"
    

        
      Media : duration
        
      Media : family_words
        
          
    
        
        
        Media --> "0..1" MediaFamilyWords : family_words
        click MediaFamilyWords href "../MediaFamilyWords/"
    

        
      Media : height
        
      Media : id
        
      Media : inscription
        
          
    
        
        
        Media --> "0..1" MediaText : inscription
        click MediaText href "../MediaText/"
    

        
      Media : kind
        
          
    
        
        
        Media --> "1" MediaKind : kind
        click MediaKind href "../MediaKind/"
    

        
      Media : link
        
      Media : master
        
          
    
        
        
        Media --> "0..1" MediaMaster : master
        click MediaMaster href "../MediaMaster/"
    

        
      Media : rights
        
      Media : shows_unidentified
        
      Media : source_id
        
      Media : transcript
        
          
    
        
        
        Media --> "0..1" MediaText : transcript
        click MediaText href "../MediaText/"
    

        
      Media : width
        
      Media : withdrawn
        
          
    
        
        
        Media --> "0..1" MediaWithdrawal : withdrawn
        click MediaWithdrawal href "../MediaWithdrawal/"
    

        
      
```





## Inheritance
* [PublicMedia](PublicMedia.md)
    * **Media**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [rico:Instantiation](https://www.ica.org/standards/RiC/ontology#Instantiation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [master](master.md) | 0..1 <br/> [MediaMaster](MediaMaster.md) | Where the private master file is kept; never public. | direct |
| [consent](consent.md) | 0..1 <br/> [MediaConsent](MediaConsent.md) | The private record of the permission to show the medium; never public. | direct |
| [id](id.md) | 1 <br/> [String](String.md) | The medium's id: lowercase letters and digits in parts joined by hyphens. | [PublicMedia](PublicMedia.md) |
| [source_id](source_id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The source this medium is a copy of, by its id; never the person shown. | [PublicMedia](PublicMedia.md) |
| [kind](kind.md) | 1 <br/> [MediaKind](MediaKind.md) | What the medium is: image, audio, video or document. | [PublicMedia](PublicMedia.md) |
| [caption](caption.md) | 1 <br/> [MediaText](MediaText.md) | The caption the site shows, with its language and review. | [PublicMedia](PublicMedia.md) |
| [alt](alt.md) | 0..1 <br/> [MediaText](MediaText.md) | The description for screen readers of what is visible; required for images and documents. | [PublicMedia](PublicMedia.md) |
| [inscription](inscription.md) | 0..1 <br/> [MediaText](MediaText.md) | The object's own words, such as writing on the back of a photograph. | [PublicMedia](PublicMedia.md) |
| [transcript](transcript.md) | 0..1 <br/> [MediaText](MediaText.md) | A document's full text; required for documents. | [PublicMedia](PublicMedia.md) |
| [family_words](family_words.md) | 0..1 <br/> [MediaFamilyWords](MediaFamilyWords.md) | The family's words about the medium, quoted from a source. | [PublicMedia](PublicMedia.md) |
| [depicted](depicted.md) | 1..* <br/> [MediaDepicted](MediaDepicted.md) | The people the picture shows, identified or not, and where. | [PublicMedia](PublicMedia.md) |
| [shows_unidentified](shows_unidentified.md) | 1 <br/> [Boolean](Boolean.md) | True when the picture shows people not identified. | [PublicMedia](PublicMedia.md) |
| [width](width.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | The master's width in pixels, after orientation. | [PublicMedia](PublicMedia.md) |
| [height](height.md) | 0..1 <br/> [PositiveInteger](PositiveInteger.md) | The master's height in pixels, after orientation. | [PublicMedia](PublicMedia.md) |
| [duration](duration.md) | 0..1 <br/> [NonNegativeNumber](NonNegativeNumber.md) | The master's length in seconds, for sound and film. | [PublicMedia](PublicMedia.md) |
| [credit](credit.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The holder's or the family's credit, as they word it. | [PublicMedia](PublicMedia.md) |
| [conditions_of_access](conditions_of_access.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The holder's terms of access, as written. | [PublicMedia](PublicMedia.md) |
| [conditions_of_use](conditions_of_use.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The holder's terms of use, as written, with no permission inferred from them. | [PublicMedia](PublicMedia.md) |
| [rights](rights.md) | 0..1 <br/> [String](String.md) | The rights statement or licence that applies, by its address; when absent, copyright not evaluated. | [PublicMedia](PublicMedia.md) |
| [cleared](cleared.md) | 0..1 <br/> [MediaDecision](MediaDecision.md) | Who cleared the medium for the site, by role, and on what day. | [PublicMedia](PublicMedia.md) |
| [withdrawn](withdrawn.md) | 0..1 <br/> [MediaWithdrawal](MediaWithdrawal.md) | That the medium was withdrawn, on what day and why. | [PublicMedia](PublicMedia.md) |
| [link](link.md) | 0..1 <br/> [String](String.md) | For sound or film: the page on the holder's own host where it can be heard or seen. | [PublicMedia](PublicMedia.md) |
| [derived](derived.md) | 1..* <br/> [MediaDerivative](MediaDerivative.md) | The served copies of the picture, one for each exported width. | [PublicMedia](PublicMedia.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:Instantiation |
| native | pc:Media |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Media
description: 'One held or linked copy of a registered source, as the shared record
  keeps it: all that the public may see, with the private master file and the private
  permission besides.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
is_a: PublicMedia
attributes:
  master:
    name: master
    description: Where the private master file is kept; never public.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_master
    domain_of:
    - Media
    range: MediaMaster
    inlined: true
  consent:
    name: consent
    description: The private record of the permission to show the medium; never public.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_consent
    domain_of:
    - Media
    range: MediaConsent
    inlined: true
class_uri: rico:Instantiation

```
</details>

### Induced

<details>
```yaml
name: Media
description: 'One held or linked copy of a registered source, as the shared record
  keeps it: all that the public may see, with the private master file and the private
  permission besides.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
is_a: PublicMedia
attributes:
  master:
    name: master
    description: Where the private master file is kept; never public.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_master
    owner: Media
    domain_of:
    - Media
    range: MediaMaster
    inlined: true
  consent:
    name: consent
    description: The private record of the permission to show the medium; never public.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_consent
    owner: Media
    domain_of:
    - Media
    range: MediaConsent
    inlined: true
  id:
    name: id
    description: 'The medium''s id: lowercase letters and digits in parts joined by
      hyphens.'
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    owner: Media
    domain_of:
    - PublicMedia
    range: string
    required: true
    pattern: ^[a-z0-9]+(?:-[a-z0-9]+)*$(?![\s\S])
  source_id:
    name: source_id
    description: The source this medium is a copy of, by its id; never the person
      shown.
    from_schema: https://pruzhany.org/ns/media
    slot_uri: rico:isOrWasInstantiationOf
    owner: Media
    domain_of:
    - MediaFamilyWords
    - PublicMedia
    range: NonBlankText
    required: true
  kind:
    name: kind
    description: 'What the medium is: image, audio, video or document.'
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: rico:hasRepresentationType
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaKind
    required: true
  caption:
    name: caption
    description: The caption the site shows, with its language and review.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_caption
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaText
    required: true
    inlined: true
  alt:
    name: alt
    description: The description for screen readers of what is visible; required for
      images and documents.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_alt
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaText
    inlined: true
  inscription:
    name: inscription
    description: The object's own words, such as writing on the back of a photograph.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_inscription
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaText
    inlined: true
  transcript:
    name: transcript
    description: A document's full text; required for documents.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_transcript
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaText
    inlined: true
  family_words:
    name: family_words
    description: The family's words about the medium, quoted from a source.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_family_words
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaFamilyWords
    inlined: true
  depicted:
    name: depicted
    description: The people the picture shows, identified or not, and where.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_depicted
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaDepicted
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  shows_unidentified:
    name: shows_unidentified
    description: True when the picture shows people not identified.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_shows_unidentified
    owner: Media
    domain_of:
    - PublicMedia
    range: boolean
    required: true
  width:
    name: width
    description: The master's width in pixels, after orientation.
    from_schema: https://pruzhany.org/ns/media
    slot_uri: rico:width
    owner: Media
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
  height:
    name: height
    description: The master's height in pixels, after orientation.
    from_schema: https://pruzhany.org/ns/media
    slot_uri: rico:height
    owner: Media
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
  duration:
    name: duration
    description: The master's length in seconds, for sound and film.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_duration
    owner: Media
    domain_of:
    - PublicMedia
    range: NonNegativeNumber
  credit:
    name: credit
    description: The holder's or the family's credit, as they word it.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_credit
    owner: Media
    domain_of:
    - PublicMedia
    range: NonBlankText
    required: true
  conditions_of_access:
    name: conditions_of_access
    description: The holder's terms of access, as written.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: rico:conditionsOfAccess
    owner: Media
    domain_of:
    - PublicMedia
    range: NonBlankText
  conditions_of_use:
    name: conditions_of_use
    description: The holder's terms of use, as written, with no permission inferred
      from them.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: rico:conditionsOfUse
    owner: Media
    domain_of:
    - PublicMedia
    range: NonBlankText
  rights:
    name: rights
    description: The rights statement or licence that applies, by its address; when
      absent, copyright not evaluated.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_rights
    owner: Media
    domain_of:
    - PublicMedia
    range: string
    equals_string_in:
    - http://rightsstatements.org/vocab/InC/1.0/
    - http://rightsstatements.org/vocab/InC-OW-EU/1.0/
    - http://rightsstatements.org/vocab/InC-EDU/1.0/
    - http://rightsstatements.org/vocab/InC-NC/1.0/
    - http://rightsstatements.org/vocab/InC-RUU/1.0/
    - http://rightsstatements.org/vocab/NoC-CR/1.0/
    - http://rightsstatements.org/vocab/NoC-NC/1.0/
    - http://rightsstatements.org/vocab/NoC-OKLR/1.0/
    - http://rightsstatements.org/vocab/NoC-US/1.0/
    - http://rightsstatements.org/vocab/CNE/1.0/
    - http://rightsstatements.org/vocab/UND/1.0/
    - http://rightsstatements.org/vocab/NKC/1.0/
    - https://creativecommons.org/licenses/by/4.0/
    - https://creativecommons.org/licenses/by-sa/4.0/
    - https://creativecommons.org/licenses/by-nd/4.0/
    - https://creativecommons.org/licenses/by-nc/4.0/
    - https://creativecommons.org/licenses/by-nc-sa/4.0/
    - https://creativecommons.org/licenses/by-nc-nd/4.0/
    - https://creativecommons.org/publicdomain/zero/1.0/
    - https://creativecommons.org/publicdomain/mark/1.0/
  cleared:
    name: cleared
    description: Who cleared the medium for the site, by role, and on what day.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_clearance
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaDecision
    inlined: true
  withdrawn:
    name: withdrawn
    description: That the medium was withdrawn, on what day and why.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_withdrawn
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaWithdrawal
    inlined: true
  link:
    name: link
    description: 'For sound or film: the page on the holder''s own host where it can
      be heard or seen.'
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_link
    owner: Media
    domain_of:
    - PublicMedia
    range: string
    pattern: ^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$(?![\s\S])
  derived:
    name: derived
    description: The served copies of the picture, one for each exported width.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    slot_uri: pc:media_derived
    owner: Media
    domain_of:
    - PublicMedia
    range: MediaDerivative
    multivalued: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
class_uri: rico:Instantiation

```
</details></div>
