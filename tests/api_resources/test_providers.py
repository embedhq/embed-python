# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import Provider, ProviderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        provider = client.providers.retrieve(
            provider="github",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Embed) -> None:
        provider = client.providers.retrieve(
            provider="github",
            include_action_templates=False,
            include_collection_templates=False,
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.providers.with_raw_response.retrieve(
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.providers.with_streaming_response.retrieve(
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.providers.with_raw_response.retrieve(
                provider="",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        provider = client.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        provider = client.providers.list(
            include_action_templates=False,
            include_collection_templates=False,
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProviders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        provider = await async_client.providers.retrieve(
            provider="github",
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmbed) -> None:
        provider = await async_client.providers.retrieve(
            provider="github",
            include_action_templates=False,
            include_collection_templates=False,
        )
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.with_raw_response.retrieve(
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(Provider, provider, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.with_streaming_response.retrieve(
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(Provider, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.providers.with_raw_response.retrieve(
                provider="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        provider = await async_client.providers.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        provider = await async_client.providers.list(
            include_action_templates=False,
            include_collection_templates=False,
        )
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True
