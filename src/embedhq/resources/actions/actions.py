# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
from ...types import action_list_params, action_trigger_params, action_retrieve_params
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
from ...types.action import Action
from ...types.action_list_response import ActionListResponse
from ...types.action_trigger_response import ActionTriggerResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        action: str,
        *,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Action:
        """
        Returns an action.

        Args:
          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action to retrieve (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._get(
            f"/actions/{action}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "integration": integration,
                        "action_version": action_version,
                    },
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=Action,
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
    ) -> ActionListResponse:
        """
        Returns a list of actions.

        Args:
          integration: The slug of the integration to which the actions belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration": integration}, action_list_params.ActionListParams),
            ),
            cast_to=ActionListResponse,
        )

    def trigger(
        self,
        action: str,
        *,
        connected_account_id: str,
        integration: str,
        input: Dict[str, object],
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTriggerResponse:
        """
        Triggers an action.

        Args:
          connected_account_id: The ID of the connected account used to trigger the action.

          integration: The slug of the integration to which the action belongs.

          input: The input parameters for the action.

          action_version: The version of the action to trigger (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._post(
            f"/actions/{action}/trigger",
            body=maybe_transform({"input": input}, action_trigger_params.ActionTriggerParams),
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
                    action_trigger_params.ActionTriggerParams,
                ),
            ),
            cast_to=ActionTriggerResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        action: str,
        *,
        integration: str,
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Action:
        """
        Returns an action.

        Args:
          integration: The slug of the integration to which the action belongs.

          action_version: The version of the action to retrieve (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._get(
            f"/actions/{action}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "integration": integration,
                        "action_version": action_version,
                    },
                    action_retrieve_params.ActionRetrieveParams,
                ),
            ),
            cast_to=Action,
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
    ) -> ActionListResponse:
        """
        Returns a list of actions.

        Args:
          integration: The slug of the integration to which the actions belong.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/actions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"integration": integration}, action_list_params.ActionListParams),
            ),
            cast_to=ActionListResponse,
        )

    async def trigger(
        self,
        action: str,
        *,
        connected_account_id: str,
        integration: str,
        input: Dict[str, object],
        action_version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionTriggerResponse:
        """
        Triggers an action.

        Args:
          connected_account_id: The ID of the connected account used to trigger the action.

          integration: The slug of the integration to which the action belongs.

          input: The input parameters for the action.

          action_version: The version of the action to trigger (defaults to latest).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._post(
            f"/actions/{action}/trigger",
            body=await async_maybe_transform({"input": input}, action_trigger_params.ActionTriggerParams),
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
                    action_trigger_params.ActionTriggerParams,
                ),
            ),
            cast_to=ActionTriggerResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )
        self.trigger = to_raw_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._actions.runs)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.trigger = async_to_raw_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._actions.runs)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.trigger = to_streamed_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._actions.runs)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.trigger = async_to_streamed_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._actions.runs)
