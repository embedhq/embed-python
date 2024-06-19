# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionTokenCreateParams"]


class SessionTokenCreateParams(TypedDict, total=False):
    integration_id: Required[str]
    """The unique identifier of the integration to connect the account to."""

    auth_scheme: Literal["oauth2", "oauth1", "basic", "api_key"]
    """The authentication scheme to use to connect the account.

    Only applicable for integrations that support multiple auth schemes.
    """

    configuration: Optional[Dict[str, object]]
    """Configuration options to assign to the connection."""

    connection_id: str
    """The unique identifier of the connection."""

    exclusions: Optional[Dict[str, object]]
    """Exclusion rules to assign to the connection.

    Only applicable for integrations that support exclusions.
    """

    expires_in_mins: int
    """The number of minutes until the session token expires."""

    inclusions: Optional[Dict[str, object]]
    """Inclusion rules to assign to the connection.

    Only applicable for integrations that support inclusions.
    """

    metadata: Optional[Dict[str, object]]
    """Additional metadata to assign to the connection."""

    redirect_url: Optional[str]
    """The URL to redirect to after the authentication flow is complete."""
