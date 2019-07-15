## Display Name

This is an abstract function Node Type. It represents an abstract FaaS-hosted function independently of the underlying provider.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Function | radon.nodes.abstract.Function | 1.0.0 | tosca.nodes.Root |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `name` | `true` | `string` | N/A | Name of the function |

### Attributes

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |

### Capabilities

| Name | Type | Valid Source Types |
|:---- |:---- |:------------------ |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | N/A | `tosca.relationships.HostedOn` | N/A |

### Notes

* Arbitrary list of additional notes
* ...

---
