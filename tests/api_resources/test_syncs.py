# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import SyncListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        sync = client.syncs.list()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.list(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSyncs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.list()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.list(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True
