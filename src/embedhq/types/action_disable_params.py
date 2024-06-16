# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDisableParams"]


class ActionDisableParams(TypedDict, total=False):
    integration_id: Required[str]
    """The ID of the integration to which the action belongs."""
