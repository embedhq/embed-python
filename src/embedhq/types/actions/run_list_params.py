# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection to which the action runs belong."""

    integration_id: Required[str]
    """The ID of the integration to which the action runs belong."""
