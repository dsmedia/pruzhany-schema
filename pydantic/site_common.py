"""Printed places, titles and translation in the proposed site shape."""
from typing import Annotated, Literal
from pydantic import Field, model_validator
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


class PrintedTitle(Strict):
    text: Text
    addresses: list[PrintedAddress] = Field(min_length=1)

    @model_validator(mode='after')
    def printed_words(self):
        if self.text != '\n'.join(a.text for a in self.addresses):
            raise ValueError('printed title must be its addressed words, joined by newlines')
        return self


class SuppliedTitle(Strict):
    text: Text
    language: Literal['en']
    based_on: TextBasis
    attribution: Authorship


class Translation(SuppliedTitle):
    """Translation is semantic work, distinct from a supplied title."""


def text_basis_matches(basis: TextBasis, current_text: str) -> bool:
    return basis.source_text == current_text


class ContentItemBlockRef(Strict):
    page_id: Text
    block_ids: list[Text] = Field(min_length=1)  # Regions, in reading order.


def unique_ids(values, label):
    return [] if len(set(values)) == len(values) else [f'duplicate {label}']
