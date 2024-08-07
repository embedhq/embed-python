# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import QueryExecResponse, QueryMultiResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuery:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_exec(self, client: Embed) -> None:
        query = client.query.exec(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    def test_method_exec_with_all_params(self, client: Embed) -> None:
        query = client.query.exec(
            connected_account_id="user-123",
            integration="github-123",
            alpha=0,
            collection="issues",
            filter={"foo": "bar"},
            image="image",
            limit=1,
            query="query",
            return_properties=["string", "string", "string"],
            type="hybrid",
        )
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Embed) -> None:
        response = client.query.with_raw_response.exec(
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Embed) -> None:
        with client.query.with_streaming_response.exec(
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryExecResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_multi(self, client: Embed) -> None:
        query = client.query.multi()
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    def test_method_multi_with_all_params(self, client: Embed) -> None:
        query = client.query.multi(
            queries=[
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
            ],
        )
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    def test_raw_response_multi(self, client: Embed) -> None:
        response = client.query.with_raw_response.multi()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_multi(self, client: Embed) -> None:
        with client.query.with_streaming_response.multi() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryMultiResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuery:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_exec(self, async_client: AsyncEmbed) -> None:
        query = await async_client.query.exec(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    async def test_method_exec_with_all_params(self, async_client: AsyncEmbed) -> None:
        query = await async_client.query.exec(
            connected_account_id="user-123",
            integration="github-123",
            alpha=0,
            collection="issues",
            filter={"foo": "bar"},
            image="image",
            limit=1,
            query="query",
            return_properties=["string", "string", "string"],
            type="hybrid",
        )
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncEmbed) -> None:
        response = await async_client.query.with_raw_response.exec(
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryExecResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncEmbed) -> None:
        async with async_client.query.with_streaming_response.exec(
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryExecResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_multi(self, async_client: AsyncEmbed) -> None:
        query = await async_client.query.multi()
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    async def test_method_multi_with_all_params(self, async_client: AsyncEmbed) -> None:
        query = await async_client.query.multi(
            queries=[
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
                {
                    "integration": "github-123",
                    "connected_account_id": "user-123",
                    "collection": "issues",
                    "type": "hybrid",
                    "query": "query",
                    "filter": {"foo": "bar"},
                    "image": "image",
                    "alpha": 0,
                    "limit": 1,
                    "return_properties": ["string", "string", "string"],
                },
            ],
        )
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_multi(self, async_client: AsyncEmbed) -> None:
        response = await async_client.query.with_raw_response.multi()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryMultiResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_multi(self, async_client: AsyncEmbed) -> None:
        async with async_client.query.with_streaming_response.multi() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryMultiResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True
