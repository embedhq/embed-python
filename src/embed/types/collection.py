# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Collection"]


class Collection(BaseModel):
    auto_start_syncs: bool
    """
    Whether to automatically start syncing this collection after a connection is
    created.
    """

    created_at: int
    """The Unix timestamp (in seconds) for when the collection was created."""

    default_sync_frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"]
    """The default sync frequency for the collection."""

    exclude_properties_from_syncs: List[str]
    """An array of properties to exclude from being synced."""

    integration_id: str
    """The ID of the integration to which the collection belongs."""

    is_enabled: bool
    """Whether the collection is enabled."""

    object: Literal["collection"]
    """The object type, which is always `collection`."""

    provider_key: str
    """The unique key of the integration provider."""

    unique_key: str
    """The unique key of the collection."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the collection was updated."""
