"""An instantiation and its explicitly public projection; masters stay private."""
from typing import Annotated, Literal
from urllib.parse import urlsplit
from pydantic import Field, model_validator
from .sourced_entities import Strict, Text, Day, Source
from .site_common import unique_ids

Pixels = Annotated[int, Field(gt=0, le=9007199254740991)]


class MediaDecision(Strict):
    by: Text
    on: Day


class MediaText(Strict):
    text: Text
    reviewed: MediaDecision | None = None


class MediaMaster(Strict):
    key: Annotated[str, Field(pattern=r'^(?:[a-z0-9_-]+/)*[0-9a-f]{64}$')]
    sha256: Annotated[str, Field(pattern=r'^[0-9a-f]{64}$')]
    mime: Annotated[str, Field(pattern=r'^(?:image|audio|video|application)/[a-z0-9][a-z0-9.+-]*$')]
    bytes: Pixels

    @model_validator(mode='after')
    def named_by_digest(self):
        if self.key.rsplit('/', 1)[-1] != self.sha256:
            raise ValueError('master key must be named by its sha256')
        return self


class MediaDerivative(Strict):
    url: Annotated[str, Field(pattern=r'^https://pictures\.pruzhanychronicles\.org/(?:[a-z0-9_-]+/)*[a-z0-9-]+-w(?:100|400|800|1200)\.webp$')]
    width: Pixels
    height: Pixels


class PublicMedia(Strict):
    id: Annotated[str, Field(pattern=r'^[a-z0-9]+(?:-[a-z0-9]+)*$')]
    source_id: Text
    kind: Literal['image', 'audio', 'video', 'document']
    caption: MediaText
    alt: MediaText | None = None
    width: Pixels | None = None
    height: Pixels | None = None
    duration: Annotated[float, Field(gt=0, allow_inf_nan=False)] | None = None
    conditions_of_use: Text | None = None
    rights: Annotated[str, Field(pattern=r'^https?://(?:rightsstatements\.org|creativecommons\.org)/[^\s\\]+$')] | None = None
    cleared: MediaDecision | None = None
    link: Annotated[str, Field(pattern=r'^https://[a-z0-9]+(?:[.-][a-z0-9]+)*(?:/[^\s\\]*)?$')] | None = None
    derived: Annotated[list[MediaDerivative], Field(min_length=1)] | None = None

    @model_validator(mode='after')
    def media_contract(self):
        errors = []
        if self.kind == 'image' and not self.alt:
            errors.append('image needs alt')
        if bool(self.width) != bool(self.height):
            errors.append('media width and height must occur together')
        if self.link and self.kind not in {'audio', 'video'}:
            errors.append('holder link is only for audio or video')
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


class Media(PublicMedia):
    master: MediaMaster | None = None


def public_media(value: Media) -> PublicMedia:
    checked = Media.model_validate_json(value.model_dump_json())
    return PublicMedia.model_validate({k: v for k, v in checked.model_dump().items() if k in PublicMedia.model_fields})


def media_reference_errors(media: list[Media], sources: list[Source], subjects: set[str]) -> list[str]:
    errors = []
    by_source = {s.id: s for s in sources}
    for source in sources:
        errors += unique_ids(source.subjects or [], 'source subject')
        if any(id not in subjects for id in source.subjects or []):
            errors.append('source subject must resolve to a person, place or event')
    for medium in media:
        source = by_source.get(medium.source_id)
        if not source:
            errors.append('unknown media source')
        if medium.link:
            # Ticket 01 replaces source.host with source.holder_id -> holder.host.
            host = source.host if source else None
            name = urlsplit(medium.link).hostname or ''
            if not host or not (name == host or name.endswith('.' + host)):
                errors.append('media link must be on its holder host')
    return errors
