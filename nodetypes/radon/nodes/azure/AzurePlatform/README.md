## Azure Platform Node Type

This is Node Type represents the Azure cloud platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzurePlatform` | `radon.nodes.azure.AzurePlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`user_name`| `false` | `string` |   |   | The user name used for authentication. |
|`password`|`false`|`string`| | | The password used for authentication. |
|`region`|`false`|`string`| | | The region in which resources are/will be deployed. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`|`tosca.capabilities.Container`| `[radon.nodes.azure.AzureFunction, radon.nodes.azure.AzureResource]`| [0, UNBOUNDED]|

### Notes

* Parameters added to the inputs of the `Standard` interface:
    * `USER_NAME`
    * `PASSWORD`
