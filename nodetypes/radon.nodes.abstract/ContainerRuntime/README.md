![](https://img.shields.io/badge/Status:-RELEASED-green)

## Container Runtime Node Type (Abstract)

Abstract node type representing a container runtime.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ContainerRuntime` | `radon.nodes.abstract.ContainerRuntime` | 1.0.0 | `tosca.nodes.Container.Runtime` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the container runtime |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Compute` | `[radon.nodes.abstract.ContainerApplication]` | [1, UNBOUNDED] |
