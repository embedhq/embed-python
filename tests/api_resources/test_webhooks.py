# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    Webhook,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookDisableResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        webhook = client.webhooks.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        webhook = client.webhooks.retrieve(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        webhook = client.webhooks.update(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        webhook = client.webhooks.update(
            "webhook-123",
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.update(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.update(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        webhook = client.webhooks.delete(
            "webhook-123",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.delete(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.delete(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_disable(self, client: Embed) -> None:
        webhook = client.webhooks.disable(
            "webhook-123",
        )
        assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_disable(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.disable(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_disable(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.disable(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_disable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.disable(
                "",
            )

    @parametrize
    def test_method_enable(self, client: Embed) -> None:
        webhook = client.webhooks.enable(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: Embed) -> None:
        response = client.webhooks.with_raw_response.enable(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: Embed) -> None:
        with client.webhooks.with_streaming_response.enable(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.enable(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.retrieve(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.update(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.update(
            "webhook-123",
            events=["sync.succeeded", "sync.failed"],
            url="https://my-app.com/webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.delete(
            "webhook-123",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_disable(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.disable(
            "webhook-123",
        )
        assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.disable(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.disable(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDisableResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_disable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.disable(
                "",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncEmbed) -> None:
        webhook = await async_client.webhooks.enable(
            "webhook-123",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncEmbed) -> None:
        response = await async_client.webhooks.with_raw_response.enable(
            "webhook-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncEmbed) -> None:
        async with async_client.webhooks.with_streaming_response.enable(
            "webhook-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.enable(
                "",
            )
