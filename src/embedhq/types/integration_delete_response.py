# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntegrationDeleteResponse"]


class IntegrationDeleteResponse(BaseModel):
    deleted: bool

    object: Literal["integration"]

    slug: Optional[str] = None
