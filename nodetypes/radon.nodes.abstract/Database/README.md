![](https://img.shields.io/badge/Status:-RELEASED-green)

## Database Node Type (Abstract)

Abstract node type representing a database.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Database` | `radon.nodes.abstract.Database` | 1.0.0 | `tosca.nodes.Database` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `entries`<sup>[1](#fn1)</sup> | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |

<sup name="fn1">1</sup> The name of each `Entry` must be prefixed with the name of the operation that it is associated with, e.g. "get", "get_item" and and "getItem". This enables the decomposition tool to compute the operating cost of a `Database` on the target cloud platform. The following table summarizes the supported operations for platform-specific node types derived from `Database`.

| Derived Node Type | Supported Operations |
|:---- |:-------- |
| `radon.nodes.aws.AwsDynamoDBTable` | get, put, update, delete, query, scan |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` |   | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.Triggers` | [ 0, UNBOUNDED ] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `database_endpoint` | `tosca.capabilities.Endpoint.Database` |   | [0, UNBOUNDED] |
