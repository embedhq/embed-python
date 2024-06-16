# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    id: str
    """The unique identifier for the connection."""

    auth_scheme: Literal["oauth2", "oauth1", "basic", "api_key"]
    """The authentication scheme the connection uses."""

    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the connection."""

    created_at: int
    """The Unix timestamp (in seconds) for when the connection was created."""

    exclusions: Optional[Dict[str, object]] = None
    """Exclusions rules for the connection."""

    inclusions: Optional[Dict[str, object]] = None
    """Inclusion rules for the connection."""

    integration_id: str
    """The unique identifier of the integration used by the connection."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata associated with the connection."""

    object: Literal["connection"]
    """The object type, which is always `connection`."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the connection was updated."""
