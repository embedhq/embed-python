# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import CollectionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        collection = client.collections.list(
            integration="github-123",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.collections.with_raw_response.list(
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.collections.with_streaming_response.list(
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.list(
            integration="github-123",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.list(
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.list(
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True
