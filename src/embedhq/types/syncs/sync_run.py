# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SyncRun"]


class SyncRun(BaseModel):
    id: str
    """The unique identifier of the sync run."""

    collection_key: str
    """The unique key of the collection being synced."""

    connection_id: str
    """The unique identifier of the connection to which the sync belongs."""

    created_at: int
    """The Unix timestamp (in seconds) for when the sync run was created."""

    integration_id: str
    """The unique identifier of the integration to which the sync belongs."""

    object: Literal["sync_run"]
    """The object type, which is always `sync_run`."""

    records_added: Optional[int] = None
    """The number of records added during the sync run."""

    records_deleted: Optional[int] = None
    """The number of records deleted during the sync run."""

    records_updated: Optional[int] = None
    """The number of records updated during the sync run."""

    status: Literal["running", "stopped", "completed", "failed"]
    """The status of the sync run."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the sync run was updated."""
