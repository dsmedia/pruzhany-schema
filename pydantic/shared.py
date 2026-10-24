"""Shared compatibility values and external references."""

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

class ExternalReference(BaseModel):
    """Reference to external database or resource."""

    source: str = Field(description="Source name (e.g., 'yad_vashem', 'jri_poland')")
    url: str | None = Field(default=None, description="URL to the record (may be null for negative-evidence citations)")
    record_id: str | None = Field(default=None, description="Record identifier")
    notes: str | None = Field(default=None, description="Additional notes")
    verified: bool | None = Field(
        default=None,
        description="True if a human has reviewed and confirmed this citation",
    )
