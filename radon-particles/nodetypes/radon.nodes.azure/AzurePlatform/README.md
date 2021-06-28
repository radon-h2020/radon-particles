![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Platform Node Type

A node type that represents the Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzurePlatform` | `radon.nodes.azure.AzurePlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `username` | `true` | `string` |   |   | The Azure username used for authentication |
| `password` | `true` | `string` |   |   | The Azure password used for authentication |
| `region` | `true` | `string` |   |   | The identifier for Azure region in which resources are/will be deployed |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[radon.nodes.azure.AzureResourceGroup, radon.nodes.azure.AzureStorageAccount, radon.nodes.azure.AzureBlobStorageContainer, radon.nodes.azure.AzureCosmosDB, radon.nodes.azure.AzureFunction, radon.nodes.azure.AzureResourceTriggeredFunction, radon.nodes.azure.AzureHttpTriggeredFunction]` | [1, UNBOUNDED] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
    * `username`
    * `password`
