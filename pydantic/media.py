"""Media council contract; storage and consent never enter the public projection."""
from .generated.models import Media, MediaConsent, MediaConsentScope, MediaDecision, MediaDepicted, MediaDerivative, MediaFamilyWords, MediaFixity, MediaMaster, MediaPortrait, MediaRegion, MediaText, MediaWithdrawal, PublicMedia
import json
import re
from pathlib import Path
from typing import Annotated, Literal
from urllib.parse import urlsplit
from pydantic import Field, model_validator
from .sourced_entities import Strict, Text, Day, Source, SourceLanguage
from .site_common import unique_ids

ROOT = Path(__file__).resolve().parents[1]
MEDIA_WIDTHS = json.loads((ROOT / 'zod/media-widths.json').read_text())
RIGHTS = json.loads((ROOT / 'standards/media-rights.json').read_text())
MediaRights = Literal[tuple(RIGHTS['uris'])]
Pixels = Annotated[int, Field(gt=0, le=9007199254740991)]
Coordinate = Annotated[int, Field(ge=0, le=9007199254740991)]
Digest = Annotated[str, Field(pattern=r'^[0-9a-f]{64}$')]


def region_fits(region, width, height):
    return bool(width and height and region.x + region.w <= width and region.y + region.h <= height)


def _MediaConsentScope__unique_people(self):
    errors = unique_ids(self.person_ids, 'consent person')
    if errors:
        raise ValueError('; '.join(errors))
    return self


def _MediaMaster__named_by_digest(self):
    if self.bucket == 'pruzhany-page-pictures':
        raise ValueError('master needs its own private bucket')
    if self.key.rsplit('/', 1)[-1] != self.sha256:
        raise ValueError('master key must be named by its sha256')
    if self.checked and self.checked.sha256 != self.sha256:
        raise ValueError('master check must match its sha256')
    return self


def _PublicMedia__media_contract(self):
    errors = []
    if self.kind in {'image', 'document'} and not self.alt:
        errors.append('image or document needs alt')
    if self.kind == 'document' and not self.transcript:
        errors.append('document needs transcript')
    if bool(self.width) != bool(self.height):
        errors.append('media width and height must occur together')
    if self.link and self.kind not in {'audio', 'video'}:
        errors.append('holder link is only for audio or video')
    if self.withdrawn and (self.derived or self.link):
        errors.append('withdrawn media cannot be served or linked')
    if any(p.person_id is None for p in self.depicted) and not self.shows_unidentified:
        errors.append('unidentified depiction needs shows_unidentified')
    if any(not region_fits(p.region, self.width, self.height) for p in self.depicted):
        errors.append('depicted region must fit master pixels')
    errors += unique_ids([p.person_id for p in self.depicted if p.person_id], 'depicted person')
    if self.kind == 'image' and self.rights == 'http://rightsstatements.org/vocab/InC-OW-EU/1.0/':
        errors.append('EU orphan-work statement excludes photographs')
    if self.alt:
        if len(self.alt.text) > 150:
            errors.append('alt must be at most 150 characters')
        if self.alt.text.strip().lower() == self.caption.text.strip().lower():
            errors.append('alt must not repeat caption')
        if self.alt.lang.lower().startswith('en') and re.search(r'(^image of\b|\b(?:holocaust victim|before the war|unaware|doomed|happy|little did they know)\b)', self.alt.text.strip(), re.I):
            errors.append('alt must describe only what is visible')
    if self.derived:
        if not self.cleared:
            errors.append('derived media needs clearance')
        if not (self.width and self.height) and not self.duration:
            errors.append('derived media needs dimensions or duration')
        if self.kind in {'image', 'document'} and not (self.width and self.height):
            errors.append('derived picture needs master dimensions')
        errors += unique_ids([d.url for d in self.derived], 'derived address')
        for d in self.derived:
            nominal = int(d.url.rsplit('-w', 1)[-1].removesuffix('.webp'))
            if d.width > nominal or (self.width and d.width > self.width) or (self.height and d.height > self.height):
                errors.append('derived picture cannot exceed its width or master')
    if errors:
        raise ValueError('; '.join(errors))
    return self


def _Media__consent_state(self):
    if self.consent and self.consent.withdrawn_on and not self.withdrawn:
        raise ValueError('withdrawn consent needs withdrawn media state')
    return self


def public_media(value: Media) -> PublicMedia:
    checked = Media.model_validate_json(value.model_dump_json())
    return PublicMedia.model_validate({k: v for k, v in checked.model_dump().items() if k in PublicMedia.model_fields})


def media_reference_errors(media: list[Media], sources: list[Source], subjects: set[str], persons=()) -> list[str]:
    errors = []
    by_source = {s.id: s for s in sources}
    people = {p.id for p in persons}
    for source in sources:
        errors += unique_ids(source.subjects or [], 'source subject')
        if any(id not in subjects for id in source.subjects or []):
            errors.append('source subject must resolve to a person, place or event')
    for medium in media:
        source = by_source.get(medium.source_id)
        if not source:
            errors.append('unknown media source')
        depicted = {p.person_id for p in medium.depicted if p.person_id}
        if depicted - people:
            errors.append('depicted person must resolve to a person')
        if medium.consent and set(medium.consent.scope.person_ids) - depicted:
            errors.append('consent person must be depicted')
        if medium.family_words and medium.family_words.source_id not in by_source:
            errors.append('unknown family words source')
        if medium.link:
            host = source.host if source else None
            name = urlsplit(medium.link).hostname or ''
            if not host or not (name == host or name.endswith('.' + host)):
                errors.append('media link must be on its holder host')
        for person in persons:
            if person.id in depicted or not medium.alt:
                continue
            for name in [person.name, *(n.value for n in person.names)]:
                if re.search(r'(?<![^\W_])' + re.escape(name) + r'(?![^\W_])', medium.alt.text, re.I):
                    errors.append('alt names must come from depicted people')
    for person in persons:
        if not person.portrait:
            continue
        portrait = person.portrait
        medium = next((m for m in media if m.id == portrait.media_id), None)
        if (not medium or medium.kind != 'image' or not medium.cleared or medium.withdrawn
                or not medium.caption.reviewed or not any(p.person_id == person.id for p in medium.depicted)
                or not region_fits(portrait.region, medium.width, medium.height)):
            errors.append('portrait needs a cleared reviewed image depicting this person and a region in master pixels')
    return errors
