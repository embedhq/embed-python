# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Action"]


class Action(BaseModel):
    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the action."""

    created_at: int
    """The Unix timestamp (in seconds) for when the action was created."""

    integration: str
    """The slug of the integration to which the action belongs."""

    is_enabled: bool
    """Whether the action is enabled."""

    name: str
    """The display name of the action."""

    object: Literal["action"]
    """The object type, which is always `action`."""

    slug: str
    """The unique slug of the action."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the action was updated."""

    version: str
    """The version of the action, formatted as "MAJOR.MINOR"."""

    required_scopes: Optional[List[str]] = None
    """The OAuth scopes required to trigger the action."""
