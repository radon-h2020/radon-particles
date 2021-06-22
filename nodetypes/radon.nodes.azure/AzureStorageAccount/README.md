![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Storage Account Node Type

A node type that represents a storage account hosted on the Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureStorageAccount` | `radon.nodes.azure.AzureStorageAccount` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `storage_account_name` | `true` | `string` |   |   | The name of the new Azure storage account |
| `resource_group_name` | `true` | `string` |   |   | The name of the existing Azure resource group |
| `region` | `true` | `string` |   |   | The identifier for Azure region in which resources are/will be deployed |
| `account_type` | `true` | `string` |   |   | The type of Azure storage account |
| `access_tier` | `true` | `string` |   |   | The access tier for this storage account |
| `storage_kind` | `true` | `string` |   |   | The kind of Azure storage |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |
