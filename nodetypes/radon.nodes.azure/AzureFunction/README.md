## Azure Function Node Type (Abstract)

Abstract node type that represents an function hosted on the Azure cloud platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureFunction` | `radon.nodes.azure.AzureFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_name` | `true` | `string` |   |   | The name of the function |
| `timeout` | `true` | `integer` | `in_range: [1, 600]` | 300 | The timeout in seconds of the function is alive after the first start |
| `app_name` | `true` | `string` |   |   | The name of the Azure application |
| `app_runtime` | `false` | `string` | `valid_values: [dotnet, node, java, python, powershell]` |   | The identifier of the runtime to be used |
| `app_os_type` | `false` | `string` | `valid_values: [Windows, Linux]` |   | The OS type of the underlying infrastructure |
| `app_storage_account` | `false` | `string` |   |   | The name of the application's storage account |
| `app_resource_group` | `false` | `string` |   |   | The name of the application's resource group |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` |   |
