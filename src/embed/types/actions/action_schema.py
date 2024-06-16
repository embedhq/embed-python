# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionSchema", "Parameters"]


class Parameters(BaseModel):
    properties: Dict[str, object]
    """The properties of the input schema."""

    type: Literal["object"]
    """The type of the input schema."""

    required: Optional[List[str]] = None
    """The required properties of the input schema."""


class ActionSchema(BaseModel):
    description: str
    """A description of the action schema."""

    name: str
    """The name of the action schema."""

    parameters: Parameters
    """The input schema of the action."""
