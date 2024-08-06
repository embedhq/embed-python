# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Sync"]


class Sync(BaseModel):
    collection: str
    """The unique slug of the collection being synced."""

    collection_version: str
    """The version of the collection schema used for the sync."""

    connected_account_id: str
    """The unique identifier of the connected account being synced."""

    created_at: int
    """The Unix timestamp (in seconds) for when the sync was created."""

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

    integration: str
    """The unique slug of the integration to which the collection belongs."""

    last_synced_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the collection was last synced."""

    object: Literal["sync"]
    """The object type, which is always `sync`."""

    status: Literal["running", "stopped", "error"]
    """The status of the sync."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the sync was updated."""
