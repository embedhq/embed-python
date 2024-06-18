# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunRetrieveParams"]


class RunRetrieveParams(TypedDict, total=False):
    collection_key: Required[str]

    connection_id: Required[str]
    """The ID of the connection to which the sync run belongs."""

    integration_id: Required[str]
    """The ID of the integration to which the sync run belongs."""
