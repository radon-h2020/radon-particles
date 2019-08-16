## Lambda Function

A node type that represents an AWS Lambda Function that can be triggered by an AWS resource, a fixed schedule or via an API gateway.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `LambdaFunction` | `radon.nodes.aws.LambdaFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `role_name` | `true` | `string` | N/A | N/A |  |
| `role_description` | `true` | `string` | N/A | N/A |  |
| `runtime` | `true` | `string` | N/A | N/A |  |
| `handler` | `true` | `string` | N/A | N/A |  |
| `memory` | `true` | `integer` | `in_range: [128, 3008]` | N/A | Size in megabytes. |
| `timeout` | `true` | `integer` | `in_range: [1, 900]` | N/A | Time in seconds |
| `schedule` | `false` | `string` | N/A | N/A | The schedule in which the platform will invoke this function, can be a rate or a cron. |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` | N/A | |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `radon.capabilities.Invocable` | N/A | [0, UNBOUNDED] |


### Notes

* Parameters added to the `Standard` interface inputs:
    * `function_name`
    * `function_role_name`
    * `function_runtime`
    * `function_handler`
    * `function_memory`
    * `function_timeout`
    * `function_code_location`
    * `aws_access_key_id`
    * `aws_secret_access_key`
    * `aws_region`
    * `schedule`

---