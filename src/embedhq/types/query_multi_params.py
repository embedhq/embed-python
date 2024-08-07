# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryMultiParams", "Query"]


class QueryMultiParams(TypedDict, total=False):
    queries: Iterable[Query]
    """An array of query objects to execute in parallel."""


class Query(TypedDict, total=False):
    connected_account_id: Required[str]
    """The unique identifier of the connected account to query."""

    integration: Required[str]
    """The unique slug of the integration to query."""

    alpha: float
    """The relative weight used to merge vector and hybrid result sets.

    Only applicable for `hybrid` queries.
    """

    collection: str
    """The unique slug of the collection to query.

    If empty, all collections associated with the integration/connected account will
    be queried.
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
