# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.providers.collection_template_list_response import CollectionTemplateListResponse
from ...types.providers.collection_template_retrieve_response import CollectionTemplateRetrieveResponse

__all__ = ["CollectionTemplatesResource", "AsyncCollectionTemplatesResource"]


class CollectionTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionTemplatesResourceWithRawResponse:
        return CollectionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionTemplatesResourceWithStreamingResponse:
        return CollectionTemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection: str,
        *,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionTemplateRetrieveResponse:
        """
        Returns a collection template for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._get(
            f"/providers/{provider}/collection-templates/{collection}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionTemplateRetrieveResponse,
        )

    def list(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionTemplateListResponse:
        """
        Returns a list of collection templates for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/providers/{provider}/collection-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionTemplateListResponse,
        )


class AsyncCollectionTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionTemplatesResourceWithRawResponse:
        return AsyncCollectionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionTemplatesResourceWithStreamingResponse:
        return AsyncCollectionTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection: str,
        *,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionTemplateRetrieveResponse:
        """
        Returns a collection template for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._get(
            f"/providers/{provider}/collection-templates/{collection}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionTemplateRetrieveResponse,
        )

    async def list(
        self,
        provider: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionTemplateListResponse:
        """
        Returns a list of collection templates for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/providers/{provider}/collection-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionTemplateListResponse,
        )


class CollectionTemplatesResourceWithRawResponse:
    def __init__(self, collection_templates: CollectionTemplatesResource) -> None:
        self._collection_templates = collection_templates

        self.retrieve = to_raw_response_wrapper(
            collection_templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            collection_templates.list,
        )


class AsyncCollectionTemplatesResourceWithRawResponse:
    def __init__(self, collection_templates: AsyncCollectionTemplatesResource) -> None:
        self._collection_templates = collection_templates

        self.retrieve = async_to_raw_response_wrapper(
            collection_templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            collection_templates.list,
        )


class CollectionTemplatesResourceWithStreamingResponse:
    def __init__(self, collection_templates: CollectionTemplatesResource) -> None:
        self._collection_templates = collection_templates

        self.retrieve = to_streamed_response_wrapper(
            collection_templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            collection_templates.list,
        )


class AsyncCollectionTemplatesResourceWithStreamingResponse:
    def __init__(self, collection_templates: AsyncCollectionTemplatesResource) -> None:
        self._collection_templates = collection_templates

        self.retrieve = async_to_streamed_response_wrapper(
            collection_templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            collection_templates.list,
        )
