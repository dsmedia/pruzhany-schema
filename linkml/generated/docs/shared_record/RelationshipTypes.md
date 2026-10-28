---
search:
  boost: 2.0
---


# Enum: RelationshipTypes 




_Relationship types: the values of relationship_types in vocabulary/sourced-entities.json, version 1.3.0._



<div data-search-exclude markdown="1">

URI: [pc:RelationshipTypes](https://pruzhany.org/ns/sourced-entities#RelationshipTypes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| child_in_law | rico:hasFamilyAssociationWith | The subject is child in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Child-in-law<br>|
| child_of | rico:isChildOf | The subject is child of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Child of<br>|
| colleague | rico:isAgentAssociatedWithAgent | The subject is colleague of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Colleague<br>|
| cousin | rico:hasFamilyAssociationWith | The subject is cousin of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Cousin<br>|
| family_member | rico:hasFamilyAssociationWith | The subject is family member of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Family member (unspecified)<br>|
| friend | rico:isAgentAssociatedWithAgent | The subject is friend of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Friend<br>|
| grandchild_of | rico:hasAncestor | The subject is grandchild of the related person; direction is descendant to ascendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | Title: Grandchild of<br>|
| grandparent_of | rico:hasDescendant | The subject is grandparent of the related person; direction is ascendant to descendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | Title: Grandparent of<br>|
| in_law | rico:hasFamilyAssociationWith | The subject is in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: In-law (Mechutan)<br>|
| nephew_niece_of | rico:hasFamilyAssociationWith | The subject is nephew niece of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Nephew/Niece of<br>|
| parent_in_law | rico:hasFamilyAssociationWith | The subject is parent in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Parent-in-law<br>|
| parent_of | rico:hasChild | The subject is parent of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Parent of<br>|
| sibling | rico:hasSibling | The subject is sibling of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Sibling<br>|
| sibling_in_law | rico:hasFamilyAssociationWith | The subject is sibling in law of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Sibling-in-law<br>|
| spouse | rico:hasOrHadSpouse | The subject is spouse of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Spouse<br>|
| student_of | rico:hasOrHadTeacher | The subject is student of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Student of<br>|
| teacher_of | rico:hasOrHadStudent | The subject is teacher of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Teacher of<br>|
| uncle_aunt_of | rico:hasFamilyAssociationWith | The subject is uncle aunt of of the related person; direction is subject to related person. The specific relationship is retained by this vocabulary ID even when RiC-O provides only a broader association. | Title: Uncle/Aunt of<br>|
| great_grandparent_of | rico:hasDescendant | The subject is great-grandparent of the related person; direction is ascendant to descendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | Title: Great-grandparent of<br>|
| great_grandchild_of | rico:hasAncestor | The subject is great-grandchild of the related person; direction is descendant to ascendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation covers descent across any number of intermediate persons. | Title: Great-grandchild of<br>|




## Slots

| Name | Description |
| ---  | --- |
| [relationship_type](relationship_type.md) | For kinship: how the relative is related, from the subject to the relative. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record






## LinkML Source

<details>
```yaml
name: RelationshipTypes
description: 'Relationship types: the values of relationship_types in vocabulary/sourced-entities.json,
  version 1.3.0.'
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
permissible_values:
  child_in_law:
    text: child_in_law
    description: The subject is child in law of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Child-in-law
  child_of:
    text: child_of
    description: The subject is child of of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:isChildOf
    annotations:
      via:
        tag: via
        value: rico:ChildRelation
    title: Child of
  colleague:
    text: colleague
    description: The subject is colleague of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:isAgentAssociatedWithAgent
    annotations:
      via:
        tag: via
        value: rico:AgentToAgentRelation
    title: Colleague
  cousin:
    text: cousin
    description: The subject is cousin of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Cousin
  family_member:
    text: family_member
    description: The subject is family member of the related person; direction is
      subject to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Family member (unspecified)
  friend:
    text: friend
    description: The subject is friend of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:isAgentAssociatedWithAgent
    annotations:
      via:
        tag: via
        value: rico:AgentToAgentRelation
    title: Friend
  grandchild_of:
    text: grandchild_of
    description: The subject is grandchild of the related person; direction is descendant
      to ascendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation
      covers descent across any number of intermediate persons.
    meaning: rico:hasAncestor
    annotations:
      via:
        tag: via
        value: rico:DescendanceRelation
    title: Grandchild of
  grandparent_of:
    text: grandparent_of
    description: The subject is grandparent of the related person; direction is ascendant
      to descendant. The vocabulary ID retains the exact generation; RiC-O DescendanceRelation
      covers descent across any number of intermediate persons.
    meaning: rico:hasDescendant
    annotations:
      via:
        tag: via
        value: rico:DescendanceRelation
    title: Grandparent of
  in_law:
    text: in_law
    description: The subject is in law of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: In-law (Mechutan)
  nephew_niece_of:
    text: nephew_niece_of
    description: The subject is nephew niece of of the related person; direction is
      subject to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Nephew/Niece of
  parent_in_law:
    text: parent_in_law
    description: The subject is parent in law of the related person; direction is
      subject to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Parent-in-law
  parent_of:
    text: parent_of
    description: The subject is parent of of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasChild
    annotations:
      via:
        tag: via
        value: rico:ChildRelation
    title: Parent of
  sibling:
    text: sibling
    description: The subject is sibling of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasSibling
    annotations:
      via:
        tag: via
        value: rico:SiblingRelation
    title: Sibling
  sibling_in_law:
    text: sibling_in_law
    description: The subject is sibling in law of the related person; direction is
      subject to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Sibling-in-law
  spouse:
    text: spouse
    description: The subject is spouse of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasOrHadSpouse
    annotations:
      via:
        tag: via
        value: rico:SpouseRelation
    title: Spouse
  student_of:
    text: student_of
    description: The subject is student of of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasOrHadTeacher
    annotations:
      via:
        tag: via
        value: rico:TeachingRelation
    title: Student of
  teacher_of:
    text: teacher_of
    description: The subject is teacher of of the related person; direction is subject
      to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasOrHadStudent
    annotations:
      via:
        tag: via
        value: rico:TeachingRelation
    title: Teacher of
  uncle_aunt_of:
    text: uncle_aunt_of
    description: The subject is uncle aunt of of the related person; direction is
      subject to related person. The specific relationship is retained by this vocabulary
      ID even when RiC-O provides only a broader association.
    meaning: rico:hasFamilyAssociationWith
    annotations:
      via:
        tag: via
        value: rico:FamilyRelation
    title: Uncle/Aunt of
  great_grandparent_of:
    text: great_grandparent_of
    description: The subject is great-grandparent of the related person; direction
      is ascendant to descendant. The vocabulary ID retains the exact generation;
      RiC-O DescendanceRelation covers descent across any number of intermediate persons.
    meaning: rico:hasDescendant
    annotations:
      via:
        tag: via
        value: rico:DescendanceRelation
    title: Great-grandparent of
  great_grandchild_of:
    text: great_grandchild_of
    description: The subject is great-grandchild of the related person; direction
      is descendant to ascendant. The vocabulary ID retains the exact generation;
      RiC-O DescendanceRelation covers descent across any number of intermediate persons.
    meaning: rico:hasAncestor
    annotations:
      via:
        tag: via
        value: rico:DescendanceRelation
    title: Great-grandchild of

```
</details>

</div>
