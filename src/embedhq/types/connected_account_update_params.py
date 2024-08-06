# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectedAccountUpdateParams"]


class ConnectedAccountUpdateParams(TypedDict, total=False):
    connected_account_id: Required[str]

    integration: Required[str]
    """The slug of the integration to which the connected account belongs."""

    configuration: Optional[Dict[str, object]]
    """Configuration options for the connected account."""

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the connected account."""

    name: str
    """The display name of the connected account."""
