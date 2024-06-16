# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProxyDeleteParams"]


class ProxyDeleteParams(TypedDict, total=False):
    body: Required[Dict[str, object]]
