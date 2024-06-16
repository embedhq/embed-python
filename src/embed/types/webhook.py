# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """The unique identifier for the webhook."""

    created_at: int
    """The Unix timestamp (in seconds) for when the webhook was created."""

    is_enabled: bool
    """Whether the webhook is enabled."""

    object: Literal["webhook"]
    """The object type, which is always `webhook`."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the webhook was updated."""

    url: str
    """The URL to send events to."""

    events: Optional[List[str]] = None
    """The events to send to the webhook."""

    signing_secret: Optional[str] = None
    """The secret used to sign the webhook payload."""
