# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    events: List[str]
    """The events to send to the webhook."""

    is_enabled: bool
    """Whether the webhook is enabled."""

    url: str
    """The URL to send events to."""
