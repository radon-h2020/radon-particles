![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## Lambda Function Node Type

A node type that represents an AWS Lambda Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsLambdaFunction` | `radon.nodes.aws.AwsLambdaFunction` | 1.0.0 | `radon.nodes.abstract.Function` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `alias` | `true` | `string` |  |  | Lambda function's alias |
| `runtime` | `true` | `string` | `valid_values: [nodejs, nodejs4.3, nodejs6.10, nodejs8.10, nodejs10.x, java8, python2.7, python3.6, python3.7, dotnetcore1.0, dotnetcore2.0, dotnetcore2.1, nodejs4.3-edge, go1.x, ruby2.5]` |   | The identifier of the function's runtime |
| `handler` | `true` | `string` |   | `index.handler` | The name of the method within your code that Lambda calls to execute your function |
| `memory` | `true` | `integer` | `in_range: [128, 3008]` | 128 | The amount of memory in megabytes that your function has access to |
| `memory_range` | `true` | `range` | `in_range: [128, 3008]` |   | Range of function memory in MB to search |
| `concurrency` | `false` | `integer` | `in_range: [0, UNBOUNDED]` | 0 | The amount of concurrency that your function has access to |
| `concurrency_range` | `false` | `range` | `in_range: [1, UNBOUNDED]` |   | Range of function concurrency to search |
| `timeout` | `true` | `integer` | `in_range: [1, 900]` | 3 | The amount of time that Lambda allows a function to run before stopping it |
| `statement_id` | `true` | `string` |  |  | Lambda policy statement identifier |
| `zip_file` | `true` | `string` |  |  | path to a function zip file |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |  | Amazon's resource name for this Lambda function |
| `role_arn` | `string` |  | AWS function's role ARN |
| `region` | `string` |  |  |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_region`
    * `role_arn`
    * `lambda_runtime`
    * `function_name`
    * `lambda_timeout`
    * `lambda_memory`
    * `func_alias`
    * `permission_id`
    * `lambda_handler`
    * `zip_file`
    * `lambda_concurrency`
    * `env_vars`
