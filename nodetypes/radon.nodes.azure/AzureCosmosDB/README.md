![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Cosmos DB Node Type

A node type that represents a Cosmos DB hosted by the Azure platform

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureCosmosDB` | `radon.nodes.azure.AzureCosmosDB` | 1.0.0 | `radon.nodes.azure.AzureResource` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `collection_name` | `true` | `string`|   |   | The name of the collection. |
| `connection_string_setting` | `true` | `string` |   |   | The name of an app setting that contains the connection string used to connect to the Azure Cosmos DB account. |
| `account_name` | `true` | `string` |  |   | The Azure Cosmos account name. |
| `resource_group` | `true` | `string` |   |   | The name of the resource group. |

### Notes

* Parameters added to the inputs of the `Standard` interface operations:
    * `create`: `COLLECTION_NAME`, `CONNECTION_STRING_SETTING`, `ACCOUNT_NAME`, `RESOURCE_GROUP`
