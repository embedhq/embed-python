# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Provider"]


class Provider(BaseModel):
    auth_methods: List[str]
    """The authentication methods supported by the provider."""

    base_url: str
    """The base URL of the provider's API."""

    docs_url: Optional[str] = None
    """The URL to the provider's API documentation."""

    headers: Optional[Dict[str, object]] = None
    """Headers to attach to requests made to the provider."""

    logo_url: Optional[str] = None
    """The URL to the provider's logo."""

    logo_url_dark_mode: str
    """The URL to the provider's logo, optimized for dark mode."""

    name: str
    """The display name of the provider."""

    oauth_configuration: Optional[Dict[str, object]] = None
    """The configuration details required for OAuth authentication."""

    object: Literal["provider"]
    """The object type, which is always `provider`."""

    rate_limit_configuration: Optional[Dict[str, builtins.object]] = None
    """
    The configuration details required to handle rate limits imposed by the
    provider.
    """

    slug: str
    """The unique slug of the integration provider."""

    visibility: Literal["public", "private"]
    """Whether the provider is public or private."""
