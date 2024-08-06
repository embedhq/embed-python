# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .connected_account import ConnectedAccount

__all__ = ["ConnectedAccountListResponse"]


class ConnectedAccountListResponse(BaseModel):
    data: List[ConnectedAccount]

    object: Literal["list"]

    first: Optional[str] = None

    has_more: Optional[bool] = None

    last: Optional[str] = None
