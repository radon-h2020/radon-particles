![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## Google Cloud Bucket Node Type

A node type representing a Google Cloud bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudBucket` | `radon.nodes.google.GoogleCloudBucket` | 1.0.0 | `radon.nodes.abstract.ObjectStorage` |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.GoogleCloudPlatform` | `tosca.relationships.HostedOn` | [1, 1] |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.google.GoogleCloudBucketTriggeredFunction` | `radon.relationships.google.GoogleCloudTriggers` | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `bucket_location`
    * `project_id`
    * `bucket_name`
    * `service_account_file`
