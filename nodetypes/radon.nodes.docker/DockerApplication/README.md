![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Docker Application Node Type

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DockerApplication` | `radon.nodes.docker.DockerApplication` | 1.0.0 | `radon.nodes.abstract.ContainerApplication` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `radon.capabilities.container.DockerRuntime` | `radon.nodes.abstract.ContainerRuntime` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* An `image` artifact can be supplied of type `radon.artifacts.docker.DockerImage` in the node template
