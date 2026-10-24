"""Pages and blocks: the physical document shared by the current site contracts."""

from pydantic import BaseModel, Field

class Block(BaseModel):
    """A physical text region on a newspaper page."""

    id: str = Field(description="Block ID like 'blk-p4-001'")
    bbox: tuple[int, int, int, int] = Field(
        description="[x, y, width, height] in absolute pixels"
    )
    transcription: str = Field(description="Transcribed text content")
    confidence: float | None = Field(default=None, description="OCR confidence 0-1")
    image_crop: str | None = Field(
        default=None, description="Path to cropped image file"
    )
    unit_id: str | None = Field(description="Foreign key to content unit")

class Page(BaseModel):
    """A newspaper page with its blocks."""

    id: str = Field(description="Page ID like 'page-1938-12-16-4'")
    issue_date: str = Field(description="Issue date in ISO format")
    page_number: int = Field(description="Page number (1-4)")
    image_uri: str = Field(description="Path to page image file")
    dimensions: tuple[int, int] = Field(description="[width, height] in pixels")
    blocks: list[Block] = Field(description="All blocks on this page")

class PagesData(BaseModel):
    """Top-level wrapper for pages JSON file."""

    edition_date: str = Field(description="Edition date in ISO format")
    pages: list[Page] = Field(description="All pages in the edition")
