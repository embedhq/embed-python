# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionTemplateRetrieveResponse"]


class ActionTemplateRetrieveResponse(BaseModel):
    configuration: Optional[Dict[str, object]] = None
    """Configuration options for the action template."""

    name: str
    """The display name of the action template."""

    object: Literal["action_template"]
    """The object type, which is always `action_template`."""

    provider: str
    """The unique slug of the provider."""

    required_scopes: List[str]
    """The OAuth scopes required for the action template."""

    schema_: Dict[str, builtins.object] = FieldInfo(alias="schema")
    """The schema of the action template."""

    slug: str
    """The unique slug of the action template."""
