# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .action import Action
from .._models import BaseModel

__all__ = ["ActionListResponse"]


class ActionListResponse(BaseModel):
    data: List[Action]

    object: Literal["list"]
