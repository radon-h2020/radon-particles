## Display Name

This is an abstract event data type. It represents an abstract event based on the CNCF cloud events schema.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Event | radon.datatypes.Event | 1.0.0 | tosca.datatypes.Root |

### Properties

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |
| `specversion` | `false` | `string` | N/A | CNCF CloudEvents spec version |
| `type` | `true` | `string` | N/A | Event type, e.g., `s3:ObjectCreated:Put` |
| `source` | `false` | `string` | N/A | Event source |
| `subject` | `false` | `string` | N/A | The subject of the event, e.g., `mynewfile.jpg` |
| `id` | `false` | `string` | N/A | Event's unique identifier |
| `time` | `false` | `string` | N/A | The time when event occurred |
| `datacontenttype` | `false` | `string` | N/A | Type of event's data content, e.g., `text/xml` |
| `data` | `false` | `string` | N/A | Event's payload |

### Attributes

| Name | Required | Type | Constraint | Description |
|:---- |:-------- |:---- |:---------- |:----------- |

### Capabilities

| Name | Type | Valid Source Types |
|:---- |:---- |:------------------ |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|

### Notes

* Arbitrary list of additional notes
* ...

---
