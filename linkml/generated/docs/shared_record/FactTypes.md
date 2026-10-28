---
search:
  boost: 2.0
---


# Enum: FactTypes 




_Fact types: the values of fact_types in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:FactTypes](https://pruzhany.org/ns/sourced-entities#FactTypes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| birth | rico:hasBirthDate | A sourced birth date; a birth place uses rico:hasBirthPlace independently, including when no date is known. | Title: Birth<br>|
| death | rico:hasDeathDate | A sourced death date; a death place uses rico:hasDeathPlace independently, including when no date is known. | Title: Death<br>|
| residence | rico:hasOrHadLocation | Residence in a place at a specified time. | Title: Residence<br>|
| occupation | rico:hasOrHadOccupationOfType | An occupation, optionally bounded in time. | Title: Occupation<br>|
| office | rico:occupiesOrOccupied | Holding a Position at a time; person occupiesOrOccupied the position, qualified through PositionHoldingRelation. | Title: Office<br>|
| membership | rico:isOrWasMemberOf | A person isOrWasMemberOf a group, inverse of group hasOrHadMember, qualified through MembershipRelation. | Title: Membership<br>|
| education | pc:fact_types_education | School attendance or education at a specified time. | Title: Education<br>|
| emigration | pc:fact_types_emigration | A dated departure to live elsewhere; establishes neither death nor survival. | Title: Emigration<br>|
| survival | pc:fact_types_survival | Evidence that a person was alive at a specified time. | Title: Survival<br>|
| parenthood | pc:fact_types_parenthood | Parenthood of an unnamed child without inventing a person node; claims naming a relative use kinship, and links between identified people use relationships. Deprecated in 1.2.0: represent the child as a person and link each parent by parent_of. | Title: Parenthood<br> **DEPRECATED**|
| ghetto_role | pc:fact_types_ghetto_role | A sourced ghetto activity not expressible as membership or office; use membership or office whenever those fit. | Title: Ghetto role<br>|
| partisan_service | pc:fact_types_partisan_service | A sourced partisan activity beyond membership or office; use membership or office whenever those fit. | Title: Partisan service<br>|
| deportation | pc:fact_types_deportation | A sourced forced removal at a date and place; event participation may link its event. | Title: Deportation<br>|
| burial | pc:fact_types_burial | A sourced interment, optionally dated and placed; distinct from death. | Title: Burial<br>|
| commemoration | pc:fact_types_commemoration | A sourced act of remembrance; event participation may link its event. | Title: Commemoration<br>|
| event_participation | rico:isOrWasParticipantIn | Taking part in an event with an explicit mention role; weddings are events, not marriage facts. | Title: Event participation<br>|
| other | pc:fact_types_other | An assertion awaiting an owner-approved type; requires a nonempty proposed_type. | Title: Other<br>|
| kinship | rico:hasFamilyAssociationWith | A source's statement that the person is related, in a stated way, to a named person who need not be identified | Title: Kinship<br>|




## Slots

| Name | Description |
| ---  | --- |
| [type](type.md) | kinship for a released relationship type; other, with a proposed type, for one not yet released. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: FactTypes
description: 'Fact types: the values of fact_types in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  birth:
    text: birth
    description: A sourced birth date; a birth place uses rico:hasBirthPlace independently,
      including when no date is known.
    meaning: rico:hasBirthDate
    title: Birth
  death:
    text: death
    description: A sourced death date; a death place uses rico:hasDeathPlace independently,
      including when no date is known.
    meaning: rico:hasDeathDate
    title: Death
  residence:
    text: residence
    description: Residence in a place at a specified time.
    meaning: rico:hasOrHadLocation
    title: Residence
  occupation:
    text: occupation
    description: An occupation, optionally bounded in time.
    meaning: rico:hasOrHadOccupationOfType
    title: Occupation
  office:
    text: office
    description: Holding a Position at a time; person occupiesOrOccupied the position,
      qualified through PositionHoldingRelation.
    meaning: rico:occupiesOrOccupied
    annotations:
      via:
        tag: via
        value: rico:PositionHoldingRelation
    title: Office
  membership:
    text: membership
    description: A person isOrWasMemberOf a group, inverse of group hasOrHadMember,
      qualified through MembershipRelation.
    meaning: rico:isOrWasMemberOf
    annotations:
      via:
        tag: via
        value: rico:MembershipRelation
    title: Membership
  education:
    text: education
    description: School attendance or education at a specified time.
    meaning: pc:fact_types_education
    title: Education
    comments:
    - TeachingRelation identifies teaching rather than establishing school attendance;
      retain attendance without asserting a teacher relationship.
  emigration:
    text: emigration
    description: A dated departure to live elsewhere; establishes neither death nor
      survival.
    meaning: pc:fact_types_emigration
    title: Emigration
    comments:
    - RiC-O MigrationRelation concerns instantiations, not migration of people.
  survival:
    text: survival
    description: Evidence that a person was alive at a specified time.
    meaning: pc:fact_types_survival
    title: Survival
    comments:
    - No dedicated pinned relation expresses evidence of being alive at a time.
  parenthood:
    text: parenthood
    description: 'Parenthood of an unnamed child without inventing a person node;
      claims naming a relative use kinship, and links between identified people use
      relationships. Deprecated in 1.2.0: represent the child as a person and link
      each parent by parent_of.'
    meaning: pc:fact_types_parenthood
    title: Parenthood
    deprecated: 'Deprecated in 1.2.0; replaced by parent_of in relationship_types:
      Replace this fact with a parent_of relation from each parent to the child as
      a person; use a supplied name when the source does not name the child.'
    comments:
    - Preserves an unnamed child without inventing a person node for a child relation.
  ghetto_role:
    text: ghetto_role
    description: A sourced ghetto activity not expressible as membership or office;
      use membership or office whenever those fit.
    meaning: pc:fact_types_ghetto_role
    title: Ghetto role
    comments:
    - No precise pinned counterpart for residual ghetto activities beyond membership
      or office.
  partisan_service:
    text: partisan_service
    description: A sourced partisan activity beyond membership or office; use membership
      or office whenever those fit.
    meaning: pc:fact_types_partisan_service
    title: Partisan service
    comments:
    - No precise pinned counterpart for residual partisan activities beyond membership
      or office.
  deportation:
    text: deportation
    description: A sourced forced removal at a date and place; event participation
      may link its event.
    meaning: pc:fact_types_deportation
    title: Deportation
    comments:
    - No dedicated pinned term captures forced removal of a person.
  burial:
    text: burial
    description: A sourced interment, optionally dated and placed; distinct from death.
    meaning: pc:fact_types_burial
    title: Burial
    comments:
    - No dedicated pinned term captures interment of a person.
  commemoration:
    text: commemoration
    description: A sourced act of remembrance; event participation may link its event.
    meaning: pc:fact_types_commemoration
    title: Commemoration
    comments:
    - No dedicated pinned term captures an act of remembrance of a person.
  event_participation:
    text: event_participation
    description: Taking part in an event with an explicit mention role; weddings are
      events, not marriage facts.
    meaning: rico:isOrWasParticipantIn
    title: Event participation
  other:
    text: other
    description: An assertion awaiting an owner-approved type; requires a nonempty
      proposed_type.
    meaning: pc:fact_types_other
    title: Other
    comments:
    - Retains an assertion pending owner approval of a specific type and mapping.
  kinship:
    text: kinship
    description: A source's statement that the person is related, in a stated way,
      to a named person who need not be identified
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Kinship

```
</details>

</div>
