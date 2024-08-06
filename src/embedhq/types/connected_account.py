# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectedAccount"]


class ConnectedAccount(BaseModel):
    id: str
    """The unique identifier for the connected account."""

    auth_method: Literal["oauth2", "basic", "api_key", "none"]
    """The authentication method used to connect the account."""

    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the connected account."""

    created_at: int
    """The Unix timestamp (in seconds) for when the connected account was created."""

    integration: str
    """The unique slug of the integration associated with the connected account."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata associated with the connected account."""

    name: str
    """The display name of the connected account."""

    object: Literal["connected_account"]
    """The object type, which is always `connected_account`."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the connected account was updated."""
