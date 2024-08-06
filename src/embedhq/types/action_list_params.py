# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionListParams"]


class ActionListParams(TypedDict, total=False):
    integration: Required[str]
    """The slug of the integration to which the actions belong."""
