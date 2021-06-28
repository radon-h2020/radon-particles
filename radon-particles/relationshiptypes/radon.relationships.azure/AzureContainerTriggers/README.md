![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Container Triggers Relationship

Azure-specific relationship type representing AzureContainer-to-AzureFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureContainerTriggers` | `radon.relationships.azure.AzureContainerTriggers` | 1.0.0 | `radon.relationships.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `event_subscription_name` | `true` | `string` |   |   | The name of the new Azure event subscription trigger |
| `event_types` | `false` | `string` |   | "Microsoft.Storage.BlobCreated" | A space-separated list of event types |
| `event_ttl` | `false` | `integer` | `in_range: [1, 1440]` | 1440 | The event time to live (in minutes) |
| `may_delivery_attempts` | `false` | `integer` | `in_range: [1, 30]` |  30 | The maximum number of delivery attempts |
| `resource_group_name` | `true` | `string` |   |   | The name of the existing Azure resource group |
| `storage_account_name` | `true` | `string` |   |   | The name of the existing Azure storage account |
| `container_name` | `true` | `string` |   |   | The name of the existing Azure container to set up trigger for |
| `function_app_name` | `true` | `string` |   |   | The name of the existing Azure function app |
| `function_name` | `true` | `string` |   |   | The name of the existing Azure function to set up trigger for |

### Notes

* A template of this type should provide implementation artifacts that deploy the Azure Function specified at the `TARGET` side.
