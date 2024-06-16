# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .sync import Sync
from .._models import BaseModel

__all__ = ["SyncListResponse"]


class SyncListResponse(BaseModel):
    data: List[Sync]

    object: Literal["list"]
