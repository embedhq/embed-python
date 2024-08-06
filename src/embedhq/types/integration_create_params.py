# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["IntegrationCreateParams"]


class IntegrationCreateParams(TypedDict, total=False):
    provider: Required[str]
    """The unique slug of the integration provider."""

    name: str
    """The display name of the integration (defaults to provider name)."""

    oauth_client_id: Optional[str]
    """The OAuth Client ID. Required for integrations that use OAuth."""

    oauth_client_secret: Optional[str]
    """The OAuth Client Secret. Required for integrations that use OAuth."""

    oauth_scopes: List[str]
    """Additional OAuth scopes to request from the user.

    By default, Embed will request the minimum required scopes for the collections
    and actions enabled on the integration.
    """

    slug: str
    """The unique slug of the integration (defaults to provider slug)."""

    use_test_credentials: bool
    """Use test credentials provided by Embed."""
