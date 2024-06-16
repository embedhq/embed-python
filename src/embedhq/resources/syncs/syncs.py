# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import (
    sync_list_params,
    sync_stop_params,
    sync_start_params,
    sync_update_params,
    sync_trigger_params,
    sync_retrieve_params,
)
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
from ...types.sync import Sync
from ..._base_client import (
    make_request_options,
)
from ...types.sync_list_response import SyncListResponse

__all__ = ["SyncsResource", "AsyncSyncsResource"]


class SyncsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SyncsResourceWithRawResponse:
        return SyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncsResourceWithStreamingResponse:
        return SyncsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Returns a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._get(
            f"/syncs/{collection_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_retrieve_params.SyncRetrieveParams,
                ),
            ),
            cast_to=Sync,
        )

    def update(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Updates a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          frequency: The frequency of the sync.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._put(
            f"/syncs/{collection_key}",
            body=maybe_transform({"frequency": frequency}, sync_update_params.SyncUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_update_params.SyncUpdateParams,
                ),
            ),
            cast_to=Sync,
        )

    def list(
        self,
        *,
        connection_id: str,
        integration_id: str,
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
          connection_id: The ID of the connection to which the syncs belong.

          integration_id: The ID of the integration to which the syncs belong.

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
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_list_params.SyncListParams,
                ),
            ),
            cast_to=SyncListResponse,
        )

    def start(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Starts a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/syncs/{collection_key}/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=Sync,
        )

    def stop(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Stops a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/syncs/{collection_key}/stop",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_stop_params.SyncStopParams,
                ),
            ),
            cast_to=Sync,
        )

    def trigger(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Triggers a one-time sync run.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/syncs/{collection_key}/trigger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_trigger_params.SyncTriggerParams,
                ),
            ),
            cast_to=Sync,
        )


class AsyncSyncsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSyncsResourceWithRawResponse:
        return AsyncSyncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncsResourceWithStreamingResponse:
        return AsyncSyncsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Returns a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._get(
            f"/syncs/{collection_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_retrieve_params.SyncRetrieveParams,
                ),
            ),
            cast_to=Sync,
        )

    async def update(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Updates a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          frequency: The frequency of the sync.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._put(
            f"/syncs/{collection_key}",
            body=await async_maybe_transform({"frequency": frequency}, sync_update_params.SyncUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_update_params.SyncUpdateParams,
                ),
            ),
            cast_to=Sync,
        )

    async def list(
        self,
        *,
        connection_id: str,
        integration_id: str,
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
          connection_id: The ID of the connection to which the syncs belong.

          integration_id: The ID of the integration to which the syncs belong.

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
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_list_params.SyncListParams,
                ),
            ),
            cast_to=SyncListResponse,
        )

    async def start(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Starts a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/syncs/{collection_key}/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=Sync,
        )

    async def stop(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Stops a sync.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/syncs/{collection_key}/stop",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_stop_params.SyncStopParams,
                ),
            ),
            cast_to=Sync,
        )

    async def trigger(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Triggers a one-time sync run.

        Args:
          connection_id: The ID of the connection to which the sync belongs.

          integration_id: The ID of the integration to which the sync belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/syncs/{collection_key}/trigger",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    sync_trigger_params.SyncTriggerParams,
                ),
            ),
            cast_to=Sync,
        )


class SyncsResourceWithRawResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.retrieve = to_raw_response_wrapper(
            syncs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            syncs.update,
        )
        self.list = to_raw_response_wrapper(
            syncs.list,
        )
        self.start = to_raw_response_wrapper(
            syncs.start,
        )
        self.stop = to_raw_response_wrapper(
            syncs.stop,
        )
        self.trigger = to_raw_response_wrapper(
            syncs.trigger,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._syncs.runs)


class AsyncSyncsResourceWithRawResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.retrieve = async_to_raw_response_wrapper(
            syncs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            syncs.update,
        )
        self.list = async_to_raw_response_wrapper(
            syncs.list,
        )
        self.start = async_to_raw_response_wrapper(
            syncs.start,
        )
        self.stop = async_to_raw_response_wrapper(
            syncs.stop,
        )
        self.trigger = async_to_raw_response_wrapper(
            syncs.trigger,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._syncs.runs)


class SyncsResourceWithStreamingResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.retrieve = to_streamed_response_wrapper(
            syncs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            syncs.update,
        )
        self.list = to_streamed_response_wrapper(
            syncs.list,
        )
        self.start = to_streamed_response_wrapper(
            syncs.start,
        )
        self.stop = to_streamed_response_wrapper(
            syncs.stop,
        )
        self.trigger = to_streamed_response_wrapper(
            syncs.trigger,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._syncs.runs)


class AsyncSyncsResourceWithStreamingResponse:
    def __init__(self, syncs: AsyncSyncsResource) -> None:
        self._syncs = syncs

        self.retrieve = async_to_streamed_response_wrapper(
            syncs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            syncs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            syncs.list,
        )
        self.start = async_to_streamed_response_wrapper(
            syncs.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            syncs.stop,
        )
        self.trigger = async_to_streamed_response_wrapper(
            syncs.trigger,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._syncs.runs)
