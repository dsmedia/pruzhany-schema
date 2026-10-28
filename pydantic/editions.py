"""The catalog's generated Python models and its optional-key policy."""
from .generated.models import Edition, EditionsCatalog, HistoricalEvent, Holiday


def present_value(value):
    """Zod's optional catalog keys may be absent, but never explicit null."""
    if value is None:
        raise ValueError('omit an absent catalog value; a present value must not be null')
    return value


__all__ = ['Edition', 'EditionsCatalog', 'HistoricalEvent', 'Holiday']
