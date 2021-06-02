![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Function Node Type

A node type that represents a function app hosted on the Azure platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureFunction` | `radon.nodes.azure.AzureFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_app_name` | `true` | `string` |   |   | The name of the new Azure function app |
| `resource_group_name` | `true` | `string` |   |   | The name of the existing Azure resource group |
| `storage_account_name` | `true` | `string` |   |   | The name of the existing Azure storage account |
| `region` | `true` | `string` |   |   | The identifier for Azure region in which resources are/will be deployed |
| `functions_version` | `false` | `integer` | `valid_values: [2, 3]` | 3 | The version of the Azure function app |
| `os_type` | `true` | `string` | `valid_values: [Windows, Linux]` |   | The Azure function app OS type |
| `runtime_type` | `true` | `string` | `valid_values: [dotnet, node, java, python, powershell]` |   | The Azure function runtime type |
| `runtime_version` | `true` | `float` |   |   | The version of the Azure functions runtime stack |
| `zip_file` | `true` | `string` |   |   | The path to the function zip file |
| `build_remote` | `false` | `boolean` |   | true | The option to enable remote build during deployment |
| `timeout` | `false` | `integer` | `in_range: [1, 600]` | 300 | The timeout in seconds for checking the status of deployment |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` | [1, 1] |
