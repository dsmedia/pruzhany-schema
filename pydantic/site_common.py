"""Printed places, titles, translation and cross-references in the site shape."""
from .generated.models import Authorship, ContentItemBlockRef, CrossReference, EnglishCheck, PrintedAddress, PrintedTitle, SuppliedTitle, TextBasis, TitleCheck, Translation, TranslationCheck
from typing import Annotated, Literal
from pydantic import BaseModel, Field, field_validator, model_validator
from .sourced_entities import Strict, Text, Day, Attribution


Sha256 = Annotated[str, Field(min_length=64, max_length=64, pattern=r'^[0-9a-f]{64}$')]


# Opaque ID plus field suffix; include NEL/BOM in whitespace in both runtimes.
# Pydantic's Rust regex $ already requires the absolute end of the string.


def _PrintedTitle__printed_words(self):
    if self.text != '\n'.join(a.text for a in self.addresses):
        raise ValueError('printed title must be its addressed words, joined by newlines')
    return self


def __AttributedEnglish__check_is_not_null(cls, value: object) -> object:
    if value is None:
        raise ValueError('omit an absent check; a present check must be complete')
    return value


def text_basis_matches(basis: TextBasis, current_text: str) -> bool:
    return basis.source_text == current_text


def unique_ids(values, label):
    return [] if len(set(values)) == len(values) else [f'duplicate {label}']
