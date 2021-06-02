![](https://img.shields.io/badge/Status:-RELEASED-green)

## Data Pipeline Node Type (Abstract)

Abstract node type representing a data pipeline.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DataPipeline` | `radon.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `name` | `true` | `string` |   | Name of the data pipeline |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` |   | `tosca.relationships.HostedOn` | [1, 1] |
