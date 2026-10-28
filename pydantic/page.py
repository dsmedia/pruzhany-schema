"""Pages and blocks: the physical document shared by the current site contracts."""
from .generated.models import Block, Page, PagesData

from pydantic import BaseModel, Field
