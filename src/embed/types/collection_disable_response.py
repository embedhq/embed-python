# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .collection import Collection

__all__ = ["CollectionDisableResponse"]


class CollectionDisableResponse(Collection):
    is_enabled: Optional[bool] = None
