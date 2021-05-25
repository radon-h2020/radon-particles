![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Resource Group Node Type

A node type that represents a resource group hosted on the Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureResourceGroup` | `radon.nodes.azure.AzureResourceGroup` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `resource_group_name` | `true` | `string` |   |   | The name of the new Azure resource group |
| `region` | `true` | `string` |   |   | The identifier for Azure region in which resources are/will be deployed |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |
