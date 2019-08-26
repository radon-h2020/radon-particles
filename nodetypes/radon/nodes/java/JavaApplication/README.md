## Java Application Node Type

An abstract type that defines a Java application

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `JavaApplication` | `radon.nodes.java.JavaApplication` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `radon.capabilities.container.JavaRuntime` | `tosca.nodes.Compute` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes:

* A `deployment_package` artifact can be supplied of type `radon.artifacts.archive.JAR` in the node template.
