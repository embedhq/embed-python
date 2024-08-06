# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CollectionTemplateListResponse", "Data"]


class Data(BaseModel):
    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the collection template."""

    name: str
    """The display name of the collection template."""

    object: Literal["collection_template"]
    """The object type, which is always `collection_template`."""

    provider: str
    """The unique slug of the provider."""

    required_scopes: List[str]
    """The OAuth scopes required for the collection template."""

    schema_: Dict[str, builtins.object] = FieldInfo(alias="schema")
    """The schema of the collection template."""

    slug: str
    """The unique slug of the collection template."""


class CollectionTemplateListResponse(BaseModel):
    data: List[Data]

    object: Literal["list"]
