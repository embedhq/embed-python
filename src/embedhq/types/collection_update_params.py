# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    collection: Required[str]

    integration: Required[str]
    """The slug of the integration to which the collection belongs."""

    collection_version: str
    """The version of the collection to update (defaults to latest)."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the collection."""

    is_enabled: bool
    """Whether the collection is enabled."""

    name: str
    """The display name of the collection."""

    required_scopes: List[str]
    """The OAuth scopes required to sync the collection."""
