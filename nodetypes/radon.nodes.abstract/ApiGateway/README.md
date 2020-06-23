## API Gateway Node Type (Abstract)

Abstract node type representing an API Gateway independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ApiGateway` | `radon.nodes.abstract.ApiGateway` | 1.0.0 | `tosca.nodes.Root` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.abstract.CloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.abstract.Function` | `radon.relationships.abstract.Triggers` | [0, UNBOUNDED] |
