"""The catalog's generated Python models and its optional-key policy."""
from .generated.models import Edition, EditionsCatalog, HistoricalEvent, Holiday, Newspaper


def _Edition__key_date(self):
    # Pydantic Validators, read 2 November 2026:
    # https://docs.pydantic.dev/latest/concepts/validators/ (after model validator).
    if self.key[-10:] != self.date:
        raise ValueError('edition key must agree with date')
    return self


def _EditionsCatalog__newspaper_references(self):
    if self.newspapers is None:
        return self
    ids = set()
    for paper in self.newspapers:
        if paper.id in ids:
            raise ValueError('duplicate newspaper id')
        ids.add(paper.id)
    for edition in self.editions:
        if edition.newspaper not in ids:
            raise ValueError('edition newspaper is not listed in newspapers')
    return self


def present_value(value):
    """Zod's optional catalog keys may be absent, but never explicit null."""
    if value is None:
        raise ValueError('omit an absent catalog value; a present value must not be null')
    return value


__all__ = ['Edition', 'EditionsCatalog', 'HistoricalEvent', 'Holiday', 'Newspaper']
