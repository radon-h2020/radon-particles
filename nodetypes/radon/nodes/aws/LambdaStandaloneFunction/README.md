## Lambda Standalone Function

A node type that represents an AWS Lambda Function that is triggered by a fixed schedule or via an API gateway.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `LambdaStandaloneFunction` | `radon.nodes.aws.LambdaStandaloneFunction` | 1.0.0 | `radon.nodes.aws.LambdaFunction` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `schedule` | `true` | `string` | N/A | N/A | The schedule in which the platform will invoke this function, can be a rate or a cron. |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `schedule`

---