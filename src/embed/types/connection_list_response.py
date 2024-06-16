# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .connection import Connection

__all__ = ["ConnectionListResponse"]


class ConnectionListResponse(BaseModel):
    data: List[Connection]

    object: Literal["list"]

    first_id: Optional[str] = None

    has_more: Optional[bool] = None

    last_id: Optional[str] = None
