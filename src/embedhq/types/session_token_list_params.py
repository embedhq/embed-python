# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionTokenListParams"]


class SessionTokenListParams(TypedDict, total=False):
    connected_account_id: str
    """Filter for session tokens associated with a connected account."""

    integration: str
    """Filter for session tokens associated with an integration."""
