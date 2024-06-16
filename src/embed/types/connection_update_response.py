# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .connection import Connection

__all__ = ["ConnectionUpdateResponse"]


class ConnectionUpdateResponse(Connection):
    metadata: Optional[Dict[str, object]] = None
