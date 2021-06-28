![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## OpenFaaS Function Node Type

A node type that represents a function hosted on an OpenFaas Platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenFaasFunction` | `radon.nodes.openfaas.OpenFaasFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `function_url` | `string` | `concat: [get_attribute: [SELF, gateway_url], "/function/", get_property: [SELF, function_name]]` | The URL at which the function can be addressed via a REST call. |
| `gateway_url` | `string` | `get_attribute: [SELF, host, url]` | The URL of the underlying platform. |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_language_template` | `true` | `string` | `valid_values: [csharp, dockerfile, docekrfile-armhf, go-armhf, go, java8, node-arm64, node-armhf, node, php7, python-armhf, python, python3-armhf, python3, ruby]` |   | The runtime of this function. |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.openfaas.OpenFaasPlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
    * `FUNCTION_NAME`
    * `FUNCTION_LANGUAGE_TEMPLATE`
    * `GATEWAY`
