## Cloud Platform Node Type (Abstract)

Abstract node type representing a provider-managed cloud platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `CloudPlatform` | `radon.nodes.abstract.CloudPlatform` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the cloud platform |

### Capabilities
| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[radon.nodes.abstract.Function, radon.nodes.abstract.ObjectStorage]` | [1, UNBOUNDED] |
