# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Sync"]


class Sync(BaseModel):
    collection_key: str
    """The unique key of the collection being synced."""

    connection_id: str
    """The unique identifier of the connection to which the sync belongs."""

    created_at: int
    """The Unix timestamp (in seconds) for when the sync was created."""

    frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"]
    """The frequency of the sync."""

    integration_id: str
    """The unique identifier of the integration to which the sync belongs."""

    last_synced_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the collection was last synced."""

    object: Literal["sync"]
    """The object type, which is always `sync`."""

    provider_key: str
    """The unique key of the integration provider."""

    status: Literal["running", "stopped", "error"]
    """The status of the sync."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the sync was updated."""
