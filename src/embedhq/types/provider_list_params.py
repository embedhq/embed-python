# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProviderListParams"]


class ProviderListParams(TypedDict, total=False):
    include_action_templates: bool
    """Include action templates for each provider in the response."""

    include_collection_templates: bool
    """Include collection templates for each provider in the response."""
