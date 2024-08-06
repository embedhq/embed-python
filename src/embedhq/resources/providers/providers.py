# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import provider_list_params, provider_retrieve_params
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
from ..._base_client import make_request_options
from ...types.provider import Provider
from .action_templates import (
    ActionTemplatesResource,
    AsyncActionTemplatesResource,
    ActionTemplatesResourceWithRawResponse,
    AsyncActionTemplatesResourceWithRawResponse,
    ActionTemplatesResourceWithStreamingResponse,
    AsyncActionTemplatesResourceWithStreamingResponse,
)
from .collection_templates import (
    CollectionTemplatesResource,
    AsyncCollectionTemplatesResource,
    CollectionTemplatesResourceWithRawResponse,
    AsyncCollectionTemplatesResourceWithRawResponse,
    CollectionTemplatesResourceWithStreamingResponse,
    AsyncCollectionTemplatesResourceWithStreamingResponse,
)
from ...types.provider_list_response import ProviderListResponse

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def collection_templates(self) -> CollectionTemplatesResource:
        return CollectionTemplatesResource(self._client)

    @cached_property
    def action_templates(self) -> ActionTemplatesResource:
        return ActionTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        return ProvidersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        provider: str,
        *,
        include_action_templates: bool | NotGiven = NOT_GIVEN,
        include_collection_templates: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Provider:
        """
        Returns a provider.

        Args:
          include_action_templates: Include action templates in the response.

          include_collection_templates: Include collection templates in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/providers/{provider}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_action_templates": include_action_templates,
                        "include_collection_templates": include_collection_templates,
                    },
                    provider_retrieve_params.ProviderRetrieveParams,
                ),
            ),
            cast_to=Provider,
        )

    def list(
        self,
        *,
        include_action_templates: bool | NotGiven = NOT_GIVEN,
        include_collection_templates: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """
        Returns a list of integration providers.

        Args:
          include_action_templates: Include action templates for each provider in the response.

          include_collection_templates: Include collection templates for each provider in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_action_templates": include_action_templates,
                        "include_collection_templates": include_collection_templates,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def collection_templates(self) -> AsyncCollectionTemplatesResource:
        return AsyncCollectionTemplatesResource(self._client)

    @cached_property
    def action_templates(self) -> AsyncActionTemplatesResource:
        return AsyncActionTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        return AsyncProvidersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        provider: str,
        *,
        include_action_templates: bool | NotGiven = NOT_GIVEN,
        include_collection_templates: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Provider:
        """
        Returns a provider.

        Args:
          include_action_templates: Include action templates in the response.

          include_collection_templates: Include collection templates in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/providers/{provider}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_action_templates": include_action_templates,
                        "include_collection_templates": include_collection_templates,
                    },
                    provider_retrieve_params.ProviderRetrieveParams,
                ),
            ),
            cast_to=Provider,
        )

    async def list(
        self,
        *,
        include_action_templates: bool | NotGiven = NOT_GIVEN,
        include_collection_templates: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """
        Returns a list of integration providers.

        Args:
          include_action_templates: Include action templates for each provider in the response.

          include_collection_templates: Include collection templates for each provider in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_action_templates": include_action_templates,
                        "include_collection_templates": include_collection_templates,
                    },
                    provider_list_params.ProviderListParams,
                ),
            ),
            cast_to=ProviderListResponse,
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.retrieve = to_raw_response_wrapper(
            providers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            providers.list,
        )

    @cached_property
    def collection_templates(self) -> CollectionTemplatesResourceWithRawResponse:
        return CollectionTemplatesResourceWithRawResponse(self._providers.collection_templates)

    @cached_property
    def action_templates(self) -> ActionTemplatesResourceWithRawResponse:
        return ActionTemplatesResourceWithRawResponse(self._providers.action_templates)


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.retrieve = async_to_raw_response_wrapper(
            providers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )

    @cached_property
    def collection_templates(self) -> AsyncCollectionTemplatesResourceWithRawResponse:
        return AsyncCollectionTemplatesResourceWithRawResponse(self._providers.collection_templates)

    @cached_property
    def action_templates(self) -> AsyncActionTemplatesResourceWithRawResponse:
        return AsyncActionTemplatesResourceWithRawResponse(self._providers.action_templates)


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.retrieve = to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            providers.list,
        )

    @cached_property
    def collection_templates(self) -> CollectionTemplatesResourceWithStreamingResponse:
        return CollectionTemplatesResourceWithStreamingResponse(self._providers.collection_templates)

    @cached_property
    def action_templates(self) -> ActionTemplatesResourceWithStreamingResponse:
        return ActionTemplatesResourceWithStreamingResponse(self._providers.action_templates)


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.retrieve = async_to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )

    @cached_property
    def collection_templates(self) -> AsyncCollectionTemplatesResourceWithStreamingResponse:
        return AsyncCollectionTemplatesResourceWithStreamingResponse(self._providers.collection_templates)

    @cached_property
    def action_templates(self) -> AsyncActionTemplatesResourceWithStreamingResponse:
        return AsyncActionTemplatesResourceWithStreamingResponse(self._providers.action_templates)
