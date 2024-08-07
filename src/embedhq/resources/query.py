# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..types import query_exec_params, query_multi_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.query_exec_response import QueryExecResponse
from ..types.query_multi_response import QueryMultiResponse

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        return QueryResourceWithStreamingResponse(self)

    def exec(
        self,
        *,
        connected_account_id: str,
        integration: str,
        alpha: float | NotGiven = NOT_GIVEN,
        collection: str | NotGiven = NOT_GIVEN,
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
    ) -> QueryExecResponse:
        """
        Executes a single query.

        Args:
          connected_account_id: The unique identifier of the connected account to query.

          integration: The unique slug of the integration to query.

          alpha: The relative weight used to merge vector and hybrid result sets. Only applicable
              for `hybrid` queries.

          collection: The unique slug of the collection to query. If empty, all collections associated
              with the integration/connected account will be queried.

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
        return self._post(
            "/query",
            body=maybe_transform(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "alpha": alpha,
                    "collection": collection,
                    "filter": filter,
                    "image": image,
                    "limit": limit,
                    "query": query,
                    "return_properties": return_properties,
                    "type": type,
                },
                query_exec_params.QueryExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryExecResponse,
        )

    def multi(
        self,
        *,
        queries: Iterable[query_multi_params.Query] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryMultiResponse:
        """
        Executes multiple queries in a single request.

        Args:
          queries: An array of query objects to execute in parallel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/multi-query",
            body=maybe_transform({"queries": queries}, query_multi_params.QueryMultiParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryMultiResponse,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        return AsyncQueryResourceWithStreamingResponse(self)

    async def exec(
        self,
        *,
        connected_account_id: str,
        integration: str,
        alpha: float | NotGiven = NOT_GIVEN,
        collection: str | NotGiven = NOT_GIVEN,
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
    ) -> QueryExecResponse:
        """
        Executes a single query.

        Args:
          connected_account_id: The unique identifier of the connected account to query.

          integration: The unique slug of the integration to query.

          alpha: The relative weight used to merge vector and hybrid result sets. Only applicable
              for `hybrid` queries.

          collection: The unique slug of the collection to query. If empty, all collections associated
              with the integration/connected account will be queried.

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
        return await self._post(
            "/query",
            body=await async_maybe_transform(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "alpha": alpha,
                    "collection": collection,
                    "filter": filter,
                    "image": image,
                    "limit": limit,
                    "query": query,
                    "return_properties": return_properties,
                    "type": type,
                },
                query_exec_params.QueryExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryExecResponse,
        )

    async def multi(
        self,
        *,
        queries: Iterable[query_multi_params.Query] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryMultiResponse:
        """
        Executes multiple queries in a single request.

        Args:
          queries: An array of query objects to execute in parallel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/multi-query",
            body=await async_maybe_transform({"queries": queries}, query_multi_params.QueryMultiParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryMultiResponse,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.exec = to_raw_response_wrapper(
            query.exec,
        )
        self.multi = to_raw_response_wrapper(
            query.multi,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.exec = async_to_raw_response_wrapper(
            query.exec,
        )
        self.multi = async_to_raw_response_wrapper(
            query.multi,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.exec = to_streamed_response_wrapper(
            query.exec,
        )
        self.multi = to_streamed_response_wrapper(
            query.multi,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.exec = async_to_streamed_response_wrapper(
            query.exec,
        )
        self.multi = async_to_streamed_response_wrapper(
            query.multi,
        )
