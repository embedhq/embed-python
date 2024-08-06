# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .sync_run import SyncRun
from ..._models import BaseModel

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    data: List[SyncRun]

    object: Literal["list"]
