# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    ConnectSession,
    ConnectSessionListResponse,
    ConnectSessionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Embed) -> None:
        connect_session = client.connect_sessions.create(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Embed) -> None:
        connect_session = client.connect_sessions.create(
            connected_account_id="user-123",
            integration="github-123",
            configuration={"foo": "bar"},
            expires_in_mins=60,
            metadata={"foo": "bar"},
            name="Octocat",
            redirect_url="https://my-app.com/callback",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Embed) -> None:
        response = client.connect_sessions.with_raw_response.create(
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = response.parse()
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Embed) -> None:
        with client.connect_sessions.with_streaming_response.create(
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = response.parse()
            assert_matches_type(ConnectSession, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        connect_session = client.connect_sessions.retrieve(
            "cs_1a2b3c",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.connect_sessions.with_raw_response.retrieve(
            "cs_1a2b3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = response.parse()
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.connect_sessions.with_streaming_response.retrieve(
            "cs_1a2b3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = response.parse()
            assert_matches_type(ConnectSession, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connect_session_id` but received ''"):
            client.connect_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        connect_session = client.connect_sessions.list()
        assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.connect_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = response.parse()
        assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.connect_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = response.parse()
            assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        connect_session = client.connect_sessions.delete(
            "cs_1a2b3c",
        )
        assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.connect_sessions.with_raw_response.delete(
            "cs_1a2b3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = response.parse()
        assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.connect_sessions.with_streaming_response.delete(
            "cs_1a2b3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = response.parse()
            assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connect_session_id` but received ''"):
            client.connect_sessions.with_raw_response.delete(
                "",
            )


class TestAsyncConnectSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncEmbed) -> None:
        connect_session = await async_client.connect_sessions.create(
            connected_account_id="user-123",
            integration="github-123",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncEmbed) -> None:
        connect_session = await async_client.connect_sessions.create(
            connected_account_id="user-123",
            integration="github-123",
            configuration={"foo": "bar"},
            expires_in_mins=60,
            metadata={"foo": "bar"},
            name="Octocat",
            redirect_url="https://my-app.com/callback",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connect_sessions.with_raw_response.create(
            connected_account_id="user-123",
            integration="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = await response.parse()
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncEmbed) -> None:
        async with async_client.connect_sessions.with_streaming_response.create(
            connected_account_id="user-123",
            integration="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = await response.parse()
            assert_matches_type(ConnectSession, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        connect_session = await async_client.connect_sessions.retrieve(
            "cs_1a2b3c",
        )
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connect_sessions.with_raw_response.retrieve(
            "cs_1a2b3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = await response.parse()
        assert_matches_type(ConnectSession, connect_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.connect_sessions.with_streaming_response.retrieve(
            "cs_1a2b3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = await response.parse()
            assert_matches_type(ConnectSession, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connect_session_id` but received ''"):
            await async_client.connect_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        connect_session = await async_client.connect_sessions.list()
        assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connect_sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = await response.parse()
        assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.connect_sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = await response.parse()
            assert_matches_type(ConnectSessionListResponse, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        connect_session = await async_client.connect_sessions.delete(
            "cs_1a2b3c",
        )
        assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connect_sessions.with_raw_response.delete(
            "cs_1a2b3c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect_session = await response.parse()
        assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.connect_sessions.with_streaming_response.delete(
            "cs_1a2b3c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect_session = await response.parse()
            assert_matches_type(ConnectSessionDeleteResponse, connect_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connect_session_id` but received ''"):
            await async_client.connect_sessions.with_raw_response.delete(
                "",
            )
