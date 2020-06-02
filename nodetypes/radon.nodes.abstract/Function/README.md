## Function Node Type (Abstract)

Abstract node type representing a serverless function independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Function` | `radon.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the function |
| `environment` | `false` | `map: string` |   |   | Map of environment variables |
| `entries` | `false` | `radon.datatypes.function.Entries` |   |   | Set of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `endpoint` | `tosca.capabilities.Endpoint` |   | `radon.relationships.abstract.ConnectsTo` | [0, UNBOUNDED] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `radon.capabilities.Invocable` |   | [0, UNBOUNDED] |
