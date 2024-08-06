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
from ...types.providers.action_template_list_response import ActionTemplateListResponse
from ...types.providers.action_template_retrieve_response import ActionTemplateRetrieveResponse

__all__ = ["ActionTemplatesResource", "AsyncActionTemplatesResource"]


class ActionTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionTemplatesResourceWithRawResponse:
        return ActionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionTemplatesResourceWithStreamingResponse:
        return ActionTemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        action: str,
        *,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTemplateRetrieveResponse:
        """
        Returns an action template for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._get(
            f"/providers/{provider}/action-templates/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTemplateRetrieveResponse,
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
    ) -> ActionTemplateListResponse:
        """
        Returns a list of action templates for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return self._get(
            f"/providers/{provider}/action-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTemplateListResponse,
        )


class AsyncActionTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionTemplatesResourceWithRawResponse:
        return AsyncActionTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionTemplatesResourceWithStreamingResponse:
        return AsyncActionTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        action: str,
        *,
        provider: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTemplateRetrieveResponse:
        """
        Returns an action template for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._get(
            f"/providers/{provider}/action-templates/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTemplateRetrieveResponse,
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
    ) -> ActionTemplateListResponse:
        """
        Returns a list of action templates for a provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider:
            raise ValueError(f"Expected a non-empty value for `provider` but received {provider!r}")
        return await self._get(
            f"/providers/{provider}/action-templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionTemplateListResponse,
        )


class ActionTemplatesResourceWithRawResponse:
    def __init__(self, action_templates: ActionTemplatesResource) -> None:
        self._action_templates = action_templates

        self.retrieve = to_raw_response_wrapper(
            action_templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            action_templates.list,
        )


class AsyncActionTemplatesResourceWithRawResponse:
    def __init__(self, action_templates: AsyncActionTemplatesResource) -> None:
        self._action_templates = action_templates

        self.retrieve = async_to_raw_response_wrapper(
            action_templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            action_templates.list,
        )


class ActionTemplatesResourceWithStreamingResponse:
    def __init__(self, action_templates: ActionTemplatesResource) -> None:
        self._action_templates = action_templates

        self.retrieve = to_streamed_response_wrapper(
            action_templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            action_templates.list,
        )


class AsyncActionTemplatesResourceWithStreamingResponse:
    def __init__(self, action_templates: AsyncActionTemplatesResource) -> None:
        self._action_templates = action_templates

        self.retrieve = async_to_streamed_response_wrapper(
            action_templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            action_templates.list,
        )
