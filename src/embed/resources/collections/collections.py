# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    collection_list_params,
    collection_query_params,
    collection_enable_params,
    collection_update_params,
    collection_disable_params,
    collection_retrieve_params,
)
from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
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
from ..._base_client import (
    make_request_options,
)
from ...types.collection import Collection
from ...types.collection_list_response import CollectionListResponse
from ...types.collection_query_response import CollectionQueryResponse
from ...types.collection_disable_response import CollectionDisableResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def schemas(self) -> SchemasResource:
        return SchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Returns a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._get(
            f"/collections/{collection_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, collection_retrieve_params.CollectionRetrieveParams
                ),
            ),
            cast_to=Collection,
        )

    def update(
        self,
        collection_key: str,
        *,
        integration_id: str,
        auto_start_syncs: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        default_sync_frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"] | NotGiven = NOT_GIVEN,
        exclude_properties_from_syncs: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Updates a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          auto_start_syncs: Whether to automatically start syncing this collection after a connection is
              created.

          configuration: Configuration options for the collection.

          default_sync_frequency: The default sync frequency for the collection.

          exclude_properties_from_syncs: An array of properties to exclude from being synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._put(
            f"/collections/{collection_key}",
            body=maybe_transform(
                {
                    "auto_start_syncs": auto_start_syncs,
                    "configuration": configuration,
                    "default_sync_frequency": default_sync_frequency,
                    "exclude_properties_from_syncs": exclude_properties_from_syncs,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, collection_update_params.CollectionUpdateParams
                ),
            ),
            cast_to=Collection,
        )

    def list(
        self,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Returns a list of collections.

        Args:
          integration_id: The ID of the integration to which the collections belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, collection_list_params.CollectionListParams),
            ),
            cast_to=CollectionListResponse,
        )

    def disable(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDisableResponse:
        """
        Disables a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/collections/{collection_key}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, collection_disable_params.CollectionDisableParams
                ),
            ),
            cast_to=CollectionDisableResponse,
        )

    def enable(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Enables a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/collections/{collection_key}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, collection_enable_params.CollectionEnableParams
                ),
            ),
            cast_to=Collection,
        )

    def query(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        alpha: float | NotGiven = NOT_GIVEN,
        filter: Dict[str, object] | NotGiven = NOT_GIVEN,
        image: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        return_properties: List[str] | NotGiven = NOT_GIVEN,
        type: Literal["hybrid", "vector", "keyword"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionQueryResponse:
        """
        Query a collection.

        Args:
          connection_id: The ID of the connection to use for the query.

          integration_id: The ID of the integration to which the collection belongs.

          alpha: The relative weight used to merge vector and hybrid result sets. Only applicable
              for `hybrid` queries.

          filter: The filter to apply to the query.

          image: The URL or base-64 string of the image to match against. Only applicable for
              `vector` queries.

          limit: A limit on the number of objects to be returned.

          query: The query string to match against.

          return_properties: Specify properties you want to return in the results set.

          type: The type of query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._post(
            f"/collections/{collection_key}/query",
            body=maybe_transform(
                {
                    "alpha": alpha,
                    "filter": filter,
                    "image": image,
                    "limit": limit,
                    "query": query,
                    "return_properties": return_properties,
                    "type": type,
                },
                collection_query_params.CollectionQueryParams,
            ),
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
                    collection_query_params.CollectionQueryParams,
                ),
            ),
            cast_to=CollectionQueryResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        return AsyncSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Returns a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._get(
            f"/collections/{collection_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, collection_retrieve_params.CollectionRetrieveParams
                ),
            ),
            cast_to=Collection,
        )

    async def update(
        self,
        collection_key: str,
        *,
        integration_id: str,
        auto_start_syncs: bool | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        default_sync_frequency: Literal["real_time", "hourly", "daily", "weekly", "monthly"] | NotGiven = NOT_GIVEN,
        exclude_properties_from_syncs: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Updates a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          auto_start_syncs: Whether to automatically start syncing this collection after a connection is
              created.

          configuration: Configuration options for the collection.

          default_sync_frequency: The default sync frequency for the collection.

          exclude_properties_from_syncs: An array of properties to exclude from being synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._put(
            f"/collections/{collection_key}",
            body=await async_maybe_transform(
                {
                    "auto_start_syncs": auto_start_syncs,
                    "configuration": configuration,
                    "default_sync_frequency": default_sync_frequency,
                    "exclude_properties_from_syncs": exclude_properties_from_syncs,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, collection_update_params.CollectionUpdateParams
                ),
            ),
            cast_to=Collection,
        )

    async def list(
        self,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Returns a list of collections.

        Args:
          integration_id: The ID of the integration to which the collections belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, collection_list_params.CollectionListParams
                ),
            ),
            cast_to=CollectionListResponse,
        )

    async def disable(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDisableResponse:
        """
        Disables a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/collections/{collection_key}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, collection_disable_params.CollectionDisableParams
                ),
            ),
            cast_to=CollectionDisableResponse,
        )

    async def enable(
        self,
        collection_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Enables a collection.

        Args:
          integration_id: The ID of the integration to which the collection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/collections/{collection_key}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, collection_enable_params.CollectionEnableParams
                ),
            ),
            cast_to=Collection,
        )

    async def query(
        self,
        collection_key: str,
        *,
        connection_id: str,
        integration_id: str,
        alpha: float | NotGiven = NOT_GIVEN,
        filter: Dict[str, object] | NotGiven = NOT_GIVEN,
        image: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        return_properties: List[str] | NotGiven = NOT_GIVEN,
        type: Literal["hybrid", "vector", "keyword"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionQueryResponse:
        """
        Query a collection.

        Args:
          connection_id: The ID of the connection to use for the query.

          integration_id: The ID of the integration to which the collection belongs.

          alpha: The relative weight used to merge vector and hybrid result sets. Only applicable
              for `hybrid` queries.

          filter: The filter to apply to the query.

          image: The URL or base-64 string of the image to match against. Only applicable for
              `vector` queries.

          limit: A limit on the number of objects to be returned.

          query: The query string to match against.

          return_properties: Specify properties you want to return in the results set.

          type: The type of query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._post(
            f"/collections/{collection_key}/query",
            body=await async_maybe_transform(
                {
                    "alpha": alpha,
                    "filter": filter,
                    "image": image,
                    "limit": limit,
                    "query": query,
                    "return_properties": return_properties,
                    "type": type,
                },
                collection_query_params.CollectionQueryParams,
            ),
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
                    collection_query_params.CollectionQueryParams,
                ),
            ),
            cast_to=CollectionQueryResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.disable = to_raw_response_wrapper(
            collections.disable,
        )
        self.enable = to_raw_response_wrapper(
            collections.enable,
        )
        self.query = to_raw_response_wrapper(
            collections.query,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self._collections.schemas)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.disable = async_to_raw_response_wrapper(
            collections.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            collections.enable,
        )
        self.query = async_to_raw_response_wrapper(
            collections.query,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self._collections.schemas)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.disable = to_streamed_response_wrapper(
            collections.disable,
        )
        self.enable = to_streamed_response_wrapper(
            collections.enable,
        )
        self.query = to_streamed_response_wrapper(
            collections.query,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self._collections.schemas)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            collections.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            collections.enable,
        )
        self.query = async_to_streamed_response_wrapper(
            collections.query,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self._collections.schemas)
