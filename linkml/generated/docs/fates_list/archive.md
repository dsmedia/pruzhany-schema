---
search:
  boost: 5.0
---

# Slot: archive 

<div data-search-exclude markdown="1">



URI: [pc:archive](https://pruzhany.org/ns/sourced-entities#archive)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FatesListOutsideRecord](FatesListOutsideRecord.md) | A record an archive holds about the person: the archive, the database it is in, the record's type and id as the archive gives them, and its own address where the record has one. |  no  |
| [FatesListArchiveCount](FatesListArchiveCount.md) | How many people an archive's database names, and how many of them with an address. |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FatesListOutsideRecord](FatesListOutsideRecord.md), [FatesListArchiveCount](FatesListArchiveCount.md) |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:archive |
| native | pc:archive |




## LinkML Source

<details>
```yaml
name: archive
domain_of:
- FatesListOutsideRecord
- FatesListArchiveCount
range: string

```
</details></div>
