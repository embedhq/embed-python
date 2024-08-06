# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionRun"]


class ActionRun(BaseModel):
    id: str
    """The unique identifier of the action run."""

    action: str
    """The unique slug of the action being run."""

    connected_account_id: str
    """The unique identifier of the connected account to which the action belongs."""

    duration: Optional[float] = None
    """The duration of the action run (in seconds)."""

    input: Dict[str, object]
    """The input parameters for the action run."""

    integration: str
    """The slug of the integration to which the action belongs."""

    object: Literal["action_run"]
    """The object type, which is always `action_run`."""

    output: Optional[Dict[str, builtins.object]] = None
    """The output of the action run."""

    status: Literal["running", "succeeded", "failed"]
    """The status of the action run."""

    timestamp: int
    """The Unix timestamp (in seconds) for when the action ran."""
