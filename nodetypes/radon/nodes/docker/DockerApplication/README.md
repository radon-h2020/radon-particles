## Docker Application

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DockerApplication` | `radon.nodes.docker.DockerApplication` | 1.0.0 | `tosca.nodes.Container.Application` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `radon.capabilities.container.DockerRuntime` | N/A | `tosca.relationships.HostedOn` | [1,1] | 

### Notes

* An `image` artifact can be supplied of type `radon.artifacts.docker.DockerImage` in the node template

---