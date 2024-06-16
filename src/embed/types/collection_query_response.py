# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CollectionQueryResponse"]


class CollectionQueryResponse(BaseModel):
    data: List[Dict[str, object]]

    object: Literal["list"]
