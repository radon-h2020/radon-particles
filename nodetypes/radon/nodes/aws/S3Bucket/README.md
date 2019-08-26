## S3 Bucket Node Type

A node type that represents an AWS S3 Bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `S3Bucket` | `radon.nodes.aws.S3Bucket` | 1.0.0 | `tosca.nodes.Storage.ObjectStorage` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `true` | `string` | N/A | N/A | The name of this bucket. |

### Attributes

| Name | Type | Default Value | Description |
|:---- |:---- |:------------- |:----------- |
| `arn` | `string` | N/A | Amazon's resource name for this bucket |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | N/A | `tosca.relationships.HostedOn`| [1,1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.aws.LambdaFunction` | `radon.relationships.aws.Triggers`| [0,UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `aws_access_key_id`
    * `aws_secret_access_key`
    * `aws_region`
    * `bucket_name`
