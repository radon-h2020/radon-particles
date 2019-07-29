## Goolge Cloud Resource

An abstract node type to describe a generic Google Cloud Resource. All specific Google Cloud Resources should derive from this type.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudResource` | `node_types.radon.nodes.google.GoogleCloudResource` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`name`|`true`|`string`|N/A|N/A| The name of the resource |


### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `HostedOn` | [1,1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.google.CloudFunctio` | `radon.relationships.google.Triggers` | [0,UNBOUNDED] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
  * `NAME`: taken from the `name` property.
* All type-specific Google Cloud Resources should derive from this type.
* This type is the source of the `radon.relationships.google.Triggers` relationship.

---