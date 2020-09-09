![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## DynamoDB Table Node Type

A node type that represents an AWS DynamoDB table

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsDynamoDBTable` | `radon.nodes.aws.AwsDynamoDBTable` | 1.0.0 | `tosca.nodes.Database` |

### Properties	

| Name | Required | Type | Constraint | Default Value | Description |	
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |	
| `table_name` | `true` | `string` |   |   | The name of the AWS DynamoDB table |
| `hash_key_name` | `false` | `string` |   |   | The name of the hash key |
| `hash_key_type` | `false` | `string` |   |   | The type of the hash key {STRING, NUMBER, BINARY} |
| `range_key_name` | `false` | `string` |   |   | The name of the range key |
| `range_key_type` | `false` | `string` |   |   | The type of the range key {STRING, NUMBER, BINARY} |
| `read_capacity` | `false` | `integer` |   |   | Read throughput capacity (units) to provision |
| `write_capacity` | `false` | `integer` |   |   | Write throughput capacity (units) to provision |


### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn`| [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.aws.LambdaFunction` | `radon.relationships.aws.Triggers`| [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_region`
    * `table_name`
    * `hash_key_name`
    * `hash_key_type`
    * `read_capacity`
    * `write_capacity`
