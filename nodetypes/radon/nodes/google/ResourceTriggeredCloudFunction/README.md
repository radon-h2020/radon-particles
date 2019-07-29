## Resource-triggered Cloud Function

A node type that represents a Google Cloud Function that can be triggered by a Google Cloud Resource, such as, a `Bucket` or a `Topic`

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `ResourceTriggeredCloudFunction` | `radon.nodes.google.ResourceTriggeredCloudFunction` | 1.0.0 | `radon.nodes.google.CloudFunction` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `inovcable` | `radon.capabilities.Invocable` | `radon.nodes.google.CloudResource`| [1, 1] |


---