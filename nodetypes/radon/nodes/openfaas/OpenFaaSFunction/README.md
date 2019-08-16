## OpenFaaS Function Node Type

A node type that represents a function hosted on an OpenFaas Platform

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenFaaSFunction` | `radon.nodes.openfaas.OpenFaaSFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`function_name`| `true` | `string` | N/A | N/A | The name of the function. |
|`function_language_template`| `true` | `string` | `valid_values: [csharp, dockerfile, docekrfile-armhf, go-armhf, go, java8, node-arm64, node-armhf, node, php7, python-armhf, python, python3-armhf, python3, ruby]` | N/A | The runtime of this function. |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `function_url` | `string` | `concat [ get_attribute: [SELF, gateway_url], "/function/", get_property: [SELF, function_name] ]` | The URL at which the function can be addressed via a REST call. |
| `gateway_url` | `string` | `get_attribute: [HOST, url]` | The URL of the underlying platform. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`invocable`| `radon.capabilities.Invocable` | N/A | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | N/A | `radon.nodes.openfaas.OpenFaaSPlatform` | N/A | [1,1] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
    * `FUNCTION_NAME`
    * `FUNCTION_LANGUAGE_TEMPLATE`
    * `GATEWAY`
