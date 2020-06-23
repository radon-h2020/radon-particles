## AWS API Gateway Node Type

A node type that represents an AWS Lambda Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsApiGateway` | `radon.nodes.aws.AwsApiGateway` | 1.0.0 | `radon.nodes.abstract.ApiGateway` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `role_name` | `true` | `string` |  |   | The Amazon Resource Name (ARN) of the execution role |
| `aws_region` | `true` | `string` |  |   | The selected Amazon region |
| `function_name` | `true` | `string` |  | `index.handler` | The name of the lambda function |
| `api_gateway_title` | `true` | `string` |  |   | Name of the API gateway region |
| `api_gateway_resource_uri` | `true` | `string` |  |   | The amount of concurrency that your function has access to |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon's resource name for this entity |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `requires_role` | `tosca.capabilities.Node` |  | `tosca.relationships.DependsOn` | [1, 1] |
| `receives_notification` | `tosca.capabilities.Compute` |  | `tosca.relationships.DependsOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `role_name`
    * `lambda_function_arn`
    * `aws_region`
    * `function_name`
    * `api_gateway_title`
    * `api_gateway_resource_uri`
    * `aws_role`
