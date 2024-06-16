# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .provider import Provider

__all__ = ["ProviderListResponse"]


class ProviderListResponse(BaseModel):
    data: List[Provider]

    object: Literal["list"]
