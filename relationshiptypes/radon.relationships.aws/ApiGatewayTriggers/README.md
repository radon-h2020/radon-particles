## AWS Triggers Relationship

AWS-specific relationship type representing AwsResource-to-AwsLambdaFunction communication.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsTriggers` | `radon.relationships.aws.AwsTriggers` | 1.0.0 | `radon.relationships.abstract.Triggers` |

### Properties

| Name | Required | Type | Constraint | Default Value| Description |
|:---- |:-------- |:---- |:---------- |:-----------  |:----------- |
| `events` | `true` | `string` |   |   | List of events |
