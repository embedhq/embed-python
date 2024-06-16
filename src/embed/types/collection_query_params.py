# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionQueryParams"]


class CollectionQueryParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection to use for the query."""

    integration_id: Required[str]
    """The ID of the integration to which the collection belongs."""

    alpha: float
    """The relative weight used to merge vector and hybrid result sets.

    Only applicable for `hybrid` queries.
    """

    filter: Dict[str, object]
    """The filter to apply to the query."""

    image: str
    """The URL or base-64 string of the image to match against.

    Only applicable for `vector` queries.
    """

    limit: int
    """A limit on the number of objects to be returned."""

    query: str
    """The query string to match against."""

    return_properties: List[str]
    """Specify properties you want to return in the results set."""

    type: Literal["hybrid", "vector", "keyword"]
    """The type of query."""
