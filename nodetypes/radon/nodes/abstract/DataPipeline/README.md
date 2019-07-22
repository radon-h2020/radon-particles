## Data Pipeline

Abstract data pipeline type.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `DataPipeline` | `radon.nodes.abstract.Function` | 1.0.0 | `tosca.nodes.Root` |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `name` | `true` | `string` | N/A | Name of the data pipeline |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | N/A | `tosca.relationships.HostedOn` | N/A |

---