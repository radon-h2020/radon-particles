## AWS API Gateway Triggers Relationship

AWS-specific relationship type representing AwsApiGateway-to-AwsLambdaFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsApiGatewayTriggers` | `radon.relationships.aws.AwsApiGatewayTriggers` | 1.0.0 | `radon.relationships.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `endpoint` | `true` | `string` |   |   | Endpoint name |
| `http_methods` | `true` | `string` |   |   | List of HTTP methods |
