"""The fates list's generated Python models and their retained checks."""
from .generated.models import (
    FatesList,
    FatesListAge,
    FatesListArchiveCount,
    FatesListCounts,
    FatesListDate,
    FatesListFateDetail,
    FatesListOutsideRecord,
    FatesListPerson,
    FatesListPiece,
)


def _FatesListFateDetail__place_or_date(self):
    """A fate detail places the fate, dates it, or both."""
    if self.place_id is None and self.date is None:
        raise ValueError('a fate detail needs a place_id or a date')
    return self


# Each way of knowing an age, and the fields it needs.
AGE_NEEDS = {
    'birth_year': ('birth_year', 'fact_ids'),
    'birth_announced': ('announced',),
    'birth_years_disagree': ('birth_years',),
}


def _FatesListAge__basis(self):
    """An age gives what its way of knowing it needs."""
    missing = [name for name in AGE_NEEDS[self.known_by] if getattr(self, name) is None]
    if missing:
        raise ValueError(f'an age known by {self.known_by} needs {", ".join(missing)}')
    return self


__all__ = [
    'FatesList', 'FatesListAge', 'FatesListArchiveCount', 'FatesListCounts', 'FatesListDate',
    'FatesListFateDetail', 'FatesListOutsideRecord', 'FatesListPerson', 'FatesListPiece',
]
