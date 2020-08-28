## OpenWhisk Function Node Type

A node type that represents a function hosted on an OpenWhisk Platform

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `OpenWhiskFunction` | `radon.nodes.apache.openWhisk.OpenWhiskFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
|`function_name`| `true` | `string` |   |   | The name of the function. |
|`function_runtime`| `true` | `string` | `valid_values: [go_1_11, java_8, ballerina_0_990, nodejs_12, nodejs_10, nodejs_8, nodejs_6, php_7_3, python_2, python_3, ruby_2_5, swift_4_2, dotnet_2_2]` |   | The runtime of this function. |
|`function_package_name`| `true` | `string` |   |   | The name of the package this function belongs to. |
|`entry_point`| `false` | `string` |   |   | The optional entry point at which the function can be found. |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `rest_api_endpoint` | `string` | `concat: [ get_attribute: [SELF, host, api_url], "/api/v1/namespaces/", get_property: [SELF, host, default_namespace], "/actions/", get_property: [SELF, function_package_name], "/", get_property: [SELF, function_name] ]` | The URL at which the function can be addressed via a REST call. |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
|`invocable`| `radon.capabilities.Invocable` |   | [0, UNBOUNDED] |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` |   | `radon.nodes.apache.openWhisk.OpenWhiskPlatform` |   | [1, 1] |

### Notes

* Parameters added to the inputs of the `Standard` interface:
    * `FUNCTION_NAME`
    * `FUNCTION_RUNTIME`
    * `ENTRY_POINT`
