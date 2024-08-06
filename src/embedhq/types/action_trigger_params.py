# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ActionTriggerParams"]


class ActionTriggerParams(TypedDict, total=False):
    action: Required[str]

    connected_account_id: Required[str]
    """The ID of the connected account used to trigger the action."""

    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    input: Required[Dict[str, object]]
    """The input parameters for the action."""

    action_version: str
    """The version of the action to trigger (defaults to latest)."""
