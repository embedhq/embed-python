# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    connected_account_list_params,
    connected_account_delete_params,
    connected_account_update_params,
    connected_account_upsert_params,
    connected_account_retrieve_params,
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
from .._base_client import make_request_options
from ..types.connected_account import ConnectedAccount
from ..types.connected_account_list_response import ConnectedAccountListResponse
from ..types.connected_account_delete_response import ConnectedAccountDeleteResponse

__all__ = ["ConnectedAccountsResource", "AsyncConnectedAccountsResource"]


class ConnectedAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectedAccountsResourceWithRawResponse:
        return ConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectedAccountsResourceWithStreamingResponse:
        return ConnectedAccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        connected_account_id: str,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """
        Returns a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return self._get(
            f"/connected-accounts/{connected_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration": integration}, connected_account_retrieve_params.ConnectedAccountRetrieveParams
                ),
            ),
            cast_to=ConnectedAccount,
        )

    def update(
        self,
        *,
        connected_account_id: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """
        Updates a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          configuration: Configuration options for the connected account.

          metadata: Additional metadata for the connected account.

          name: The display name of the connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return self._put(
            f"/connected-accounts/{connected_account_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                    "name": name,
                },
                connected_account_update_params.ConnectedAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration": integration}, connected_account_update_params.ConnectedAccountUpdateParams
                ),
            ),
            cast_to=ConnectedAccount,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        integration: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountListResponse:
        """
        Returns a list of connected accounts.

        Args:
          after: A cursor for use in pagination. `after` is an object ID or slug that defines
              your place in the list.

          before: A cursor for use in pagination. `before` is an object ID or slug that defines
              your place in the list.

          integration: Filter connected accounts by integration slug.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/connected-accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "integration": integration,
                        "limit": limit,
                        "order": order,
                    },
                    connected_account_list_params.ConnectedAccountListParams,
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    def delete(
        self,
        *,
        connected_account_id: str,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountDeleteResponse:
        """
        Deletes a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return self._delete(
            f"/connected-accounts/{connected_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"integration": integration}, connected_account_delete_params.ConnectedAccountDeleteParams
                ),
            ),
            cast_to=ConnectedAccountDeleteResponse,
        )

    def upsert(
        self,
        *,
        id: str,
        auth_method: Literal["oauth2", "basic", "api_key", "none"],
        credentials: connected_account_upsert_params.Credentials,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """Manually add a connected account.

        We recommend using the
        [authentication flow](https://useembed.com/docs/guides/connect-an-account)
        provided by Embed. However, if you've already obtained account credentials, you
        can use them to create a connected account with this endpoint.

        Args:
          id: The unique identifier for the connected account.

          auth_method: The authentication method used to connect the account.

          credentials: The connected account's authentication credentials.

          integration: The unique slug of the integration associated with the connected account.

          configuration: Configuration options for the connected account.

          metadata: Additional metadata for the connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/connected-accounts",
            body=maybe_transform(
                {
                    "id": id,
                    "auth_method": auth_method,
                    "credentials": credentials,
                    "integration": integration,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                connected_account_upsert_params.ConnectedAccountUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccount,
        )


class AsyncConnectedAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectedAccountsResourceWithRawResponse:
        return AsyncConnectedAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectedAccountsResourceWithStreamingResponse:
        return AsyncConnectedAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        connected_account_id: str,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """
        Returns a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return await self._get(
            f"/connected-accounts/{connected_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration": integration}, connected_account_retrieve_params.ConnectedAccountRetrieveParams
                ),
            ),
            cast_to=ConnectedAccount,
        )

    async def update(
        self,
        *,
        connected_account_id: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """
        Updates a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          configuration: Configuration options for the connected account.

          metadata: Additional metadata for the connected account.

          name: The display name of the connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return await self._put(
            f"/connected-accounts/{connected_account_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "metadata": metadata,
                    "name": name,
                },
                connected_account_update_params.ConnectedAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration": integration}, connected_account_update_params.ConnectedAccountUpdateParams
                ),
            ),
            cast_to=ConnectedAccount,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        integration: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountListResponse:
        """
        Returns a list of connected accounts.

        Args:
          after: A cursor for use in pagination. `after` is an object ID or slug that defines
              your place in the list.

          before: A cursor for use in pagination. `before` is an object ID or slug that defines
              your place in the list.

          integration: Filter connected accounts by integration slug.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/connected-accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "integration": integration,
                        "limit": limit,
                        "order": order,
                    },
                    connected_account_list_params.ConnectedAccountListParams,
                ),
            ),
            cast_to=ConnectedAccountListResponse,
        )

    async def delete(
        self,
        *,
        connected_account_id: str,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccountDeleteResponse:
        """
        Deletes a connected account.

        Args:
          integration: The slug of the integration to which the connected account belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connected_account_id:
            raise ValueError(
                f"Expected a non-empty value for `connected_account_id` but received {connected_account_id!r}"
            )
        return await self._delete(
            f"/connected-accounts/{connected_account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration": integration}, connected_account_delete_params.ConnectedAccountDeleteParams
                ),
            ),
            cast_to=ConnectedAccountDeleteResponse,
        )

    async def upsert(
        self,
        *,
        id: str,
        auth_method: Literal["oauth2", "basic", "api_key", "none"],
        credentials: connected_account_upsert_params.Credentials,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConnectedAccount:
        """Manually add a connected account.

        We recommend using the
        [authentication flow](https://useembed.com/docs/guides/connect-an-account)
        provided by Embed. However, if you've already obtained account credentials, you
        can use them to create a connected account with this endpoint.

        Args:
          id: The unique identifier for the connected account.

          auth_method: The authentication method used to connect the account.

          credentials: The connected account's authentication credentials.

          integration: The unique slug of the integration associated with the connected account.

          configuration: Configuration options for the connected account.

          metadata: Additional metadata for the connected account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/connected-accounts",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "auth_method": auth_method,
                    "credentials": credentials,
                    "integration": integration,
                    "configuration": configuration,
                    "metadata": metadata,
                },
                connected_account_upsert_params.ConnectedAccountUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectedAccount,
        )


class ConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.retrieve = to_raw_response_wrapper(
            connected_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connected_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            connected_accounts.delete,
        )
        self.upsert = to_raw_response_wrapper(
            connected_accounts.upsert,
        )


class AsyncConnectedAccountsResourceWithRawResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.retrieve = async_to_raw_response_wrapper(
            connected_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connected_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            connected_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connected_accounts.delete,
        )
        self.upsert = async_to_raw_response_wrapper(
            connected_accounts.upsert,
        )


class ConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: ConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.retrieve = to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connected_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            connected_accounts.delete,
        )
        self.upsert = to_streamed_response_wrapper(
            connected_accounts.upsert,
        )


class AsyncConnectedAccountsResourceWithStreamingResponse:
    def __init__(self, connected_accounts: AsyncConnectedAccountsResource) -> None:
        self._connected_accounts = connected_accounts

        self.retrieve = async_to_streamed_response_wrapper(
            connected_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connected_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connected_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connected_accounts.delete,
        )
        self.upsert = async_to_streamed_response_wrapper(
            connected_accounts.upsert,
        )
