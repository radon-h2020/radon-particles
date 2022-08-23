![](https://img.shields.io/badge/Status:-RELEASED-green)

## Container Application Node Type (Abstract)

Abstract node type representing a container application.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ContainerApplication` | `radon.nodes.abstract.ContainerApplication` | 1.0.0 | `tosca.nodes.Container.Application` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the container application |
| `granularity` | `false` | `string` | `valid_values: [coarse-grained, fine-grained]` |   | Decomposition granularity |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |
| `core_elements` | `false` | `list: string` |   |   | List of core elements |
| `global_utilities` | `false` | `list: string` |   |   | List of global utilities |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.abstract.ContainerRuntime` | `tosca.relationships.HostedOn` | [1, 1] |
| `storage` | `tosca.capabilities.Storage` |   |   | [0, 1] |
| `network` | `tosca.capabilities.Endpoint` |   |   | [0, 1] |
