## Function Node Type (Abstract)

Abstract function type representing a FaaS-hosted function independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Function` | `radon.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `name` | `true` | `string` |   | Name of the function |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` |   | `tosca.relationships.HostedOn` |   |

### Notes

* A `deployment_package` artifact can be supplied of type `radon.artifacts.archive.Zip` in the node template.
