# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
    sync_create_params,
    sync_delete_params,
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
from ..._base_client import make_request_options
from ...types.sync_list_response import SyncListResponse
from ...types.sync_delete_response import SyncDeleteResponse

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

    def create(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        exclusions: List[str] | NotGiven = NOT_GIVEN,
        frequency: str | NotGiven = NOT_GIVEN,
        inclusions: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Creates a sync.

        Args:
          collection: The unique slug of the collection.

          connected_account_id: The unique identifier of the connected account.

          integration: The unique slug of the integration.

          collection_version: The collection version used for the sync (defaults to latest).

          exclusions: Array of IDs to exclude from the sync. If present, objects with matching IDs
              will not be synced.

          frequency: The frequency of the sync.

          inclusions: Array of IDs to include in the sync. If present, only objects with matching IDs
              will be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/syncs",
            body=maybe_transform(
                {
                    "collection": collection,
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "collection_version": collection_version,
                    "exclusions": exclusions,
                    "frequency": frequency,
                    "inclusions": inclusions,
                },
                sync_create_params.SyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sync,
        )

    def retrieve(
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
    ) -> Sync:
        """
        Returns a sync.

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
            f"/syncs/{collection}",
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
                    sync_retrieve_params.SyncRetrieveParams,
                ),
            ),
            cast_to=Sync,
        )

    def update(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        exclusions: List[str] | NotGiven = NOT_GIVEN,
        frequency: str | NotGiven = NOT_GIVEN,
        inclusions: List[str] | NotGiven = NOT_GIVEN,
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
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          exclusions: Array of IDs to exclude from the sync. If present, objects with matching IDs
              will not be synced.

          frequency: The frequency of the sync.

          inclusions: Array of IDs to include in the sync. If present, only objects with matching IDs
              will be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._put(
            f"/syncs/{collection}",
            body=maybe_transform(
                {
                    "exclusions": exclusions,
                    "frequency": frequency,
                    "inclusions": inclusions,
                },
                sync_update_params.SyncUpdateParams,
            ),
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
                    sync_update_params.SyncUpdateParams,
                ),
            ),
            cast_to=Sync,
        )

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

    def delete(
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
    ) -> SyncDeleteResponse:
        """
        Deletes a sync.

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
        return self._delete(
            f"/syncs/{collection}",
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
                    sync_delete_params.SyncDeleteParams,
                ),
            ),
            cast_to=SyncDeleteResponse,
        )

    def start(
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
    ) -> Sync:
        """
        Starts a sync.

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
        return self._post(
            f"/syncs/{collection}/start",
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
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=Sync,
        )

    def stop(
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
    ) -> Sync:
        """
        Stops a sync.

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
        return self._post(
            f"/syncs/{collection}/stop",
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
                    sync_stop_params.SyncStopParams,
                ),
            ),
            cast_to=Sync,
        )

    def trigger(
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
    ) -> Sync:
        """
        Triggers a one-time sync run.

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
        return self._post(
            f"/syncs/{collection}/trigger",
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

    async def create(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        exclusions: List[str] | NotGiven = NOT_GIVEN,
        frequency: str | NotGiven = NOT_GIVEN,
        inclusions: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Sync:
        """
        Creates a sync.

        Args:
          collection: The unique slug of the collection.

          connected_account_id: The unique identifier of the connected account.

          integration: The unique slug of the integration.

          collection_version: The collection version used for the sync (defaults to latest).

          exclusions: Array of IDs to exclude from the sync. If present, objects with matching IDs
              will not be synced.

          frequency: The frequency of the sync.

          inclusions: Array of IDs to include in the sync. If present, only objects with matching IDs
              will be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/syncs",
            body=await async_maybe_transform(
                {
                    "collection": collection,
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "collection_version": collection_version,
                    "exclusions": exclusions,
                    "frequency": frequency,
                    "inclusions": inclusions,
                },
                sync_create_params.SyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Sync,
        )

    async def retrieve(
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
    ) -> Sync:
        """
        Returns a sync.

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
            f"/syncs/{collection}",
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
                    sync_retrieve_params.SyncRetrieveParams,
                ),
            ),
            cast_to=Sync,
        )

    async def update(
        self,
        *,
        collection: str,
        connected_account_id: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        exclusions: List[str] | NotGiven = NOT_GIVEN,
        frequency: str | NotGiven = NOT_GIVEN,
        inclusions: List[str] | NotGiven = NOT_GIVEN,
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
          connected_account_id: The ID of the connected account to which the syncs belong.

          integration: The slug of the integration to which the sync belongs.

          collection_version: The collection version (defaults to latest).

          exclusions: Array of IDs to exclude from the sync. If present, objects with matching IDs
              will not be synced.

          frequency: The frequency of the sync.

          inclusions: Array of IDs to include in the sync. If present, only objects with matching IDs
              will be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._put(
            f"/syncs/{collection}",
            body=await async_maybe_transform(
                {
                    "exclusions": exclusions,
                    "frequency": frequency,
                    "inclusions": inclusions,
                },
                sync_update_params.SyncUpdateParams,
            ),
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
                    sync_update_params.SyncUpdateParams,
                ),
            ),
            cast_to=Sync,
        )

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

    async def delete(
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
    ) -> SyncDeleteResponse:
        """
        Deletes a sync.

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
        return await self._delete(
            f"/syncs/{collection}",
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
                    sync_delete_params.SyncDeleteParams,
                ),
            ),
            cast_to=SyncDeleteResponse,
        )

    async def start(
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
    ) -> Sync:
        """
        Starts a sync.

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
        return await self._post(
            f"/syncs/{collection}/start",
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
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=Sync,
        )

    async def stop(
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
    ) -> Sync:
        """
        Stops a sync.

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
        return await self._post(
            f"/syncs/{collection}/stop",
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
                    sync_stop_params.SyncStopParams,
                ),
            ),
            cast_to=Sync,
        )

    async def trigger(
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
    ) -> Sync:
        """
        Triggers a one-time sync run.

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
        return await self._post(
            f"/syncs/{collection}/trigger",
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
                    sync_trigger_params.SyncTriggerParams,
                ),
            ),
            cast_to=Sync,
        )


class SyncsResourceWithRawResponse:
    def __init__(self, syncs: SyncsResource) -> None:
        self._syncs = syncs

        self.create = to_raw_response_wrapper(
            syncs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            syncs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            syncs.update,
        )
        self.list = to_raw_response_wrapper(
            syncs.list,
        )
        self.delete = to_raw_response_wrapper(
            syncs.delete,
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

        self.create = async_to_raw_response_wrapper(
            syncs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            syncs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            syncs.update,
        )
        self.list = async_to_raw_response_wrapper(
            syncs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            syncs.delete,
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

        self.create = to_streamed_response_wrapper(
            syncs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            syncs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            syncs.update,
        )
        self.list = to_streamed_response_wrapper(
            syncs.list,
        )
        self.delete = to_streamed_response_wrapper(
            syncs.delete,
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

        self.create = async_to_streamed_response_wrapper(
            syncs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            syncs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            syncs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            syncs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            syncs.delete,
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
