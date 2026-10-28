---
search:
  boost: 10.0
---

# Class: SharedFact 


_One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it._



<div data-search-exclude markdown="1">



URI: [pc:SharedFact](https://pruzhany.org/ns/sourced-entities#SharedFact)





```mermaid
 classDiagram
    class SharedFact
    click SharedFact href "../SharedFact/"
      Fact <|-- SharedFact
        click Fact href "../Fact/"
      
      SharedFact : attribution
        
          
    
        
        
        SharedFact --> "1" Attribution : attribution
        click Attribution href "../Attribution/"
    

        
      SharedFact : citations
        
          
    
        
        
        SharedFact --> "1..*" SiteCitation : citations
        click SiteCitation href "../SiteCitation/"
    

        
      SharedFact : date
        
          
    
        
        
        SharedFact --> "0..1" SourcedDate : date
        click SourcedDate href "../SourcedDate/"
    

        
      SharedFact : event_id
        
      SharedFact : evidence_confidence
        
          
    
        
        
        SharedFact --> "1" Confidence : evidence_confidence
        click Confidence href "../Confidence/"
    

        
      SharedFact : family_id
        
      SharedFact : holocaust_related
        
      SharedFact : id
        
      SharedFact : identity_confidence
        
          
    
        
        
        SharedFact --> "1" Confidence : identity_confidence
        click Confidence href "../Confidence/"
    

        
      SharedFact : organization_id
        
      SharedFact : place_id
        
      SharedFact : proposed_type
        
      SharedFact : qualifiers
        
          
    
        
        
        SharedFact --> "0..1" FactQualifiers : qualifiers
        click FactQualifiers href "../FactQualifiers/"
    

        
      SharedFact : related_name
        
      SharedFact : related_person_id
        
      SharedFact : relationship_type
        
          
    
        
        
        SharedFact --> "0..1" RelationshipTypes : relationship_type
        click RelationshipTypes href "../RelationshipTypes/"
    

        
      SharedFact : representation
        
          
    
        
        
        SharedFact --> "1" SharedFactRepresentation : representation
        click SharedFactRepresentation href "../SharedFactRepresentation/"
    

        
      SharedFact : review
        
          
    
        
        
        SharedFact --> "1" Review : review
        click Review href "../Review/"
    

        
      SharedFact : status
        
          
    
        
        
        SharedFact --> "1" ClaimStatus : status
        click ClaimStatus href "../ClaimStatus/"
    

        
      SharedFact : subject_id
        
      SharedFact : type
        
          
    
        
        
        SharedFact --> "1" FactTypes : type
        click FactTypes href "../FactTypes/"
    

        
      SharedFact : value
        
      
```





## Inheritance
* [Fact](Fact.md)
    * **SharedFact**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [citations](citations.md) | 1..* <br/> [SiteCitation](SiteCitation.md) | The evidence: where in which sources the statement is found. | direct |
| [subject_id](subject_id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | Whose statement it is: a person, a family, a place, an organisation, an event or a relation, by its id. | direct |
| [family_id](family_id.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The family the statement concerns, by its id; on a membership fact, the family the person belongs to. | direct |
| [representation](representation.md) | 1 <br/> [SharedFactRepresentation](SharedFactRepresentation.md) | The form the statement is kept in: structured, prose or an image path. | direct |
| [id](id.md) | 1 <br/> [NonBlankText](NonBlankText.md) | The fact's id in the record. | [Fact](Fact.md) |
| [type](type.md) | 1 <br/> [FactTypes](FactTypes.md) | What the statement is about: a birth, a death, a residence, an occupation and so on. | [Fact](Fact.md) |
| [proposed_type](proposed_type.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | For a statement of type other: the type proposed for it, awaiting the owner's approval. | [Fact](Fact.md) |
| [value](value.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The statement's words or value, such as an occupation. | [Fact](Fact.md) |
| [date](date.md) | 0..1 <br/> [SourcedDate](SourcedDate.md) | When, as the source gives it. | [Fact](Fact.md) |
| [place_id](place_id.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | Where, by the place's id in the record. | [Fact](Fact.md) |
| [organization_id](organization_id.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The organisation the statement concerns, by its id in the record. | [Fact](Fact.md) |
| [event_id](event_id.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | The life event the statement concerns, by its id in the record. | [Fact](Fact.md) |
| [related_person_id](related_person_id.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | For kinship: the relative, by the person's id in the record. | [Fact](Fact.md) |
| [relationship_type](relationship_type.md) | 0..1 <br/> [RelationshipTypes](RelationshipTypes.md) | For kinship: how the relative is related, from the subject to the relative. | [Fact](Fact.md) |
| [related_name](related_name.md) | 0..1 <br/> [NonBlankText](NonBlankText.md) | For kinship: the relative's name, where the relative has no person of their own. | [Fact](Fact.md) |
| [qualifiers](qualifiers.md) | 0..1 <br/> [FactQualifiers](FactQualifiers.md) | More about the statement, as named texts. | [Fact](Fact.md) |
| [holocaust_related](holocaust_related.md) | 0..1 <br/> [Boolean](Boolean.md) | True when the statement concerns the Holocaust. | [Fact](Fact.md) |
| [evidence_confidence](evidence_confidence.md) | 1 <br/> [Confidence](Confidence.md) | How sure the evidence makes the statement. | [Fact](Fact.md) |
| [identity_confidence](identity_confidence.md) | 1 <br/> [Confidence](Confidence.md) | How sure it is that the statement is about this person. | [Fact](Fact.md) |
| [status](status.md) | 1 <br/> [ClaimStatus](ClaimStatus.md) | The statement's standing: proposed, accepted, disputed or rejected. | [Fact](Fact.md) |
| [review](review.md) | 1 <br/> [Review](Review.md) | Whether a person has reviewed the statement. | [Fact](Fact.md) |
| [attribution](attribution.md) | 1 <br/> [Attribution](Attribution.md) | Who recorded the statement, and on what day. | [Fact](Fact.md) |

<details>
<summary>Expressions & Logic</summary>
#### None Of

The class must not satisfy any of:
- AnonymousClassExpression({
  'description': ('A shared fact is never a parenthood, which is a parent_of relation to the '
     'child as a person.'),
  'slot_conditions': {'type': SlotDefinition({'name': 'type', 'equals_string': 'parenthood'})}
})
- AnonymousClassExpression({
  'slot_conditions': {'proposed_type': SlotDefinition({'name': 'proposed_type', 'equals_string': 'parenthood'})}
})

</details>





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SharedRecord](SharedRecord.md) | [facts](facts.md) | range | [SharedFact](SharedFact.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'representation': {'equals_string_in': ['prose', 'image']}}``` |```{'value': {'required': True}}``` | |



### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'representation': {'equals_string_in': ['prose', 'image']}}``` |```{'type': {'equals_string': 'other'}}``` | |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:SharedFact |
| native | pc:SharedFact |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SharedFact
description: 'One source''s statement as the shared record keeps it: a fact with its
  subject, its form and its evidence located on the printed page where the site writer
  found it.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
is_a: Fact
attributes:
  citations:
    name: citations
    description: 'The evidence: where in which sources the statement is found.'
    from_schema: https://pruzhany.org/ns/shared_record
    domain_of:
    - SharedName
    - SharedFact
    - SourcedRelation
    - Fact
    - Name
    range: SiteCitation
    required: true
    multivalued: true
    inlined_as_list: true
    minimum_cardinality: 1
  subject_id:
    name: subject_id
    description: 'Whose statement it is: a person, a family, a place, an organisation,
      an event or a relation, by its id.'
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: pc:site_fact_subject
    domain_of:
    - SharedFact
    - SourcedRelation
    range: NonBlankText
    required: true
  family_id:
    name: family_id
    annotations:
      via:
        tag: via
        value: rico:MembershipRelation
    description: The family the statement concerns, by its id; on a membership fact,
      the family the person belongs to.
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: rico:isOrWasMemberOf
    domain_of:
    - SharedFact
    - SourcedRelation
    range: NonBlankText
  representation:
    name: representation
    description: 'The form the statement is kept in: structured, prose or an image
      path.'
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: pc:site_fact_representation
    domain_of:
    - SharedFact
    range: SharedFactRepresentation
    required: true
rules:
- preconditions:
    slot_conditions:
      representation:
        name: representation
        equals_string_in:
        - prose
        - image
  postconditions:
    slot_conditions:
      value:
        name: value
        required: true
  description: A prose or image fact has its value.
- preconditions:
    slot_conditions:
      representation:
        name: representation
        equals_string_in:
        - prose
        - image
  postconditions:
    slot_conditions:
      type:
        name: type
        equals_string: other
  description: A prose or image fact is of type other.
none_of:
- description: A shared fact is never a parenthood, which is a parent_of relation
    to the child as a person.
  slot_conditions:
    type:
      name: type
      equals_string: parenthood
- slot_conditions:
    proposed_type:
      name: proposed_type
      equals_string: parenthood

```
</details>

### Induced

<details>
```yaml
name: SharedFact
description: 'One source''s statement as the shared record keeps it: a fact with its
  subject, its form and its evidence located on the printed page where the site writer
  found it.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
is_a: Fact
attributes:
  citations:
    name: citations
    description: 'The evidence: where in which sources the statement is found.'
    from_schema: https://pruzhany.org/ns/shared_record
    owner: SharedFact
    domain_of:
    - SharedName
    - SharedFact
    - SourcedRelation
    - Fact
    - Name
    range: SiteCitation
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
    minimum_cardinality: 1
  subject_id:
    name: subject_id
    description: 'Whose statement it is: a person, a family, a place, an organisation,
      an event or a relation, by its id.'
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: pc:site_fact_subject
    owner: SharedFact
    domain_of:
    - SharedFact
    - SourcedRelation
    range: NonBlankText
    required: true
  family_id:
    name: family_id
    annotations:
      via:
        tag: via
        value: rico:MembershipRelation
    description: The family the statement concerns, by its id; on a membership fact,
      the family the person belongs to.
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: rico:isOrWasMemberOf
    owner: SharedFact
    domain_of:
    - SharedFact
    - SourcedRelation
    range: NonBlankText
  representation:
    name: representation
    description: 'The form the statement is kept in: structured, prose or an image
      path.'
    from_schema: https://pruzhany.org/ns/shared_record
    rank: 1000
    slot_uri: pc:site_fact_representation
    owner: SharedFact
    domain_of:
    - SharedFact
    range: SharedFactRepresentation
    required: true
  id:
    name: id
    description: The fact's id in the record.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SharedFact
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
  type:
    name: type
    description: 'What the statement is about: a birth, a death, a residence, an occupation
      and so on.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SharedFact
    domain_of:
    - SourcedRelation
    - SharedPlace
    - SharedEvent
    - Fact
    range: FactTypes
    required: true
  proposed_type:
    name: proposed_type
    description: 'For a statement of type other: the type proposed for it, awaiting
      the owner''s approval.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SharedFact
    domain_of:
    - SharedEvent
    - Fact
    range: NonBlankText
  value:
    name: value
    description: The statement's words or value, such as an occupation.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SharedFact
    domain_of:
    - PlaceIdentifier
    - Fact
    - Name
    range: NonBlankText
  date:
    name: date
    description: When, as the source gives it.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: SourcedDate
    inlined: true
  place_id:
    name: place_id
    description: Where, by the place's id in the record.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: NonBlankText
  organization_id:
    name: organization_id
    description: The organisation the statement concerns, by its id in the record.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: NonBlankText
  event_id:
    name: event_id
    description: The life event the statement concerns, by its id in the record.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: NonBlankText
  related_person_id:
    name: related_person_id
    description: 'For kinship: the relative, by the person''s id in the record.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: NonBlankText
  relationship_type:
    name: relationship_type
    description: 'For kinship: how the relative is related, from the subject to the
      relative.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: RelationshipTypes
  related_name:
    name: related_name
    description: 'For kinship: the relative''s name, where the relative has no person
      of their own.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: NonBlankText
  qualifiers:
    name: qualifiers
    description: More about the statement, as named texts.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: FactQualifiers
    inlined: true
  holocaust_related:
    name: holocaust_related
    description: True when the statement concerns the Holocaust.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: boolean
  evidence_confidence:
    name: evidence_confidence
    description: How sure the evidence makes the statement.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    slot_uri: rico:relationCertainty
    owner: SharedFact
    domain_of:
    - Fact
    range: Confidence
    required: true
  identity_confidence:
    name: identity_confidence
    description: How sure it is that the statement is about this person.
    from_schema: https://pruzhany.org/ns/sourced_entities
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: Confidence
    required: true
  status:
    name: status
    description: 'The statement''s standing: proposed, accepted, disputed or rejected.'
    from_schema: https://pruzhany.org/ns/sourced_entities
    related_mappings:
    - pc:site_standing
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    range: ClaimStatus
    required: true
  review:
    name: review
    description: Whether a person has reviewed the statement.
    from_schema: https://pruzhany.org/ns/sourced_entities
    related_mappings:
    - pc:site_standing
    rank: 1000
    owner: SharedFact
    domain_of:
    - Fact
    - Fate
    range: Review
    required: true
    inlined: true
  attribution:
    name: attribution
    description: Who recorded the statement, and on what day.
    from_schema: https://pruzhany.org/ns/sourced_entities
    owner: SharedFact
    domain_of:
    - PlaceIdentifier
    - Fact
    - Name
    - EnglishCheck
    - SuppliedTitle
    - Translation
    range: Attribution
    required: true
    inlined: true
rules:
- preconditions:
    slot_conditions:
      representation:
        name: representation
        equals_string_in:
        - prose
        - image
  postconditions:
    slot_conditions:
      value:
        name: value
        required: true
  description: A prose or image fact has its value.
- preconditions:
    slot_conditions:
      representation:
        name: representation
        equals_string_in:
        - prose
        - image
  postconditions:
    slot_conditions:
      type:
        name: type
        equals_string: other
  description: A prose or image fact is of type other.
none_of:
- description: A shared fact is never a parenthood, which is a parent_of relation
    to the child as a person.
  slot_conditions:
    type:
      name: type
      equals_string: parenthood
- slot_conditions:
    proposed_type:
      name: proposed_type
      equals_string: parenthood

```
</details></div>
