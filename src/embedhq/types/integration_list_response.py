# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .integration import Integration

__all__ = ["IntegrationListResponse"]


class IntegrationListResponse(BaseModel):
    data: List[Integration]

    object: Literal["list"]

    first: Optional[str] = None

    has_more: Optional[bool] = None

    last: Optional[str] = None
