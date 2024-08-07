# Integrations

Types:

```python
from embedhq.types import Integration, IntegrationListResponse, IntegrationDeleteResponse
```

Methods:

- <code title="post /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">create</a>(\*\*<a href="src/embedhq/types/integration_create_params.py">params</a>) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="get /integrations/{integration}">client.integrations.<a href="./src/embedhq/resources/integrations.py">retrieve</a>(integration) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="put /integrations/{integration}">client.integrations.<a href="./src/embedhq/resources/integrations.py">update</a>(integration, \*\*<a href="src/embedhq/types/integration_update_params.py">params</a>) -> <a href="./src/embedhq/types/integration.py">Integration</a></code>
- <code title="get /integrations">client.integrations.<a href="./src/embedhq/resources/integrations.py">list</a>(\*\*<a href="src/embedhq/types/integration_list_params.py">params</a>) -> <a href="./src/embedhq/types/integration_list_response.py">IntegrationListResponse</a></code>
- <code title="delete /integrations/{integration}">client.integrations.<a href="./src/embedhq/resources/integrations.py">delete</a>(integration) -> <a href="./src/embedhq/types/integration_delete_response.py">IntegrationDeleteResponse</a></code>

# ConnectedAccounts

Types:

```python
from embedhq.types import (
    ConnectedAccount,
    ConnectedAccountListResponse,
    ConnectedAccountDeleteResponse,
)
```

Methods:

- <code title="get /connected-accounts/{connected_account_id}">client.connected_accounts.<a href="./src/embedhq/resources/connected_accounts.py">retrieve</a>(\*, connected_account_id, \*\*<a href="src/embedhq/types/connected_account_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/connected_account.py">ConnectedAccount</a></code>
- <code title="put /connected-accounts/{connected_account_id}">client.connected_accounts.<a href="./src/embedhq/resources/connected_accounts.py">update</a>(\*, connected_account_id, \*\*<a href="src/embedhq/types/connected_account_update_params.py">params</a>) -> <a href="./src/embedhq/types/connected_account.py">ConnectedAccount</a></code>
- <code title="get /connected-accounts">client.connected_accounts.<a href="./src/embedhq/resources/connected_accounts.py">list</a>(\*\*<a href="src/embedhq/types/connected_account_list_params.py">params</a>) -> <a href="./src/embedhq/types/connected_account_list_response.py">ConnectedAccountListResponse</a></code>
- <code title="delete /connected-accounts/{connected_account_id}">client.connected_accounts.<a href="./src/embedhq/resources/connected_accounts.py">delete</a>(\*, connected_account_id, \*\*<a href="src/embedhq/types/connected_account_delete_params.py">params</a>) -> <a href="./src/embedhq/types/connected_account_delete_response.py">ConnectedAccountDeleteResponse</a></code>
- <code title="post /connected-accounts">client.connected_accounts.<a href="./src/embedhq/resources/connected_accounts.py">upsert</a>(\*\*<a href="src/embedhq/types/connected_account_upsert_params.py">params</a>) -> <a href="./src/embedhq/types/connected_account.py">ConnectedAccount</a></code>

# SessionTokens

Types:

```python
from embedhq.types import SessionToken, SessionTokenListResponse, SessionTokenDeleteResponse
```

Methods:

- <code title="post /session-tokens">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">create</a>(\*\*<a href="src/embedhq/types/session_token_create_params.py">params</a>) -> <a href="./src/embedhq/types/session_token.py">SessionToken</a></code>
- <code title="get /session-tokens/{token}">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">retrieve</a>(token) -> <a href="./src/embedhq/types/session_token.py">SessionToken</a></code>
- <code title="get /session-tokens">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">list</a>(\*\*<a href="src/embedhq/types/session_token_list_params.py">params</a>) -> <a href="./src/embedhq/types/session_token_list_response.py">SessionTokenListResponse</a></code>
- <code title="delete /session-tokens/{token}">client.session_tokens.<a href="./src/embedhq/resources/session_tokens.py">delete</a>(token) -> <a href="./src/embedhq/types/session_token_delete_response.py">SessionTokenDeleteResponse</a></code>

# Providers

Types:

```python
from embedhq.types import Provider, ProviderListResponse
```

Methods:

- <code title="get /providers/{provider}">client.providers.<a href="./src/embedhq/resources/providers/providers.py">retrieve</a>(provider, \*\*<a href="src/embedhq/types/provider_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/provider.py">Provider</a></code>
- <code title="get /providers">client.providers.<a href="./src/embedhq/resources/providers/providers.py">list</a>(\*\*<a href="src/embedhq/types/provider_list_params.py">params</a>) -> <a href="./src/embedhq/types/provider_list_response.py">ProviderListResponse</a></code>

## CollectionTemplates

Types:

```python
from embedhq.types.providers import (
    CollectionTemplateRetrieveResponse,
    CollectionTemplateListResponse,
)
```

Methods:

- <code title="get /providers/{provider}/collection-templates/{collection}">client.providers.collection_templates.<a href="./src/embedhq/resources/providers/collection_templates.py">retrieve</a>(collection, \*, provider) -> <a href="./src/embedhq/types/providers/collection_template_retrieve_response.py">CollectionTemplateRetrieveResponse</a></code>
- <code title="get /providers/{provider}/collection-templates">client.providers.collection_templates.<a href="./src/embedhq/resources/providers/collection_templates.py">list</a>(provider) -> <a href="./src/embedhq/types/providers/collection_template_list_response.py">CollectionTemplateListResponse</a></code>

## ActionTemplates

Types:

```python
from embedhq.types.providers import ActionTemplateRetrieveResponse, ActionTemplateListResponse
```

Methods:

- <code title="get /providers/{provider}/action-templates/{action}">client.providers.action_templates.<a href="./src/embedhq/resources/providers/action_templates.py">retrieve</a>(action, \*, provider) -> <a href="./src/embedhq/types/providers/action_template_retrieve_response.py">ActionTemplateRetrieveResponse</a></code>
- <code title="get /providers/{provider}/action-templates">client.providers.action_templates.<a href="./src/embedhq/resources/providers/action_templates.py">list</a>(provider) -> <a href="./src/embedhq/types/providers/action_template_list_response.py">ActionTemplateListResponse</a></code>

# Collections

Types:

```python
from embedhq.types import Collection, CollectionListResponse, CollectionDeleteResponse
```

Methods:

- <code title="post /collections">client.collections.<a href="./src/embedhq/resources/collections.py">create</a>(\*\*<a href="src/embedhq/types/collection_create_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="get /collections/{collection}">client.collections.<a href="./src/embedhq/resources/collections.py">retrieve</a>(\*, collection, \*\*<a href="src/embedhq/types/collection_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="put /collections/{collection}">client.collections.<a href="./src/embedhq/resources/collections.py">update</a>(\*, collection, \*\*<a href="src/embedhq/types/collection_update_params.py">params</a>) -> <a href="./src/embedhq/types/collection.py">Collection</a></code>
- <code title="get /collections">client.collections.<a href="./src/embedhq/resources/collections.py">list</a>(\*\*<a href="src/embedhq/types/collection_list_params.py">params</a>) -> <a href="./src/embedhq/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /collections/{collection}">client.collections.<a href="./src/embedhq/resources/collections.py">delete</a>(\*, collection, \*\*<a href="src/embedhq/types/collection_delete_params.py">params</a>) -> <a href="./src/embedhq/types/collection_delete_response.py">CollectionDeleteResponse</a></code>

# Syncs

Types:

```python
from embedhq.types import Sync, SyncListResponse, SyncDeleteResponse
```

Methods:

- <code title="post /syncs">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">create</a>(\*\*<a href="src/embedhq/types/sync_create_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="get /syncs/{collection}">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">retrieve</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="put /syncs/{collection}">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">update</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_update_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="get /syncs">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">list</a>(\*\*<a href="src/embedhq/types/sync_list_params.py">params</a>) -> <a href="./src/embedhq/types/sync_list_response.py">SyncListResponse</a></code>
- <code title="delete /syncs/{collection}">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">delete</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_delete_params.py">params</a>) -> <a href="./src/embedhq/types/sync_delete_response.py">SyncDeleteResponse</a></code>
- <code title="post /syncs/{collection}/start">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">start</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_start_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="post /syncs/{collection}/stop">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">stop</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_stop_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>
- <code title="post /syncs/{collection}/trigger">client.syncs.<a href="./src/embedhq/resources/syncs/syncs.py">trigger</a>(\*, collection, \*\*<a href="src/embedhq/types/sync_trigger_params.py">params</a>) -> <a href="./src/embedhq/types/sync.py">Sync</a></code>

## Runs

Types:

```python
from embedhq.types.syncs import SyncRun, RunListResponse
```

Methods:

- <code title="get /syncs/{collection}/runs/{sync_run_id}">client.syncs.runs.<a href="./src/embedhq/resources/syncs/runs.py">retrieve</a>(\*, collection, sync_run_id, \*\*<a href="src/embedhq/types/syncs/run_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/syncs/sync_run.py">SyncRun</a></code>
- <code title="get /syncs/{collection}/runs">client.syncs.runs.<a href="./src/embedhq/resources/syncs/runs.py">list</a>(\*, collection, \*\*<a href="src/embedhq/types/syncs/run_list_params.py">params</a>) -> <a href="./src/embedhq/types/syncs/run_list_response.py">RunListResponse</a></code>

# Query

Types:

```python
from embedhq.types import QueryExecResponse, QueryMultiResponse
```

Methods:

- <code title="post /query">client.query.<a href="./src/embedhq/resources/query.py">exec</a>(\*\*<a href="src/embedhq/types/query_exec_params.py">params</a>) -> <a href="./src/embedhq/types/query_exec_response.py">QueryExecResponse</a></code>
- <code title="post /multi-query">client.query.<a href="./src/embedhq/resources/query.py">multi</a>(\*\*<a href="src/embedhq/types/query_multi_params.py">params</a>) -> <a href="./src/embedhq/types/query_multi_response.py">QueryMultiResponse</a></code>

# Actions

Types:

```python
from embedhq.types import Action, ActionListResponse, ActionDeleteResponse, ActionTriggerResponse
```

Methods:

- <code title="post /actions">client.actions.<a href="./src/embedhq/resources/actions/actions.py">create</a>(\*\*<a href="src/embedhq/types/action_create_params.py">params</a>) -> <a href="./src/embedhq/types/action.py">Action</a></code>
- <code title="get /actions/{action}">client.actions.<a href="./src/embedhq/resources/actions/actions.py">retrieve</a>(\*, action, \*\*<a href="src/embedhq/types/action_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/action.py">Action</a></code>
- <code title="put /actions/{action}">client.actions.<a href="./src/embedhq/resources/actions/actions.py">update</a>(\*, action, \*\*<a href="src/embedhq/types/action_update_params.py">params</a>) -> <a href="./src/embedhq/types/action.py">Action</a></code>
- <code title="get /actions">client.actions.<a href="./src/embedhq/resources/actions/actions.py">list</a>(\*\*<a href="src/embedhq/types/action_list_params.py">params</a>) -> <a href="./src/embedhq/types/action_list_response.py">ActionListResponse</a></code>
- <code title="delete /actions/{action}">client.actions.<a href="./src/embedhq/resources/actions/actions.py">delete</a>(\*, action, \*\*<a href="src/embedhq/types/action_delete_params.py">params</a>) -> <a href="./src/embedhq/types/action_delete_response.py">ActionDeleteResponse</a></code>
- <code title="post /actions/{action}/trigger">client.actions.<a href="./src/embedhq/resources/actions/actions.py">trigger</a>(\*, action, \*\*<a href="src/embedhq/types/action_trigger_params.py">params</a>) -> <a href="./src/embedhq/types/action_trigger_response.py">ActionTriggerResponse</a></code>

## Runs

Types:

```python
from embedhq.types.actions import ActionRun, RunListResponse
```

Methods:

- <code title="get /actions/{action}/runs/{action_run_id}">client.actions.runs.<a href="./src/embedhq/resources/actions/runs.py">retrieve</a>(\*, action, action_run_id, \*\*<a href="src/embedhq/types/actions/run_retrieve_params.py">params</a>) -> <a href="./src/embedhq/types/actions/action_run.py">ActionRun</a></code>
- <code title="get /actions/{action}/runs">client.actions.runs.<a href="./src/embedhq/resources/actions/runs.py">list</a>(\*, action, \*\*<a href="src/embedhq/types/actions/run_list_params.py">params</a>) -> <a href="./src/embedhq/types/actions/run_list_response.py">RunListResponse</a></code>

# Proxy

Types:

```python
from embedhq.types import ProxyDeleteResponse, ProxyGetResponse, ProxyPostResponse, ProxyPutResponse
```

Methods:

- <code title="delete /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">delete</a>(\*, endpoint, \*\*<a href="src/embedhq/types/proxy_delete_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_delete_response.py">ProxyDeleteResponse</a></code>
- <code title="get /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">get</a>(\*, endpoint) -> <a href="./src/embedhq/types/proxy_get_response.py">ProxyGetResponse</a></code>
- <code title="post /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">post</a>(\*, endpoint, \*\*<a href="src/embedhq/types/proxy_post_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_post_response.py">ProxyPostResponse</a></code>
- <code title="put /proxy/{endpoint}">client.proxy.<a href="./src/embedhq/resources/proxy.py">put</a>(\*, endpoint, \*\*<a href="src/embedhq/types/proxy_put_params.py">params</a>) -> <a href="./src/embedhq/types/proxy_put_response.py">ProxyPutResponse</a></code>

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

- <code title="get /webhooks/{webhook_id}/events/{webhook_event_id}">client.webhooks.events.<a href="./src/embedhq/resources/webhooks/events.py">retrieve</a>(webhook_event_id, \*, webhook_id) -> <a href="./src/embedhq/types/webhooks/webhook_event_object.py">WebhookEventObject</a></code>
- <code title="get /webhooks/{webhook_id}/events">client.webhooks.events.<a href="./src/embedhq/resources/webhooks/events.py">list</a>(webhook_id) -> <a href="./src/embedhq/types/webhooks/event_list_response.py">EventListResponse</a></code>
