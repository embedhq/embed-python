# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embed import Embed, AsyncEmbed
from embed.types import (
    Integration,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationDisableResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        integration = client.integrations.create(
            provider_key="github",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        integration = client.integrations.create(
            provider_key="github",
            id="github-123",
            auth_scheme="oauth2",
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
            use_test_credentials=False,
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.create(
            provider_key="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.create(
            provider_key="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        integration = client.integrations.retrieve(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.retrieve(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.retrieve(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        integration = client.integrations.update(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        integration = client.integrations.update(
            "github-123",
            is_using_test_credentials=False,
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.update(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.update(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.update(
                "",
            )

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

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        integration = client.integrations.delete(
            "github-123",
        )
        assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.delete(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.delete(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_disable(self, client: Embed) -> None:
        integration = client.integrations.disable(
            "github-123",
        )
        assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.disable(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.disable(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.disable(
                "",
            )

    @parametrize
    def test_method_enable(self, client: Embed) -> None:
        integration = client.integrations.enable(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Embed) -> None:
        response = client.integrations.with_raw_response.enable(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Embed) -> None:
        with client.integrations.with_streaming_response.enable(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integrations.with_raw_response.enable(
                "",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.create(
            provider_key="github",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.create(
            provider_key="github",
            id="github-123",
            auth_scheme="oauth2",
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
            use_test_credentials=False,
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.create(
            provider_key="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.create(
            provider_key="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.retrieve(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.retrieve(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.retrieve(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.update(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.update(
            "github-123",
            is_using_test_credentials=False,
            oauth_client_id="string",
            oauth_client_secret="string",
            oauth_scopes=["string", "string", "string"],
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.update(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.update(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.update(
                "",
            )

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

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.delete(
            "github-123",
        )
        assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.delete(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.delete(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationDeleteResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.disable(
            "github-123",
        )
        assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.disable(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.disable(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationDisableResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.disable(
                "",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncEmbed) -> None:
        integration = await async_client.integrations.enable(
            "github-123",
        )
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.integrations.with_raw_response.enable(
            "github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(Integration, integration, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncEmbed) -> None:
        async with async_client.integrations.with_streaming_response.enable(
            "github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(Integration, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integrations.with_raw_response.enable(
                "",
            )
