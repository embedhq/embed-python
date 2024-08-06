# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types import (
    ProxyGetResponse,
    ProxyPutResponse,
    ProxyPostResponse,
    ProxyDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Embed) -> None:
        proxy = client.proxy.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Embed) -> None:
        proxy = client.proxy.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Embed) -> None:
        response = client.proxy.with_raw_response.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Embed) -> None:
        with client.proxy.with_streaming_response.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            client.proxy.with_raw_response.delete(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    def test_method_get(self, client: Embed) -> None:
        proxy = client.proxy.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Embed) -> None:
        proxy = client.proxy.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Embed) -> None:
        response = client.proxy.with_raw_response.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Embed) -> None:
        with client.proxy.with_streaming_response.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyGetResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            client.proxy.with_raw_response.get(
                endpoint="",
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    def test_method_post(self, client: Embed) -> None:
        proxy = client.proxy.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    def test_method_post_with_all_params(self, client: Embed) -> None:
        proxy = client.proxy.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    def test_raw_response_post(self, client: Embed) -> None:
        response = client.proxy.with_raw_response.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    def test_streaming_response_post(self, client: Embed) -> None:
        with client.proxy.with_streaming_response.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyPostResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_post(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            client.proxy.with_raw_response.post(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    def test_method_put(self, client: Embed) -> None:
        proxy = client.proxy.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    def test_method_put_with_all_params(self, client: Embed) -> None:
        proxy = client.proxy.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    def test_raw_response_put(self, client: Embed) -> None:
        response = client.proxy.with_raw_response.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = response.parse()
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    def test_streaming_response_put(self, client: Embed) -> None:
        with client.proxy.with_streaming_response.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = response.parse()
            assert_matches_type(ProxyPutResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_put(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            client.proxy.with_raw_response.put(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )


class TestAsyncProxy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncEmbed) -> None:
        response = await async_client.proxy.with_raw_response.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncEmbed) -> None:
        async with async_client.proxy.with_streaming_response.delete(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyDeleteResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            await async_client.proxy.with_raw_response.delete(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncEmbed) -> None:
        response = await async_client.proxy.with_raw_response.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyGetResponse, proxy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncEmbed) -> None:
        async with async_client.proxy.with_streaming_response.get(
            endpoint="endpoint",
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyGetResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            await async_client.proxy.with_raw_response.get(
                endpoint="",
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    async def test_method_post(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    async def test_method_post_with_all_params(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    async def test_raw_response_post(self, async_client: AsyncEmbed) -> None:
        response = await async_client.proxy.with_raw_response.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyPostResponse, proxy, path=["response"])

    @parametrize
    async def test_streaming_response_post(self, async_client: AsyncEmbed) -> None:
        async with async_client.proxy.with_streaming_response.post(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyPostResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_post(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            await async_client.proxy.with_raw_response.post(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )

    @parametrize
    async def test_method_put(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    async def test_method_put_with_all_params(self, async_client: AsyncEmbed) -> None:
        proxy = await async_client.proxy.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
            base_url_override="base_url_override",
            retries=0,
        )
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    async def test_raw_response_put(self, async_client: AsyncEmbed) -> None:
        response = await async_client.proxy.with_raw_response.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy = await response.parse()
        assert_matches_type(ProxyPutResponse, proxy, path=["response"])

    @parametrize
    async def test_streaming_response_put(self, async_client: AsyncEmbed) -> None:
        async with async_client.proxy.with_streaming_response.put(
            endpoint="endpoint",
            body={"foo": "bar"},
            connected_account_id="connected_account_id",
            integration="integration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy = await response.parse()
            assert_matches_type(ProxyPutResponse, proxy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_put(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint` but received ''"):
            await async_client.proxy.with_raw_response.put(
                endpoint="",
                body={"foo": "bar"},
                connected_account_id="connected_account_id",
                integration="integration",
            )
