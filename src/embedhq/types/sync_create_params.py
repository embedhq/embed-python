# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SyncCreateParams"]


class SyncCreateParams(TypedDict, total=False):
    collection: Required[str]
    """The unique slug of the collection."""

    connected_account_id: Required[str]
    """The unique identifier of the connected account."""

    integration: Required[str]
    """The unique slug of the integration."""

    collection_version: str
    """The collection version used for the sync (defaults to latest)."""

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
