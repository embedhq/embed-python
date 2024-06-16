# Integrations

Types:

```python
from embedhq.types import (
    Integration,
    IntegrationListResponse,
    IntegrationDeleteResponse,
    IntegrationDisableResponse,
)
```

Methods:

- <code title="post /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">create</a>(\*\*<a href="src/embedhq/types/integration_create_params.py">params</a>) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="get /integrations/{integration_id}">client.integrations.<a href="./src/embedhq/resources/integrations.py">retrieve</a>(integration_id) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="put /integrations/{integration_id}">client.integrations.<a href="./src/embedhq/resources/integrations.py">update</a>(integration_id, \*\*<a href="src/embedhq/types/integration_update_params.py">params</a>) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="get /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">list</a>(\*\*<a href="src/embedhq/types/integration_list_params.py">params</a>) -> <a href="./src/embedhq/types/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="delete /integrations/{integration_id}">client.integrations.<a href="./src/embedhq/resources/integrations.py">delete</a>(integration_id) -> <a href="./src/embedhq/types/integration_delete_response.py">IntegrationDeleteResponse</a></code>
- <code title="post /integrations/{integration_id}/disable">client.integrations.<a href="./src/embedhq/resources/integrations.py">disable</a>(integration_id) -> <a href="./src/embedhq/types/integration_disable_response.py">IntegrationDisableResponse</a></code>
- <code title="post /integrations/{integration_id}/enable">client.integrations.<a href="./src/embedhq/resources/integrations.py">enable</a>(integration_id) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>

# Connections

Types:

```python
from embedhq.types import (
    Connection,
    ConnectionUpdateResponse,
    ConnectionListResponse,
    ConnectionDeleteResponse,
)
```

Methods:

- <code title="get /connections/{connection_id}">client.connections.<a href="./src/embedhq/resources/connections.py">retrieve</a>(connection_id, \*\*<a href="src/embedhq/types/connection_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/connection.py">Connection</a></code>
- <code title="put /connections/{connection_id}">client.connections.<a href="./src/embedhq/resources/connections.py">update</a>(connection_id, \*\*<a href="src/embedhq/types/connection_update_params.py">params</a>) -> <a href="./src/embedhq/types/connection_update_response.py">ConnectionUpdateResponse</a></code>
- <code title="get /connections">client.connections.<a href="./src/embedhq/resources/connections.py">list</a>(\*\*<a href="src/embedhq/types/connection_list_params.py">params</a>) -> <a href="./src/embedhq/types/connection_list_response.py">ConnectionListResponse</a></code>
- <code title="delete /connections/{connection_id}">client.connections.<a href="./src/embedhq/resources/connections.py">delete</a>(connection_id, \*\*<a href="src/embedhq/types/connection_delete_params.py">params</a>) -> <a href="./src/embedhq/types/connection_delete_response.py">ConnectionDeleteResponse</a></code>
- <code title="post /connections">client.connections.<a href="./src/embedhq/resources/connections.py">upsert</a>(\*\*<a href="src/embedhq/types/connection_upsert_params.py">params</a>) -> <a href="./src/embedhq/types/connection.py">Connection</a></code>

# SessionTokens

Types:

```python
from embedhq.types import SessionToken, SessionTokenListResponse, SessionTokenDeleteResponse
```

Methods:

- <code title="post /session-tokens">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">create</a>(\*\*<a href="src/embedhq/types/session_token_create_params.py">params</a>) -> <a href="./src/embedhq/types/session_token.py">SessionToken</a></code>
- <code title="get /session-tokens/{token}">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">retrieve</a>(token) -> <a href="./src/embedhq/types/session_token.py">SessionToken</a></code>
- <code title="get /session-tokens">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">list</a>() -> <a href="./src/embedhq/types/session_token_list_response.py">SessionTokenListResponse</a></code>
- <code title="delete /session-tokens/{token}">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">delete</a>(token) -> <a href="./src/embedhq/types/session_token_delete_response.py">SessionTokenDeleteResponse</a></code>

# Providers

Types:

```python
from embedhq.types import Provider, ProviderListResponse
```

Methods:

- <code title="get /providers/{provider_key}">client.providers.<a href="./src/embedhq/resources/providers.py">retrieve</a>(provider_key) -> <a href="./src/embedhq/types/provider.py">Provider</a></code>
- <code title="get /providers">client.providers.<a href="./src/embedhq/resources/providers.py">list</a>() -> <a href="./src/embedhq/types/provider_list_response.py">ProviderListResponse</a></code>

# Collections

Types:

```python
from embedhq.types import (
    Collection,
    CollectionListResponse,
    CollectionDisableResponse,
    CollectionQueryResponse,
)
```

Methods:

- <code title="get /collections/{collection_key}">client.collections.<a href="./src/embedhq/resources/collections/collections.py">retrieve</a>(collection_key, \*\*<a href="src/embedhq/types/collection_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="put /collections/{collection_key}">client.collections.<a href="./src/embedhq/resources/collections/collections.py">update</a>(collection_key, \*\*<a href="src/embedhq/types/collection_update_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="get /collections">client.collections.<a href="./src/embedhq/resources/collections/collections.py">list</a>(\*\*<a href="src/embedhq/types/collection_list_params.py">params</a>) -> <a href="./src/embedhq/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="post /collections/{collection_key}/disable">client.collections.<a href="./src/embedhq/resources/collections/collections.py">disable</a>(collection_key, \*\*<a href="src/embedhq/types/collection_disable_params.py">params</a>) -> <a href="./src/embedhq/types/collection_disable_response.py">CollectionDisableResponse</a></code>
- <code title="post /collections/{collection_key}/enable">client.collections.<a href="./src/embedhq/resources/collections/collections.py">enable</a>(collection_key, \*\*<a href="src/embedhq/types/collection_enable_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="post /collections/{collection_key}/query">client.collections.<a href="./src/embedhq/resources/collections/collections.py">query</a>(collection_key, \*\*<a href="src/embedhq/types/collection_query_params.py">params</a>) -> <a href="./src/embedhq/types/collection_query_response.py">CollectionQueryResponse</a></code>

## Schemas

Types:

```python
from embedhq.types.collections import CollectionSchema, SchemaListResponse
```

Methods:

- <code title="get /collections/{collection_key}/schema">client.collections.schemas.<a href="./src/embedhq/resources/collections/schemas.py">retrieve</a>(collection_key, \*\*<a href="src/embedhq/types/collections/schema_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/collections/collection_schema.py">CollectionSchema</a></code>
- <code title="get /collections/schemas">client.collections.schemas.<a href="./src/embedhq/resources/collections/schemas.py">list</a>(\*\*<a href="src/embedhq/types/collections/schema_list_params.py">params</a>) -> <a href="./src/embedhq/types/collections/schema_list_response.py">SchemaListResponse</a></code>

# Syncs

Types:

```python
from embedhq.types import Sync, SyncListResponse
```

Methods:

- <code title="get /syncs/{collection_key}">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">retrieve</a>(collection_key, \*\*<a href="src/embedhq/types/sync_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="put /syncs/{collection_key}">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">update</a>(collection_key, \*\*<a href="src/embedhq/types/sync_update_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="get /syncs">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">list</a>(\*\*<a href="src/embedhq/types/sync_list_params.py">params</a>) -> <a href="./src/embedhq/types/sync_list_response.py">SyncListResponse</a></code>
- <code title="post /syncs/{collection_key}/start">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">start</a>(collection_key, \*\*<a href="src/embedhq/types/sync_start_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="post /syncs/{collection_key}/stop">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">stop</a>(collection_key, \*\*<a href="src/embedhq/types/sync_stop_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="post /syncs/{collection_key}/trigger">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">trigger</a>(collection_key, \*\*<a href="src/embedhq/types/sync_trigger_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>

## Runs

Types:

```python
from embedhq.types.syncs import SyncRun, RunListResponse
```

Methods:

- <code title="get /syncs/{collection_key}/runs/{run_id}">client.syncs.runs.<a href="./src/embedhq/resources/syncs/runs.py">retrieve</a>(run_id, \*, collection_key, \*\*<a href="src/embedhq/types/syncs/run_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/syncs/sync_run.py">SyncRun</a></code>
- <code title="get /syncs/{collection_key}/runs">client.syncs.runs.<a href="./src/embedhq/resources/syncs/runs.py">list</a>(collection_key, \*\*<a href="src/embedhq/types/syncs/run_list_params.py">params</a>) -> <a href="./src/embedhq/types/syncs/run_list_response.py">RunListResponse</a></code>

# Actions

Types:

```python
from embedhq.types import Action, ActionListResponse, ActionDisableResponse, ActionTriggerResponse
```

Methods:

- <code title="get /actions/{action_key}">client.actions.<a href="./src/embedhq/resources/actions/actions.py">retrieve</a>(action_key, \*\*<a href="src/embedhq/types/action_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/action.py">Action</a></code>
- <code title="get /actions">client.actions.<a href="./src/embedhq/resources/actions/actions.py">list</a>(\*\*<a href="src/embedhq/types/action_list_params.py">params</a>) -> <a href="./src/embedhq/types/action_list_response.py">ActionListResponse</a></code>
- <code title="post /actions/{action_key}/disable">client.actions.<a href="./src/embedhq/resources/actions/actions.py">disable</a>(action_key, \*\*<a href="src/embedhq/types/action_disable_params.py">params</a>) -> <a href="./src/embedhq/types/action_disable_response.py">ActionDisableResponse</a></code>
- <code title="post /actions/{action_key}/enable">client.actions.<a href="./src/embedhq/resources/actions/actions.py">enable</a>(action_key, \*\*<a href="src/embedhq/types/action_enable_params.py">params</a>) -> <a href="./src/embedhq/types/action.py">Action</a></code>
- <code title="get /actions/{action_key}/schema">client.actions.<a href="./src/embedhq/resources/actions/actions.py">schema</a>(action_key, \*\*<a href="src/embedhq/types/action_schema_params.py">params</a>) -> <a href="./src/embedhq/types/actions/action_schema.py">ActionSchema</a></code>
- <code title="post /actions/{action_key}/trigger">client.actions.<a href="./src/embedhq/resources/actions/actions.py">trigger</a>(action_key, \*\*<a href="src/embedhq/types/action_trigger_params.py">params</a>) -> <a href="./src/embedhq/types/action_trigger_response.py">ActionTriggerResponse</a></code>

## Schemas

Types:

```python
from embedhq.types.actions import ActionSchema, SchemaListResponse
```

Methods:

- <code title="get /actions/{action_key}/schema">client.actions.schemas.<a href="./src/embedhq/resources/actions/schemas.py">retrieve</a>(action_key, \*\*<a href="src/embedhq/types/actions/schema_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/actions/action_schema.py">ActionSchema</a></code>
- <code title="get /actions/schemas">client.actions.schemas.<a href="./src/embedhq/resources/actions/schemas.py">list</a>(\*\*<a href="src/embedhq/types/actions/schema_list_params.py">params</a>) -> <a href="./src/embedhq/types/actions/schema_list_response.py">SchemaListResponse</a></code>

# Proxy

Types:

```python
from embedhq.types import ProxyDeleteResponse, ProxyGetResponse, ProxyPostResponse, ProxyPutResponse
```

Methods:

- <code title="delete /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">delete</a>(endpoint, \*\*<a href="src/embedhq/types/proxy_delete_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_delete_response.py">ProxyDeleteResponse</a></code>
- <code title="get /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">get</a>(endpoint) -> <a href="./src/embedhq/types/proxy_get_response.py">ProxyGetResponse</a></code>
- <code title="post /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">post</a>(endpoint, \*\*<a href="src/embedhq/types/proxy_post_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_post_response.py">ProxyPostResponse</a></code>
- <code title="put /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">put</a>(endpoint, \*\*<a href="src/embedhq/types/proxy_put_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_put_response.py">ProxyPutResponse</a></code>

# Webhooks

Types:

```python
from embedhq.types import (
    Webhook,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookDisableResponse,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/embedhq/types/webhook_create_params.py">params</a>) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="put /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">update</a>(webhook_id, \*\*<a href="src/embedhq/types/webhook_update_params.py">params</a>) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">list</a>() -> <a href="./src/embedhq/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">delete</a>(webhook_id) -> <a href="./src/embedhq/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="post /webhooks/{webhook_id}/disable">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">disable</a>(webhook_id) -> <a href="./src/embedhq/types/webhook_disable_response.py">WebhookDisableResponse</a></code>
- <code title="post /webhooks/{webhook_id}/enable">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">enable</a>(webhook_id) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>

## Events

Types:

```python
from embedhq.types.webhooks import WebhookEventObject, EventListResponse
```

Methods:

- <code title="get /webhooks/{webhook_id}/events/{event_id}">client.webhooks.events.<a href="./src/embedhq/resources/webhooks/events.py">retrieve</a>(event_id, \*, webhook_id) -> <a href="./src/embedhq/types/webhooks/webhook_event_object.py">WebhookEventObject</a></code>
- <code title="get /webhooks/{webhook_id}/events">client.webhooks.events.<a href="./src/embedhq/resources/webhooks/events.py">list</a>(webhook_id) -> <a href="./src/embedhq/types/webhooks/event_list_response.py">EventListResponse</a></code>
