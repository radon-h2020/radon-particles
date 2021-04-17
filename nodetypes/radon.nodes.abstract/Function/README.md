![](https://img.shields.io/badge/Status:-RELEASED-green)

## Function Node Type (Abstract)

Abstract node type representing a serverless function independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Function` | `radon.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the function |
| `entries` | `false` | `map: radon.datatypes.Entry` | `length: 1` |   | Map of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` |   | `radon.relationships.Triggers` | [0, UNBOUNDED] |
| `endpoint` | `tosca.capabilities.Endpoint` |   | `radon.relationships.ConnectsTo` | [0, UNBOUNDED] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `radon.capabilities.Invocable` |   | [0, UNBOUNDED] |
