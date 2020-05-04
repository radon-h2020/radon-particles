## NiFi Node Type

A type representing an Apache NiFi middleware component.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `Nifi` | `radon.nodes.nifi.Nifi` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description | 
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `component_version` | `true` | `version` |   |   | The version of Apache NiFi |
| `port` | `true` | `integer` |   | 8080 | The listening port of Apache NiFi |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`| `tosca.capabilities.Container`| `radon.nodes.apache.nifi.NifiPipeline` | [1, UNBOUNDED] |
