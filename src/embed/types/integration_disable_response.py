# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .integration import Integration

__all__ = ["IntegrationDisableResponse"]


class IntegrationDisableResponse(Integration):
    is_enabled: Optional[bool] = None
