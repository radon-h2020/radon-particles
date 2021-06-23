![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Resource-Triggered Function Node Type

A node type that represents an Azure function which is triggered by an internal resource. This includes:
[Blob storage](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-storage-blob),
[Cosmos DB](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-documentdb),
[Event Grid](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-event-grid),
[Event Hubs](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-event-hubs),
[Microsoft Graph events](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-microsoft-graph),
[Queue storage](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-storage-queue), and
[Service Bus](https://docs.microsoft.com/en-in/azure/azure-functions/functions-bindings-service-bus).

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureResourceTriggeredFunction` | `radon.nodes.azure.AzureResourceTriggeredFunction` | 1.0.0 | `radon.nodes.azure.AzureFunction` |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `radon.capabilities.Invocable` | `[ radon.nodes.azure.AzureBlobStorageContainer, radon.nodes.azure.AzureCosmosDB ]` | [1, 1] |

### Notes

* To connect to each triggering resource, use the associated resource-specific relationship type.
* The deployment of an ResourceTriggeredAzureFunction is performed by the relationship.
