# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Collection"]


class Collection(BaseModel):
    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the collection."""

    created_at: int
    """The Unix timestamp (in seconds) for when the collection was created."""

    integration: str
    """The slug of the integration to which the collection belongs."""

    is_enabled: bool
    """Whether the collection is enabled."""

    name: str
    """The display name of the collection."""

    object: Literal["collection"]
    """The object type, which is always `collection`."""

    schema_: Dict[str, builtins.object] = FieldInfo(alias="schema")
    """The collection schema."""

    slug: str
    """The unique slug of the collection."""

    updated_at: int
    """The Unix timestamp (in seconds) for when the collection was updated."""

    version: str
    """The version of the collection, formatted as "MAJOR.MINOR"."""

    required_scopes: Optional[List[str]] = None
    """The OAuth scopes required to sync the collection."""
