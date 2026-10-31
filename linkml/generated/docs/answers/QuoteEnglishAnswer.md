---
search:
  boost: 10.0
---

# Class: Answer (QuoteEnglishAnswer) 


_The answer about a batch of quotations: every quotation it was sent, by its number._



<div data-search-exclude markdown="1">



URI: [pc:QuoteEnglishAnswer](https://pruzhany.org/ns/sourced-entities#QuoteEnglishAnswer)





```mermaid
 classDiagram
    class QuoteEnglishAnswer
    click QuoteEnglishAnswer href "../QuoteEnglishAnswer/"
      QuoteEnglishAnswer : quotations
        
          
    
        
        
        QuoteEnglishAnswer --> "1..*" QuoteEnglishQuotedEnglish : quotations
        click QuoteEnglishQuotedEnglish href "../QuoteEnglishQuotedEnglish/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [quotations](quotations.md) | 1..* <br/> [QuoteEnglishQuotedEnglish](QuoteEnglishQuotedEnglish.md) | The quotations field in the Answer response. | direct |















## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| asking | quote_english |




### Schema Source


* from schema: https://pruzhany.org/ns/answers




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:QuoteEnglishAnswer |
| native | pc:QuoteEnglishAnswer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QuoteEnglishAnswer
annotations:
  asking:
    tag: asking
    value: quote_english
description: 'The answer about a batch of quotations: every quotation it was sent,
  by its number.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  quotations:
    name: quotations
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The quotations field in the Answer response.
    title: Quotations
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    domain_of:
    - QuoteEnglishAnswer
    range: QuoteEnglishQuotedEnglish
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>

### Induced

<details>
```yaml
name: QuoteEnglishAnswer
annotations:
  asking:
    tag: asking
    value: quote_english
description: 'The answer about a batch of quotations: every quotation it was sent,
  by its number.'
title: Answer
from_schema: https://pruzhany.org/ns/answers
rank: 1000
attributes:
  quotations:
    name: quotations
    annotations:
      description_in_wire:
        tag: description_in_wire
        value: false
    description: The quotations field in the Answer response.
    title: Quotations
    from_schema: https://pruzhany.org/ns/answers
    rank: 1000
    owner: QuoteEnglishAnswer
    domain_of:
    - QuoteEnglishAnswer
    range: QuoteEnglishQuotedEnglish
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details></div>
