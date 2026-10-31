# Source words and their English

Read and audited **31 October 2026**, for the fates-in-English model ticket 02.
All examples below are invented. This is a slot audit of every module under
`linkml/schema/`, including the external contracts. “English” means an attributed
rendering of the particular source words, not an English summary of a fact.

## The contract added now

`Citation.quote_english` is optional and nullable, range **CitedTranslation**.
`SiteCitation` inherits it. `MediaFamilyWords.quote_english` uses the same class;
`Source.title_english` also uses it because a catalogue title has no image box.
These are the only three companion slots added: each has data and a writer in
this work's scope. Later steps' possible needs do not justify more fields now.

`CitedTranslation is_a Translation`, with `slot_usage.based_on.range` narrowed to
**CitedTextBasis**. It inherits required `text` (nonblank), `language` (exactly
`en`), `based_on`, and `attribution` (required `kind: person|model`, nonblank `by`,
valid day `on`, optional note). Optional `checked_against` retains the existing
complete TranslationCheck contract and must be omitted rather than null.

`CitedTextBasis is_a TextBasis` with `slot_usage.addresses.required: false`.
Its `source_text` remains required. Addresses may be absent or null; when present
they must be nonempty PrintedAddress witnesses with real `image_uri`, four-part
`bbox`, and `text`. The containing citation's own locator, or the source's
description, identifies the words without inventing boxes. **TextBasis and
Translation used by pieces and supplied titles keep their required addresses.**
No class's fields are copied into a second LinkML definition.

A present rendering's `based_on.source_text` equals **exactly** its sibling
`quote` or `title`, including whitespace and punctuation. A broader passage,
paraphrase or private research note does not meet that binding. Existing
`quote_language` keeps its language-override meaning. Fictional fixtures include
a paper quotation with real-shaped addresses and a book quotation at page `795`,
URL `https://archive.org/details/fictional-memorial-book/page/795`, without boxes;
both pass and a changed source string fails. Source-title fixtures also omit boxes.

Attribution can name `Fictional translator` or a kept English witness such as
`kept:fictional-issue/fictional-piece:text`, retaining its original day and kind.
This is attribution, not a dereferenceable translation link. The later writer
resolves kept English and refreshes this value when that English changes.
No paid call, new translation or data migration is part of this schema change.

The twins validate exact text, calendar, box and check refinements through the
containing documents. Source-title equality runs at **SharedRecord** so the
site's existing `SourceSchema.pick()` API remains usable. JSON Schema checks the
shape but cannot compare sibling strings; the retained twins enforce equality.
The duties are inventoried in `linkml/checks/record.yaml`.

`Attribution` moves into `site_common.yaml`, preserving public runtime imports.
The dependency is types/vocabulary → site_common → sourced_entities; media also
imports site_common. Citation can therefore refine Translation without a cycle.

## Slot audit

“Added” means a field in this change, not a claim that existing data has English.
Inherited fields are included explicitly by the parent/child names in the table.
No raw OCR word, name or source spelling is replaced by English.

| Module / source-word slots | English before this change | Resolution now |
| --- | --- | --- |
| `sourced_entities`: `Citation.quote`; inherited `SiteCitation.quote` in `shared_record` | None. `quote_language` is only an override; `public_note` and private `note` are not translations. | Added `quote_english: CitedTranslation`, exact-bound to `quote`. |
| `media`: `MediaFamilyWords.quote` | Language only (`quote_language`). | Added `quote_english: CitedTranslation`; explicit original language retained. |
| `sourced_entities`: `Source.title` | None. `short_name` is a display label, not attributed English of the title. | Added `title_english: CitedTranslation`, exact-bound to `title`, without required boxes. |
| `sourced_entities`: `Source.published` | None for its “as written” publication statement. | **Open:** publication-statement English needs a writer, original-language attribution, an exact `published` binding and a reliable catalogue/page locator. |
| `sourced_entities`: `Citation.record_type`; inherited `SiteCitation.record_type` | None for the holder's own documentary-form label. | **Open:** documentary-form English needs a writer, the holder's verbatim label and language, an exact `record_type` binding and its record locator. |
| `sourced_entities`: `SourcedDate.printed`; `shared_record`: `LifeEventDate.printed` | `start`/`end` can normalize a Gregorian date; this does not translate printed words or a Hebrew-calendar date. | **Open:** `printed_english` on each date form needs a writer, verbatim date words/language, an exact `printed` binding and provenance distinct from Gregorian normalization. |
| `sourced_entities`: `Fact.value`; inherited `SharedFact.value` and `SourcedRelation.value` | May be our English interpretation, or source words; no exact attributed English field for the latter. | **Open:** `value_english` needs a writer and a reliable distinction between verbatim source words and editorial interpretation, then exact `value` binding, language and evidence. |
| `sourced_entities`: legacy `Mention.title`, `Mention.function`; `mentions`: `IssueMention.title`, `IssueMention.function` | Sometimes already English descriptions; a printed honorific/function has no companion. | **Open:** `title_english` and `function_english` on both mention forms need writers, verbatim honorific/function labels and language, exact sibling bindings and located witnesses; identity is unchanged. |
| `site_common`: `PrintedTitle.text`; reached by `ContentItem.printed_title` and `PrintedSection.printed_title` | `supplied_title: SuppliedTitle` exists (required on items, optional on sections), but can be an editorial title made from the whole piece rather than a translation of its headline. | **Open:** `PrintedTitle.english` needs a writer for verbatim headlines, exact `text` binding and existing title addresses; supplied editorial titles retain their independent meaning. |
| `content_items`: `ContentItem.full_text` | Optional `translation: Translation` already exists with its exact historical basis and attribution. | Reused unchanged; a later rereading may intentionally leave the historical translation basis intact. No new mandatory full-text rule in this staging change. |
| `site_common`: `PrintedAddress.text`, `TextBasis.source_text`, `TextBasis.addresses[].text`; `pages`: `Block.transcription` | Addressed portions of the original layer; English belongs to their containing translation/title/content item, not necessarily to each line or box. | Kept as witnesses, not independently translated. Citation English binds to the quote, not all surrounding address text. |
| `media`: `MediaText.text`, reached as `PublicMedia.caption`, `alt`, `inscription`, `transcript` and inherited by `Media` | `lang` and review only. Captions/alt may already be ours in English; inscriptions/transcripts may be source words. | **Open:** `MediaText.english` needs a writer that distinguishes source inscriptions/transcripts from editorial captions/alt, exact `text` binding, language and a picture/time locator; accessibility prose remains separate. |
| `media`: `PublicMedia.credit`, `conditions_of_access`, `conditions_of_use` (inherited by `Media`) | Holder's own wording, no English companion. A rights URI is not a translation. | **Open:** `credit_english`, `conditions_of_access_english` and `conditions_of_use_english` each need a writer, verbatim holder wording/language, exact sibling binding, provenance and a safe publication policy; permission rules remain separate. |
| `sourced_entities`: `Name.value` (including `SharedName`); legacy `Mention.printed_name`; `mentions`: `IssueMention.printed_name`; `Fact.related_name` | Names may have a separate Latin/English name in `names`, or resolve to one shared person. No exact attributed transliteration relation. | **Approval candidate:** an attributed name rendering/transliteration, source-name-bound, distinct from translation and identity equivalence. See below. |
| `shared_record`: `SharedPerson.name`, `SharedFamily.name`, `SharedPlace.name`, `SharedOrganization.name`, `SharedEvent.name`; `Holder.name`, `Holder.short_name`; `sourced_entities`: `Source.author`, `editor`, `repository`, `short_name` | Site-supplied display names, authority names or credited names, sometimes original-language strings. No uniform language/provenance-bound rendering. | Same name-rendering candidate where source wording is preserved. Existing `Name`/shared identities continue to supply display spellings; do not translate names or invent a new identity. |
| `sourced_entities`: `Source.reference_code`, `Citation.reference_code`, `record_id`, `page`, `scan`, `time`; `shared_record`: `PlaceIdentifier.value`; `media`: `MediaFamilyWords.page` | Identifiers and locators, possibly containing letters. | Preserve exactly. A record-type label would need its own future rendering; an identifier is never translated. A quoted page heading belongs in Citation/Translation, not in the locator. |
| `sourced_entities`: `Citation.note`, `public_note`, `Attribution.note`, `Fate.summary`; `shared_record`: `SharedEvent.description`; `shared`: `ExternalReference.notes`; `site_common`: `CrossReference.evidence`, `relationship` | Editorial prose or private notes, potentially containing embedded quotes; no language or excerpt-level English bindings. | A freestanding verbatim passage belongs in `Citation.quote` with `quote_english`. **Approval candidate:** structured multilingual note excerpts if mixed notes must preserve separate quote spans; do not call a translation of the entire note the source's own English. Private notes remain private. |
| `editions`: `Edition.hebrew_date`, `holiday`; `Holiday.hebrew_name`, `name`; `HistoricalEvent.name`, `description` | Calendar and supplied catalogue labels, not transcriptions of a historical source. Holiday has parallel Hebrew/Latin names; event prose is English. | No source-quote field added. Hebrew-calendar date presentation remains a separate calendar/localization question. |
| `physical`: `PhysicalWord.tx`, `nf` | Exact/normalized OCR tokens. No English per token. | Preserved Impresso contract; parent content-item English is the semantic layer. No independent translation of each token. |
| `impresso_contentitem`: `ImpressoContentItem.title`, `title_text`, `media_title_variant`, `rc`, `rp`, `ft`; `ImpressoContentSection.title_text`; `impresso_issue`: `ImpressoIssue.media_title_variant`, `rc`, `rp`, `notes`, `provided_metadata`; `ImpressoMetadata.title`, `var_t`, `archival_note`, `speakers`; `ImpressoIssueSection.title_text` | Upstream rebuilt text, titles, broadcast/provider metadata and opaque notes; no English companions in the pinned wire formats. | Preserve exact external contracts. Project readable text into ContentItem/PrintedTitle/Translation; unstructured provider metadata or broadcast text needs an approved provenance/address form before broadening Translation. Neither upstream schemas nor stored formats are changed here. |
| `answers`: `ReadLatinLine.text`; `WriteEnglishDoubt.printed`, `likely`, `why`; `WriteEnglishPerson.printed`/`name`, `WriteEnglishOrganization.printed`/`name`, `WriteEnglishPlace.printed`/`name`; `WriteEnglishLifeEvent.date_hebrew`, `date_gregorian`, `name`, `principals`; `WriteEnglishAnsweredPiece.title`, `english`; `JoinPeopleGroup.name`, `why` | Procedural replies already pair printed people/places/organizations with English names; whole-piece title/English are separate reply fields. Doubt alternatives are readings, not English; date words lack an exact translation companion. | Paid-answer bytes and extraction models preserved. They are input exchanges, not publication contracts; the persisted Translation/Citation carries final exact binding and attribution. A future answer version, not an edit to the released one, can ask for further English. |
| `types`, `vocabulary`, `life_events`, `exchanges`; other technical slots in the modules above | No additional source-word payload: enums, ids, hashes, references, flags, geometry, timestamps, URLs, model metadata and content-item links. `ImpressoLegacy.source`, `comp_fileid`, `comp_role`, `ImpressoStyle.font` are file/style identifiers. | No translation slot appropriate. |

The three new slots refine Translation; no vocabulary enum, released type, ontology
pin, extraction contract or isolated pilot changes. Proper names and mixed notes
are recorded as open design work rather than silently treated as translations.

## Mapping and owner approval queue

Read the pinned **EHRI 0.2.0**, **RiC-O 1.1**, and **RiC-O 1.1 axioms** in
`standards/` on **31 October 2026**. They offer no quote-to-attributed-English
property. `rico:hasOrHadDerivedInstantiation` has Instantiation at both ends;
a Citation/Translation value is not that assertion. `rico:hasOrHadTitle` ranges
over Title; `rico:textualValue` has Appellation/Date/Extent as domain. None is
invented as a direct predicate from a citation to this compound translation.

All new fields reuse the already approved `pc:site_translation` exact mapping
from `vocabulary/site-content.json` and `site-content.profile.ttl`, with the
existing reason: neither standard combines an attributed translation and the
exact source reading/printed addresses. Printed/supplied title classes retain
`rico:Title` and their existing title mappings; dates retain `rico:Date` and
`rico:expressedDate`. `bin/verify standards` checks every named term. This is
mapping to the pinned standards with a declared local gap, not a new vocabulary
release or a claim of EHRI conformance.

Candidates for an owner's future batch (not added):

- **Attributed name rendering/transliteration**: distinguish a rendering of one
  printed Name from a new identity or an equivalent appellation. Tentative
  mapping: existing `rico:AgentName` / `rico:PlaceName` for the name; a local
  source-name-to-rendering relation is needed. Fictional illustrations:
  `Fiktivski` / `Fictive`, and a fictional institution `Di Erfundene Bibliotek` /
  `The Invented Library`. Keep the required real examples privately in steps.
- **Other catalogue/web/audio bases** remain open beyond the three implemented
  slots. The owner's present refinement permits box-free cited quotes and source
  titles only. General provider metadata or audio spans need a concrete writer,
  locator/provenance requirements and mapping review before any further slot.
- **Mixed note quote spans**, if needed instead of a separate Citation: source
  words, language, exact span, English and provenance separated from editorial
  prose. No pinned EHRI/RiC-O compound term; a local extension would need a
  reason and owner approval. No public/private boundary is changed by translation.

## The single staged switch and rollout

The rule named **`require_non_english_quote_english`**, under
`Citation.rules` in `linkml/schema/sourced_entities.yaml`, has
**`deactivated: true`**. This is the sole switch. Generation derives
`REQUIRE_NON_ENGLISH_QUOTE_ENGLISH = false` in both
`zod/generated/words_policy.ts` and `pydantic/generated/words_policy.py`.
No environment variable or independent runtime flag controls release behavior.

When activated, a nonblank quote requires a non-null CitedTranslation unless its
explicit language is `en` or an `en-*` tag (case insensitive). An omitted/null
language is conservatively **not an English exemption**: Citation alone cannot
resolve Source.language. Thus ordinary inherited non-English quotes are covered
without changing what quote_language means. English quotes with no override also
need a rendering under this conservative local rule; the later data rollout must
resolve that case explicitly. Missing/null/blank quotes need no rendering.
SiteCitation inherits the rule. MediaFamilyWords gains English now; the staged
Citation requirement does not independently make family quotes mandatory.

The original YAML retains the real LinkML rule. Pinned LinkML 1.12.1's JSON
Schema emitter ignores `deactivated`, so `external_schema.ReleaseGenerator`
honors it before generation. Typed conditions explicitly opt into preserving
their declared ranges (`json_schema_typed_range`): otherwise this emitter drops
the range and lets a required translation be null. Unannotated existing rules
retain their behavior. Fictional tests activate the actual rule and compare it
with both twins, including absent/null language/English and inherited citations.

To enable later, set `deactivated: false`, regenerate, and land the populated
data together. The existing conditional-inventory guard still requires review of
Python enforcement when emitted conditions change; it is not another switch.
Exact-text bindings already reject stale English while coverage is off.

Documentation read **31 October 2026** beside this implementation:
[Slots](https://linkml.io/linkml/schemas/slots.html),
[Annotations](https://linkml.io/linkml/schemas/annotations.html),
[Advanced features, Rules](https://linkml.io/linkml/schemas/advanced.html#rules),
[JSON Schema, Rules and optional nulls](https://linkml.io/linkml/generators/json-schema.html),
and [ClassRule.deactivated](https://linkml.io/linkml-model/latest/docs/deactivated/).
The locked 1.12.1 `generators/jsonschemagen.py` methods `handle_class`,
`get_subschema_for_anonymous_class`, and `get_subschema_for_slot` were read too.
The documentation describes the feature; the tests establish this pinned
emitter's actual behavior.

## Consumer findings

Read steps' `publish/site_writer.py` (`_pin`, notice quotation flow),
`identity/people_registers.py` (Citation writer), `publish/site_evidence.py`,
and `identity/site_event_children.py`; read the site's `PersonFate.svelte`,
`CitedRecord.svelte`, `record-words.ts`, `data/public.schema.ts`, and
`src/lib/privacy/` projection/evidence modules. The writer currently locates
quotes and preserves their exact words; it does not emit English for quotes.
The site currently reads the quote and source label. This change only gives the
later writer and renderer a validated place to put the English.

The privacy projection rebuilds citations and sources with explicit
`CITATION_FIELDS`/`SOURCE_FIELDS` allowlists. It omits the new fields (and the
quote-language override today); it does not spread Translation or its
attribution to the browser. The schema's RDF profile likewise explicitly omits
new English fields. The website follow-up must deliberately project safe English
and attribution, never private notes, locator paths, translator identities or
raw basis objects. Current site files validate while the switch is off. The
consumer checks use master exported with `git archive`, a real frozen-lockfile
install, and this worktree's schema symlink; neither reference checkout is edited.
