# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SyncUpdateParams"]


class SyncUpdateParams(TypedDict, total=False):
    collection: Required[str]

    connected_account_id: Required[str]
    """The ID of the connected account to which the syncs belong."""

    integration: Required[str]
    """The slug of the integration to which the sync belongs."""

    collection_version: str
    """The collection version (defaults to latest)."""

    exclusions: List[str]
    """Array of IDs to exclude from the sync.

    If present, objects with matching IDs will not be synced.
    """

    frequency: str
    """The frequency of the sync."""

    inclusions: List[str]
    """Array of IDs to include in the sync.

    If present, only objects with matching IDs will be synced.
    """
