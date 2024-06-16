# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .actions.action_schema import ActionSchema
from .collections.collection_schema import CollectionSchema

__all__ = ["Provider", "Schema"]


class Schema(BaseModel):
    auth: List[Dict[str, object]]
    """The authentication schemes supported by the integration provider."""

    base_url: str
    """The base URL of the integration provider."""

    logo_url: str
    """The URL of the logo of the integration provider."""

    name: str
    """The name of the integration provider."""

    unique_key: str
    """The unique key of the integration provider."""

    actions: Optional[List[ActionSchema]] = None

    collections: Optional[List[CollectionSchema]] = None

    docs_url: Optional[str] = None
    """The documentation URL of the integration provider."""

    logo_url_dark_mode: Optional[str] = None
    """The URL of the dark mode logo of the integration provider."""


class Provider(BaseModel):
    object: Literal["provider"]
    """The object type, which is always `provider`."""

    schema_: Schema = FieldInfo(alias="schema")

    unique_key: str
    """The unique key of the integration provider."""
