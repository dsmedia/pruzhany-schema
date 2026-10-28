---
search:
  boost: 5.0
---

# Slot: evidence_confidence 


_How sure the evidence makes the statement._



<div data-search-exclude markdown="1">



URI: [rico:relationCertainty](https://www.ica.org/standards/RiC/ontology#relationCertainty)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SharedFact](SharedFact.md) | One source's statement as the shared record keeps it: a fact with its subject, its form and its evidence located on the printed page where the site writer found it. |  no  |
| [SourcedRelation](SourcedRelation.md) | One source's statement that a person is related to another, from the subject to the relative, of a released kinship type, or of type other with a proposed type. |  no  |
| [Fact](Fact.md) | One source's statement about a person, a family or a relation, kept as that source gives it, with its evidence, its confidence, its standing and who recorded it. What it means depends on its type (see FactTypes). |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Confidence](Confidence.md) |
| Domain Of | [Fact](Fact.md) |
| Slot URI | [rico:relationCertainty](https://www.ica.org/standards/RiC/ontology#relationCertainty) |
### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |


### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Fact](Fact.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/shared_record




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rico:relationCertainty |
| native | pc:evidence_confidence |




## LinkML Source

<details>
```yaml
name: evidence_confidence
description: How sure the evidence makes the statement.
from_schema: https://pruzhany.org/ns/shared_record
rank: 1000
slot_uri: rico:relationCertainty
owner: Fact
domain_of:
- Fact
range: Confidence
required: true

```
</details></div>
