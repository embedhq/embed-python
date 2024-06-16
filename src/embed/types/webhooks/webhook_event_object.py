# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebhookEventObject"]


class WebhookEventObject(BaseModel):
    id: str
    """The unique identifier for the webhook event."""

    delivered: bool
    """Whether the event was successfully delivered."""

    event: str
    """The event that occurred."""

    object: Literal["webhook_event"]
    """The object type, which is always `webhook_event`."""

    payload: Dict[str, builtins.object]
    """The payload of the event."""

    timestamp: int
    """The Unix timestamp (in seconds) for when the webhook event was created."""

    webhook_id: str
    """The unique identifier of the webhook that received the event."""
