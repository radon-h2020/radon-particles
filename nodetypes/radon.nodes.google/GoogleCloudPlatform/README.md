![](https://img.shields.io/badge/Status:-DEVELOPMENT-red)

## Google Cloud Platform Node Type

A node type representing the Google Cloud Platform which capable of hosting resources and functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudPlatform` | `radon.nodes.google.GoogleCloudPlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `project_id` | `true` | `string` |   |   | The unique project-id to be used |
| `region` | `true` | `string` |   |   | The region to be used for deployment |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `tosca.capabilities.Container` | `radon.nodes.google.CloudFunction`, `radon.nodes.google.GoogleCloudResource` | [1, UNBOUNDED] |
