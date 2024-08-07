# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SessionToken"]


class SessionToken(BaseModel):
    token: str
    """The unique token for the session."""

    configuration: Optional[Dict[str, object]] = None
    """Configuration options to assign to the connected account."""

    connected_account_id: str
    """The unique identifier to assign to the connected account."""

    created_at: int
    """The Unix timestamp (in seconds) for when the session token was created."""

    expires_at: int
    """The Unix timestamp (in seconds) for when the session token expires."""

    integration: str
    """The unique slug of the integration to connect the account to."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata to assign to the connected account."""

    name: Optional[str] = None
    """The display name to assign to the connected account."""

    object: Literal["session_token"]
    """The object type, which is always `session_token`."""

    redirect_url: Optional[str] = None
    """The URL to redirect to after the authorization flow is complete."""

    url: str
    """The magic link used to connect an account."""
