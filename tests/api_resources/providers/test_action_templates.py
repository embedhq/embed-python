# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types.providers import ActionTemplateListResponse, ActionTemplateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActionTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        action_template = client.providers.action_templates.retrieve(
            action="create-issue",
            provider="github",
        )
        assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.providers.action_templates.with_raw_response.retrieve(
            action="create-issue",
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_template = response.parse()
        assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.providers.action_templates.with_streaming_response.retrieve(
            action="create-issue",
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_template = response.parse()
            assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.providers.action_templates.with_raw_response.retrieve(
                action="create-issue",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.providers.action_templates.with_raw_response.retrieve(
                action="",
                provider="github",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        action_template = client.providers.action_templates.list(
            "github",
        )
        assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.providers.action_templates.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_template = response.parse()
        assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.providers.action_templates.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_template = response.parse()
            assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.providers.action_templates.with_raw_response.list(
                "",
            )


class TestAsyncActionTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        action_template = await async_client.providers.action_templates.retrieve(
            action="create-issue",
            provider="github",
        )
        assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.action_templates.with_raw_response.retrieve(
            action="create-issue",
            provider="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_template = await response.parse()
        assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.action_templates.with_streaming_response.retrieve(
            action="create-issue",
            provider="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_template = await response.parse()
            assert_matches_type(ActionTemplateRetrieveResponse, action_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.providers.action_templates.with_raw_response.retrieve(
                action="create-issue",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.providers.action_templates.with_raw_response.retrieve(
                action="",
                provider="github",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        action_template = await async_client.providers.action_templates.list(
            "github",
        )
        assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.providers.action_templates.with_raw_response.list(
            "github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_template = await response.parse()
        assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.providers.action_templates.with_streaming_response.list(
            "github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_template = await response.parse()
            assert_matches_type(ActionTemplateListResponse, action_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.providers.action_templates.with_raw_response.list(
                "",
            )
