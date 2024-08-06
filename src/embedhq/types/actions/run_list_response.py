# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .action_run import ActionRun

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    data: List[ActionRun]

    object: Literal["list"]
