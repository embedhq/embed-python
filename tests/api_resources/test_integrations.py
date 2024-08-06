# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import Integration, IntegrationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        integration = client.integrations.create(
            provider="github",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        integration = client.integrations.create(
            provider="github",
            name="GitHub",
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
            slug="github-123",
            use_test_credentials=False,
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.create(
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.create(
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        integration = client.integrations.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        integration = client.integrations.list(
            after="string",
            before="string",
            limit=20,
            order="desc",
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.create(
            provider="github",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.create(
            provider="github",
            name="GitHub",
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
            slug="github-123",
            use_test_credentials=False,
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.create(
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.create(
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.list()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.list(
            after="string",
            before="string",
            limit=20,
            order="desc",
        )
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationListResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationListResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True
