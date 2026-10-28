---
search:
  boost: 2.0
---


# Enum: MediaKind 




_What a medium is: an image, a sound recording, a film or a document._



<div data-search-exclude markdown="1">

URI: [pc:MediaKind](https://pruzhany.org/ns/sourced-entities#MediaKind)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| image | pc:media_image | A still picture, such as a photograph. |
| audio | pc:media_audio | A sound recording. |
| video | pc:media_video | A film or video. |
| document | pc:media_document | A document, with its transcript. |




## Slots

| Name | Description |
| ---  | --- |
| [kind](kind.md) | What the medium is: image, audio, video or document. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/media






## LinkML Source

<details>
```yaml
name: MediaKind
description: 'What a medium is: an image, a sound recording, a film or a document.'
from_schema: https://pruzhany.org/ns/media
rank: 1000
permissible_values:
  image:
    text: image
    description: A still picture, such as a photograph.
    meaning: pc:media_image
  audio:
    text: audio
    description: A sound recording.
    meaning: pc:media_audio
  video:
    text: video
    description: A film or video.
    meaning: pc:media_video
  document:
    text: document
    description: A document, with its transcript.
    meaning: pc:media_document

```
</details>

</div>
