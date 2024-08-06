# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["IntegrationUpdateParams"]


class IntegrationUpdateParams(TypedDict, total=False):
    is_using_test_credentials: bool
    """Whether the integration is using test credentials provided by Embed."""

    oauth_client_id: Optional[str]
    """The OAuth Client ID. Required for integrations that use OAuth authentication."""

    oauth_client_secret: Optional[str]
    """The OAuth Client Secret.

    Required for integrations that use OAuth authentication.
    """

    oauth_scopes: List[str]
    """Additional OAuth scopes to request from the user.

    By default, Embed will request the minimum required scopes for the collections
    and actions enabled on the integration.
    """
