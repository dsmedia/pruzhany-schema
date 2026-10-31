---
search:
  boost: 2.0
---


# Enum: ContentItemSubtypes 




_Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json, version 1.1.0._



<div data-search-exclude markdown="1">

URI: [pc:ContentItemSubtypes](https://pruzhany.org/ns/sourced-entities#ContentItemSubtypes)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| wedding_greeting | pc:subtype_wedding_greeting | A greeting to a couple on their wedding. | Title: Wedding greeting<br>|
| engagement_greeting | pc:subtype_engagement_greeting | A greeting on an engagement. | Title: Engagement greeting<br>|
| birth_greeting | pc:subtype_birth_greeting | A greeting on the birth of a child. | Title: Birth greeting<br>|
| bar_mitzvah_greeting | pc:subtype_bar_mitzvah_greeting | A greeting on a bar mitzvah. | Title: Bar mitzvah greeting<br>|
| new_year_greeting | pc:subtype_new_year_greeting | A greeting for the New Year. | Title: New Year greeting<br>|
| departure_greeting | pc:subtype_departure_greeting | Good wishes on departure or settlement elsewhere. | Title: Departure greeting<br>|
| greeting | pc:subtype_greeting | A greeting whose occasion is not specified by a narrower form. | Title: Greeting<br>|
| thanks | pc:subtype_thanks | A public expression of thanks or acknowledgement. | Title: Thanks<br>|
| meeting_notice | pc:subtype_meeting_notice | A notice inviting people to a meeting. | Title: Meeting notice<br>|
| announcement | pc:subtype_announcement | A public announcement without a narrower established form. | Title: Announcement<br>|
| appeal | pc:subtype_appeal | A public request for support, contributions or participation. | Title: Appeal<br>|
| commercial_advertisement | pc:subtype_commercial_advertisement | An advertisement for goods, services or premises. | Title: Commercial advertisement<br>|
| condolence | pc:subtype_condolence | An expression of sympathy to mourners. | Title: Condolence<br>|
| memorial_notice | pc:subtype_memorial_notice | A notice commemorating someone who has died. | Title: Memorial notice<br>|
| death_announcement | pc:subtype_death_announcement | An announcement of a death or funeral. | Title: Death announcement<br>|
| editorial | pc:subtype_editorial | An editorial statement by the newspaper. | Title: Editorial<br>|
| opinion | pc:subtype_opinion | An argument or commentary expressing a view. | Title: Opinion<br>|
| letter | pc:subtype_letter | A letter printed for readers, including letters to the editor. | Title: Letter<br>|
| poem | pc:subtype_poem | A composition in verse. | Title: Poem<br>|
| sketch | pc:subtype_sketch | A short literary sketch. | Title: Sketch<br>|
| humour | pc:subtype_humour | A joke or short humorous composition. | Title: Humour<br>|




## Slots

| Name | Description |
| ---  | --- |
| [subtype](subtype.md) | The narrower form the content item takes within its kind, such as a wedding greeting within advertisements, where one is known. |










## Identifier and Mapping Information





### Schema Source


* from schema: https://pruzhany.org/ns/content_items






## LinkML Source

<details>
```yaml
name: ContentItemSubtypes
description: 'Content item subtypes: the values of content_item_subtypes in vocabulary/site-content.json,
  version 1.1.0.'
from_schema: https://pruzhany.org/ns/content_items
rank: 1000
permissible_values:
  wedding_greeting:
    text: wedding_greeting
    description: A greeting to a couple on their wedding.
    meaning: pc:subtype_wedding_greeting
    title: Wedding greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  engagement_greeting:
    text: engagement_greeting
    description: A greeting on an engagement.
    meaning: pc:subtype_engagement_greeting
    title: Engagement greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  birth_greeting:
    text: birth_greeting
    description: A greeting on the birth of a child.
    meaning: pc:subtype_birth_greeting
    title: Birth greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  bar_mitzvah_greeting:
    text: bar_mitzvah_greeting
    description: A greeting on a bar mitzvah.
    meaning: pc:subtype_bar_mitzvah_greeting
    title: Bar mitzvah greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  new_year_greeting:
    text: new_year_greeting
    description: A greeting for the New Year.
    meaning: pc:subtype_new_year_greeting
    title: New Year greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  departure_greeting:
    text: departure_greeting
    description: Good wishes on departure or settlement elsewhere.
    meaning: pc:subtype_departure_greeting
    title: Departure greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  greeting:
    text: greeting
    description: A greeting whose occasion is not specified by a narrower form.
    meaning: pc:subtype_greeting
    title: Greeting
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  thanks:
    text: thanks
    description: A public expression of thanks or acknowledgement.
    meaning: pc:subtype_thanks
    title: Thanks
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  meeting_notice:
    text: meeting_notice
    description: A notice inviting people to a meeting.
    meaning: pc:subtype_meeting_notice
    title: Meeting notice
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  announcement:
    text: announcement
    description: A public announcement without a narrower established form.
    meaning: pc:subtype_announcement
    title: Announcement
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  appeal:
    text: appeal
    description: A public request for support, contributions or participation.
    meaning: pc:subtype_appeal
    title: Appeal
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  commercial_advertisement:
    text: commercial_advertisement
    description: An advertisement for goods, services or premises.
    meaning: pc:subtype_commercial_advertisement
    title: Commercial advertisement
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  condolence:
    text: condolence
    description: An expression of sympathy to mourners.
    meaning: pc:subtype_condolence
    title: Condolence
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  memorial_notice:
    text: memorial_notice
    description: A notice commemorating someone who has died.
    meaning: pc:subtype_memorial_notice
    title: Memorial notice
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  death_announcement:
    text: death_announcement
    description: An announcement of a death or funeral.
    meaning: pc:subtype_death_announcement
    title: Death announcement
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  editorial:
    text: editorial
    description: An editorial statement by the newspaper.
    meaning: pc:subtype_editorial
    title: Editorial
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  opinion:
    text: opinion
    description: An argument or commentary expressing a view.
    meaning: pc:subtype_opinion
    title: Opinion
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  letter:
    text: letter
    description: A letter printed for readers, including letters to the editor.
    meaning: pc:subtype_letter
    title: Letter
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  poem:
    text: poem
    description: A composition in verse.
    meaning: pc:subtype_poem
    title: Poem
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  sketch:
    text: sketch
    description: A short literary sketch.
    meaning: pc:subtype_sketch
    title: Sketch
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.
  humour:
    text: humour
    description: A joke or short humorous composition.
    meaning: pc:subtype_humour
    title: Humour
    comments:
    - A local documentary form concept refines one Impresso type; the pinned ontologies
      do not enumerate this newspaper's forms.

```
</details>

</div>
