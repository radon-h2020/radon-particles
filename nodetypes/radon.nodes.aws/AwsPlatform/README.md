![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS Platform  Node Type

A node type that represents the AWS platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsPlatform` | `radon.nodes.aws.AwsPlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `role_arn` | `string` |   | AWS role arn identifier |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` |  | AWS |  |
| `region` | `true` | `string` |  |  | The region identifier, e.g., us-west-1 |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[ radon.nodes.aws.AwsLambdaFunction, radon.nodes.aws.AwsS3Bucket, radon.nodes.VM.EC2, radon.nodes.aws.AwsApiGateway, radon.nodes.aws.AwsDynamoDBTable ]` | [1, UNBOUNDED] |
