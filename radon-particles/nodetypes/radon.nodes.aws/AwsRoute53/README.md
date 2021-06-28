![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## AWS Route 53 Node Type

A node type that represents an AWS Route 53.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AwsRoute53` | `radon.nodes.aws.AwsRoute53` | 1.0.0 | `tosca.nodes.SoftwareComponent` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `alias_zone` | `true` | `string` |   |   | The hosted zone identifier |
| `zone` | `true` | `string` |   |   | The DNS zone to modify |
| `record` | `true` | `string` |   |   | The full DNS record to create or delete |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.aws.AwsPlatform` | `tosca.relationships.HostedOn` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `alias_zone`
    * `zone`
    * `record`
    * `endpoint_url`
