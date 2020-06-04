## AWS Platform  Node Type

A node type that represents the AWS platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsPlatform` | `radon.nodes.aws.AwsPlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `access_key_id` | `true` | `string` |   |   | The identifier of your AWS access key |
| `secret_access_key` | `true` | `string` |   |   | The secret access key associated to your access key |
| `region` | `true` | `string` |   |   | The region identifier, e.g., us-west-1 |

### Capabilities
| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `[radon.nodes.aws.LambdaFunction, radon.nodes.aws.S3Bucket, radon.nodes.VM.EC2]` | [0, UNBOUNDED] |
