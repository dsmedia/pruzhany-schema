"""Printed places, titles and translation in the proposed site shape."""
from typing import Annotated, Literal
from pydantic import Field, field_validator, model_validator
from .sourced_entities import Strict, Text, Day, Attribution


class PrintedAddress(Strict):
    image_uri: Text
    bbox: tuple[Annotated[float, Field(ge=0)], Annotated[float, Field(ge=0)],
                Annotated[float, Field(gt=0)], Annotated[float, Field(gt=0)]]
    text: str  # Empty is allowed for a patch without a readable line.


class TextBasis(Strict):
    source_text: str  # Exact text used, never silently replaced after a rereading.
    addresses: list[PrintedAddress] = Field(min_length=1)


class Authorship(Attribution):
    kind: Literal['person', 'model']


Sha256 = Annotated[str, Field(min_length=64, max_length=64, pattern=r'^[0-9a-f]{64}$')]


# Opaque ID plus field suffix; include NEL/BOM in whitespace in both runtimes.
# Pydantic's Rust regex $ already requires the absolute end of the string.
class EnglishCheck(Strict):
    reading_id: Text
    reading_sha256: Sha256
    english_sha256: Sha256
    judgement_id: Annotated[str, Field(pattern=r'^[^\s\u0085\uFEFF]+:(title|text)$')]
    judgement_sha256: Sha256
    attribution: Authorship


class TitleCheck(EnglishCheck):
    judgement_id: Annotated[str, Field(pattern=r'^[^\s\u0085\uFEFF]+:title$')]


class TranslationCheck(EnglishCheck):
    judgement_id: Annotated[str, Field(pattern=r'^[^\s\u0085\uFEFF]+:text$')]


class PrintedTitle(Strict):
    text: Text
    addresses: list[PrintedAddress] = Field(min_length=1)

    @model_validator(mode='after')
    def printed_words(self):
        if self.text != '\n'.join(a.text for a in self.addresses):
            raise ValueError('printed title must be its addressed words, joined by newlines')
        return self


class _AttributedEnglish(Strict):
    text: Text
    language: Literal['en']
    based_on: TextBasis
    attribution: Authorship
    checked_against: EnglishCheck | None = Field(default=None, exclude_if=lambda v: v is None)

    @field_validator('checked_against', mode='before')
    @classmethod
    def check_is_not_null(cls, value: object) -> object:
        if value is None:
            raise ValueError('omit an absent check; a present check must be complete')
        return value


class SuppliedTitle(_AttributedEnglish):
    """An attributed English name, distinct from a translation."""
    checked_against: TitleCheck | None = Field(default=None, exclude_if=lambda v: v is None)


class Translation(_AttributedEnglish):
    """Translation is semantic work, distinct from a supplied title."""
    checked_against: TranslationCheck | None = Field(default=None, exclude_if=lambda v: v is None)


def text_basis_matches(basis: TextBasis, current_text: str) -> bool:
    return basis.source_text == current_text


class ContentItemBlockRef(Strict):
    page_id: Text
    block_ids: list[Text] = Field(min_length=1)  # Regions, in reading order.


def unique_ids(values, label):
    return [] if len(set(values)) == len(values) else [f'duplicate {label}']
