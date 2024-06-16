# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .session_token import SessionToken

__all__ = ["SessionTokenListResponse"]


class SessionTokenListResponse(BaseModel):
    data: List[SessionToken]

    object: Literal["list"]
