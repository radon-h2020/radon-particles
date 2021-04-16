![](https://img.shields.io/badge/Status:-RELEASED-green)

## Database Node Type (Abstract)

Abstract node type representing a database.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Database` | `radon.nodes.abstract.Database` | 1.0.0 | `tosca.nodes.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` |   | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.Triggers` | [ 0, UNBOUNDED ] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `database_endpoint` | `tosca.capabilities.Endpoint.Database` |   | [0, UNBOUNDED] |
