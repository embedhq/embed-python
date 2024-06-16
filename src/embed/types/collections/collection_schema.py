# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["CollectionSchema"]


class CollectionSchema(BaseModel):
    description: str
    """A description of the schema."""

    name: str
    """The name of the schema."""

    properties: Dict[str, object]
    """The properties of the schema."""

    required: Optional[List[str]] = None
    """The required properties of the schema."""
