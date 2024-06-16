# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embed import Embed, AsyncEmbed
from embed.types import (
    Connection,
    ConnectionListResponse,
    ConnectionDeleteResponse,
    ConnectionUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Embed) -> None:
        connection = client.connections.retrieve(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Embed) -> None:
        response = client.connections.with_raw_response.retrieve(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Embed) -> None:
        with client.connections.with_streaming_response.retrieve(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.retrieve(
                "",
                integration_id="string",
            )

    @parametrize
    def test_method_update(self, client: Embed) -> None:
        connection = client.connections.update(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Embed) -> None:
        connection = client.connections.update(
            "user-123",
            integration_id="string",
            exclusions={"foo": "bar"},
            inclusions={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Embed) -> None:
        response = client.connections.with_raw_response.update(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Embed) -> None:
        with client.connections.with_streaming_response.update(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.update(
                "",
                integration_id="string",
            )

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        connection = client.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Embed) -> None:
        connection = client.connections.list(
            after="string",
            before="string",
            integration_id="string",
            limit=20,
            order="desc",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        connection = client.connections.delete(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.connections.with_raw_response.delete(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.connections.with_streaming_response.delete(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.connections.with_raw_response.delete(
                "",
                integration_id="string",
            )

    @parametrize
    def test_method_upsert(self, client: Embed) -> None:
        connection = client.connections.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Embed) -> None:
        connection = client.connections.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
            configuration={"foo": "bar"},
            exclusions={"foo": "bar"},
            inclusions={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Embed) -> None:
        response = client.connections.with_raw_response.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Embed) -> None:
        with client.connections.with_streaming_response.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.retrieve(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connections.with_raw_response.retrieve(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncEmbed) -> None:
        async with async_client.connections.with_streaming_response.retrieve(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.retrieve(
                "",
                integration_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.update(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.update(
            "user-123",
            integration_id="string",
            exclusions={"foo": "bar"},
            inclusions={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connections.with_raw_response.update(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncEmbed) -> None:
        async with async_client.connections.with_streaming_response.update(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionUpdateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.update(
                "",
                integration_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.list()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.list(
            after="string",
            before="string",
            integration_id="string",
            limit=20,
            order="desc",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.delete(
            "user-123",
            integration_id="string",
        )
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connections.with_raw_response.delete(
            "user-123",
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.connections.with_streaming_response.delete(
            "user-123",
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionDeleteResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.connections.with_raw_response.delete(
                "",
                integration_id="string",
            )

    @parametrize
    async def test_method_upsert(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncEmbed) -> None:
        connection = await async_client.connections.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
            configuration={"foo": "bar"},
            exclusions={"foo": "bar"},
            inclusions={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncEmbed) -> None:
        response = await async_client.connections.with_raw_response.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(Connection, connection, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncEmbed) -> None:
        async with async_client.connections.with_streaming_response.upsert(
            id="string",
            auth_scheme="oauth2",
            credentials={
                "access_token": "string",
                "refresh_token": "string",
                "expires_at": 0,
            },
            integration_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(Connection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True
