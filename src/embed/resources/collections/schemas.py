# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.collections import schema_list_params, schema_retrieve_params
from ...types.collections.collection_schema import CollectionSchema
from ...types.collections.schema_list_response import SchemaListResponse

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self)

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
    ) -> CollectionSchema:
        """
        Returns a collection schema.

        Args:
          integration_id: The ID of the integration to which the collection schema belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return self._get(
            f"/collections/{collection_key}/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, schema_retrieve_params.SchemaRetrieveParams),
            ),
            cast_to=CollectionSchema,
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
    ) -> SchemaListResponse:
        """
        Returns a list of collection schemas.

        Args:
          integration_id: The ID of the integration to which the collection schemas belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/collections/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, schema_list_params.SchemaListParams),
            ),
            cast_to=SchemaListResponse,
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self)

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
    ) -> CollectionSchema:
        """
        Returns a collection schema.

        Args:
          integration_id: The ID of the integration to which the collection schema belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection_key:
            raise ValueError(f"Expected a non-empty value for `collection_key` but received {collection_key!r}")
        return await self._get(
            f"/collections/{collection_key}/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, schema_retrieve_params.SchemaRetrieveParams
                ),
            ),
            cast_to=CollectionSchema,
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
    ) -> SchemaListResponse:
        """
        Returns a list of collection schemas.

        Args:
          integration_id: The ID of the integration to which the collection schemas belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/collections/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, schema_list_params.SchemaListParams
                ),
            ),
            cast_to=SchemaListResponse,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_raw_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.retrieve = async_to_streamed_response_wrapper(
            schemas.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
