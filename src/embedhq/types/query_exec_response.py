# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["QueryExecResponse", "Hit", "HitHighlight"]


class HitHighlight(BaseModel):
    field: Optional[str] = None

    matched_tokens: Optional[List[str]] = None

    snippet: Optional[str] = None


class Hit(BaseModel):
    highlights: Optional[List[HitHighlight]] = None

    object: Optional[Dict[str, builtins.object]] = None
    """The data object returned by the query."""

    score: Optional[float] = None
    """The relevance score of the object for the given query."""


class QueryExecResponse(BaseModel):
    found: int
    """The total number of objects matching the query."""

    hits: List[Hit]

    out_of: int
    """The total number of objects considered for the query."""

    page: int
    """The current page number of the results."""

    search_time_ms: int
    """The time taken to execute the search in milliseconds."""
