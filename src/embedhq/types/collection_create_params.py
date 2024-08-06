# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    collection_template: Required[str]
    """The unique slug of the collection template to use."""

    integration: Required[str]
    """The unique slug of the integration to which the collection belongs."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the collection."""

    name: str
    """The display name of the collection (defaults to the collection template name)."""

    required_scopes: List[str]
    """
    The OAuth scopes required to sync the collection (defaults to the collection
    template scopes, if applicable).
    """

    slug: str
    """The unique slug of the collection (defaults to the collection template slug)."""
