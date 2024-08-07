# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Integration"]


class Integration(BaseModel):
    auth_method: Literal["oauth2", "basic", "api_key", "none"]
    """The authentication method the integration uses."""

    created_at: int
    """The Unix timestamp (in seconds) for when the integration was created."""

    is_enabled: bool
    """Whether the integration is enabled."""

    is_using_test_credentials: bool
    """Whether the integration is using test credentials provided by Embed."""

    logo_url: str
    """The URL of the integration provider's logo."""

    oauth_client_id: Optional[str] = None
    """The OAuth Client ID. Required for integrations that use OAuth."""

    oauth_client_secret: Optional[str] = None
    """The OAuth Client Secret. Required for integrations that use OAuth."""

    oauth_scopes: List[str]
    """Additional OAuth scopes to request from the user.

    By default, Embed will request the minimum required scopes for the collections
    and actions enabled on the integration.
    """

    object: Literal["integration"]
    """The object type, which is always `integration`."""

    provider: str
    """The unique slug of the provider."""

    slug: str
    """The unique slug of the integration."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the integration was updated."""

    logo_url_dark_mode: Optional[str] = None
    """The URL of the integration provider's logo suitable for dark mode."""
