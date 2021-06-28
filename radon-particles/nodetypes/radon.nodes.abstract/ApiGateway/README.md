![](https://img.shields.io/badge/Status:-RELEASED-green)

## API Gateway Node Type (Abstract)

Abstract node type representing an API Gateway independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ApiGateway` | `radon.nodes.abstract.ApiGateway` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |   |   | Name of the API |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.Triggers` | [0, UNBOUNDED] |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `api_endpoint` | `radon.capabilities.Endpoint` |   | [0, UNBOUNDED] |
