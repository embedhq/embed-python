# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectSessionCreateParams"]


class ConnectSessionCreateParams(TypedDict, total=False):
    connected_account_id: Required[str]
    """The unique identifier for the connected account."""

    integration: Required[str]
    """The unique slug of the integration to connect the account to."""

    configuration: Optional[Dict[str, object]]
    """Configuration options to assign to the connected account."""

    expires_in_mins: int
    """The number of minutes until the connect session expires."""

    metadata: Optional[Dict[str, object]]
    """Additional metadata to assign to the connected account."""

    name: Optional[str]
    """The display name of the connected account."""

    redirect_url: Optional[str]
    """The URL to redirect to after the authorization flow is complete."""
