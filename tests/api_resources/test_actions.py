# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    Action,
    ActionListResponse,
    ActionDisableResponse,
    ActionTriggerResponse,
)
from embedhq.types.actions import ActionSchema

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        action = client.actions.retrieve(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.actions.with_raw_response.retrieve(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.actions.with_streaming_response.retrieve(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            client.actions.with_raw_response.retrieve(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        action = client.actions.list(
            integration_id="github-123",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.actions.with_raw_response.list(
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.actions.with_streaming_response.list(
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_disable(self, client: Embed) -> None:
        action = client.actions.disable(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Embed) -> None:
        response = client.actions.with_raw_response.disable(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Embed) -> None:
        with client.actions.with_streaming_response.disable(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionDisableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            client.actions.with_raw_response.disable(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_enable(self, client: Embed) -> None:
        action = client.actions.enable(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Embed) -> None:
        response = client.actions.with_raw_response.enable(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Embed) -> None:
        with client.actions.with_streaming_response.enable(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            client.actions.with_raw_response.enable(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_schema(self, client: Embed) -> None:
        action = client.actions.schema(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(ActionSchema, action, path=["response"])

    @parametrize
    def test_raw_response_schema(self, client: Embed) -> None:
        response = client.actions.with_raw_response.schema(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionSchema, action, path=["response"])

    @parametrize
    def test_streaming_response_schema(self, client: Embed) -> None:
        with client.actions.with_streaming_response.schema(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionSchema, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schema(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            client.actions.with_raw_response.schema(
                "",
                integration_id="github-123",
            )

    @parametrize
    def test_method_trigger(self, client: Embed) -> None:
        action = client.actions.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Embed) -> None:
        response = client.actions.with_raw_response.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Embed) -> None:
        with client.actions.with_streaming_response.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionTriggerResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            client.actions.with_raw_response.trigger(
                "",
                connection_id="user-123",
                integration_id="github-123",
                input={
                    "title": "bar",
                    "body": "bar",
                },
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.retrieve(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.retrieve(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.retrieve(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            await async_client.actions.with_raw_response.retrieve(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.list(
            integration_id="github-123",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.list(
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.list(
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_disable(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.disable(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.disable(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionDisableResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.disable(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionDisableResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            await async_client.actions.with_raw_response.disable(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.enable(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.enable(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.enable(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            await async_client.actions.with_raw_response.enable(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_schema(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.schema(
            "create-issue",
            integration_id="github-123",
        )
        assert_matches_type(ActionSchema, action, path=["response"])

    @parametrize
    async def test_raw_response_schema(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.schema(
            "create-issue",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionSchema, action, path=["response"])

    @parametrize
    async def test_streaming_response_schema(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.schema(
            "create-issue",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionSchema, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schema(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            await async_client.actions.with_raw_response.schema(
                "",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.trigger(
            "create-issue",
            connection_id="user-123",
            integration_id="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionTriggerResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_key` but received ''"):
            await async_client.actions.with_raw_response.trigger(
                "",
                connection_id="user-123",
                integration_id="github-123",
                input={
                    "title": "bar",
                    "body": "bar",
                },
            )
