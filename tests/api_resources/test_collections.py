# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embed import Embed, AsyncEmbed
from embed.types import (
    Collection,
    CollectionListResponse,
    CollectionQueryResponse,
    CollectionDisableResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        collection = client.collections.retrieve(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.collections.with_raw_response.retrieve(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.collections.with_streaming_response.retrieve(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.collections.with_raw_response.retrieve(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        collection = client.collections.update(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        collection = client.collections.update(
            "issues",
            integration_id="github-123",
            auto_start_syncs=True,
            configuration={"foo": "bar"},
            default_sync_frequency="daily",
            exclude_properties_from_syncs=["string", "string", "string"],
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.collections.with_raw_response.update(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.collections.with_streaming_response.update(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.collections.with_raw_response.update(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        collection = client.collections.list(
            integration_id="github-123",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.collections.with_raw_response.list(
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.collections.with_streaming_response.list(
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_disable(self, client: Embed) -> None:
        collection = client.collections.disable(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(CollectionDisableResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Embed) -> None:
        response = client.collections.with_raw_response.disable(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDisableResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Embed) -> None:
        with client.collections.with_streaming_response.disable(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDisableResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.collections.with_raw_response.disable(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_enable(self, client: Embed) -> None:
        collection = client.collections.enable(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Embed) -> None:
        response = client.collections.with_raw_response.enable(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Embed) -> None:
        with client.collections.with_streaming_response.enable(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.collections.with_raw_response.enable(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_query(self, client: Embed) -> None:
        collection = client.collections.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Embed) -> None:
        collection = client.collections.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
            alpha=0,
            filter={"foo": "bar"},
            image="string",
            limit=1,
            query="string",
            return_properties=["string", "string", "string"],
            type="hybrid",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Embed) -> None:
        response = client.collections.with_raw_response.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Embed) -> None:
        with client.collections.with_streaming_response.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionQueryResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.collections.with_raw_response.query(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.retrieve(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.update(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.update(
            "issues",
            integration_id="github-123",
            auto_start_syncs=True,
            configuration={"foo": "bar"},
            default_sync_frequency="daily",
            exclude_properties_from_syncs=["string", "string", "string"],
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.update(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.update(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.collections.with_raw_response.update(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.list(
            integration_id="github-123",
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.list(
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.list(
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_disable(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.disable(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(CollectionDisableResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.disable(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDisableResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.disable(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDisableResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.collections.with_raw_response.disable(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.enable(
            "issues",
            integration_id="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.enable(
            "issues",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.enable(
            "issues",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.collections.with_raw_response.enable(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
            alpha=0,
            filter={"foo": "bar"},
            image="string",
            limit=1,
            query="string",
            return_properties=["string", "string", "string"],
            type="hybrid",
        )
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionQueryResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.query(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionQueryResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.collections.with_raw_response.query(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )
