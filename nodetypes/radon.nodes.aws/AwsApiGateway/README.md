![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS API Gateway Node Type

A node type that represents an AWS Lambda Function.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsApiGateway` | `radon.nodes.aws.AwsApiGateway` | 1.0.0 | `radon.nodes.abstract.ApiGateway` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon's resource name for this entity |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `api_title` | `true` | `string` |  |  | Name of the API |
| `api_description` | `true` | `string` |  |  |  Description of the API |
| `api_version` | `true` | `string` |  |  | Version of the API |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn`| [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.aws.LambdaFunction` | `radon.relationships.aws.Triggers`| [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `api_title`
    * `api_description`
    * `api_version`
    * `aws_region`
