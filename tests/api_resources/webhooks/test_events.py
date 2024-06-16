# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types.webhooks import EventListResponse, WebhookEventObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        event = client.webhooks.events.retrieve(
            "event-123",
            webhook_id="webhook-123",
        )
        assert_matches_type(WebhookEventObject, event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.webhooks.events.with_raw_response.retrieve(
            "event-123",
            webhook_id="webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(WebhookEventObject, event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.webhooks.events.with_streaming_response.retrieve(
            "event-123",
            webhook_id="webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(WebhookEventObject, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.events.with_raw_response.retrieve(
                "event-123",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.webhooks.events.with_raw_response.retrieve(
                "",
                webhook_id="webhook-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        event = client.webhooks.events.list(
            "webhook-123",
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.webhooks.events.with_raw_response.list(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.webhooks.events.with_streaming_response.list(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.events.with_raw_response.list(
                "",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        event = await async_client.webhooks.events.retrieve(
            "event-123",
            webhook_id="webhook-123",
        )
        assert_matches_type(WebhookEventObject, event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.events.with_raw_response.retrieve(
            "event-123",
            webhook_id="webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(WebhookEventObject, event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.events.with_streaming_response.retrieve(
            "event-123",
            webhook_id="webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(WebhookEventObject, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.events.with_raw_response.retrieve(
                "event-123",
                webhook_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.webhooks.events.with_raw_response.retrieve(
                "",
                webhook_id="webhook-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        event = await async_client.webhooks.events.list(
            "webhook-123",
        )
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.events.with_raw_response.list(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventListResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.events.with_streaming_response.list(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventListResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.events.with_raw_response.list(
                "",
            )
