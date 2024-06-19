# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    connection_list_params,
    connection_delete_params,
    connection_update_params,
    connection_upsert_params,
    connection_retrieve_params,
)
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
from .._base_client import (
    make_request_options,
)
from ..types.connection import Connection
from ..types.connection_list_response import ConnectionListResponse
from ..types.connection_delete_response import ConnectionDeleteResponse

__all__ = ["ConnectionsResource", "AsyncConnectionsResource"]


class ConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionsResourceWithRawResponse:
        return ConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionsResourceWithStreamingResponse:
        return ConnectionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        connection_id: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """
        Returns a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, connection_retrieve_params.ConnectionRetrieveParams
                ),
            ),
            cast_to=Connection,
        )

    def update(
        self,
        connection_id: str,
        *,
        integration_id: str,
        exclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        inclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """
        Updates a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          exclusions: Exclusion rules for the connection. Only applicable for integrations that
              support exclusions.

          inclusions: Inclusion rules for the connection. Only applicable for integrations that
              support inclusions.

          metadata: Additional metadata for the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._put(
            f"/connections/{connection_id}",
            body=maybe_transform(
                {
                    "exclusions": exclusions,
                    "inclusions": inclusions,
                    "metadata": metadata,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, connection_update_params.ConnectionUpdateParams
                ),
            ),
            cast_to=Connection,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListResponse:
        """Returns a list of connections.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list.

          integration_id: Filter for connections belonging to a specific integration.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "integration_id": integration_id,
                        "limit": limit,
                        "order": order,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """
        Deletes a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._delete(
            f"/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration_id": integration_id}, connection_delete_params.ConnectionDeleteParams
                ),
            ),
            cast_to=ConnectionDeleteResponse,
        )

    def upsert(
        self,
        *,
        auth_scheme: Literal["oauth2", "oauth1", "basic", "api_key"],
        credentials: connection_upsert_params.Credentials,
        integration_id: str,
        id: str | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        exclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        inclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """Manually add a connection.

        We recommend using the authentication flow provided
        by Embed. However, if you've already obtained account credentials, you can use
        them to create a connection with this endpoint.

        Args:
          auth_scheme: The authentication scheme the connection should use.

          credentials: The connection's account credentials.

          integration_id: The unique identifier of the integration used by the connection.

          id: The unique identifier for the connection.

          configuration: Configuration options for the connection.

          exclusions: Exclusion rules for the connection. Only applicable for integrations that
              support exclusions.

          inclusions: Inclusion rules for the connection. Only applicable for integrations that
              support inclusions.

          metadata: Additional metadata for the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connections",
            body=maybe_transform(
                {
                    "auth_scheme": auth_scheme,
                    "credentials": credentials,
                    "integration_id": integration_id,
                    "id": id,
                    "configuration": configuration,
                    "exclusions": exclusions,
                    "inclusions": inclusions,
                    "metadata": metadata,
                },
                connection_upsert_params.ConnectionUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )


class AsyncConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionsResourceWithRawResponse:
        return AsyncConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionsResourceWithStreamingResponse:
        return AsyncConnectionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        connection_id: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """
        Returns a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, connection_retrieve_params.ConnectionRetrieveParams
                ),
            ),
            cast_to=Connection,
        )

    async def update(
        self,
        connection_id: str,
        *,
        integration_id: str,
        exclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        inclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """
        Updates a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          exclusions: Exclusion rules for the connection. Only applicable for integrations that
              support exclusions.

          inclusions: Inclusion rules for the connection. Only applicable for integrations that
              support inclusions.

          metadata: Additional metadata for the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._put(
            f"/connections/{connection_id}",
            body=await async_maybe_transform(
                {
                    "exclusions": exclusions,
                    "inclusions": inclusions,
                    "metadata": metadata,
                },
                connection_update_params.ConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, connection_update_params.ConnectionUpdateParams
                ),
            ),
            cast_to=Connection,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        integration_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionListResponse:
        """Returns a list of connections.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list.

          integration_id: Filter for connections belonging to a specific integration.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "integration_id": integration_id,
                        "limit": limit,
                        "order": order,
                    },
                    connection_list_params.ConnectionListParams,
                ),
            ),
            cast_to=ConnectionListResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectionDeleteResponse:
        """
        Deletes a connection.

        Args:
          integration_id: The integration to which the connection belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._delete(
            f"/connections/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, connection_delete_params.ConnectionDeleteParams
                ),
            ),
            cast_to=ConnectionDeleteResponse,
        )

    async def upsert(
        self,
        *,
        auth_scheme: Literal["oauth2", "oauth1", "basic", "api_key"],
        credentials: connection_upsert_params.Credentials,
        integration_id: str,
        id: str | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        exclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        inclusions: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Connection:
        """Manually add a connection.

        We recommend using the authentication flow provided
        by Embed. However, if you've already obtained account credentials, you can use
        them to create a connection with this endpoint.

        Args:
          auth_scheme: The authentication scheme the connection should use.

          credentials: The connection's account credentials.

          integration_id: The unique identifier of the integration used by the connection.

          id: The unique identifier for the connection.

          configuration: Configuration options for the connection.

          exclusions: Exclusion rules for the connection. Only applicable for integrations that
              support exclusions.

          inclusions: Inclusion rules for the connection. Only applicable for integrations that
              support inclusions.

          metadata: Additional metadata for the connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connections",
            body=await async_maybe_transform(
                {
                    "auth_scheme": auth_scheme,
                    "credentials": credentials,
                    "integration_id": integration_id,
                    "id": id,
                    "configuration": configuration,
                    "exclusions": exclusions,
                    "inclusions": inclusions,
                    "metadata": metadata,
                },
                connection_upsert_params.ConnectionUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Connection,
        )


class ConnectionsResourceWithRawResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connections.update,
        )
        self.list = to_raw_response_wrapper(
            connections.list,
        )
        self.delete = to_raw_response_wrapper(
            connections.delete,
        )
        self.upsert = to_raw_response_wrapper(
            connections.upsert,
        )


class AsyncConnectionsResourceWithRawResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = async_to_raw_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connections.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            connections.upsert,
        )


class ConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: ConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connections.update,
        )
        self.list = to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            connections.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            connections.upsert,
        )


class AsyncConnectionsResourceWithStreamingResponse:
    def __init__(self, connections: AsyncConnectionsResource) -> None:
        self._connections = connections

        self.retrieve = async_to_streamed_response_wrapper(
            connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connections.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            connections.upsert,
        )
