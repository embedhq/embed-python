# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionDeleteParams"]


class ActionDeleteParams(TypedDict, total=False):
    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    action_version: str
    """The version of the action to delete (defaults to latest)."""
