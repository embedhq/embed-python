# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    integration_id: Required[str]
    """The ID of the integration to which the collection belongs."""

    auto_start_syncs: bool
    """
    Whether to automatically start syncing this collection after a connection is
    created.
    """

    configuration: Optional[Dict[str, object]]
    """Configuration options for the collection."""

    default_sync_frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"]
    """The default sync frequency for the collection."""

    exclude_properties_from_syncs: List[str]
    """An array of properties to exclude from being synced."""
