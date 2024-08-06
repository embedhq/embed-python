# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import sync_list_params
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
from ..._base_client import (
    make_request_options,
)
from ...types.sync_list_response import SyncListResponse

__all__ = ["SyncsResource", "AsyncSyncsResource"]


class SyncsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncsResourceWithRawResponse:
        return SyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncsResourceWithStreamingResponse:
        return SyncsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        integration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListResponse:
        """
        Returns a list of syncs.

        Args:
          connected_account_id: Filter syncs by connected account.

          integration: Filter syncs by integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/syncs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                    },
                    sync_list_params.SyncListParams,
                ),
            ),
            cast_to=SyncListResponse,
        )


class AsyncSyncsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncsResourceWithRawResponse:
        return AsyncSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncsResourceWithStreamingResponse:
        return AsyncSyncsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        connected_account_id: str | NotGiven = NOT_GIVEN,
        integration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncListResponse:
        """
        Returns a list of syncs.

        Args:
          connected_account_id: Filter syncs by connected account.

          integration: Filter syncs by integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/syncs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                    },
                    sync_list_params.SyncListParams,
                ),
            ),
            cast_to=SyncListResponse,
        )


class SyncsResourceWithRawResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.list = to_raw_response_wrapper(
            syncs.list,
        )


class AsyncSyncsResourceWithRawResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.list = async_to_raw_response_wrapper(
            syncs.list,
        )


class SyncsResourceWithStreamingResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.list = to_streamed_response_wrapper(
            syncs.list,
        )


class AsyncSyncsResourceWithStreamingResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.list = async_to_streamed_response_wrapper(
            syncs.list,
        )
