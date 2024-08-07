# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import EmbedError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Embed",
    "AsyncEmbed",
    "Client",
    "AsyncClient",
]


class Embed(SyncAPIClient):
    integrations: resources.IntegrationsResource
    connected_accounts: resources.ConnectedAccountsResource
    session_tokens: resources.SessionTokensResource
    providers: resources.ProvidersResource
    collections: resources.CollectionsResource
    syncs: resources.SyncsResource
    query: resources.QueryResource
    actions: resources.ActionsResource
    proxy: resources.ProxyResource
    webhooks: resources.WebhooksResource
    with_raw_response: EmbedWithRawResponse
    with_streaming_response: EmbedWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Embed client instance.

        This automatically infers the `api_key` argument from the `EMBED_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("EMBED_API_KEY")
        if api_key is None:
            raise EmbedError(
                "The api_key client option must be set either by passing api_key to the client or by setting the EMBED_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("EMBED_BASE_URL")
        if base_url is None:
            base_url = f"https://api.useembed.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.integrations = resources.IntegrationsResource(self)
        self.connected_accounts = resources.ConnectedAccountsResource(self)
        self.session_tokens = resources.SessionTokensResource(self)
        self.providers = resources.ProvidersResource(self)
        self.collections = resources.CollectionsResource(self)
        self.syncs = resources.SyncsResource(self)
        self.query = resources.QueryResource(self)
        self.actions = resources.ActionsResource(self)
        self.proxy = resources.ProxyResource(self)
        self.webhooks = resources.WebhooksResource(self)
        self.with_raw_response = EmbedWithRawResponse(self)
        self.with_streaming_response = EmbedWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncEmbed(AsyncAPIClient):
    integrations: resources.AsyncIntegrationsResource
    connected_accounts: resources.AsyncConnectedAccountsResource
    session_tokens: resources.AsyncSessionTokensResource
    providers: resources.AsyncProvidersResource
    collections: resources.AsyncCollectionsResource
    syncs: resources.AsyncSyncsResource
    query: resources.AsyncQueryResource
    actions: resources.AsyncActionsResource
    proxy: resources.AsyncProxyResource
    webhooks: resources.AsyncWebhooksResource
    with_raw_response: AsyncEmbedWithRawResponse
    with_streaming_response: AsyncEmbedWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Embed client instance.

        This automatically infers the `api_key` argument from the `EMBED_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("EMBED_API_KEY")
        if api_key is None:
            raise EmbedError(
                "The api_key client option must be set either by passing api_key to the client or by setting the EMBED_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("EMBED_BASE_URL")
        if base_url is None:
            base_url = f"https://api.useembed.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.integrations = resources.AsyncIntegrationsResource(self)
        self.connected_accounts = resources.AsyncConnectedAccountsResource(self)
        self.session_tokens = resources.AsyncSessionTokensResource(self)
        self.providers = resources.AsyncProvidersResource(self)
        self.collections = resources.AsyncCollectionsResource(self)
        self.syncs = resources.AsyncSyncsResource(self)
        self.query = resources.AsyncQueryResource(self)
        self.actions = resources.AsyncActionsResource(self)
        self.proxy = resources.AsyncProxyResource(self)
        self.webhooks = resources.AsyncWebhooksResource(self)
        self.with_raw_response = AsyncEmbedWithRawResponse(self)
        self.with_streaming_response = AsyncEmbedWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class EmbedWithRawResponse:
    def __init__(self, client: Embed) -> None:
        self.integrations = resources.IntegrationsResourceWithRawResponse(client.integrations)
        self.connected_accounts = resources.ConnectedAccountsResourceWithRawResponse(client.connected_accounts)
        self.session_tokens = resources.SessionTokensResourceWithRawResponse(client.session_tokens)
        self.providers = resources.ProvidersResourceWithRawResponse(client.providers)
        self.collections = resources.CollectionsResourceWithRawResponse(client.collections)
        self.syncs = resources.SyncsResourceWithRawResponse(client.syncs)
        self.query = resources.QueryResourceWithRawResponse(client.query)
        self.actions = resources.ActionsResourceWithRawResponse(client.actions)
        self.proxy = resources.ProxyResourceWithRawResponse(client.proxy)
        self.webhooks = resources.WebhooksResourceWithRawResponse(client.webhooks)


class AsyncEmbedWithRawResponse:
    def __init__(self, client: AsyncEmbed) -> None:
        self.integrations = resources.AsyncIntegrationsResourceWithRawResponse(client.integrations)
        self.connected_accounts = resources.AsyncConnectedAccountsResourceWithRawResponse(client.connected_accounts)
        self.session_tokens = resources.AsyncSessionTokensResourceWithRawResponse(client.session_tokens)
        self.providers = resources.AsyncProvidersResourceWithRawResponse(client.providers)
        self.collections = resources.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.syncs = resources.AsyncSyncsResourceWithRawResponse(client.syncs)
        self.query = resources.AsyncQueryResourceWithRawResponse(client.query)
        self.actions = resources.AsyncActionsResourceWithRawResponse(client.actions)
        self.proxy = resources.AsyncProxyResourceWithRawResponse(client.proxy)
        self.webhooks = resources.AsyncWebhooksResourceWithRawResponse(client.webhooks)


class EmbedWithStreamedResponse:
    def __init__(self, client: Embed) -> None:
        self.integrations = resources.IntegrationsResourceWithStreamingResponse(client.integrations)
        self.connected_accounts = resources.ConnectedAccountsResourceWithStreamingResponse(client.connected_accounts)
        self.session_tokens = resources.SessionTokensResourceWithStreamingResponse(client.session_tokens)
        self.providers = resources.ProvidersResourceWithStreamingResponse(client.providers)
        self.collections = resources.CollectionsResourceWithStreamingResponse(client.collections)
        self.syncs = resources.SyncsResourceWithStreamingResponse(client.syncs)
        self.query = resources.QueryResourceWithStreamingResponse(client.query)
        self.actions = resources.ActionsResourceWithStreamingResponse(client.actions)
        self.proxy = resources.ProxyResourceWithStreamingResponse(client.proxy)
        self.webhooks = resources.WebhooksResourceWithStreamingResponse(client.webhooks)


class AsyncEmbedWithStreamedResponse:
    def __init__(self, client: AsyncEmbed) -> None:
        self.integrations = resources.AsyncIntegrationsResourceWithStreamingResponse(client.integrations)
        self.connected_accounts = resources.AsyncConnectedAccountsResourceWithStreamingResponse(
            client.connected_accounts
        )
        self.session_tokens = resources.AsyncSessionTokensResourceWithStreamingResponse(client.session_tokens)
        self.providers = resources.AsyncProvidersResourceWithStreamingResponse(client.providers)
        self.collections = resources.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.syncs = resources.AsyncSyncsResourceWithStreamingResponse(client.syncs)
        self.query = resources.AsyncQueryResourceWithStreamingResponse(client.query)
        self.actions = resources.AsyncActionsResourceWithStreamingResponse(client.actions)
        self.proxy = resources.AsyncProxyResourceWithStreamingResponse(client.proxy)
        self.webhooks = resources.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)


Client = Embed

AsyncClient = AsyncEmbed
