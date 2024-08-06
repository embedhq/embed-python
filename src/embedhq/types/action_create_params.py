# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ActionCreateParams"]


class ActionCreateParams(TypedDict, total=False):
    action_template: Required[str]
    """The slug of the action template to use."""

    integration: Required[str]
    """The slug of the integration to which the action belongs."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the action."""

    name: str
    """The display name of the action (defaults to the action template name)."""

    required_scopes: List[str]
    """
    The OAuth scopes required to trigger the action (defaults to the action template
    scopes, if applicable).
    """

    slug: str
    """The unique slug of the action (defaults to the action template slug)."""
