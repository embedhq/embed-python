# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ConnectSession"]


class ConnectSession(BaseModel):
    id: str
    """The unique identifier for the connect session."""

    configuration: Optional[Dict[str, object]] = None
    """Configuration options to assign to the connected account."""

    connected_account_id: str
    """The unique identifier for the connected account."""

    created_at: int
    """The Unix timestamp (in seconds) for when the session token was created."""

    expires_at: int
    """The Unix timestamp (in seconds) for when the connect session expires."""

    integration: str
    """The unique slug of the integration to connect the account to."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata to assign to the connected account."""

    name: Optional[str] = None
    """The display name of the connected account."""

    object: Literal["connect_session"]
    """The object type, which is always `connect_session`."""

    redirect_url: Optional[str] = None
    """The URL to redirect to after the authorization flow is complete."""

    url: str
    """The magic link used to connect an account."""
