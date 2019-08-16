## Cloud Function Node Type

An abstract node type that describes a generic Google Cloud Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `CloudFunction` | `radon.nodes.google.CloudFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `function_name` | `true` | `string` | N/A | The name of the function.
| `function_runtime` | `true` | `string` | `valid_values: [nodejs8, nodejs10, python37, go111, nodejs6]` | The runtime environment to execute the function. |
| `memory` | `true` | `integer` | 256 | `valid_values: [ 128, 256, 512, 1024, 2048]` | The limit (in MB) on the amount of memory the function can use. |
| `timeout` | `true` | `integer` | 60 | `in_range: [1, 540]` | The limit (in seconds) on time this function is allowed to execute. |
| `enttry_point`| `false` | `string` | N/A | N/A | Name of a Google Cloud Function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named "function". For Node.js this is name of a function exported by the module specified in source_location. |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `HostedOn` | [1,1] |

### Notes

* All type-specific Google Cloud Functions should derive from this type.
