# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ConnectedAccountUpsertParams",
    "Credentials",
    "CredentialsOAuth2Credentials",
    "CredentialsOAuth1Credentials",
    "CredentialsBasicCredentials",
    "CredentialsAPIKeyCredentials",
]


class ConnectedAccountUpsertParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the connected account."""

    auth_method: Required[Literal["oauth2", "basic", "api_key", "none"]]
    """The authentication method used to connect the account."""

    credentials: Required[Credentials]
    """The connected account's authentication credentials."""

    integration: Required[str]
    """The unique slug of the integration associated with the connected account."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the connected account."""

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the connected account."""


class CredentialsOAuth2Credentials(TypedDict, total=False):
    access_token: Required[str]
    """The OAuth 2.0 access token."""

    refresh_token: Required[str]
    """The OAuth 2.0 refresh token."""

    expires_at: int
    """The unix timestamp (in seconds) for when the access token expires."""


class CredentialsOAuth1Credentials(TypedDict, total=False):
    oauth_token: Required[str]
    """The OAuth 1.0a token."""

    oauth_token_secret: Required[str]
    """The OAuth 1.0a token."""


class CredentialsBasicCredentials(TypedDict, total=False):
    password: Required[str]
    """The password required for `basic` auth."""

    username: Required[str]
    """The username required for `basic` auth."""


class CredentialsAPIKeyCredentials(TypedDict, total=False):
    api_key: Required[str]
    """The API key."""


Credentials: TypeAlias = Union[
    CredentialsOAuth2Credentials,
    CredentialsOAuth1Credentials,
    CredentialsBasicCredentials,
    CredentialsAPIKeyCredentials,
]
