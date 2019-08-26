## Cloud Platform Node Type (Abstract)

Abstract cloud platform type representing an abstract, provider-managed platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `CloudPlatform` | `radon.nodes.abstract.CloudPlatform` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `name` | `false` | `string` |   | Name of the cloud platform |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` |   |   |   |
