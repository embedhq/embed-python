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
    ActionDeleteResponse,
    ActionTriggerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        action = client.actions.create(
            action_template="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        action = client.actions.create(
            action_template="create-issue",
            integration="github-123",
            configuration={"foo": "bar"},
            name="Create Issue",
            required_scopes=["repo"],
            slug="create-issue",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.actions.with_raw_response.create(
            action_template="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.actions.with_streaming_response.create(
            action_template="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        action = client.actions.retrieve(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Embed) -> None:
        action = client.actions.retrieve(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.actions.with_raw_response.retrieve(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.actions.with_streaming_response.retrieve(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.actions.with_raw_response.retrieve(
                action="",
                integration="github-123",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        action = client.actions.update(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        action = client.actions.update(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
            configuration={"foo": "bar"},
            is_enabled=True,
            name="Create Issue",
            required_scopes=["repo"],
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.actions.with_raw_response.update(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.actions.with_streaming_response.update(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.actions.with_raw_response.update(
                action="",
                integration="github-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        action = client.actions.list(
            integration="github-123",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.actions.with_raw_response.list(
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.actions.with_streaming_response.list(
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        action = client.actions.delete(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Embed) -> None:
        action = client.actions.delete(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
        )
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.actions.with_raw_response.delete(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.actions.with_streaming_response.delete(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionDeleteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.actions.with_raw_response.delete(
                action="",
                integration="github-123",
            )

    @parametrize
    def test_method_trigger(self, client: Embed) -> None:
        action = client.actions.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    def test_method_trigger_with_all_params(self, client: Embed) -> None:
        action = client.actions.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
            action_version="1.2",
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Embed) -> None:
        response = client.actions.with_raw_response.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
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
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            client.actions.with_raw_response.trigger(
                action="",
                connected_account_id="user-123",
                integration="github-123",
                input={
                    "title": "bar",
                    "body": "bar",
                },
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.create(
            action_template="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.create(
            action_template="create-issue",
            integration="github-123",
            configuration={"foo": "bar"},
            name="Create Issue",
            required_scopes=["repo"],
            slug="create-issue",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.create(
            action_template="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.create(
            action_template="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.retrieve(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.retrieve(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.retrieve(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.retrieve(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.actions.with_raw_response.retrieve(
                action="",
                integration="github-123",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.update(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.update(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
            configuration={"foo": "bar"},
            is_enabled=True,
            name="Create Issue",
            required_scopes=["repo"],
        )
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.update(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(Action, action, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.update(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(Action, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.actions.with_raw_response.update(
                action="",
                integration="github-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.list(
            integration="github-123",
        )
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.list(
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionListResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.list(
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionListResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.delete(
            action="create-issue",
            integration="github-123",
        )
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.delete(
            action="create-issue",
            integration="github-123",
            action_version="1.2",
        )
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.delete(
            action="create-issue",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionDeleteResponse, action, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.actions.with_streaming_response.delete(
            action="create-issue",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionDeleteResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.actions.with_raw_response.delete(
                action="",
                integration="github-123",
            )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncEmbed) -> None:
        action = await async_client.actions.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
            input={
                "title": "bar",
                "body": "bar",
            },
            action_version="1.2",
        )
        assert_matches_type(ActionTriggerResponse, action, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncEmbed) -> None:
        response = await async_client.actions.with_raw_response.trigger(
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
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
            action="create-issue",
            connected_account_id="user-123",
            integration="github-123",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action` but received ''"):
            await async_client.actions.with_raw_response.trigger(
                action="",
                connected_account_id="user-123",
                integration="github-123",
                input={
                    "title": "bar",
                    "body": "bar",
                },
            )
