# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    Sync,
    SyncListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        sync = client.syncs.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.with_raw_response.retrieve(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        sync = client.syncs.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
            frequency="daily",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.with_raw_response.update(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        sync = client.syncs.list(
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.list(
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.list(
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Embed) -> None:
        sync = client.syncs.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.with_raw_response.start(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    def test_method_stop(self, client: Embed) -> None:
        sync = client.syncs.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.with_raw_response.stop(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    def test_method_trigger(self, client: Embed) -> None:
        sync = client.syncs.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.with_raw_response.trigger(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )


class TestAsyncSyncs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.retrieve(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.with_raw_response.retrieve(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
            frequency="daily",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.update(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.with_raw_response.update(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.list(
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.list(
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.list(
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.start(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.with_raw_response.start(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_stop(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.stop(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.with_raw_response.stop(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.trigger(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.with_raw_response.trigger(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )
