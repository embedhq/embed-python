# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import session_token_list_params, session_token_create_params
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
from ..types.session_token import SessionToken
from ..types.session_token_list_response import SessionTokenListResponse
from ..types.session_token_delete_response import SessionTokenDeleteResponse

__all__ = ["SessionTokensResource", "AsyncSessionTokensResource"]


class SessionTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionTokensResourceWithRawResponse:
        return SessionTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionTokensResourceWithStreamingResponse:
        return SessionTokensResourceWithStreamingResponse(self)

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
    ) -> SessionToken:
        """
        Creates a session token.

        Args:
          connected_account_id: The unique identifier to assign to the connected account.

          integration: The unique slug of the integration to connect the account to.

          configuration: Configuration options to assign to the connected account.

          expires_in_mins: The number of minutes until the session token expires.

          metadata: Additional metadata to assign to the connected account.

          name: The display name to assign to the connected account.

          redirect_url: The URL to redirect to after the authorization flow is complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/session-tokens",
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
                session_token_create_params.SessionTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToken,
        )

    def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionToken:
        """
        Returns a session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            f"/session-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToken,
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
    ) -> SessionTokenListResponse:
        """
        Returns a list of session tokens.

        Args:
          connected_account_id: Filter for session tokens associated with a connected account.

          integration: Filter for session tokens associated with an integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/session-tokens",
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
                    session_token_list_params.SessionTokenListParams,
                ),
            ),
            cast_to=SessionTokenListResponse,
        )

    def delete(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionTokenDeleteResponse:
        """
        Deletes a session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._delete(
            f"/session-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionTokenDeleteResponse,
        )


class AsyncSessionTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionTokensResourceWithRawResponse:
        return AsyncSessionTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionTokensResourceWithStreamingResponse:
        return AsyncSessionTokensResourceWithStreamingResponse(self)

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
    ) -> SessionToken:
        """
        Creates a session token.

        Args:
          connected_account_id: The unique identifier to assign to the connected account.

          integration: The unique slug of the integration to connect the account to.

          configuration: Configuration options to assign to the connected account.

          expires_in_mins: The number of minutes until the session token expires.

          metadata: Additional metadata to assign to the connected account.

          name: The display name to assign to the connected account.

          redirect_url: The URL to redirect to after the authorization flow is complete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/session-tokens",
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
                session_token_create_params.SessionTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToken,
        )

    async def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionToken:
        """
        Returns a session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            f"/session-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionToken,
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
    ) -> SessionTokenListResponse:
        """
        Returns a list of session tokens.

        Args:
          connected_account_id: Filter for session tokens associated with a connected account.

          integration: Filter for session tokens associated with an integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/session-tokens",
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
                    session_token_list_params.SessionTokenListParams,
                ),
            ),
            cast_to=SessionTokenListResponse,
        )

    async def delete(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionTokenDeleteResponse:
        """
        Deletes a session token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._delete(
            f"/session-tokens/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionTokenDeleteResponse,
        )


class SessionTokensResourceWithRawResponse:
    def __init__(self, session_tokens: SessionTokensResource) -> None:
        self._session_tokens = session_tokens

        self.create = to_raw_response_wrapper(
            session_tokens.create,
        )
        self.retrieve = to_raw_response_wrapper(
            session_tokens.retrieve,
        )
        self.list = to_raw_response_wrapper(
            session_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            session_tokens.delete,
        )


class AsyncSessionTokensResourceWithRawResponse:
    def __init__(self, session_tokens: AsyncSessionTokensResource) -> None:
        self._session_tokens = session_tokens

        self.create = async_to_raw_response_wrapper(
            session_tokens.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            session_tokens.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            session_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            session_tokens.delete,
        )


class SessionTokensResourceWithStreamingResponse:
    def __init__(self, session_tokens: SessionTokensResource) -> None:
        self._session_tokens = session_tokens

        self.create = to_streamed_response_wrapper(
            session_tokens.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            session_tokens.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            session_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            session_tokens.delete,
        )


class AsyncSessionTokensResourceWithStreamingResponse:
    def __init__(self, session_tokens: AsyncSessionTokensResource) -> None:
        self._session_tokens = session_tokens

        self.create = async_to_streamed_response_wrapper(
            session_tokens.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            session_tokens.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            session_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            session_tokens.delete,
        )
