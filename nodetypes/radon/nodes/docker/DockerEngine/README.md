## Docker Engine Node Type

Type that represents a Docker runtime to run multiple Docker container applications on a single host.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DockerRuntime` | `radon.nodes.docker.DockerRuntime` | 1.0.0 | `tosca.nodes.Container.Runtime` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `port` | `integer` | The port value exposed by the `docker` capability | Exposed port of the Docker daemon |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `docker` | `radon.capabilities.container.DockerRuntime` | `radon.nodes.docker.DockerApplication` | [1, UNBOUNDED] |
