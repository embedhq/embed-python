# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectedAccountListParams"]


class ConnectedAccountListParams(TypedDict, total=False):
    after: str
    """A cursor for use in pagination.

    `after` is an object ID or slug that defines your place in the list.
    """

    before: str
    """A cursor for use in pagination.

    `before` is an object ID or slug that defines your place in the list.
    """

    integration: str
    """Filter connected accounts by integration slug."""

    limit: int
    """A limit on the number of objects to be returned."""

    order: Literal["asc", "desc"]
    """Sort order by the `created_at` timestamp of the objects."""
