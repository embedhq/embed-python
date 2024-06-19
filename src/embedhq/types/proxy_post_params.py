# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProxyPostParams"]


class ProxyPostParams(TypedDict, total=False):
    body: Required[Dict[str, object]]

    connection_id: Required[str]
    """The ID of the connection to use for the request."""

    integration_id: Required[str]
    """The ID of the integration to use for the request."""

    base_url_override: str
    """Override the base URL for the request."""

    retries: int
    """The number of times to retry the request."""
