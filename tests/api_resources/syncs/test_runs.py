# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from embedhq import Embed, AsyncEmbed
from tests.utils import assert_matches_type
from embedhq.types.syncs import RunListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Embed) -> None:
        run = client.syncs.runs.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Embed) -> None:
        response = client.syncs.runs.with_raw_response.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Embed) -> None:
        with client.syncs.runs.with_streaming_response.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Embed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            client.syncs.runs.with_raw_response.list(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncEmbed) -> None:
        run = await async_client.syncs.runs.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncEmbed) -> None:
        response = await async_client.syncs.runs.with_raw_response.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunListResponse, run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncEmbed) -> None:
        async with async_client.syncs.runs.with_streaming_response.list(
            "issues",
            connection_id="user-123",
            integration_id="github-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunListResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncEmbed) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection_key` but received ''"):
            await async_client.syncs.runs.with_raw_response.list(
                "",
                connection_id="user-123",
                integration_id="github-123",
            )
