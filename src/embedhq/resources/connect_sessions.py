# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import connect_session_create_params
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
from ..types.connect_session import ConnectSession
from ..types.connect_session_list_response import ConnectSessionListResponse
from ..types.connect_session_delete_response import ConnectSessionDeleteResponse

__all__ = ["ConnectSessionsResource", "AsyncConnectSessionsResource"]


class ConnectSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectSessionsResourceWithRawResponse:
        return ConnectSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectSessionsResourceWithStreamingResponse:
        return ConnectSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connected_account_id: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        expires_in_mins: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSession:
        """
        Creates a connect session.

        Args:
          connected_account_id: The unique identifier for the connected account.

          integration: The unique slug of the integration to connect the account to.

          configuration: Configuration options to assign to the connected account.

          expires_in_mins: The number of minutes until the connect session expires.

          metadata: Additional metadata to assign to the connected account.

          name: The display name of the connected account.

          redirect_url: The URL to redirect to after the authorization flow is complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connect-sessions",
            body=maybe_transform(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "configuration": configuration,
                    "expires_in_mins": expires_in_mins,
                    "metadata": metadata,
                    "name": name,
                    "redirect_url": redirect_url,
                },
                connect_session_create_params.ConnectSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSession,
        )

    def retrieve(
        self,
        connect_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSession:
        """
        Returns a connect session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connect_session_id:
            raise ValueError(f"Expected a non-empty value for `connect_session_id` but received {connect_session_id!r}")
        return self._get(
            f"/connect-sessions/{connect_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSession,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSessionListResponse:
        """Returns a list of connect sessions."""
        return self._get(
            "/connect-sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSessionListResponse,
        )

    def delete(
        self,
        connect_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSessionDeleteResponse:
        """
        Deletes a connect session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connect_session_id:
            raise ValueError(f"Expected a non-empty value for `connect_session_id` but received {connect_session_id!r}")
        return self._delete(
            f"/connect-sessions/{connect_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSessionDeleteResponse,
        )


class AsyncConnectSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectSessionsResourceWithRawResponse:
        return AsyncConnectSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectSessionsResourceWithStreamingResponse:
        return AsyncConnectSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connected_account_id: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        expires_in_mins: int | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        redirect_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSession:
        """
        Creates a connect session.

        Args:
          connected_account_id: The unique identifier for the connected account.

          integration: The unique slug of the integration to connect the account to.

          configuration: Configuration options to assign to the connected account.

          expires_in_mins: The number of minutes until the connect session expires.

          metadata: Additional metadata to assign to the connected account.

          name: The display name of the connected account.

          redirect_url: The URL to redirect to after the authorization flow is complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connect-sessions",
            body=await async_maybe_transform(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "configuration": configuration,
                    "expires_in_mins": expires_in_mins,
                    "metadata": metadata,
                    "name": name,
                    "redirect_url": redirect_url,
                },
                connect_session_create_params.ConnectSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSession,
        )

    async def retrieve(
        self,
        connect_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSession:
        """
        Returns a connect session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connect_session_id:
            raise ValueError(f"Expected a non-empty value for `connect_session_id` but received {connect_session_id!r}")
        return await self._get(
            f"/connect-sessions/{connect_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSession,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSessionListResponse:
        """Returns a list of connect sessions."""
        return await self._get(
            "/connect-sessions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSessionListResponse,
        )

    async def delete(
        self,
        connect_session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectSessionDeleteResponse:
        """
        Deletes a connect session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connect_session_id:
            raise ValueError(f"Expected a non-empty value for `connect_session_id` but received {connect_session_id!r}")
        return await self._delete(
            f"/connect-sessions/{connect_session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectSessionDeleteResponse,
        )


class ConnectSessionsResourceWithRawResponse:
    def __init__(self, connect_sessions: ConnectSessionsResource) -> None:
        self._connect_sessions = connect_sessions

        self.create = to_raw_response_wrapper(
            connect_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connect_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            connect_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            connect_sessions.delete,
        )


class AsyncConnectSessionsResourceWithRawResponse:
    def __init__(self, connect_sessions: AsyncConnectSessionsResource) -> None:
        self._connect_sessions = connect_sessions

        self.create = async_to_raw_response_wrapper(
            connect_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connect_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            connect_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connect_sessions.delete,
        )


class ConnectSessionsResourceWithStreamingResponse:
    def __init__(self, connect_sessions: ConnectSessionsResource) -> None:
        self._connect_sessions = connect_sessions

        self.create = to_streamed_response_wrapper(
            connect_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connect_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            connect_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            connect_sessions.delete,
        )


class AsyncConnectSessionsResourceWithStreamingResponse:
    def __init__(self, connect_sessions: AsyncConnectSessionsResource) -> None:
        self._connect_sessions = connect_sessions

        self.create = async_to_streamed_response_wrapper(
            connect_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connect_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            connect_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connect_sessions.delete,
        )
