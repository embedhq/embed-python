# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .collection import Collection

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    data: List[Collection]

    object: Literal["list"]
