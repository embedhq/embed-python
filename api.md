# Integrations

Types:

```python
from embedhq.types import Integration, IntegrationListResponse
```

Methods:

- <code title="post /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">create</a>(\*\*<a href="src/embedhq/types/integration_create_params.py">params</a>) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="get /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">list</a>(\*\*<a href="src/embedhq/types/integration_list_params.py">params</a>) -> <a href="./src/embedhq/types/integration_list_response.py">IntegrationListResponse</a></code>

# Providers

Types:

```python
from embedhq.types import Provider, ProviderListResponse
```

Methods:

- <code title="get /providers">client.providers.<a href="./src/embedhq/resources/providers.py">list</a>(\*\*<a href="src/embedhq/types/provider_list_params.py">params</a>) -> <a href="./src/embedhq/types/provider_list_response.py">ProviderListResponse</a></code>

# Collections

Types:

```python
from embedhq.types import Collection, CollectionListResponse
```

Methods:

- <code title="get /collections">client.collections.<a href="./src/embedhq/resources/collections/collections.py">list</a>(\*\*<a href="src/embedhq/types/collection_list_params.py">params</a>) -> <a href="./src/embedhq/types/collection_list_response.py">CollectionListResponse</a></code>

# Syncs

Types:

```python
from embedhq.types import Sync, SyncListResponse
```

Methods:

- <code title="get /syncs">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">list</a>(\*\*<a href="src/embedhq/types/sync_list_params.py">params</a>) -> <a href="./src/embedhq/types/sync_list_response.py">SyncListResponse</a></code>

## Runs

Types:

```python
from embedhq.types.syncs import SyncRun
```

# Actions

Types:

```python
from embedhq.types import Action, ActionListResponse
```

Methods:

- <code title="get /actions">client.actions.<a href="./src/embedhq/resources/actions/actions.py">list</a>(\*\*<a href="src/embedhq/types/action_list_params.py">params</a>) -> <a href="./src/embedhq/types/action_list_response.py">ActionListResponse</a></code>

## Runs

Types:

```python
from embedhq.types.actions import ActionRun
```

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
from embedhq.types import Webhook, WebhookListResponse, WebhookDeleteResponse
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/embedhq/types/webhook_create_params.py">params</a>) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="put /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">update</a>(webhook_id, \*\*<a href="src/embedhq/types/webhook_update_params.py">params</a>) -> <a href="./src/embedhq/types/webhook.py">Webhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">list</a>() -> <a href="./src/embedhq/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhook_id}">client.webhooks.<a href="./src/embedhq/resources/webhooks/webhooks.py">delete</a>(webhook_id) -> <a href="./src/embedhq/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>

## Events

Types:

```python
from embedhq.types.webhooks import WebhookEventObject, EventListResponse
```

Methods:

- <code title="get /webhooks/{webhook_id}/events">client.webhooks.events.<a href="./src/embedhq/resources/webhooks/events.py">list</a>(webhook_id) -> <a href="./src/embedhq/types/webhooks/event_list_response.py">EventListResponse</a></code>
