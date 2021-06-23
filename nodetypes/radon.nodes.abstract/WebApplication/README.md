![](https://img.shields.io/badge/Status:-RELEASED-green)

## Web Application Node Type (Abstract)

Abstract node type representing a web application.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `WebApplication` | `radon.nodes.abstract.WebApplication` | 1.0.0 | `tosca.nodes.WebApplication` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the web application |
| `granularity` | `false` | `string` | `valid_values: [monolithic, coarse-grained, fine-grained]` |   | Decomposition granularity |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.abstract.WebServer` | `tosca.relationships.HostedOn` | [1, 1] |
