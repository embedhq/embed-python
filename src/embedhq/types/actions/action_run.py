# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionRun"]


class ActionRun(BaseModel):
    id: str
    """The unique identifier of the action run."""

    action_key: str
    """The unique key of the action being run."""

    connection_id: str
    """The unique identifier of the connection to which the action belongs."""

    duration: Optional[int] = None
    """The duration of the action run (in seconds)."""

    input: Dict[str, object]
    """The input parameters for the action run."""

    integration_id: str
    """The unique identifier of the integration to which the action belongs."""

    object: Literal["action_run"]
    """The object type, which is always `action_run`."""

    output: Dict[str, builtins.object]
    """The output of the action run."""

    status: Literal["running", "succeeded", "failed"]
    """The status of the action run."""

    timestamp: int
    """The Unix timestamp (in seconds) for when the action run started."""
