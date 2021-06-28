![](https://img.shields.io/badge/Status:-RELEASED-green)

## Service Node Type (Abstract)

Abstract node type representing a third-party service.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Service` | `radon.nodes.abstract.Service` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the service |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `service_endpoint` | `radon.capabilities.Endpoint` |   | [1, UNBOUNDED] |
