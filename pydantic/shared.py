"""Shared compatibility values and external references."""
from .generated.models import ExternalReference

from typing import Literal
from pydantic import BaseModel, Field

HolocaustFate = Literal[
    "unknown",
    "perished",
    "likely_perished",
    "survived",
    "likely_survived",
    "died_before",
    "not_applicable",
]
