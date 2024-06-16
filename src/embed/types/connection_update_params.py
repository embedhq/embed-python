# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectionUpdateParams"]


class ConnectionUpdateParams(TypedDict, total=False):
    integration_id: Required[str]
    """The integration to which the connection belongs."""

    exclusions: Optional[Dict[str, object]]
    """Exclusion rules for the connection.

    Only applicable for integrations that support exclusions.
    """

    inclusions: Optional[Dict[str, object]]
    """Inclusion rules for the connection.

    Only applicable for integrations that support inclusions.
    """

    metadata: Optional[Dict[str, object]]
    """Additional metadata for the connection."""
