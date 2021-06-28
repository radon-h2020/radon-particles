![](https://img.shields.io/badge/Status:-RELEASED-green)

## Workload Node Type (Abstract)

Abstract node type representing a workload in general.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Workload` | `radon.nodes.abstract.Workload` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the workload |
| `entries` | `false` | `map: radon.datatypes.Entry` | `length: 1` |   | Map of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `invoker` | `radon.capabilities.Invocable` |   | `radon.relationships.Triggers` | [0, UNBOUNDED] |
| `endpoint` | `tosca.capabilities.Endpoint` |   | `radon.relationships.ConnectsTo` | [0, UNBOUNDED] |
