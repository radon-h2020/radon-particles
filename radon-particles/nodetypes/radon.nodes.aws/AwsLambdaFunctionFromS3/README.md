![](https://img.shields.io/badge/Status:-TESTING-yellow)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS Lambda Function From S3 Node Type

A node type that represents an AWS Lambda function which is instrumented based on a function deployment package from an AWS S3 bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsLambdaFunctionFromS3` | `radon.nodes.aws.AwsLambdaFunctionFromS3` | 1.0.0 | `radon.nodes.abstract.Function` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon Resource Name (ARN) for this function |
| `role_arn` | `string` |   | ARN for the role of the function |
| `region` | `string` |   | AWS region in which the function is deployed |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `alias` | `true` | `string` |   | "dev" | Lambda function's alias |
| `runtime` | `true` | `string` | `valid_values: [nodejs, nodejs4.3, nodejs6.10, nodejs8.10, nodejs10.x, java8, python2.7, python3.6, python3.7, dotnetcore1.0, dotnetcore2.0, dotnetcore2.1, nodejs4.3-edge, go1.x, ruby2.5]` | "nodejs" | The identifier of the function's runtime |
| `handler` | `true` | `string` |   | "index.handler" | The name of the method within your code that Lambda calls to execute your function |
| `memory` | `true` | `integer` | `in_range: [128, 3008]` | 128 | The amount of memory in megabytes that your function has access to |
| `memory_range` | `true` | `range` | `in_range: [128, 3008]` |   | Range of function memory in MB to search |
| `concurrency` | `false` | `integer` | `in_range: [0, UNBOUNDED]` | 0 | The amount of concurrency that your function has access to |
| `concurrency_range` | `false` | `range` | `in_range: [1, UNBOUNDED]` |   | Range of function concurrency to search |
| `timeout` | `true` | `integer` | `in_range: [1, 900]` | 3 | The amount of time that Lambda allows a function to run before stopping it |
| `statement_id` | `true` | `string` |   |   | Lambda policy statement identifier |
| `env_vars` | `false` | `map` of `string` |   |   | The environment variables of the function |
| `s3_bucket_name` | `true` | `string` |   |   | The S3 bucket name containing the function package to be deployed |
| `s3_bucket_key` | `true` | `string` |   |   | The S3 key aka. filename referencing the file to be deployed |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `monitor` | `radon.capabilities.monitoring.Monitor` | `radon.nodes.monitoring.PushGateway` | `radon.relationships.monitoring.AWSIsMonitoredBy` | [ 0, UNBOUNDED ] |

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
    * `lambda_concurrency`
    * `env_vars`
    * `s3_bucket_name`
    * `s3_bucket_key`
