# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .action_schema import ActionSchema

__all__ = ["SchemaListResponse"]


class SchemaListResponse(BaseModel):
    data: List[ActionSchema]

    object: Literal["list"]
