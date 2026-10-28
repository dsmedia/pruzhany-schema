---
search:
  boost: 10.0
---

# Class: MediaDerivative 


_One served copy of a picture: a WebP file at one of the exported widths, named by the master's digest, made by resizing alone._



<div data-search-exclude markdown="1">



URI: [pc:MediaDerivative](https://pruzhany.org/ns/sourced-entities#MediaDerivative)





```mermaid
 classDiagram
    class MediaDerivative
    click MediaDerivative href "../MediaDerivative/"
      MediaDerivative : height
        
      MediaDerivative : process
        
      MediaDerivative : url
        
      MediaDerivative : width
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [url](url.md) | 1 <br/> [String](String.md) | The copy's address, ending in its nominal width (zod/media-widths.json). | direct |
| [width](width.md) | 1 <br/> [PositiveInteger](PositiveInteger.md) | The copy's actual width in pixels. | direct |
| [height](height.md) | 1 <br/> [PositiveInteger](PositiveInteger.md) | The copy's actual height in pixels. | direct |
| [process](process.md) | 1 <br/> [String](String.md) | How the copy was made: resizing alone. | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PublicMedia](PublicMedia.md) | [derived](derived.md) | range | [MediaDerivative](MediaDerivative.md) |
| [Media](Media.md) | [derived](derived.md) | range | [MediaDerivative](MediaDerivative.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pc:MediaDerivative |
| native | pc:MediaDerivative |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MediaDerivative
description: 'One served copy of a picture: a WebP file at one of the exported widths,
  named by the master''s digest, made by resizing alone.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
attributes:
  url:
    name: url
    description: The copy's address, ending in its nominal width (zod/media-widths.json).
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    domain_of:
    - MediaDerivative
    range: string
    required: true
    pattern: ^https://pictures\.pruzhanychronicles\.org/media/[0-9a-f]{64}-w(?:100|400|800|1200)\.webp$(?![\s\S])
  width:
    name: width
    description: The copy's actual width in pixels.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
    required: true
  height:
    name: height
    description: The copy's actual height in pixels.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
    required: true
  process:
    name: process
    description: 'How the copy was made: resizing alone.'
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    domain_of:
    - MediaDerivative
    range: string
    required: true
    equals_string: resize

```
</details>

### Induced

<details>
```yaml
name: MediaDerivative
description: 'One served copy of a picture: a WebP file at one of the exported widths,
  named by the master''s digest, made by resizing alone.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
attributes:
  url:
    name: url
    description: The copy's address, ending in its nominal width (zod/media-widths.json).
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    owner: MediaDerivative
    domain_of:
    - MediaDerivative
    range: string
    required: true
    pattern: ^https://pictures\.pruzhanychronicles\.org/media/[0-9a-f]{64}-w(?:100|400|800|1200)\.webp$(?![\s\S])
  width:
    name: width
    description: The copy's actual width in pixels.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    owner: MediaDerivative
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
    required: true
  height:
    name: height
    description: The copy's actual height in pixels.
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    owner: MediaDerivative
    domain_of:
    - MediaDerivative
    - PublicMedia
    range: PositiveInteger
    required: true
  process:
    name: process
    description: 'How the copy was made: resizing alone.'
    from_schema: https://pruzhany.org/ns/media
    rank: 1000
    owner: MediaDerivative
    domain_of:
    - MediaDerivative
    range: string
    required: true
    equals_string: resize

```
</details></div>
