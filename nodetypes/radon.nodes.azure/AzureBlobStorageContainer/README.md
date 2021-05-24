![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Blob Storage Container Node Type

A node type that represents a Blob storage container hosted on the Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureBlobStorageContainer` | `radon.nodes.azure.AzureBlobStorageContainer` | 1.0.0 | `radon.nodes.abstract.ObjectStorage` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `container_name` | `true` | `string` |   |   | The name of the new Azure container |
| `resource_group_name` | `true` | `string` |   |   | The name of the existing Azure resource group  |
| `storage_account_name` | `true` | `string` |   |   | The name of the existing Azure storage account  |
| `public_access` | `false` | `string` | `valid_values: [blob, container]` | "container" | The container's level of public access  |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.azure.AzureFunction` | `radon.relationships.azure.AzureTriggers` | [0, UNBOUNDED] |
