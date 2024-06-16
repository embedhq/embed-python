# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SyncUpdateParams"]


class SyncUpdateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection to which the sync belongs."""

    integration_id: Required[str]
    """The ID of the integration to which the sync belongs."""

    frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"]
    """The frequency of the sync."""
