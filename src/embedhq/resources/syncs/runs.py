# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.syncs import run_list_params, run_retrieve_params
from ..._base_client import make_request_options
from ...types.syncs.sync_run import SyncRun
from ...types.syncs.run_list_response import RunListResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        collection: str,
        sync_run_id: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncRun:
        """
        Returns a sync run.

        Args:
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not sync_run_id:
            raise ValueError(f"Expected a non-empty value for `sync_run_id` but received {sync_run_id!r}")
        return self._get(
            f"/syncs/{collection}/runs/{sync_run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=SyncRun,
        )

    def list(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """
        Returns a list of recent sync runs.

        Args:
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._get(
            f"/syncs/{collection}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        collection: str,
        sync_run_id: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncRun:
        """
        Returns a sync run.

        Args:
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not sync_run_id:
            raise ValueError(f"Expected a non-empty value for `sync_run_id` but received {sync_run_id!r}")
        return await self._get(
            f"/syncs/{collection}/runs/{sync_run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=SyncRun,
        )

    async def list(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """
        Returns a list of recent sync runs.

        Args:
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._get(
            f"/syncs/{collection}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
