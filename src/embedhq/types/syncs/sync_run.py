# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SyncRun"]


class SyncRun(BaseModel):
    id: str
    """The unique identifier of the sync run."""

    collection: str
    """The unique slug of the collection being synced."""

    collection_version: str
    """The collection version used for the sync."""

    connected_account_id: str
    """The unique identifier of the connected account to which the sync belongs."""

    duration: Optional[float] = None
    """The duration of the sync run (in seconds)."""

    integration: str
    """The unique slug of the integration to which the sync belongs."""

    object: Literal["sync_run"]
    """The object type, which is always `sync_run`."""

    records_added: Optional[int] = None
    """The number of records added during the sync run."""

    records_deleted: Optional[int] = None
    """The number of records deleted during the sync run."""

    records_updated: Optional[int] = None
    """The number of records updated during the sync run."""

    status: Literal["running", "stopped", "succeeded", "failed"]
    """The status of the sync run."""

    timestamp: int
    """The Unix timestamp (in seconds) for when the sync run started."""
