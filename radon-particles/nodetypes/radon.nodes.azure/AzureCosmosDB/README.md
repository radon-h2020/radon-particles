![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Cosmos DB Node Type

A node type that represents a Cosmos DB hosted on the Azure platform

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureCosmosDB` | `radon.nodes.azure.AzureCosmosDB` | 1.0.0 | `radon.nodes.abstract.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `connection_string_setting` | `true` | `string` |   |   | The name of an app setting that contains the connection string used to connect to the Azure Cosmos DB account |
| `user` | `true` | `string` |   |   | The Azure Cosmos DB account name |
| `resource_group` | `true` | `string` |   |   | The name of the resource group |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.azure.AzureResourceTriggeredFunction` | `radon.relationships.azure.AzureCosmosDBTriggers` | [0, UNBOUNDED] |

### Notes

* Parameters added to the inputs of the `Standard` interface operations:
    * `create`: `COLLECTION_NAME`, `CONNECTION_STRING_SETTING`, `ACCOUNT_NAME`, `RESOURCE_GROUP`
