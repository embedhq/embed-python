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
    SyncDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSyncs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        sync = client.syncs.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
            exclusions=["string", "string", "string"],
            frequency="Every 6 hours",
            inclusions=["string", "string", "string"],
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        sync = client.syncs.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.retrieve(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        sync = client.syncs.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
            exclusions=["string", "string", "string"],
            frequency="Every 6 hours",
            inclusions=["string", "string", "string"],
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.update(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        sync = client.syncs.list()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.list(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        sync = client.syncs.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncDeleteResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.delete(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    def test_method_start(self, client: Embed) -> None:
        sync = client.syncs.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.start(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    def test_method_stop(self, client: Embed) -> None:
        sync = client.syncs.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stop(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.stop(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    def test_method_trigger(self, client: Embed) -> None:
        sync = client.syncs.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_method_trigger_with_all_params(self, client: Embed) -> None:
        sync = client.syncs.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_raw_response_trigger(self, client: Embed) -> None:
        response = client.syncs.with_raw_response.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    def test_streaming_response_trigger(self, client: Embed) -> None:
        with client.syncs.with_streaming_response.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.syncs.with_raw_response.trigger(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )


class TestAsyncSyncs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
            exclusions=["string", "string", "string"],
            frequency="Every 6 hours",
            inclusions=["string", "string", "string"],
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.create(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.retrieve(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.retrieve(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
            exclusions=["string", "string", "string"],
            frequency="Every 6 hours",
            inclusions=["string", "string", "string"],
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.update(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.update(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.list()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.list(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncListResponse, sync, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncListResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncDeleteResponse, sync, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.delete(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncDeleteResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.delete(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    async def test_method_start(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.start(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.start(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    async def test_method_stop(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.stop(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stop(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.stop(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncEmbed) -> None:
        sync = await async_client.syncs.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
            collection_version="1.2",
        )
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.with_raw_response.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Sync, sync, path=["response"])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.with_streaming_response.trigger(
            collection="issues",
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(Sync, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.syncs.with_raw_response.trigger(
                collection="",
                connected_account_id="user-123",
                integration="github-123",
            )
