# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import proxy_put_params, proxy_post_params, proxy_delete_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from ..types.proxy_get_response import ProxyGetResponse
from ..types.proxy_put_response import ProxyPutResponse
from ..types.proxy_post_response import ProxyPostResponse
from ..types.proxy_delete_response import ProxyDeleteResponse

__all__ = ["ProxyResource", "AsyncProxyResource"]


class ProxyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProxyResourceWithRawResponse:
        return ProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProxyResourceWithStreamingResponse:
        return ProxyResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyDeleteResponse:
        """
        Proxy DELETE request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            f"/proxy/{endpoint}",
            body=maybe_transform(body, proxy_delete_params.ProxyDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyDeleteResponse,
        )

    def get(
        self,
        *,
        endpoint: str,
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyGetResponse:
        """
        Proxy GET request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            f"/proxy/{endpoint}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyGetResponse,
        )

    def post(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyPostResponse:
        """
        Proxy POST request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/proxy/{endpoint}",
            body=maybe_transform(body, proxy_post_params.ProxyPostParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPostResponse,
        )

    def put(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyPutResponse:
        """
        Proxy PUT request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._put(
            f"/proxy/{endpoint}",
            body=maybe_transform(body, proxy_put_params.ProxyPutParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPutResponse,
        )


class AsyncProxyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProxyResourceWithRawResponse:
        return AsyncProxyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProxyResourceWithStreamingResponse:
        return AsyncProxyResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyDeleteResponse:
        """
        Proxy DELETE request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            f"/proxy/{endpoint}",
            body=await async_maybe_transform(body, proxy_delete_params.ProxyDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyDeleteResponse,
        )

    async def get(
        self,
        *,
        endpoint: str,
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyGetResponse:
        """
        Proxy GET request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/proxy/{endpoint}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyGetResponse,
        )

    async def post(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyPostResponse:
        """
        Proxy POST request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/proxy/{endpoint}",
            body=await async_maybe_transform(body, proxy_post_params.ProxyPostParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPostResponse,
        )

    async def put(
        self,
        *,
        endpoint: str,
        body: Dict[str, object],
        connected_account_id: str,
        integration: str,
        base_url_override: str | NotGiven = NOT_GIVEN,
        retries: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProxyPutResponse:
        """
        Proxy PUT request with connected account's credentials.

        Args:
          endpoint: The endpoint to proxy the request to.

          connected_account_id: The ID of the connected account to use for the request.

          integration: The slug of the integration to use for the request.

          base_url_override: Override the base URL for the request.

          retries: The number of times to retry the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "connected_account_id": connected_account_id,
                    "integration": integration,
                    "base_url_override": base_url_override,
                    "retries": str(retries) if is_given(retries) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._put(
            f"/proxy/{endpoint}",
            body=await async_maybe_transform(body, proxy_put_params.ProxyPutParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProxyPutResponse,
        )


class ProxyResourceWithRawResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.delete = to_raw_response_wrapper(
            proxy.delete,
        )
        self.get = to_raw_response_wrapper(
            proxy.get,
        )
        self.post = to_raw_response_wrapper(
            proxy.post,
        )
        self.put = to_raw_response_wrapper(
            proxy.put,
        )


class AsyncProxyResourceWithRawResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.delete = async_to_raw_response_wrapper(
            proxy.delete,
        )
        self.get = async_to_raw_response_wrapper(
            proxy.get,
        )
        self.post = async_to_raw_response_wrapper(
            proxy.post,
        )
        self.put = async_to_raw_response_wrapper(
            proxy.put,
        )


class ProxyResourceWithStreamingResponse:
    def __init__(self, proxy: ProxyResource) -> None:
        self._proxy = proxy

        self.delete = to_streamed_response_wrapper(
            proxy.delete,
        )
        self.get = to_streamed_response_wrapper(
            proxy.get,
        )
        self.post = to_streamed_response_wrapper(
            proxy.post,
        )
        self.put = to_streamed_response_wrapper(
            proxy.put,
        )


class AsyncProxyResourceWithStreamingResponse:
    def __init__(self, proxy: AsyncProxyResource) -> None:
        self._proxy = proxy

        self.delete = async_to_streamed_response_wrapper(
            proxy.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            proxy.get,
        )
        self.post = async_to_streamed_response_wrapper(
            proxy.post,
        )
        self.put = async_to_streamed_response_wrapper(
            proxy.put,
        )
