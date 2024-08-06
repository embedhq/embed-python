# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ActionUpdateParams"]


class ActionUpdateParams(TypedDict, total=False):
    action: Required[str]

    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    action_version: str
    """The version of the action to update (defaults to latest)."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the action."""

    is_enabled: bool
    """Whether the action is enabled."""

    name: str
    """The display name of the action."""

    required_scopes: List[str]
    """The OAuth scopes required to trigger the action."""
