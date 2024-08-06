# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SyncListParams"]


class SyncListParams(TypedDict, total=False):
    connected_account_id: str
    """Filter syncs by connected account."""

    integration: str
    """Filter syncs by integration."""
