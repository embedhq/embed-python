# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectionDeleteParams"]


class ConnectionDeleteParams(TypedDict, total=False):
    integration_id: Required[str]
    """The integration to which the connection belongs."""
