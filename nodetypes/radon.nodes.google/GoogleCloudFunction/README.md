![](https://img.shields.io/badge/Status:-RELEASED-green)

## Google Cloud Function Node Type (Abstract)

An abstract node type representing a Google Cloud function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudFunction` | `radon.nodes.google.GoogleCloudFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_runtime` | `true` | `string` | `valid_values: [nodejs8, nodejs10, python37, go111, nodejs6]` |   | The runtime environment to execute the function |
| `function_memory` | `true` | `integer` | `valid_values: [ 128, 256, 512, 1024, 2048]`| 256 | The limit (in MB) on the amount of memory the function can use |
| `function_timeout` | `true` | `integer`  | `in_range: [1, 540]` | 60 | The limit (in seconds) on time the function is allowed to execute |
| `function_entry_point`| `true` | `string` |   | "entry_point" | Name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if the function with the given name is not found, then the system will try to use a function named "function" |
| `function_bucket_name` | `true` | `string` |   |   | Name of the GCP bucket containing the zipped function code |
| `zip_file` | `true` | `string` |   |   | Path to a zip file containing the function code |
| `environment_variables` | `true` | `map` of `string` |   |   | The function's environment variables |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `HostedOn` | [1, 1] |
| `monitor` | `radon.capabilities.monitoring.Monitor` | `radon.nodes.monitoring.PushGateway` | `radon.relationships.monitoring.GCPIsMonitoredBy` | [ 0, UNBOUNDED ] |
