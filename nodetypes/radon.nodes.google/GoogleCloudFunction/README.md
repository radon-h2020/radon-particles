![](https://img.shields.io/badge/Status:-RELEASED-green)

## Google Cloud Function Node Type

An abstract node type that describes a generic Google Cloud Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudFunction` | `radon.nodes.google.GoogleCloudFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_name` | `true` | `string` |  |  | The name of the function. |
| `function_runtime` | `true` | `string` | `valid_values: [nodejs8, nodejs10, python37, go111, nodejs6]` |  |The runtime environment to execute the function. |
| `memory` | `true` | `integer`  | `valid_values: [ 128, 256, 512, 1024, 2048]`| 256 | The limit (in MB) on the amount of memory the function can use. |
| `function_timeout` | `true` | `integer`  | `in_range: [1, 540]` | 60 | The limit (in seconds) on time this function is allowed to execute. |
| `function_entry_point`| `true` | `string` |   | "entry_point" | Name of a Google Cloud Function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in source_location. |
| `function_bucket_name` | `true` | `string` |  |  | Name of the GCP bucket containing the zipped GCP |
| `zip_file` | `true` | `string` |  |  | Path to a zip file containing the function code |
| `environment_variables` | `true` | `map of string` |  |  | The function's environment variables |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `HostedOn` | [1, 1] |
