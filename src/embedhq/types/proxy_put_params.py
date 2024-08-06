# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProxyPutParams"]


class ProxyPutParams(TypedDict, total=False):
    body: Required[Dict[str, object]]

    x_embed_connected_account_id: Required[Annotated[str, PropertyInfo(alias="X-Embed-Connected-Account-Id")]]
    """The ID of the connected account to use for the request."""

    x_embed_integration: Required[Annotated[str, PropertyInfo(alias="X-Embed-Integration")]]
    """The slug of the integration to use for the request."""

    x_embed_base_url_override: Annotated[str, PropertyInfo(alias="X-Embed-Base-Url-Override")]
    """Override the base URL for the request."""

    x_embed_retries: Annotated[int, PropertyInfo(alias="X-Embed-Retries")]
    """The number of times to retry the request."""
