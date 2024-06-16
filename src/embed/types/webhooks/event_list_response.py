# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .webhook_event_object import WebhookEventObject

__all__ = ["EventListResponse"]


class EventListResponse(BaseModel):
    data: List[WebhookEventObject]

    object: Literal["list"]
