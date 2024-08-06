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
from ..._base_client import make_request_options
from ...types.actions import run_list_params, run_retrieve_params
from ...types.actions.action_run import ActionRun
from ...types.actions.run_list_response import RunListResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        action: str,
        action_run_id: str,
        connected_account_id: str,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRun:
        """
        Returns an action run.

        Args:
          connected_account_id: The ID of the connected account to which the action belongs.

          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        if not action_run_id:
            raise ValueError(f"Expected a non-empty value for `action_run_id` but received {action_run_id!r}")
        return self._get(
            f"/actions/{action}/runs/{action_run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "action_version": action_version,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=ActionRun,
        )

    def list(
        self,
        *,
        action: str,
        connected_account_id: str,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """
        Returns a list of recent action runs.

        Args:
          connected_account_id: The ID of the connected account to which the action belongs.

          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._get(
            f"/actions/{action}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "action_version": action_version,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        action: str,
        action_run_id: str,
        connected_account_id: str,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionRun:
        """
        Returns an action run.

        Args:
          connected_account_id: The ID of the connected account to which the action belongs.

          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        if not action_run_id:
            raise ValueError(f"Expected a non-empty value for `action_run_id` but received {action_run_id!r}")
        return await self._get(
            f"/actions/{action}/runs/{action_run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "action_version": action_version,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=ActionRun,
        )

    async def list(
        self,
        *,
        action: str,
        connected_account_id: str,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """
        Returns a list of recent action runs.

        Args:
          connected_account_id: The ID of the connected account to which the action belongs.

          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._get(
            f"/actions/{action}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connected_account_id": connected_account_id,
                        "integration": integration,
                        "action_version": action_version,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
