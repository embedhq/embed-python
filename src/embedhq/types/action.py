# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Action"]


class Action(BaseModel):
    created_at: int
    """The Unix timestamp (in seconds) for when the action was created."""

    integration_id: str
    """The ID of the integration to which the action belongs."""

    is_enabled: bool
    """Whether the action is enabled."""

    object: Literal["action"]
    """The object type, which is always `action`."""

    provider_key: str
    """The unique key of the integration provider."""

    unique_key: str
    """The unique key of the action."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the action was updated."""
