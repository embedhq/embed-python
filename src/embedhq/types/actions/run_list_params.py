# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    action: Required[str]

    connected_account_id: Required[str]
    """The ID of the connected account to which the action belongs."""

    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    action_version: str
    """The version of the action (defaults to latest)."""
