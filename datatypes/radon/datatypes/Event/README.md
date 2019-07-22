## Event

Data type representing an event based on the CNCF CloudEvents schema.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Event | `radon.datatypes.Event` | 1.0.0 | `tosca.datatypes.Root` |

In the following, the properties, attributes, capabilities, and requirements changed from / added to the parent type are listed:

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `type` | `true` | `string` | N/A | N/A | Event type, e.g., `s3:ObjectCreated:Put` |
| `spec_version` | `false` | `string` | N/A | 0.3 | CloudEvents spec version |
| `data_content_encoding` | `false` | `string` | N/A | |
| `data_content_type` | `false` | `string` | N/A | | Type of event's data content, e.g., `text/xml` |
| `schema_url` | `false` | `string` | N/A |  |

---