## Activity Data Type

Data type representing an activity of an entry.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| Activity | `radon.datatypes.Activity` | 1.0.0 | `tosca.datatypes.Root` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `service_time` | `false` | `radon.datatypes.RandomVariable` |   |   | Service time in seconds |
| `bound_to_entry` | `false` | `boolean` |   |   | True if it is bound to the entry |
| `replies_to_entry` | `false` | `boolean` |   |   | True if it replies to the entry |
| `request_pattern` | `false` | `string` | `valid_values: [stochastic, deterministic]` |   | Request pattern |
