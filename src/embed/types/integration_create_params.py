# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntegrationCreateParams"]


class IntegrationCreateParams(TypedDict, total=False):
    provider_key: Required[str]
    """The unique key of the integration provider."""

    id: str
    """The unique identifier for the integration."""

    auth_scheme: Literal["oauth1", "oauth2", "basic", "api_key"]
    """The authentication scheme the integration should use.

    Only applicable for providers that support multiple auth schemes.
    """

    oauth_client_id: Optional[str]
    """The OAuth Client ID. Required for integrations that use OAuth."""

    oauth_client_secret: Optional[str]
    """The OAuth Client Secret. Required for integrations that use OAuth."""

    oauth_scopes: List[str]
    """Additional OAuth scopes to request from the user.

    By default, Embed will request the minimum required scopes for the collections
    and actions enabled on the integration.
    """

    use_test_credentials: bool
    """Use test credentials provided by Embed. Only available in staging environment."""
