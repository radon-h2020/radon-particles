## Nifi

A type representing an Apache Nifi middleware component.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Nifi` | `radon.nodes.nifi.Nifi` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description | 
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `component_version` | `true` | `version` | N/A | N/A | The version of Apache Nifi |
| `port` | `true` | `integer` | N/A | 8080 | The listening port of Apache Nifi |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`| `tosca.capabilities.Container`| `radon.nodes.nifi.NifiPipeline` | [1, UNBOUNDED] |

---