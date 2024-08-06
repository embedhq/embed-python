# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    ConnectedAccount,
    ConnectedAccountListResponse,
    ConnectedAccountDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectedAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        connected_account = client.connected_accounts.retrieve(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.connected_accounts.with_raw_response.retrieve(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.connected_accounts.with_streaming_response.retrieve(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            client.connected_accounts.with_raw_response.retrieve(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        connected_account = client.connected_accounts.update(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        connected_account = client.connected_accounts.update(
            connected_account_id="user-123",
            integration="integration",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
            name="Octocat",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.connected_accounts.with_raw_response.update(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.connected_accounts.with_streaming_response.update(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            client.connected_accounts.with_raw_response.update(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        connected_account = client.connected_accounts.list()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        connected_account = client.connected_accounts.list(
            after="after",
            before="before",
            integration="integration",
            limit=20,
            order="desc",
        )
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.connected_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.connected_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        connected_account = client.connected_accounts.delete(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.connected_accounts.with_raw_response.delete(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.connected_accounts.with_streaming_response.delete(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            client.connected_accounts.with_raw_response.delete(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    def test_method_upsert(self, client: Embed) -> None:
        connected_account = client.connected_accounts.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Embed) -> None:
        connected_account = client.connected_accounts.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "expires_at": 0,
            },
            integration="integration",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Embed) -> None:
        response = client.connected_accounts.with_raw_response.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Embed) -> None:
        with client.connected_accounts.with_streaming_response.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnectedAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.retrieve(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connected_accounts.with_raw_response.retrieve(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.connected_accounts.with_streaming_response.retrieve(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            await async_client.connected_accounts.with_raw_response.retrieve(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.update(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.update(
            connected_account_id="user-123",
            integration="integration",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
            name="Octocat",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connected_accounts.with_raw_response.update(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.connected_accounts.with_streaming_response.update(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            await async_client.connected_accounts.with_raw_response.update(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.list()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.list(
            after="after",
            before="before",
            integration="integration",
            limit=20,
            order="desc",
        )
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connected_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.connected_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.delete(
            connected_account_id="user-123",
            integration="integration",
        )
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connected_accounts.with_raw_response.delete(
            connected_account_id="user-123",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.connected_accounts.with_streaming_response.delete(
            connected_account_id="user-123",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connected_account_id` but received ''"):
            await async_client.connected_accounts.with_raw_response.delete(
                connected_account_id="",
                integration="integration",
            )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncEmbed) -> None:
        connected_account = await async_client.connected_accounts.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "expires_at": 0,
            },
            integration="integration",
            configuration={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connected_accounts.with_raw_response.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccount, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncEmbed) -> None:
        async with async_client.connected_accounts.with_streaming_response.upsert(
            id="id",
            auth_method="oauth2",
            credentials={
                "access_token": "access_token",
                "refresh_token": "refresh_token",
            },
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccount, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True
