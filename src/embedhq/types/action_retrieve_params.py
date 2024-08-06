# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRetrieveParams"]


class ActionRetrieveParams(TypedDict, total=False):
    action: Required[str]

    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    action_version: str
    """The version of the action to retrieve (defaults to latest)."""
