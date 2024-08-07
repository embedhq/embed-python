# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SessionTokenDeleteResponse"]


class SessionTokenDeleteResponse(BaseModel):
    deleted: bool

    object: Literal["session_token"]

    token: Optional[str] = None
