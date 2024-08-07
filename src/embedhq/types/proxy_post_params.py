# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProxyPostParams"]


class ProxyPostParams(TypedDict, total=False):
    endpoint: Required[str]
    """The endpoint to proxy the request to."""

    body: Required[Dict[str, object]]

    connected_account_id: Required[str]
    """The ID of the connected account to use for the request."""

    integration: Required[str]
    """The slug of the integration to use for the request."""

    base_url_override: str
    """Override the base URL for the request."""

    response_type: Literal["arraybuffer", "json", "text", "stream"]
    """Override the base URL for the request."""

    retries: int
    """The number of times to retry the request."""
