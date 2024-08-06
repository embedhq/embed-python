# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProviderRetrieveParams"]


class ProviderRetrieveParams(TypedDict, total=False):
    include_action_templates: bool
    """Include action templates in the response."""

    include_collection_templates: bool
    """Include collection templates in the response."""
