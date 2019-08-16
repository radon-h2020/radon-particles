## Nifi Pipeline

A type representing a data pipeline hosted on Apache Nifi.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `NifiPipeline` | `radon.nodes.apache.nifi.NifiPipeline` | 1.0.0 | `radon.nodes.abstract.DataPipeline` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `id` | `string` | N/A | Unique ID of the pipeline |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`connect`| `tosca.capabilities.Endpoint`| `radon.nodes.apache.nifi.NifiPipeline` | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.apache.nifi.Nifi` | `tosca.relationships.HostedOn` | [1,1] |
| `connect` | `tosca.capabilities.Endpoint` | `radon.nodes.apache.nifi.NifiPipeline` | `tosca.relationships.ConnectsTo` | [0,1] | 

### Notes

* An `pipeline_template` artifact can be supplied of type `tosca.artifacts.File` in the node template definition.

---