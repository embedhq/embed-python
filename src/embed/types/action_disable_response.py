# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .action import Action

__all__ = ["ActionDisableResponse"]


class ActionDisableResponse(Action):
    is_enabled: Optional[bool] = None
