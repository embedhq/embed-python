# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ConnectionUpsertParams",
    "Credentials",
    "CredentialsOAuth2Credentials",
    "CredentialsOAuth1Credentials",
    "CredentialsBasicCredentials",
    "CredentialsAPIKeyCredentials",
]


class ConnectionUpsertParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the connection."""

    auth_scheme: Required[Literal["oauth2", "oauth1", "basic", "api_key"]]
    """The authentication scheme the connection should use."""

    credentials: Required[Credentials]
    """The connection's account credentials."""

    integration_id: Required[str]
    """The unique identifier of the integration used by the connection."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the connection."""

    exclusions: Optional[Dict[str, object]]
    """Exclusion rules for the connection.

    Only applicable for integrations that support exclusions.
    """

    inclusions: Optional[Dict[str, object]]
    """Inclusion rules for the connection.

    Only applicable for integrations that support inclusions.
    """

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the connection."""


class CredentialsOAuth2Credentials(TypedDict, total=False):
    access_token: Required[str]
    """The OAuth 2.0 access token."""

    expires_at: Required[int]
    """The timestamp when the access token expires."""

    refresh_token: Required[str]
    """The OAuth 2.0 refresh token."""


class CredentialsOAuth1Credentials(TypedDict, total=False):
    oauth_token: Required[str]
    """The OAuth 1.0a token."""

    token_secret: Required[str]
    """The OAuth 1.0a token."""


class CredentialsBasicCredentials(TypedDict, total=False):
    password: Required[str]
    """The password required for `basic` auth."""

    username: Required[str]
    """The username required for `basic` auth."""


class CredentialsAPIKeyCredentials(TypedDict, total=False):
    api_key: Required[str]
    """The API key."""


Credentials = Union[
    CredentialsOAuth2Credentials,
    CredentialsOAuth1Credentials,
    CredentialsBasicCredentials,
    CredentialsAPIKeyCredentials,
]
