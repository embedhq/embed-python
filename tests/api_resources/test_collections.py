# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    Collection,
    CollectionListResponse,
    CollectionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        collection = client.collections.create(
            collection_template="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        collection = client.collections.create(
            collection_template="issues",
            integration="github-123",
            configuration={"foo": "bar"},
            name="Issues",
            required_scopes=["repo"],
            slug="issues",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.collections.with_raw_response.create(
            collection_template="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.collections.with_streaming_response.create(
            collection_template="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        collection = client.collections.retrieve(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Embed) -> None:
        collection = client.collections.retrieve(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.collections.with_raw_response.retrieve(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.collections.with_streaming_response.retrieve(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.collections.with_raw_response.retrieve(
                collection="",
                integration="github-123",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        collection = client.collections.update(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        collection = client.collections.update(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
            configuration={"foo": "bar"},
            is_enabled=True,
            name="Issues",
            required_scopes=["repo"],
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.collections.with_raw_response.update(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.collections.with_streaming_response.update(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.collections.with_raw_response.update(
                collection="",
                integration="github-123",
            )

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

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        collection = client.collections.delete(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Embed) -> None:
        collection = client.collections.delete(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.collections.with_raw_response.delete(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.collections.with_streaming_response.delete(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.collections.with_raw_response.delete(
                collection="",
                integration="github-123",
            )


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.create(
            collection_template="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.create(
            collection_template="issues",
            integration="github-123",
            configuration={"foo": "bar"},
            name="Issues",
            required_scopes=["repo"],
            slug="issues",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.create(
            collection_template="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.create(
            collection_template="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.retrieve(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.retrieve(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.collections.with_raw_response.retrieve(
                collection="",
                integration="github-123",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.update(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.update(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
            configuration={"foo": "bar"},
            is_enabled=True,
            name="Issues",
            required_scopes=["repo"],
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.update(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.update(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(Collection, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.collections.with_raw_response.update(
                collection="",
                integration="github-123",
            )

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

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.delete(
            collection="issues",
            integration="github-123",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmbed) -> None:
        collection = await async_client.collections.delete(
            collection="issues",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.collections.with_raw_response.delete(
            collection="issues",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.collections.with_streaming_response.delete(
            collection="issues",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.collections.with_raw_response.delete(
                collection="",
                integration="github-123",
            )
