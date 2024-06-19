# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SessionToken"]


class SessionToken(BaseModel):
    token: str
    """The unique token that identifies the session."""

    auth_scheme: Literal["oauth2", "oauth1", "basic", "api_key"]
    """The authentication scheme to use to connect the account.

    Only applicable for integrations that support multiple auth schemes.
    """

    configuration: Optional[Dict[str, object]] = None
    """Configuration options to assign to the connection."""

    connection_id: Optional[str] = None
    """The unique identifier of the connection."""

    created_at: int
    """The Unix timestamp (in seconds) for when the session token was created."""

    exclusions: Optional[Dict[str, object]] = None
    """Exclusion rules to assign to the connection.

    Only applicable for integrations that support exclusions.
    """

    expires_at: int
    """The Unix timestamp (in seconds) for when the session token expires."""

    inclusions: Optional[Dict[str, object]] = None
    """Inclusion rules to assign to the connection.

    Only applicable for integrations that support inclusions.
    """

    integration_id: str
    """The unique identifier of the integration to connect the account to."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata to assign to the connection."""

    object: Literal["session_token"]
    """The object type, which is always `session_token`."""

    redirect_url: Optional[str] = None
    """The URL to redirect to after the authentication flow is complete."""

    url: str
    """The magic link used to connect an account with the session token."""
