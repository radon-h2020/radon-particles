![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS API Gateway Node Type

A node type that represents an AWS API gateway.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsApiGateway` | `radon.nodes.aws.AwsApiGateway` | 1.0.0 | `radon.nodes.abstract.ApiGateway` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` |   | Amazon resource name for this API |
| `endpoint_url` | `string` |   | Base URL for endpoints provided by the API |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `api_description` | `true` | `string` |   |   | Description of the API |
| `api_version` | `true` | `string` |   |   | Version of the API |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.aws.AwsLambdaFunction` | `radon.relationships.aws.AwsApiGatewayTriggers` | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `api_title`
    * `api_description`
    * `api_version`
    * `aws_region`
