# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ...types import (
    action_list_params,
    action_enable_params,
    action_schema_params,
    action_disable_params,
    action_trigger_params,
    action_retrieve_params,
)
from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
)
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
from ...types.action import Action
from ...types.action_list_response import ActionListResponse
from ...types.actions.action_schema import ActionSchema
from ...types.action_disable_response import ActionDisableResponse
from ...types.action_trigger_response import ActionTriggerResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def schemas(self) -> SchemasResource:
        return SchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        action_key: str,
        *,
        integration_id: str,
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
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return self._get(
            f"/actions/{action_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, action_retrieve_params.ActionRetrieveParams),
            ),
            cast_to=Action,
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
    ) -> ActionListResponse:
        """
        Returns a list of actions.

        Args:
          integration_id: The ID of the integration to which the actions belong.

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
                query=maybe_transform({"integration_id": integration_id}, action_list_params.ActionListParams),
            ),
            cast_to=ActionListResponse,
        )

    def disable(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableResponse:
        """
        Disables an action.

        Args:
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return self._post(
            f"/actions/{action_key}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, action_disable_params.ActionDisableParams),
            ),
            cast_to=ActionDisableResponse,
        )

    def enable(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Action:
        """
        Enables an action.

        Args:
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return self._post(
            f"/actions/{action_key}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, action_enable_params.ActionEnableParams),
            ),
            cast_to=Action,
        )

    def schema(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSchema:
        """
        Returns an action schema.

        Args:
          integration_id: The ID of the integration to which the action schema belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return self._get(
            f"/actions/{action_key}/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"integration_id": integration_id}, action_schema_params.ActionSchemaParams),
            ),
            cast_to=ActionSchema,
        )

    def trigger(
        self,
        action_key: str,
        *,
        connection_id: str,
        integration_id: str,
        input: Dict[str, object],
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
          connection_id: The ID of the connection to use for the action.

          integration_id: The ID of the integration to which the action belongs.

          input: The input parameters for the action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return self._post(
            f"/actions/{action_key}/trigger",
            body=maybe_transform({"input": input}, action_trigger_params.ActionTriggerParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
                    },
                    action_trigger_params.ActionTriggerParams,
                ),
            ),
            cast_to=ActionTriggerResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        return AsyncSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        action_key: str,
        *,
        integration_id: str,
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
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return await self._get(
            f"/actions/{action_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, action_retrieve_params.ActionRetrieveParams
                ),
            ),
            cast_to=Action,
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
    ) -> ActionListResponse:
        """
        Returns a list of actions.

        Args:
          integration_id: The ID of the integration to which the actions belong.

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
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, action_list_params.ActionListParams
                ),
            ),
            cast_to=ActionListResponse,
        )

    async def disable(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionDisableResponse:
        """
        Disables an action.

        Args:
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return await self._post(
            f"/actions/{action_key}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, action_disable_params.ActionDisableParams
                ),
            ),
            cast_to=ActionDisableResponse,
        )

    async def enable(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Action:
        """
        Enables an action.

        Args:
          integration_id: The ID of the integration to which the action belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return await self._post(
            f"/actions/{action_key}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, action_enable_params.ActionEnableParams
                ),
            ),
            cast_to=Action,
        )

    async def schema(
        self,
        action_key: str,
        *,
        integration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionSchema:
        """
        Returns an action schema.

        Args:
          integration_id: The ID of the integration to which the action schema belongs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return await self._get(
            f"/actions/{action_key}/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"integration_id": integration_id}, action_schema_params.ActionSchemaParams
                ),
            ),
            cast_to=ActionSchema,
        )

    async def trigger(
        self,
        action_key: str,
        *,
        connection_id: str,
        integration_id: str,
        input: Dict[str, object],
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
          connection_id: The ID of the connection to use for the action.

          integration_id: The ID of the integration to which the action belongs.

          input: The input parameters for the action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action_key:
            raise ValueError(f"Expected a non-empty value for `action_key` but received {action_key!r}")
        return await self._post(
            f"/actions/{action_key}/trigger",
            body=await async_maybe_transform({"input": input}, action_trigger_params.ActionTriggerParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "connection_id": connection_id,
                        "integration_id": integration_id,
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
        self.disable = to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = to_raw_response_wrapper(
            actions.enable,
        )
        self.schema = to_raw_response_wrapper(
            actions.schema,
        )
        self.trigger = to_raw_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self._actions.schemas)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )
        self.disable = async_to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            actions.enable,
        )
        self.schema = async_to_raw_response_wrapper(
            actions.schema,
        )
        self.trigger = async_to_raw_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self._actions.schemas)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )
        self.disable = to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = to_streamed_response_wrapper(
            actions.enable,
        )
        self.schema = to_streamed_response_wrapper(
            actions.schema,
        )
        self.trigger = to_streamed_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self._actions.schemas)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            actions.enable,
        )
        self.schema = async_to_streamed_response_wrapper(
            actions.schema,
        )
        self.trigger = async_to_streamed_response_wrapper(
            actions.trigger,
        )

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self._actions.schemas)
