# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SyncRetrieveParams"]


class SyncRetrieveParams(TypedDict, total=False):
    collection: Required[str]

    connected_account_id: Required[str]
    """The ID of the connected account to which the syncs belong."""

    integration: Required[str]
    """The slug of the integration to which the sync belongs."""

    collection_version: str
    """The collection version (defaults to latest)."""
