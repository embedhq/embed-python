# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ActionTriggerParams"]


class ActionTriggerParams(TypedDict, total=False):
    connection_id: Required[str]
    """The ID of the connection to use for the action."""

    integration_id: Required[str]
    """The ID of the integration to which the action belongs."""

    input: Required[Dict[str, object]]
    """The input parameters for the action."""
