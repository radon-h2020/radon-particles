![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS DynamoDB Table Node Type

A node type that represents an AWS DynamoDB table.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsDynamoDBTable` | `radon.nodes.aws.AwsDynamoDBTable` | 1.0.0 | `radon.nodes.abstract.Database` |

### Properties	

| Name | Required | Type | Constraint | Default Value | Description |	
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |	
| `hash_key_name` | `false` | `string` |   |   | The name of the hash key |
| `hash_key_type` | `false` | `string` |   |   | The type of the hash key {STRING, NUMBER, BINARY} |
| `range_key_name` | `false` | `string` |   |   | The name of the range key |
| `range_key_type` | `false` | `string` |   |   | The type of the range key {STRING, NUMBER, BINARY} |
| `read_capacity` | `false` | `integer` |   | 1 | Read throughput capacity (units) to provision |
| `write_capacity` | `false` | `integer` |   | 1 | Write throughput capacity (units) to provision |
| `port` | `true` | `integer` |   | 1337 | Workaround: Dummy value required to deploy type using xOpera |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.aws.AwsLambdaFunction` | `radon.relationships.aws.AwsTriggers` | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_region`
    * `table_name`
    * `hash_key_name`
    * `hash_key_type`
    * `read_capacity`
    * `write_capacity`
