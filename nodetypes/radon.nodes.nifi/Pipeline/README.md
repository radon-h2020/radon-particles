## NiFi Pipeline Node Type

A type representing a data pipeline hosted on Apache NiFi.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Pipeline` | `radon.nodes.nifi.Pipeline` | 1.0.0 | `radon.nodes.abstract.DataPipeline` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `id` | `string` |   | Unique ID of the pipeline |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`connect`| `tosca.capabilities.Endpoint`| `radon.nodes.apache.nifi.NifiPipeline` | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.apache.nifi.NifiRuntime` | `tosca.relationships.HostedOn` | [1, 1] |
| `connect` | `tosca.capabilities.Endpoint` | `radon.nodes.apache.nifi.NifiPipeline` | `tosca.relationships.ConnectsTo` | [0, 1] |

### Notes

* An `pipeline_template` artifact can be supplied of type `tosca.artifacts.File` in the node template definition.
