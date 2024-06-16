# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionListParams"]


class ConnectionListParams(TypedDict, total=False):
    after: str
    """A cursor for use in pagination.

    `after` is an object ID that defines your place in the list.
    """

    before: str
    """A cursor for use in pagination.

    `before` is an object ID that defines your place in the list.
    """

    integration_id: str
    """Filter for connections belonging to a specific integration."""

    limit: int
    """A limit on the number of objects to be returned."""

    order: Literal["asc", "desc"]
    """Sort order by the `created_at` timestamp of the objects."""
