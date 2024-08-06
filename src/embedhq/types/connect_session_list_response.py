# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .connect_session import ConnectSession

__all__ = ["ConnectSessionListResponse"]


class ConnectSessionListResponse(BaseModel):
    data: List[ConnectSession]

    object: Literal["list"]
