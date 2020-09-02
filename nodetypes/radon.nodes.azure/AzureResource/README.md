![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Azure Resource Node Type (Abstract)

An abstract node type to describe a generic Azure Resource. All specific Azure Resources should derive from this type.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureResource` | `radon.nodes.azure.AzureResource` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`name`|`true`|`string`| | | The name of the resource. |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.azure.AzureFunction` | `radon.relationships.azure.Triggers` | [0, UNBOUNDED] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
  * `NAME`: taken from the `name` property.
* All type-specific Azure Resources should derive from this type.
* This type is the source of all `radon.relationships.azure.Triggers` relationships.
