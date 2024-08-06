# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SyncDeleteResponse"]


class SyncDeleteResponse(BaseModel):
    collection: str

    deleted: bool

    object: Literal["sync"]
