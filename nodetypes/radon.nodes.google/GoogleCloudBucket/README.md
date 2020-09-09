![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Google Cloud Bucket Node Type

Node type to deploy an object storage on Google Cloud.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudBucket` | `radon.nodes.google.GoogleCloudBucket` | 1.0.0 | `radon.nodes.google.GoogleCloudResource` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |  |  | The name of the GCP bucket |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `storage_endpoint` | `tosca.capabilities.Endpoint` |   | [0, UNBOUNDED] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `bucket_location`
    * `project_id`
    * `bucket_name`
    * `service_account_file`
