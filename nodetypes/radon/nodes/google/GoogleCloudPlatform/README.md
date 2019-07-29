## Google Cloud Platform

A node type representing the Goolge Cloud Platform which capable of hosting resources and functions.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `GoogleCloudPlatform` | `radon.nodes.google.GoogleCloudPlatform` | 1.0.0 | `radon.nodes.abstract.CloudPlatform` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `sdk_version` | `false` | `version` | N/A | N/A | Specifies the SDK version required to manage Google Cloud resources. |
| `project_id` | `true` | `string` | N/A | N/A | Specifies the unique project-id to be used. |
| `user_account` | `false` | `string` | N/A | N/A | Specifies the user account used to log-in if a service account is not used. |
| `api_key` | `false` | `string` | N/A | N/A | Encrypted key that can be used to access certain APIs that do not need to access private user data. |
| `authentication_mode` | `true` | `string` | `valid_values: [user-account, service-account, api-key]` | N/A | Indicates whether user-account, service-account or api-key authentication should be used.|
| `region` | `true` | `string` | N/A | N/A | Indicates the default region of the project. |
| `zone` | `true` | `string` | N/A | N/A | Indicates the default zone of the project.|


### Capabilities

| Name | Type | Valid Source Types | Occurrences |
|:---- |:---- |:------------------ |:----------- |
| `host` | `osca.capabilities.Container` | `radon.nodes.google.CloudFunction`, `radon.nodes.google.GoogleCloudResource` | [1, UNBOUNDED] |

### Notes

* Inputs added to the `Standard` interface operations:
    * `create`: `SDK_VERSION`
    * `configure`: `PROJECT_ID`, `AUTHENTICATION_MODE`, `USER_ACCOUNT`, `API_KEY`, `REGION`, `ZONE`
* If the selected `authentication_mode` is `service-account`, the implementing node template should provide an artifact with the service account key.

---