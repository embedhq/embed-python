# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import (
    collection_list_params,
    collection_create_params,
    collection_delete_params,
    collection_update_params,
    collection_retrieve_params,
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
from ..types.collection import Collection
from ..types.collection_list_response import CollectionListResponse
from ..types.collection_delete_response import CollectionDeleteResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_template: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_scopes: List[str] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Creates a collection from a template.

        Args:
          collection_template: The unique slug of the collection template to use.

          integration: The unique slug of the integration to which the collection belongs.

          configuration: Configuration options for the collection.

          name: The display name of the collection (defaults to the collection template name).

          required_scopes: The OAuth scopes required to sync the collection (defaults to the collection
              template scopes, if applicable).

          slug: The unique slug of the collection (defaults to the collection template slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections",
            body=maybe_transform(
                {
                    "collection_template": collection_template,
                    "integration": integration,
                    "configuration": configuration,
                    "name": name,
                    "required_scopes": required_scopes,
                    "slug": slug,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    def retrieve(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Returns a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to retrieve (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._get(
            f"/collections/{collection}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_retrieve_params.CollectionRetrieveParams,
                ),
            ),
            cast_to=Collection,
        )

    def update(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        is_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_scopes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Updates a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to update (defaults to latest).

          configuration: Configuration options for the collection.

          is_enabled: Whether the collection is enabled.

          name: The display name of the collection.

          required_scopes: The OAuth scopes required to sync the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._put(
            f"/collections/{collection}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "is_enabled": is_enabled,
                    "name": name,
                    "required_scopes": required_scopes,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_update_params.CollectionUpdateParams,
                ),
            ),
            cast_to=Collection,
        )

    def list(
        self,
        *,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Returns a list of collections.

        Args:
          integration: The slug of the integration to which the collections belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration": integration}, collection_list_params.CollectionListParams),
            ),
            cast_to=CollectionListResponse,
        )

    def delete(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDeleteResponse:
        """
        Deletes a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to delete (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._delete(
            f"/collections/{collection}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_delete_params.CollectionDeleteParams,
                ),
            ),
            cast_to=CollectionDeleteResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_template: str,
        integration: str,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_scopes: List[str] | NotGiven = NOT_GIVEN,
        slug: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Creates a collection from a template.

        Args:
          collection_template: The unique slug of the collection template to use.

          integration: The unique slug of the integration to which the collection belongs.

          configuration: Configuration options for the collection.

          name: The display name of the collection (defaults to the collection template name).

          required_scopes: The OAuth scopes required to sync the collection (defaults to the collection
              template scopes, if applicable).

          slug: The unique slug of the collection (defaults to the collection template slug).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections",
            body=await async_maybe_transform(
                {
                    "collection_template": collection_template,
                    "integration": integration,
                    "configuration": configuration,
                    "name": name,
                    "required_scopes": required_scopes,
                    "slug": slug,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Collection,
        )

    async def retrieve(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Returns a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to retrieve (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._get(
            f"/collections/{collection}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_retrieve_params.CollectionRetrieveParams,
                ),
            ),
            cast_to=Collection,
        )

    async def update(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        configuration: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        is_enabled: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        required_scopes: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Collection:
        """
        Updates a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to update (defaults to latest).

          configuration: Configuration options for the collection.

          is_enabled: Whether the collection is enabled.

          name: The display name of the collection.

          required_scopes: The OAuth scopes required to sync the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._put(
            f"/collections/{collection}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "is_enabled": is_enabled,
                    "name": name,
                    "required_scopes": required_scopes,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_update_params.CollectionUpdateParams,
                ),
            ),
            cast_to=Collection,
        )

    async def list(
        self,
        *,
        integration: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        Returns a list of collections.

        Args:
          integration: The slug of the integration to which the collections belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration": integration}, collection_list_params.CollectionListParams
                ),
            ),
            cast_to=CollectionListResponse,
        )

    async def delete(
        self,
        *,
        collection: str,
        integration: str,
        collection_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDeleteResponse:
        """
        Deletes a collection.

        Args:
          integration: The slug of the integration to which the collection belongs.

          collection_version: The version of the collection to delete (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return await self._delete(
            f"/collections/{collection}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "integration": integration,
                        "collection_version": collection_version,
                    },
                    collection_delete_params.CollectionDeleteParams,
                ),
            ),
            cast_to=CollectionDeleteResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
