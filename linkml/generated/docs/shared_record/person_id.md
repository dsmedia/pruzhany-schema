---
search:
  boost: 5.0
---

# Slot: person_id 

<div data-search-exclude markdown="1">



URI: [pc:person_id](https://pruzhany.org/ns/sourced-entities#person_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LifeEventMainPerson](LifeEventMainPerson.md) | One main person of a life event and their part in it (the baby, a parent, the bride, the groom, the boy, the one who died, the one remembered); each part means a declared local subproperty of rico:affectsOrAffected or rico:hasOrHadParticipant (EventParts). |  no  |
| [Mention](Mention.md) | The older form of a person's mention in a piece of the paper: the person, the piece, the name as printed and the person's role there. The site's current mention is IssueMention. |  no  |
| [MediaDepicted](MediaDepicted.md) | One person a picture shows, identified or not, where in the picture, and on whose identification. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [LifeEventMainPerson](LifeEventMainPerson.md), [Mention](Mention.md), [MediaDepicted](MediaDepicted.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:person_id |
| native | pc:person_id |




## LinkML Source

<details>
```yaml
name: person_id
domain_of:
- LifeEventMainPerson
- Mention
- MediaDepicted
range: string

```
</details></div>
