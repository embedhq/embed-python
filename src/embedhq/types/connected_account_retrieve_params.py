# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectedAccountRetrieveParams"]


class ConnectedAccountRetrieveParams(TypedDict, total=False):
    connected_account_id: Required[str]

    integration: Required[str]
    """The slug of the integration to which the connected account belongs."""
