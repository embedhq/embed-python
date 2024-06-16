# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .webhook import Webhook

__all__ = ["WebhookDisableResponse"]


class WebhookDisableResponse(Webhook):
    is_enabled: Optional[bool] = None
