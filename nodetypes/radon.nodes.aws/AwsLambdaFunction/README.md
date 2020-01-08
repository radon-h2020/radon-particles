## Lambda Function Node Type

A node type that represents an AWS Lambda Function that can be triggered by an AWS resource, a fixed schedule or via an API gateway.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsLambdaFunction` | `radon.nodes.aws.AwsLambdaFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `role_name` | `true` | `string` |   |   | The Amazon Resource Name (ARN) of the function's execution role |
| `role_description` | `true` | `string` |   |   | Description of the function's execution role |
| `runtime` | `true` | `string` | `valid_values: [nodejs, nodejs4.3, nodejs6.10, nodejs8.10, nodejs10.x, java8, python2.7, python3.6, python3.7, dotnetcore1.0, dotnetcore2.0, dotnetcore2.1, nodejs4.3-edge, go1.x, ruby2.5]` |   | The identifier of the function's runtime |
| `handler` | `true` | `string` |   | `index.handler` | The name of the method within your code that Lambda calls to execute your function |
| `memory` | `true` | `integer` | `in_range: [128, 3008]` |   | The amount of memory in megabytes that your function has access to |
| `timeout` | `true` | `integer` | `in_range: [1, 900]` | 3 | The amount of time that Lambda allows a function to run before stopping it |
| `schedule` | `false` | `string` |   |   | The schedule in which the platform will invoke this function, can be a rate or a cron |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon's resource name for this Lambda function |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `invocable` | `radon.capabilities.Invocable` |   | [0, UNBOUNDED] |

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
