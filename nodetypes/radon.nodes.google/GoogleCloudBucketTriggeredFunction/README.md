![](https://img.shields.io/badge/Status:-RELEASED-green)
![](https://img.shields.io/badge/%20-DEPLOYABLE-blueviolet)

## Google Cloud Bucket-Triggered Function Node Type

A node type representing a Google Cloud function that can be triggered by a Google Cloud bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudBucketTriggeredFunction` | `radon.nodes.google.GoogleCloudBucketTriggeredFunction` | 1.0.0 | `radon.nodes.google.GoogleCloudFunction` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `trigger_bucket_name` | `true` | `string` |   |   | Name of the GCP bucket to trigger this function |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `inovcable` | `radon.capabilities.Invocable` | `[radon.nodes.google.GoogleCloudBucket]` | [1, 1] |

### Notes

* Parameters added to the `Standard` interface inputs:
    * `environment_variables`
    * `function_memory`
    * `function_location`
    * `function_timeout`
    * `function_bucket_name`
    * `project_id`
    * `function_name`
    * `trigger_bucket_name`
    * `function_runtime`
    * `service_account_file`
    * `zip_file`
    * `function_entry_point`
