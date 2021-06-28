## Interaction Data Type

Data type representing an interaction on a TOSCA relationship.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Interaction | `radon.datatypes.Interaction` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `type` | `true` | `string` | `valid_values: [synchronous, asynchronous]` | synchronous | Interaction type |
| `source_activity` | `true` | `string` |   |   | Source activity |
| `target_entry` | `true` | `string` |   |   | Target entry |
| `number_of_requests` | `true` | `float` | `greater_or_equal: 0.0` | 1.0 | Number of requests |
| `network_delay` | `false` | `radon.datatypes.RandomVariable` |   |   | Network delay in seconds |
