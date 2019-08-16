## Resource-triggered Cloud Function Node Type

A node type that represents a Google Cloud Function that can be triggered by a Google Cloud Resource, such as, a `Bucket` or a `Topic`

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ResourceTriggeredCloudFunction` | `radon.nodes.google.ResourceTriggeredCloudFunction` | 1.0.0 | `radon.nodes.google.CloudFunction` |

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `inovcable` | `radon.capabilities.Invocable` | `radon.nodes.google.CloudResource`| [1, 1] |
