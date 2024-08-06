# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types.providers import CollectionTemplateListResponse, CollectionTemplateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollectionTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        collection_template = client.providers.collection_templates.retrieve(
            collection="issues",
            provider="github",
        )
        assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.providers.collection_templates.with_raw_response.retrieve(
            collection="issues",
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection_template = response.parse()
        assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.providers.collection_templates.with_streaming_response.retrieve(
            collection="issues",
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection_template = response.parse()
            assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.providers.collection_templates.with_raw_response.retrieve(
                collection="issues",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.providers.collection_templates.with_raw_response.retrieve(
                collection="",
                provider="github",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        collection_template = client.providers.collection_templates.list(
            "github",
        )
        assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.providers.collection_templates.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection_template = response.parse()
        assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.providers.collection_templates.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection_template = response.parse()
            assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.providers.collection_templates.with_raw_response.list(
                "",
            )


class TestAsyncCollectionTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        collection_template = await async_client.providers.collection_templates.retrieve(
            collection="issues",
            provider="github",
        )
        assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.collection_templates.with_raw_response.retrieve(
            collection="issues",
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection_template = await response.parse()
        assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.collection_templates.with_streaming_response.retrieve(
            collection="issues",
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection_template = await response.parse()
            assert_matches_type(CollectionTemplateRetrieveResponse, collection_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.providers.collection_templates.with_raw_response.retrieve(
                collection="issues",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.providers.collection_templates.with_raw_response.retrieve(
                collection="",
                provider="github",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        collection_template = await async_client.providers.collection_templates.list(
            "github",
        )
        assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.collection_templates.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection_template = await response.parse()
        assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.collection_templates.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection_template = await response.parse()
            assert_matches_type(CollectionTemplateListResponse, collection_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.providers.collection_templates.with_raw_response.list(
                "",
            )
