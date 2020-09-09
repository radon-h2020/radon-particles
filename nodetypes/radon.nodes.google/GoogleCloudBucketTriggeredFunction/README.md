![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Google Bucket-triggered Cloud Function Node Type

A node type that represents a Google Cloud Function that can be triggered by a Google Cloud bucket.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudBucketTriggeredFunction` | `radon.nodes.google.GoogleCloudBucketTriggeredFunction` | 1.0.0 | `radon.nodes.google.GoogleCloudFunction` |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `inovcable` | `radon.capabilities.Invocable` | `radon.nodes.google.GoogleCloudResource`| [1, 1] |
