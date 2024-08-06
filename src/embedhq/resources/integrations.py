# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import integration_list_params, integration_create_params
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
from ..types.integration import Integration
from ..types.integration_list_response import IntegrationListResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        provider: str,
        name: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_scopes: List[str] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        use_test_credentials: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration:
        """
        Creates an integration.

        Args:
          provider: The unique slug of the integration provider.

          name: The display name of the integration (defaults to provider name).

          oauth_client_id: The OAuth Client ID. Required for integrations that use OAuth.

          oauth_client_secret: The OAuth Client Secret. Required for integrations that use OAuth.

          oauth_scopes: Additional OAuth scopes to request from the user. By default, Embed will request
              the minimum required scopes for the collections and actions enabled on the
              integration.

          slug: The unique slug of the integration (defaults to provider slug).

          use_test_credentials: Use test credentials provided by Embed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integrations",
            body=maybe_transform(
                {
                    "provider": provider,
                    "name": name,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_scopes": oauth_scopes,
                    "slug": slug,
                    "use_test_credentials": use_test_credentials,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Integration,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationListResponse:
        """Returns a list of integrations.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID or slug that defines
              your place in the list.

          before: A cursor for use in pagination. `before` is an object ID or slug that defines
              your place in the list.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=IntegrationListResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        provider: str,
        name: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_scopes: List[str] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        use_test_credentials: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration:
        """
        Creates an integration.

        Args:
          provider: The unique slug of the integration provider.

          name: The display name of the integration (defaults to provider name).

          oauth_client_id: The OAuth Client ID. Required for integrations that use OAuth.

          oauth_client_secret: The OAuth Client Secret. Required for integrations that use OAuth.

          oauth_scopes: Additional OAuth scopes to request from the user. By default, Embed will request
              the minimum required scopes for the collections and actions enabled on the
              integration.

          slug: The unique slug of the integration (defaults to provider slug).

          use_test_credentials: Use test credentials provided by Embed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integrations",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "name": name,
                    "oauth_client_id": oauth_client_id,
                    "oauth_client_secret": oauth_client_secret,
                    "oauth_scopes": oauth_scopes,
                    "slug": slug,
                    "use_test_credentials": use_test_credentials,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Integration,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationListResponse:
        """Returns a list of integrations.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID or slug that defines
              your place in the list.

          before: A cursor for use in pagination. `before` is an object ID or slug that defines
              your place in the list.

          limit: A limit on the number of objects to be returned.

          order: Sort order by the `created_at` timestamp of the objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            cast_to=IntegrationListResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_raw_response_wrapper(
            integrations.create,
        )
        self.list = to_raw_response_wrapper(
            integrations.list,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_raw_response_wrapper(
            integrations.create,
        )
        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_streamed_response_wrapper(
            integrations.create,
        )
        self.list = to_streamed_response_wrapper(
            integrations.list,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_streamed_response_wrapper(
            integrations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
