## OpenWhisk Platform

A node type that represents an externally managed OpenWhisk Platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenWhiskPlatform` | `radon.nodes.apache.openwhisk.OpenWhiskPlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `kubernetes_version` | `false` | `version` | N/A | 1.8 | The version of the Kubernetes cluster hosting this platform. |
| `auth_username` | `true` | `string` | N/A | N/A | The username used for basic authentication. |
| `auth_password` | `true` | `string` | N/A | N/A | The password used for basic authentication. |
| `api_host` | `true` | `string` | N/A | N/A | The host name to access OpenWhisk API gateway at. |
| `api_port` | `true` | `integer` | N/A | 31112 | The port to access OpenWhisk API gateway at. |
| `default_namespace` | `true` | `string` | N/A | N/A | The default namespace in which resources are deployed. |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `url` | `string` | `concat: ["http://", get_property: [SELF, api_gateway_host], get_property: [SELF, api_gateway_port] ]` | The full gateway url. |
| `auth_key` | `string` | `concat: [get_property: [SELF, auth_username], get_property: [SELF, auth_password] ]` | The string used for basic authentication. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`host`| `tosca.capabilities.Container` | `radon.nodes.openfaas.OpenWhiskFunction` | [0,UNBOUNDED]

### Notes

* Parameters added to the `Standard` interface operations:
    * `create`: `KUBERNETES_VERSION`
    * `configure`: `API_URL`, `AUTH_KEY`

---