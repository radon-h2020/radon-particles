## Event Data Type

Data type representing an event based on the CNCF CloudEvents schema.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Event | `radon.datatypes.Event` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `type` | `true` | `string` | N/A | N/A | Event type, e.g., `s3:ObjectCreated:Put` |
| `spec_version` | `false` | `string` | N/A | 0.3 | CloudEvents spec version |
| `data_content_encoding` | `false` | `string` | N/A | Event's content encoding |
| `data_content_type` | `false` | `string` | N/A | | Type of event's data content, e.g., `text/xml` |
| `schema_url` | `false` | `string` | N/A | URL to the event's schema definition |
