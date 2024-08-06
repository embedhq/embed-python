# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollectionDeleteParams"]


class CollectionDeleteParams(TypedDict, total=False):
    collection: Required[str]

    integration: Required[str]
    """The slug of the integration to which the collection belongs."""

    collection_version: str
    """The version of the collection to delete (defaults to latest)."""
